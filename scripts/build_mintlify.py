#!/usr/bin/env python3
"""Build a self-contained Mintlify content directory from the release package."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "mintlify-site"
MARKER = OUTPUT / ".generated-by-counso-docs"

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
LEGACY_BRAND_RE = re.compile(r"(?i)(?:\bdust\b|dust-tt|dustapi)")

VIRTUAL_GROUP_TITLES = {
    "en": {
        "general-questions": "General questions",
        "managing-agents": "Agents and conversations",
        "troubleshooting-and-limitations": "Troubleshooting",
        "llm-best-practices": "LLM best practices",
        "data-sources": "Data sources",
        "conversation-files": "Conversation files",
        "triggers": "Triggers",
        "webhooks": "Webhooks",
        "examples": "Examples",
        "admin-governance": "Governance and access",
        "single-sign-on-sso": "Single sign-on (SSO)",
        "tools-management": "Tool management",
        "salesforce": "Salesforce",
        "audit-logs": "Audit logs",
        "usage-seats-and-credits": "Usage, seats, and credits",
    },
    "zh-Hans": {
        "general-questions": "一般问题",
        "managing-agents": "智能体与对话",
        "troubleshooting-and-limitations": "故障排除",
        "llm-best-practices": "大语言模型最佳实践",
        "data-sources": "数据源",
        "conversation-files": "对话文件",
        "triggers": "触发器",
        "webhooks": "Webhook",
        "examples": "示例",
        "admin-governance": "治理与访问权限",
        "single-sign-on-sso": "单点登录（SSO）",
        "tools-management": "工具管理",
        "salesforce": "Salesforce",
        "audit-logs": "审计日志",
        "usage-seats-and-credits": "用量、席位与积分",
    },
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def strip_first_heading(markdown: str) -> str:
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        if line.startswith("# "):
            del lines[index]
        break
    return "\n".join(lines).strip() + "\n"


def with_frontmatter(markdown: str, title: str, description: str | None = None) -> str:
    fields = ["---", f"title: {yaml_string(title)}"]
    if description:
        fields.append(f"description: {yaml_string(description)}")
    fields.extend(["---", ""])
    body = strip_first_heading(markdown).replace("<br>", "<br />")
    return "\n".join(fields) + body


def route_to_file(route: str, suffix: str = ".md") -> Path:
    route = route.strip("/") or "index"
    if route.endswith("/index"):
        route = route[: -len("/index")]
    return OUTPUT / f"{route}{suffix}"


def page_id(route: str) -> str:
    return route.strip("/") or "index"


def route_to_asset(route: str) -> Path:
    return OUTPUT / route.strip("/")


def rewrite_links(
    markdown: str,
    source_file: Path,
    file_routes: dict[str, str],
    asset_routes: dict[str, str],
) -> str:
    source_rel = source_file.relative_to(ROOT).as_posix()

    def replace(match: re.Match[str]) -> str:
        label, target = match.groups()
        if target.startswith(("http://", "https://", "mailto:", "#", "/")):
            return match.group(0)

        path_part, separator, fragment = target.partition("#")
        if not path_part.endswith((".md", ".mdx", ".json")):
            return match.group(0)

        resolved = (PurePosixPath(source_rel).parent / path_part)
        normalized_parts: list[str] = []
        for part in resolved.parts:
            if part == "..":
                if normalized_parts:
                    normalized_parts.pop()
            elif part != ".":
                normalized_parts.append(part)
        resolved_key = PurePosixPath(*normalized_parts).as_posix()
        route = (
            asset_routes.get(resolved_key)
            if path_part.endswith(".json")
            else file_routes.get(resolved_key)
        )
        if not route:
            return match.group(0)
        suffix = f"#{fragment}" if separator else ""
        return f"[{label}]({route}{suffix})"

    return LINK_RE.sub(replace, markdown)


def nest_navigation_pages(
    routes: list[str],
    route_titles: dict[str, str],
    language: str,
    base: str | None = None,
):
    """Turn both page roots and shared directories into collapsed navigation groups."""
    nested: list[str | dict] = []
    remaining = set(routes)

    for route in routes:
        if route not in remaining:
            continue

        descendants = [
            candidate
            for candidate in routes
            if candidate in remaining and candidate.startswith(f"{route}/")
        ]
        if descendants:
            remaining.remove(route)
            remaining.difference_update(descendants)
            nested.append(
                {
                    "group": route_titles.get(route, route.rsplit("/", 1)[-1].replace("-", " ").title()),
                    "root": route,
                    "expanded": False,
                    "pages": nest_navigation_pages(descendants, route_titles, language, route),
                }
            )
            continue

        parts = route.split("/")
        base_depth = len(base.split("/")) if base else 0
        virtual_branch = None
        virtual_title = None
        virtual_prefix = None
        for depth in range(base_depth + 1, len(parts)):
            segment = parts[depth - 1]
            title = VIRTUAL_GROUP_TITLES.get(language, {}).get(segment)
            if not title:
                continue
            prefix = "/".join(parts[:depth])
            branch = [
                candidate
                for candidate in routes
                if candidate in remaining and candidate.startswith(f"{prefix}/")
            ]
            if len(branch) >= 2:
                virtual_branch = branch
                virtual_title = title
                virtual_prefix = prefix
                break

        if virtual_branch and virtual_title and virtual_prefix:
            remaining.difference_update(virtual_branch)
            nested.append(
                {
                    "group": virtual_title,
                    "expanded": False,
                    "pages": nest_navigation_pages(
                        virtual_branch, route_titles, language, virtual_prefix
                    ),
                }
            )
        else:
            remaining.remove(route)
            nested.append(route)

    return nested


def parse_summary(
    path: Path,
    prefix: str,
    file_routes: dict[str, str],
    route_titles: dict[str, str],
    language: str,
    home: str,
):
    groups: list[dict] = [{"group": "Counso Docs" if prefix == "en" else "Counso 文档", "pages": [home]}]
    current: dict | None = None
    container: dict | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            current = {"group": line[3:].strip(), "pages": []}
            groups.append(current)
            container = current
            continue
        if line.startswith("### ") and current is not None:
            container = {"group": line[4:].strip(), "expanded": False, "pages": []}
            current["pages"].append(container)
            continue
        match = re.match(r"^- \[[^\]]+\]\(([^)]+)\)$", line)
        if not match or container is None:
            continue
        linked = (PurePosixPath(prefix) / match.group(1)).as_posix()
        route = file_routes.get(linked)
        if route:
            container["pages"].append(page_id(route))

    def organize(items: list[str | dict]):
        organized: list[str | dict] = []
        pending: list[str] = []

        def flush() -> None:
            if pending:
                organized.extend(nest_navigation_pages(pending, route_titles, language))
                pending.clear()

        for item in items:
            if isinstance(item, str):
                pending.append(item)
                continue
            flush()
            item["pages"] = organize(item["pages"])
            organized.append(item)
        flush()
        return organized

    for group in groups:
        group["pages"] = organize(group["pages"])
    return [group for group in groups if group["pages"]]


def reshape_developer_navigation(groups: list[dict], language: str) -> list[dict]:
    """Match the official site's compact Developers hierarchy."""
    labels = {
        "en": {
            "source": "Developer documentation",
            "target": "Developers",
            "api": "API reference",
            "overview": "Overview",
            "core": "Core concepts",
            "api_docs": "Counso API documentation",
            "cli": "Counso CLI",
            "prefix": "",
        },
        "zh-Hans": {
            "source": "开发者文档",
            "target": "开发者",
            "api": "API 参考",
            "overview": "概览",
            "core": "核心概念",
            "api_docs": "Counso API 文档",
            "cli": "Counso CLI",
            "prefix": "zh-cn/",
        },
    }[language]

    developer = next((g for g in groups if g.get("group") == labels["source"]), None)
    api_reference = next((g for g in groups if g.get("group") == labels["api"]), None)
    if not developer or not api_reference:
        return groups

    flat_pages = [item for item in developer["pages"] if isinstance(item, str)]

    def matching(fragment: str) -> list[str]:
        return [page for page in flat_pages if fragment in page]

    top_pages = matching("/developers/client-side-mcp-server")
    overview_pages = matching("/developer-platform/overview/")
    core_pages = matching("/developer-platform/core-concepts/")
    specification_pages = matching(
        "/developer-platform/counso-api-documentation/openapi-and-postman"
    )
    cli_page = f'{labels["prefix"]}docs/developer-platform/counso-cli/counso-cli'

    developer["group"] = labels["target"]
    developer["pages"] = [
        *top_pages,
        {
            "group": labels["overview"],
            "expanded": False,
            "pages": overview_pages,
        },
        {
            "group": labels["core"],
            "expanded": False,
            "pages": core_pages,
        },
        {
            "group": labels["api_docs"],
            "expanded": False,
            "pages": [*specification_pages, *api_reference["pages"]],
        },
        {
            "group": labels["cli"],
            "expanded": False,
            "pages": [cli_page],
        },
    ]
    developer["pages"] = [
        item for item in developer["pages"] if not isinstance(item, dict) or item["pages"]
    ]
    return [group for group in groups if group is not api_reference]


