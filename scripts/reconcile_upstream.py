#!/usr/bin/env python3
"""Reconcile the branded release package with the current upstream source snapshot."""

from __future__ import annotations

import copy
import hashlib
import json
import re
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
TRANSLATIONS = ROOT / "translations.json"
REDIRECTS = ROOT / "redirects.json"
SYNC_POLICY = ROOT / "sync-policy.json"
CHINESE_PREFIX = "/zh-Hans"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def branded_path(value: str) -> str:
    return re.sub(r"(?<![A-Za-z0-9])dust(?![A-Za-z0-9])", "counso", value, flags=re.I)


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


def route_for(entry: dict) -> str:
    url = official_url(entry)
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc == "docs.dust.tt":
        return branded_path(parsed.path or "/")
    return "/" + branded_path(entry["path"])


def api_metadata(entry: dict) -> dict | None:
    if not entry["path"].startswith("api-reference/"):
        return None
    text = (SOURCE / entry["path"]).read_text(encoding="utf-8")
    match = re.search(r"^````yaml\s+\S+\s+(get|post|put|patch|delete|head|options)\s+([^\s]+)", text, re.M)
    if not match:
        raise RuntimeError(f"cannot find API operation in {entry['path']}")
    method, path = match.groups()
    auth = "webhook" if "/triggers/hooks/" in path else "workspace"
    return {"path": path, "method": method, "auth": auth}


def new_page(entry: dict) -> dict:
    url = official_url(entry)
    route = route_for(entry)
    path = branded_path(entry["path"])
    base = {
        "original_url": url,
        "original_file": "source/" + entry["path"],
        "original_repository_path": entry["path"],
        "original_sha256": digest(SOURCE / entry["path"]),
        "original_source": "source/" + entry["path"],
        "in_sitemap": url in SITEMAP_URLS,
        "original_title": entry["title"],
    }
    if entry["path"] == "docs/user-documentation/agents/tools/servicenow.md":
        base.update(
            {
                "status": "updating",
                "reason": "Counso 的 ServiceNow 工具、OAuth 回调和读写权限流程尚待部署验证。",
                "translations": None,
                "notice": {
                    "en": {"file": "en/UPDATING.md", "route": route, "title": "Documentation update"},
                    "zh-cn": {"file": "zh-cn/UPDATING.md", "route": CHINESE_PREFIX + route, "title": "文档更新中"},
                },
                "prepared": {
                    "en": {
                        "file": "prepared/en/" + path,
                        "route": route,
                        "title": "ServiceNow",
                    },
                    "zh-cn": {
                        "file": "prepared/zh-cn/" + path,
                        "route": CHINESE_PREFIX + route,
                        "title": "ServiceNow",
                    },
                },
            }
        )
        return base

    titles = {
        "api-reference/analytics/export-consumption-analytics.md": ("Export consumption analytics", "导出消费分析数据"),
        "docs/user-documentation/agents/frames/overview.md": ("MiniApps overview", "MiniApps 概览"),
    }
    en_title, zh_title = titles[entry["path"]]
    base.update(
        {
            "status": "publish",
            "reason": "提供中英文正文。",
            "translations": {
                "en": {"title": en_title, "file": "en/" + path, "route": route},
                "zh-cn": {"title": zh_title, "file": "zh-cn/" + path, "route": CHINESE_PREFIX + route},
            },
        }
    )
    api = api_metadata(entry)
    if api:
        base["api"] = api
    return base


def update_page(row: dict, entry: dict) -> dict:
    row = copy.deepcopy(row)
    url = official_url(entry)
    row.update(
        {
            "original_url": url,
            "original_file": "source/" + entry["path"],
            "original_repository_path": entry["path"],
            "original_sha256": digest(SOURCE / entry["path"]),
            "original_source": "source/" + entry["path"],
            "in_sitemap": url in SITEMAP_URLS,
            "original_title": entry["title"],
        }
    )
    api = api_metadata(entry)
    if api:
        row["api"] = api
    else:
        row.pop("api", None)
    return row


def force_updating(row: dict, entry: dict, reason: str) -> dict:
    """Move a published bilingual pair to prepared/ and retain its public routes as notices."""
    row = copy.deepcopy(row)
    route = route_for(entry)
    translations = row.get("translations") or {}
    prepared = copy.deepcopy(row.get("prepared") or {})
    for language in ("en", "zh-cn"):
        target_relative = "prepared/" + language + "/" + branded_path(entry["path"])
        target = ROOT / target_relative
        published = translations.get(language)
        if published:
            source = ROOT / published["file"]
            target.parent.mkdir(parents=True, exist_ok=True)
            source.replace(target)
            title = published["title"]
        else:
            title = prepared[language]["title"]
        prepared[language] = {
            "file": target_relative,
            "route": route if language == "en" else CHINESE_PREFIX + route,
            "title": title,
        }
    row.update(
        {
            "status": "updating",
            "reason": reason,
            "translations": None,
            "notice": {
                "en": {
                    "file": "en/UPDATING.md",
                    "route": route,
                    "title": "Documentation update",
                },
                "zh-cn": {
                    "file": "zh-cn/UPDATING.md",
                    "route": CHINESE_PREFIX + route,
                    "title": "文档更新中",
                },
            },
            "prepared": prepared,
        }
    )
    return row


