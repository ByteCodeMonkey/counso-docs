#!/usr/bin/env python3
"""Regression check for collapsible Mintlify navigation."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "mintlify-site" / "docs.json"


def walk_groups(items):
    for item in items:
        if not isinstance(item, dict):
            continue
        yield item
        yield from walk_groups(item.get("pages", []))


config = json.loads(CONFIG.read_text(encoding="utf-8"))
languages = config["navigation"]["languages"]

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
    "zh-Hans": (
        "zh-cn/docs/user-documentation/getting-started/use-cases-and-guides",
        "zh-cn/docs/user-documentation/getting-started/use-cases-and-guides/sales",
        "zh-cn/docs/user-documentation/getting-started/faq",
        {
            "一般问题",
            "智能体与对话",
            "故障排除",
        },
    ),
}

for language in languages:
    code = language["language"]
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

for prefix in ("", "zh-cn/"):
    asset_dir = ROOT / "mintlify-site" / prefix / "docs/developer-platform/counso-api-documentation"
    for filename in ("postman.collection.json", "postman.environment.json"):
        asset = asset_dir / filename
        assert asset.exists(), f"missing downloadable API asset: {asset.relative_to(ROOT)}"
        json.loads(asset.read_text(encoding="utf-8"))
    for filename in ("openapi.json", "swagger.json"):
        assert not (asset_dir / filename).exists(), f"legacy-branded asset is still public: {filename}"
        notice = asset_dir / f"{filename}.md"
        assert notice.exists(), f"missing update notice for gated asset: {notice.relative_to(ROOT)}"

legacy_brand = re.compile(r"(?i)(?:\bdust\b|dust-tt|dustapi)")
for pattern in ("*.md", "*.mdx"):
    for page in (ROOT / "mintlify-site").rglob(pattern):
        assert not legacy_brand.search(page.read_text(encoding="utf-8")), (
            f"legacy brand leaked into rendered documentation: {page.relative_to(ROOT)}"
        )

print("navigation: collapsible hierarchy verified")