def copy_downloadable_assets(skipped_files: set[str]) -> int:
    copied = 0
    for language_dir in ("en", "zh-cn"):
        source_root = ROOT / language_dir
        for source in source_root.rglob("*.json"):
            if source.relative_to(ROOT).as_posix() in skipped_files:
                continue
            relative = source.relative_to(source_root)
            target = OUTPUT / relative if language_dir == "en" else OUTPUT / "zh-cn" / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            copied += 1
    return copied


def write_logo_files() -> None:
    logo_dir = OUTPUT / "logo"
    logo_dir.mkdir(parents=True, exist_ok=True)
    light = """<svg xmlns="http://www.w3.org/2000/svg" width="176" height="36" viewBox="0 0 176 36" role="img" aria-label="Counso AI">
  <rect x="1" y="1" width="34" height="34" rx="10" fill="#0C84FE"/>
  <path d="M12 12h12M12 18h8M12 24h12" fill="none" stroke="white" stroke-width="2.6" stroke-linecap="round"/>
  <circle cx="25" cy="18" r="3" fill="white"/>
  <text x="45" y="24" fill="#111827" font-family="Inter, ui-sans-serif, system-ui" font-size="20" font-weight="700">Counso AI</text>
</svg>
"""
    dark = light.replace('fill="#111827"', 'fill="#F8FAFC"')
    favicon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 36 36">
  <rect x="1" y="1" width="34" height="34" rx="10" fill="#0C84FE"/>
  <path d="M12 12h12M12 18h8M12 24h12" fill="none" stroke="white" stroke-width="2.6" stroke-linecap="round"/>
  <circle cx="25" cy="18" r="3" fill="white"/>
