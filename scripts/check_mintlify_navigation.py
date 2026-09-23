#!/usr/bin/env python3
"""Regression check for collapsible Mintlify navigation."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "mintlify-site" / "docs.json"
CHINESE_LANGUAGE = "zh-Hans"
CHINESE_ROUTE_PREFIX = "/zh-Hans"
LEGACY_CHINESE_ROUTE_PREFIX = "/zh-cn"


def walk_groups(items):
    for item in items:
        if not isinstance(item, dict):
            continue
        yield item
        yield from walk_groups(item.get("pages", []))


config = json.loads(CONFIG.read_text(encoding="utf-8"))
languages = config["navigation"]["languages"]


def navigation_pages(items):
    for item in items:
        if isinstance(item, str):
            yield item
        elif isinstance(item, dict):
            yield from navigation_pages(item.get("pages", []))

expected = {
    "en": (
        "docs/user-documentation/getting-started/use-cases-and-guides",
        "docs/user-documentation/getting-started/use-cases-and-guides/sales",
        "docs/user-documentation/getting-started/faq",
        {
            "General questions",
            "Agents and conversations",
            "Troubleshooting",
        },
    ),
    CHINESE_LANGUAGE: (
        "zh-Hans/docs/user-documentation/getting-started/use-cases-and-guides",
        "zh-Hans/docs/user-documentation/getting-started/use-cases-and-guides/sales",
        "zh-Hans/docs/user-documentation/getting-started/faq",
        {
            "一般问题",
            "智能体与对话",
            "故障排除",
        },
    ),
}

for language in languages:
    code = language["language"]
    page_routes = set(navigation_pages(language["groups"]))
    route_prefix = "" if code == "en" else "zh-Hans/"
    assert route_prefix + "docs/user-documentation/agents/frames/overview" in page_routes, (
        f"{code}: MiniApps overview is missing from navigation"
    )
    assert route_prefix + "docs/user-documentation/agents/tools/servicenow" not in page_routes, (
        f"{code}: unverified ServiceNow tool leaked into navigation"
    )
    assert not any("/miniapps/" in route for route in page_routes), (
        f"{code}: technical /frames/ route was renamed"
    )
    root, child, faq_root, faq_subgroups = expected[code]
    all_groups = list(walk_groups(language["groups"]))
    nested = [group for group in all_groups if group.get("root") == root]
    assert nested, f"{code}: use-cases root is still flat"
    assert child in nested[0]["pages"], f"{code}: sales is not nested under use cases"
    assert nested[0].get("expanded") is False, f"{code}: nested group must default to collapsed"
    faq = next(group for group in all_groups if group.get("root") == faq_root)
    faq_groups = list(walk_groups(faq["pages"]))
    faq_names = {group.get("group") for group in faq_groups}
    assert faq_subgroups <= faq_names, f"{code}: FAQ subgroups are still flat"
    for group in faq_groups:
        if group.get("group") in faq_subgroups:
            assert group.get("expanded") is False, f"{code}: FAQ subgroup must default to collapsed"
    all_names = {group.get("group") for group in all_groups}
    assert not ({"Docs", "User Documentation", "Admins"} & all_names), (
        f"{code}: technical path segments leaked into navigation"
    )

    developer_title = "Developers" if code == "en" else "开发者"
    api_title = "Counso API documentation" if code == "en" else "Counso API 文档"
    agents_title = "Agents" if code == "en" else "智能体"
    developer_group = next(
        group for group in language["groups"] if group.get("group") == developer_title
    )
    developer_subgroups = list(walk_groups(developer_group["pages"]))
    api_group = next(group for group in developer_subgroups if group.get("group") == api_title)
    api_subgroups = list(walk_groups(api_group["pages"]))
    assert any(group.get("group") == agents_title for group in api_subgroups), (
        f"{code}: API categories are still flat"
    )
    assert not any(group.get("group") in {"API reference", "API 参考"} for group in language["groups"]), (
        f"{code}: API reference should be nested under Developers"
    )

for prefix in ("", "zh-Hans/"):
    asset_dir = ROOT / "mintlify-site" / prefix / "docs/developer-platform/counso-api-documentation"
    for filename in ("postman.collection.json", "postman.environment.json"):
        asset = asset_dir / filename
        assert asset.exists(), f"missing downloadable API asset: {asset.relative_to(ROOT)}"
        json.loads(asset.read_text(encoding="utf-8"))
    for filename in ("openapi.json", "swagger.json"):
        asset = asset_dir / filename
        assert asset.exists(), f"missing downloadable API asset: {asset.relative_to(ROOT)}"
        spec = json.loads(asset.read_text(encoding="utf-8"))
        assert spec["servers"] == [{"url": "https://app.counso.ai", "description": "Counso"}], (
            f"unbranded API server in {asset.relative_to(ROOT)}"
        )

legacy_brand = re.compile(r"(?i)(?:\bdust\b|dust-tt|dustapi)")
for pattern in ("*.md", "*.mdx"):
    for page in (ROOT / "mintlify-site").rglob(pattern):
        visible = re.sub(
            r"^\s*(```|~~~).*?^\s*\1\s*$",
            "",
            page.read_text(encoding="utf-8"),
            flags=re.M | re.S,
        )
        visible = re.sub(r"\[([^]]+)]\([^)]+\)", r"\1", visible)
        if page.as_posix().endswith("overview/javascript-sdk.md"):
            visible = visible.replace("@dust-tt/client", "@client/package")
            visible = visible.replace("DustAPI", "ClientAPI")
        assert not legacy_brand.search(visible), (
            f"legacy brand leaked into rendered documentation: {page.relative_to(ROOT)}"
        )

assert not (ROOT / "mintlify-site" / "zh-cn").exists(), (
    "legacy Chinese path was generated instead of zh-Hans"
)

translations = json.loads((ROOT / "translations.json").read_text(encoding="utf-8"))
chinese_routes = {CHINESE_ROUTE_PREFIX}
for page in translations["pages"]:
    entries = (
        page.get("translations")
        if page["status"] == "publish"
        else page.get("notice")
        if page["status"] == "updating"
        else None
    )
    if entries and entries.get("zh-cn"):
        chinese_route = entries["zh-cn"]["route"]
        assert chinese_route == CHINESE_ROUTE_PREFIX + entries["en"]["route"], (
            f"language routes do not pair: {entries['en']['route']} and {chinese_route}"
        )
        chinese_routes.add(chinese_route)
for artifact in translations.get("artifacts", []):
    entries = artifact["translations"]
    chinese_route = entries["zh-cn"]["route"]
    assert chinese_route == CHINESE_ROUTE_PREFIX + entries["en"]["route"], (
        f"artifact language routes do not pair: {entries['en']['route']} and {chinese_route}"
    )
    chinese_routes.add(chinese_route)

redirect_map = {item["source"]: item["destination"] for item in config["redirects"]}
assert len(redirect_map) == len(config["redirects"]), "duplicate redirect source"
for destination in chinese_routes:
    assert destination.startswith(CHINESE_ROUTE_PREFIX), f"wrong Chinese route: {destination}"
    source = LEGACY_CHINESE_ROUTE_PREFIX + destination.removeprefix(CHINESE_ROUTE_PREFIX)
    assert redirect_map.get(source) == destination, (
        f"missing Chinese path redirect: {source} -> {destination}"
    )

print("navigation: collapsible hierarchy verified")