def referenced_files(row: dict) -> set[str]:
    result: set[str] = set()
    for field in ("translations", "prepared"):
        for value in (row.get(field) or {}).values():
            result.add(value["file"])
    return result


def refresh_hashes(row: dict) -> None:
    for field in ("translations", "notice", "prepared"):
        for value in (row.get(field) or {}).values():
            value["sha256"] = digest(ROOT / value["file"])


def filter_summary(path: Path) -> None:
    language_root = path.parent
    output: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^- \[([^]]+)]\(([^)]+)\)$", line)
        if match and not (language_root / match.group(2)).is_file():
            continue
        output.append(line)
    text = "\n".join(output) + "\n"
    additions = {
        "en": [
            ("- [Add your brand to shared MiniApps](docs/user-documentation/agents/frames/white-labeled-frames.md)", "- [MiniApps overview](docs/user-documentation/agents/frames/overview.md)"),
            ("- [Export workspace analytics](api-reference/analytics/export-workspace-analytics.md)", "- [Export consumption analytics](api-reference/analytics/export-consumption-analytics.md)"),
        ],
        "zh-cn": [
            ("- [为共享 MiniApp 添加品牌信息](docs/user-documentation/agents/frames/white-labeled-frames.md)", "- [MiniApps 概览](docs/user-documentation/agents/frames/overview.md)"),
            ("- [导出工作区分析数据](api-reference/analytics/export-workspace-analytics.md)", "- [导出消费分析数据](api-reference/analytics/export-consumption-analytics.md)"),
        ],
    }[path.parent.name]
    for anchor, addition in additions:
        if addition not in text:
            text = text.replace(anchor, addition + "\n" + anchor)
    lines = text.splitlines()
    cleaned: list[str] = []
    for index, line in enumerate(lines):
        if line.startswith("### "):
            end = next(
                (i for i in range(index + 1, len(lines)) if lines[i].startswith(("## ", "### "))),
                len(lines),
            )
            if not any(candidate.startswith("- [") for candidate in lines[index + 1 : end]):
                continue
        if line.startswith("## "):
            end = next(
                (i for i in range(index + 1, len(lines)) if lines[i].startswith("## ")),
                len(lines),
            )
            if not any(candidate.startswith("- [") for candidate in lines[index + 1 : end]):
                continue
        if not line and cleaned and not cleaned[-1]:
            continue
        cleaned.append(line)
    while cleaned and not cleaned[-1]:
        cleaned.pop()
    path.write_text("\n".join(cleaned) + "\n", encoding="utf-8")


data = read_json(TRANSLATIONS)
manifest = read_json(SOURCE / "manifest.json")
index = read_json(SOURCE / "url-index.json")
sync_policy = read_json(SYNC_POLICY)
hidden_pages = sync_policy["publication"].get("hidden_pages", {})
SITEMAP_URLS = set(index["routes"])
old_rows = {row["original_url"]: row for row in data["pages"]}
new_urls = {official_url(entry) for entry in manifest}

for url, row in old_rows.items():
    if url in new_urls:
        continue
    for relative in referenced_files(row):
        path = ROOT / relative
        if path.name != "UPDATING.md" and path.exists():
            path.unlink()

pages = []
for entry in manifest:
    url = official_url(entry)
    row = update_page(old_rows[url], entry) if url in old_rows else new_page(entry)
    if entry["path"] in hidden_pages:
        row = force_updating(row, entry, hidden_pages[entry["path"]])
    pages.append(row)

for row in pages:
    refresh_hashes(row)

counts = Counter(row["status"] for row in pages)
data["source"]["manifest"] = "source/manifest.json"
data["source"]["url_index"] = "source/url-index.json"
data["source"]["sitemap"] = "source/sitemap.xml"
data["counts"] = {
    "source_files": len(pages),
    "sitemap_urls": sum(row["in_sitemap"] for row in pages),
    **dict(counts),
}
data["pages"] = pages

for artifact in data.get("artifacts", []):
    for value in artifact["translations"].values():
        value["sha256"] = digest(ROOT / value["file"])

write_json(TRANSLATIONS, data)
filter_summary(ROOT / "en/SUMMARY.md")
filter_summary(ROOT / "zh-cn/SUMMARY.md")

valid_routes = set()
for row in pages:
    entries = row.get("translations") or row.get("notice") or {}
    valid_routes.update(value["route"] for value in entries.values())
for artifact in data.get("artifacts", []):
    valid_routes.update(value["route"] for value in artifact["translations"].values())
redirects = read_json(REDIRECTS)
redirects["redirects"] = [
    item for item in redirects["redirects"] if item["from"] == "/" or item["to"] in valid_routes
]
write_json(REDIRECTS, redirects)

print(
    json.dumps(
        {
            "pages": len(pages),
            "counts": data["counts"],
            "redirects": len(redirects["redirects"]),
        },
        ensure_ascii=False,
        indent=2,
    )
)