</svg>
"""
    (logo_dir / "light.svg").write_text(light, encoding="utf-8")
    (logo_dir / "dark.svg").write_text(dark, encoding="utf-8")
    (OUTPUT / "favicon.svg").write_text(favicon, encoding="utf-8")


def write_home_pages() -> None:
    english = """---
title: "Counso Docs"
description: "Guides for using Counso AI, Agents, Skills, Knowledge, integrations, Pods, and workspace administration."
mode: wide
---

# Build better work with Counso AI

Learn how to use Counso AI, connect trusted knowledge, create Agents and Skills, and manage your workspace.

<CardGroup cols={2}>
  <Card title="Getting started" icon="rocket" href="/docs/user-documentation/getting-started/intro-to-counso">
    Set up your workspace and begin your first useful workflow.
  </Card>
  <Card title="Agents" icon="sparkles" href="/docs/user-documentation/agents/create-your-first-agent">
    Create, configure, test, and share Agents for repeatable work.
  </Card>
  <Card title="Capabilities" icon="shapes" href="/docs/user-documentation/agents/knowledge">
    Work with knowledge, tools, data sources, automations, and integrations.
  </Card>
  <Card title="Administration" icon="users-gear" href="/docs/user-documentation/admins/quickstart">
    Manage access, connections, governance, usage, and billing.
  </Card>
  <Card title="Developer documentation" icon="code" href="/docs/developer-platform/overview/developer-platform">
    Build integrations and applications with Counso's developer platform.
  </Card>
  <Card title="API reference" icon="plug" href="/api-reference/agents/list-agents">
    Explore API endpoints, request parameters, and response formats.
  </Card>
