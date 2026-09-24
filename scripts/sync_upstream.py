#!/usr/bin/env python3
"""Prepare, verify, preview, and finalize a Counso documentation sync."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "sync-policy.json"
SYNC_DIR = ROOT / ".sync"
SOURCE_DIR = ROOT / "source"


class SyncError(RuntimeError):
    pass


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def run(*args: str, cwd: Path = ROOT, capture: bool = False) -> str:
    result = subprocess.run(
        args,
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
    )
    return result.stdout.strip() if capture else ""


def git(*args: str, capture: bool = False) -> str:
    return run("git", *args, capture=capture)


def ensure_clean() -> None:
    if git("status", "--porcelain", capture=True):
        raise SyncError("working tree is not clean")


def current_branch() -> str:
    return git("branch", "--show-current", capture=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_upstream_snapshot_current(policy: dict) -> None:
    pairs = (
        (policy["upstream"]["llms_url"], SOURCE_DIR / "llms.txt"),
        (policy["upstream"]["sitemap_url"], SOURCE_DIR / "sitemap.xml"),
    )
    for url, local in pairs:
        request = urllib.request.Request(url, headers={"User-Agent": "CounsoDocsSync/1.0"})
        with urllib.request.urlopen(request, timeout=45) as response:
            remote_hash = hashlib.sha256(response.read()).hexdigest()
        if remote_hash != sha256(local):
            raise SyncError(
                f"upstream changed during review ({url}); start a fresh sync instead of publishing a stale mapping"
            )


def official_url(entry: dict) -> str:
    if entry.get("page_url"):
        return entry["page_url"].rstrip("/")
    source_url = entry["source_url"]
    parsed = urllib.parse.urlparse(source_url)
    if parsed.netloc != "docs.dust.tt":
        return source_url
    path = parsed.path[:-3] if parsed.path.endswith(".md") else parsed.path
    if path.endswith("/index"):
        path = path[:-6]
    return urllib.parse.urlunparse(parsed._replace(path=path.rstrip("/"), query="", fragment=""))


def normalized_path(path: str) -> str:
    if path == "analytics.md" or path.startswith("api-reference/"):
        return path
    return "docs/" + path.removeprefix("docs/")


def normalize_download(raw: Path, destination: Path) -> dict:
    manifest = load_json(raw / "manifest.json")
    failures = [entry for entry in manifest if entry.get("status") != "downloaded"]
    if failures:
        raise SyncError(f"upstream download contains {len(failures)} failed entries")

    destination.mkdir(parents=True)
    seen: set[str] = set()
    for entry in manifest:
        old_path = entry["path"]
        new_path = normalized_path(old_path)
        if new_path in seen:
            raise SyncError(f"duplicate normalized path: {new_path}")
        seen.add(new_path)
        source = raw / old_path
        if not source.is_file():
            raise SyncError(f"downloaded source is missing: {old_path}")
        target = destination / new_path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        entry["path"] = new_path

    llms = raw / "_source" / "llms.txt"
    sitemap = raw / "_source" / "sitemap.xml"
    shutil.copy2(llms, destination / "llms.txt")
    shutil.copy2(sitemap, destination / "sitemap.xml")
    (destination / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    sitemap_urls = [
        element.text
        for element in ET.parse(sitemap).iter()
        if element.tag.endswith("}loc") and element.text
    ]
    routes = {
        official_url(entry): entry["path"]
        for entry in manifest
        if official_url(entry) in set(sitemap_urls)
    }
    if set(routes) != set(sitemap_urls):
        missing = sorted(set(sitemap_urls) - set(routes))
        raise SyncError(f"sitemap URLs were not mapped: {missing[:5]}")
    index = {
        "schema_version": 1,
        "source": {
            "sitemap": "https://docs.dust.tt/sitemap.xml",
            "sitemap_file": "sitemap.xml",
            "sitemap_sha256": sha256(destination / "sitemap.xml"),
            "manifest_file": "manifest.json",
        },
        "stats": {
            "sitemap_urls": len(sitemap_urls),
            "mapped_pages": len(routes),
            "unmapped_pages": 0,
            "non_sitemap_sources": len(manifest) - len(routes),
        },
        "routes": dict(sorted(routes.items())),
    }
    (destination / "url-index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return {"entries": len(manifest), "sitemap_urls": len(sitemap_urls)}


def file_hashes(root: Path) -> dict[str, str]:
    ignored = {"llms.txt", "manifest.json", "sitemap.xml", "url-index.json"}
    return {
        path.relative_to(root).as_posix(): sha256(path)
        for path in root.rglob("*")
        if path.is_file() and path.name not in ignored
    }


def diff_report(old: Path, new: Path, stats: dict) -> dict:
    before = file_hashes(old)
    after = file_hashes(new)
    added = sorted(after.keys() - before.keys())
    removed = sorted(before.keys() - after.keys())
    changed = sorted(path for path in before.keys() & after.keys() if before[path] != after[path])
    unchanged = sorted(path for path in before.keys() & after.keys() if before[path] == after[path])
    return {
        "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        **stats,
        "counts": {
            "added": len(added),
            "removed": len(removed),
            "changed": len(changed),
            "unchanged": len(unchanged),
        },
        "added": added,
        "removed": removed,
        "changed": changed,
        "unchanged": unchanged,
    }


def write_report(report: dict) -> None:
    SYNC_DIR.mkdir(exist_ok=True)
    (SYNC_DIR / "upstream-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    lines = [
        "# Upstream documentation diff",
        "",
        f"Generated: {report['generated_at']}",
        "",
        *[f"- {key}: {value}" for key, value in report["counts"].items()],
    ]
    for key in ("added", "removed", "changed"):
        lines.extend(["", f"## {key.title()}", ""])
        lines.extend(f"- `{path}`" for path in report[key])
    (SYNC_DIR / "upstream-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def next_branch(prefix: str) -> str:
    base = prefix + dt.date.today().isoformat()
    existing = set(git("branch", "--format=%(refname:short)", capture=True).splitlines())
    if base not in existing:
        return base
    index = 2
    while f"{base}-{index}" in existing:
        index += 1
    return f"{base}-{index}"


def prepare(args: argparse.Namespace, policy: dict) -> None:
    ensure_clean()
    base = args.base or policy["git"]["base_branch"]
    if current_branch() != base:
        raise SyncError(f"prepare must start on {base}; current branch is {current_branch()}")
    fetch_script = Path(args.fetch_script or ROOT / policy["upstream"]["fetch_script"]).resolve()
    if not fetch_script.is_file():
        raise SyncError(f"fetch script not found: {fetch_script}")

    with tempfile.TemporaryDirectory(prefix="counso-docs-sync-") as temporary:
        temp = Path(temporary)
        raw = temp / "raw"
        normalized = temp / "source"
        run(sys.executable, str(fetch_script), str(raw), "--workers", str(args.workers), "--skip-assets")
        stats = normalize_download(raw, normalized)
        report = diff_report(SOURCE_DIR, normalized, stats)
        branch = args.branch or next_branch(policy["git"]["branch_prefix"])
        git("switch", "-c", branch)
        backup = temp / "old-source"
        SOURCE_DIR.rename(backup)
        try:
            shutil.copytree(normalized, SOURCE_DIR)
        except Exception:
            if SOURCE_DIR.exists():
                shutil.rmtree(SOURCE_DIR)
            backup.rename(SOURCE_DIR)
            raise
        write_report(report)

    print(json.dumps({"branch": branch, "report": str(SYNC_DIR / "upstream-report.md"), **report["counts"]}, indent=2))


def tool_links(summary: Path) -> set[str]:
    pattern = re.compile(r"\([^)]*docs/user-documentation/agents/tools/([^/)]+)\.md\)")
    links = set(pattern.findall(summary.read_text(encoding="utf-8")))
    links.discard("index")
    return links


def visible_markdown(text: str) -> str:
    """Remove fenced code before applying prose-only terminology checks."""
    return re.sub(r"^\s*(```|~~~).*?^\s*\1\s*$", "", text, flags=re.M | re.S)


def miniapp_number_errors(page: Path) -> list[str]:
    text = visible_markdown(page.read_text(encoding="utf-8"))
    patterns = (
        r"\b(?:a|an|one|each|every|this|that)\s+MiniApps\b",
        r"\bMiniApps\s+(?:is|has|was)\b",
        r"\bMiniApp\s+(?:are|have|were)\b",
        r"(?:所有|多个|各个|这些|那些|若干)\s*MiniApp\b",
        r"(?:一个|单个|每个|这个|该)\s*MiniApps\b",
    )
    return [match.group(0) for pattern in patterns for match in re.finditer(pattern, text, re.I)]


def policy_checks(policy: dict) -> None:
    errors: list[str] = []
    config = load_json(ROOT / "mintlify-site" / "docs.json")
    expected_logo = policy["branding"]["logo"]
    if config.get("logo", {}).get("light") != expected_logo["light"]:
        errors.append("light logo differs from sync policy")
    if config.get("logo", {}).get("dark") != expected_logo["dark"]:
        errors.append("dark logo differs from sync policy")
    if config.get("favicon") != expected_logo["favicon"]:
        errors.append("favicon differs from sync policy")

    allowed = set(policy["agent_tools"]["navigation_allowlist"])
    for language in ("en", "zh-cn"):
        actual = tool_links(ROOT / language / "SUMMARY.md")
        unexpected = sorted(actual - allowed)
        missing = sorted(allowed - actual)
        if unexpected:
            errors.append(f"{language} exposes unsupported Agent Tools: {unexpected}")
        if missing:
            errors.append(f"{language} is missing allowed Agent Tools: {missing}")

    for content_root in (ROOT / "en", ROOT / "zh-cn", ROOT / "prepared"):
        for page in content_root.rglob("*.md"):
            if "/miniapps/" in page.read_text(encoding="utf-8"):
                errors.append(f"technical frames route renamed in {page.relative_to(ROOT)}")
            mismatches = miniapp_number_errors(page)
            if mismatches:
                errors.append(
                    f"MiniApp number mismatch in {page.relative_to(ROOT)}: {', '.join(mismatches)}"
                )

    if errors:
        raise SyncError("policy checks failed:\n- " + "\n- ".join(errors))
    print("sync policy: verified")


def verify(_args: argparse.Namespace, policy: dict) -> None:
    commands = (
        (sys.executable, "scripts/rebuild_api_assets.py"),
        (sys.executable, "scripts/reconcile_upstream.py"),
        (sys.executable, "scripts/check.py"),
        (sys.executable, "scripts/build_mintlify.py"),
        (sys.executable, "scripts/check_mintlify_navigation.py"),
        ("git", "diff", "--check"),
    )
    for command in commands:
        run(*command)
    policy_checks(policy)


def port_open(port: int) -> bool:
    with socket.socket() as connection:
        connection.settimeout(0.3)
        return connection.connect_ex(("127.0.0.1", port)) == 0


def preview(args: argparse.Namespace, policy: dict) -> None:
    port = args.port or policy["preview"]["port"]
    if port_open(port):
        print(f"preview already running: http://127.0.0.1:{port}")
        return
    SYNC_DIR.mkdir(exist_ok=True)
    log = (SYNC_DIR / "preview.log").open("ab")
    process = subprocess.Popen(
        ("npx", "mint", "dev", "--port", str(port)),
        cwd=ROOT / "mintlify-site",
        stdout=log,
        stderr=subprocess.STDOUT,
        start_new_session=True,
    )
    (SYNC_DIR / "preview.pid").write_text(str(process.pid) + "\n", encoding="utf-8")
    deadline = time.monotonic() + 60
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise SyncError(f"preview exited; inspect {SYNC_DIR / 'preview.log'}")
        if port_open(port):
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=5) as response:
                if response.status == 200:
                    print(f"preview: http://127.0.0.1:{port}")
                    return
        time.sleep(1)
    raise SyncError(f"preview did not become ready; inspect {SYNC_DIR / 'preview.log'}")


def finalize(args: argparse.Namespace, policy: dict) -> None:
    if not args.reviewed:
        raise SyncError("finalize requires --reviewed after the user approves the local preview")
    base = policy["git"]["base_branch"]
    branch = current_branch()
    if not branch.startswith(policy["git"]["branch_prefix"]):
        raise SyncError(f"current branch is not a sync branch: {branch}")
    if int(git("rev-list", "--count", f"{base}..HEAD", capture=True)) != 0:
        raise SyncError("sync branch already has commits; finalization requires exactly one new sync commit")
    tag = args.tag or policy["git"]["tag_prefix"] + dt.date.today().isoformat()
    if git("tag", "--list", tag, capture=True):
        raise SyncError(f"tag already exists: {tag}")
    assert_upstream_snapshot_current(policy)
    verify(args, policy)
    git("add", "-A")
    staged = subprocess.run(
        ("git", "diff", "--cached", "--quiet"), cwd=ROOT, check=False
    ).returncode
    if staged == 0:
        raise SyncError("there are no synchronized changes to commit")
    if staged != 1:
        raise SyncError("git could not inspect staged synchronization changes")
    message = args.message or f"Sync Counso docs from upstream ({dt.date.today().isoformat()})"
    git("commit", "-m", message)
    if int(git("rev-list", "--count", f"{base}..HEAD", capture=True)) != 1:
        raise SyncError("sync branch does not contain exactly one commit")
    git("switch", base)
    git("merge", "--ff-only", branch)
    git("tag", "-a", tag, "-m", message)
    print(json.dumps({"merged_branch": branch, "base": base, "tag": tag}, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    prepare_parser = subparsers.add_parser("prepare", help="create a branch and fetch a normalized upstream snapshot")
    prepare_parser.add_argument("--base")
    prepare_parser.add_argument("--branch")
    prepare_parser.add_argument("--fetch-script")
    prepare_parser.add_argument("--workers", type=int, default=10)
    subparsers.add_parser("verify", help="rebuild and validate the branded bilingual site")
    preview_parser = subparsers.add_parser("preview", help="start the local Mintlify preview")
    preview_parser.add_argument("--port", type=int)
    finalize_parser = subparsers.add_parser("finalize", help="commit once, fast-forward main, and create an annotated tag")
    finalize_parser.add_argument("--reviewed", action="store_true")
    finalize_parser.add_argument("--tag")
    finalize_parser.add_argument("--message")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    policy = load_json(POLICY_PATH)
    try:
        globals()[args.command](args, policy)
    except (SyncError, subprocess.CalledProcessError, OSError) as error:
        print(f"sync error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