</CardGroup>
"""
    chinese = """---
title: "Counso 使用文档"
description: "了解 Counso AI、智能体、技能、知识、集成、Pod 和工作区管理。"
mode: wide
---

# 使用 Counso AI 完成更好的工作

了解如何使用 Counso AI、连接可信知识、创建智能体和技能，以及管理工作区。

<CardGroup cols={2}>
  <Card title="开始使用" icon="rocket" href="/zh-cn/docs/user-documentation/getting-started/intro-to-counso">
    设置工作区，并开始第一个实用工作流。
  </Card>
  <Card title="智能体" icon="sparkles" href="/zh-cn/docs/user-documentation/agents/create-your-first-agent">
    创建、配置、测试并共享可重复使用的智能体。
  </Card>
  <Card title="产品能力" icon="shapes" href="/zh-cn/docs/user-documentation/agents/knowledge">
    使用知识、工具、数据源、自动化和集成。
  </Card>
  <Card title="工作区管理" icon="users-gear" href="/zh-cn/docs/user-documentation/admins/quickstart">
    管理访问权限、连接、治理、用量和账单。
  </Card>
  <Card title="开发者文档" icon="code" href="/zh-cn/docs/developer-platform/overview/developer-platform">
    使用 Counso 开发者平台构建集成与应用。
  </Card>
  <Card title="API 参考" icon="plug" href="/zh-cn/api-reference/agents/list-agents">
    查看 API 端点、请求参数与响应格式。
  </Card>
</CardGroup>
"""
    (OUTPUT / "index.mdx").write_text(english, encoding="utf-8")
    zh_home = OUTPUT / "zh-cn" / "index.mdx"
    zh_home.parent.mkdir(parents=True, exist_ok=True)
    zh_home.write_text(chinese, encoding="utf-8")


def write_custom_css() -> None:
    css = """/* Keep the classic Mintlify layout used by docs.dust.tt, with Counso branding. */
:root {
  --counso-blue: #0c84fe;
}

#navbar {
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
}

#sidebar-content li[data-active] > a {
  font-weight: 650;
}

card {
  border-radius: 0.85rem;
  transition: border-color 160ms ease, transform 160ms ease, box-shadow 160ms ease;
}

card:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 28px rgb(12 132 254 / 10%);
}

img.nav-logo {
  height: 2rem !important;
  width: auto !important;
}
"""
    (OUTPUT / "style.css").write_text(css, encoding="utf-8")


def main() -> None:
    translations = load_json(ROOT / "translations.json")
    redirects_source = load_json(ROOT / "redirects.json")

    if OUTPUT.exists():
        if not MARKER.exists():
            raise SystemExit(f"refusing to replace unmarked output directory: {OUTPUT}")
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    MARKER.write_text("Generated by scripts/build_mintlify.py\n", encoding="utf-8")

    file_routes: dict[str, str] = {}
    asset_routes: dict[str, str] = {}
    route_titles: dict[str, str] = {}
    for page in translations["pages"]:
        if page["status"] != "publish":
            continue
        for translation in page["translations"].values():
            file_routes[translation["file"]] = translation["route"]
            route_titles[page_id(translation["route"])] = translation["title"]

    for language_dir in ("en", "zh-cn"):
        source_root = ROOT / language_dir
        for source in source_root.rglob("*.json"):
            source_key = source.relative_to(ROOT).as_posix()
            relative = source.relative_to(source_root).as_posix()
            asset_routes[source_key] = (
                f"/{relative}" if language_dir == "en" else f"/zh-cn/{relative}"
            )

    legacy_brand_files: set[str] = set()
    legacy_brand_routes: set[str] = set()
    for page in translations["pages"]:
        if page["status"] != "publish":
            continue
        for translation in page["translations"].values():
            source = ROOT / translation["file"]
            if source.exists() and LEGACY_BRAND_RE.search(source.read_text(encoding="utf-8")):
                legacy_brand_files.add(translation["file"])
                legacy_brand_routes.add(translation["route"])

    published = 0
    notices = 0
    brand_review_notices = 0
    for page in translations["pages"]:
        if page["status"] == "publish":
            for translation in page["translations"].values():
                source = ROOT / translation["file"]
                if translation["route"] in legacy_brand_routes:
                    is_english = translation["route"].startswith("/docs/") or translation[
                        "route"
                    ].startswith("/api-reference/")
                    notice_source = ROOT / ("en/UPDATING.md" if is_english else "zh-cn/UPDATING.md")
                    target = route_to_file(translation["route"])
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(
                        with_frontmatter(
                            notice_source.read_text(encoding="utf-8"),
                            "Documentation update" if is_english else "文档更新中",
                            "This documentation is being updated."
                            if is_english
                            else "此文档正在更新。",
                        ),
                        encoding="utf-8",
                    )
                    notices += 1
                    brand_review_notices += 1
                    continue
                if translation.get("format") != "markdown" and source.suffix not in (".md", ".mdx"):
                    continue
                body = rewrite_links(
                    source.read_text(encoding="utf-8"), source, file_routes, asset_routes
                )
                target = route_to_file(translation["route"])
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(with_frontmatter(body, translation["title"]), encoding="utf-8")
                published += 1
        elif page["status"] == "updating":
            for notice in page["notice"].values():
                source = ROOT / notice["file"]
                target = route_to_file(notice["route"])
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    with_frontmatter(
                        source.read_text(encoding="utf-8"),
                        notice["title"],
                        "This documentation is being updated." if notice["route"].startswith("/docs/") else "此文档正在更新。",
                    ),
                    encoding="utf-8",
                )
                notices += 1

    downloadable_assets = copy_downloadable_assets(legacy_brand_files)

    english_groups = parse_summary(
        ROOT / "en" / "SUMMARY.md", "en", file_routes, route_titles, "en", "index"
    )
    chinese_groups = parse_summary(
        ROOT / "zh-cn" / "SUMMARY.md",
        "zh-cn",
        file_routes,
        route_titles,
        "zh-Hans",
        "zh-cn/index",
    )
    english_groups = reshape_developer_navigation(english_groups, "en")
    chinese_groups = reshape_developer_navigation(chinese_groups, "zh-Hans")

    redirects = []
    seen_redirects: set[tuple[str, str]] = set()
    for item in redirects_source["redirects"]:
        source, destination = item["from"], item["to"]
        if source == "/":
            continue
        key = (source, destination)
        if key in seen_redirects:
            continue
        seen_redirects.add(key)
        redirects.append({"source": source, "destination": destination, "permanent": True})

    config = {
        "$schema": "https://mintlify.com/docs.json",
        "theme": "mint",
        "name": "Counso AI",
        "description": "Counso AI product documentation, guides, integrations, and workspace administration.",
        "colors": {"primary": "#0C84FE", "light": "#9FDBFF", "dark": "#0C84FE"},
        "logo": {"light": "/logo/light.svg", "dark": "/logo/dark.svg", "href": "/"},
        "favicon": "/favicon.svg",
        "appearance": {"default": "system", "strict": False},
        "icons": {"library": "fontawesome"},
        "styling": {"eyebrows": "section", "latex": True, "codeblocks": "system"},
        "thumbnails": {"appearance": "light"},
        "navbar": {
            "links": [
                {
                    "label": "GitHub",
                    "href": "https://github.com/zCloak-Network/counso-docs",
                }
            ],
            "primary": {"type": "button", "label": "Open Counso AI", "href": "https://app.counso.ai"},
        },
        "search": {"prompt": "Search Counso documentation..."},
        "seo": {"indexing": "navigable", "trailingSlash": False},
        "interaction": {"drilldown": False},
        "navigation": {
            "languages": [
                {"language": "en", "default": True, "groups": english_groups},
                {"language": "zh-Hans", "groups": chinese_groups},
            ]
        },
        "redirects": redirects,
    }
    (OUTPUT / "docs.json").write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_logo_files()
    write_home_pages()
    write_custom_css()

    print(
        json.dumps(
            {
                "output": str(OUTPUT),
                "published_pages": published,
                "updating_pages": notices,
                "brand_review_pages": brand_review_notices,
                "downloadable_assets": downloadable_assets,
                "redirects": len(redirects),
                "english_navigation_groups": len(english_groups),
                "chinese_navigation_groups": len(chinese_groups),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
