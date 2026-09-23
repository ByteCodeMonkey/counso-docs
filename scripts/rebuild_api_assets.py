#!/usr/bin/env python3
"""Build Counso API assets from the latest public upstream Swagger document."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/docs/developer-platform/dust-api-documentation/swagger.json"
METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


def transform_string(value: str) -> str:
    replacements = (
        ("https://docs.dust.tt/docs/client-side-mcp-server", "/docs/user-documentation/developers/client-side-mcp-server"),
        ("https://eu.dust.tt", "https://app.counso.ai"),
        ("https://app.dust.tt", "https://app.counso.ai"),
        ("https://dust.tt", "https://app.counso.ai"),
        ("DUST API Documentation", "Counso API"),
        ("Dust.tt", "Counso"),
        ("Dust's", "Counso's"),
        ("Dust", "Counso"),
    )
    for old, new in replacements:
        value = value.replace(old, new)
    return value


def transform(value):
    if isinstance(value, dict):
        return {key: transform(child) for key, child in value.items()}
    if isinstance(value, list):
        return [transform(child) for child in value]
    if isinstance(value, str):
        return transform_string(value)
    return value


spec = transform(json.loads(SOURCE.read_text(encoding="utf-8")))
spec["info"]["title"] = "Counso API"
spec["info"]["description"] = "API reference for Counso workspaces, Agents, conversations and data sources."
spec["servers"] = [{"url": "https://app.counso.ai", "description": "Counso"}]
security_schemes = {
    "WorkspaceApiKey": {
        "type": "http",
        "scheme": "bearer",
        "description": "A workspace API key issued by this Counso deployment. Permissions and resource access are checked for each operation.",
    },
    "UserAccessToken": {
        "type": "http",
        "scheme": "bearer",
        "description": "A user OAuth access token issued for this Counso deployment.",
    },
}
spec.setdefault("components", {})["securitySchemes"] = security_schemes

operations = {}
for path, item in spec["paths"].items():
    for method, operation in item.items():
        if method not in METHODS:
            continue
        mode = "webhook" if "/triggers/hooks/" in path else "workspace"
        operation["x-counso-auth"] = mode
        operation["security"] = [] if mode == "webhook" else [{"WorkspaceApiKey": []}, {"UserAccessToken": []}]
        operations[(path, method)] = operation


def postman_url(path: str, parameters: list[dict]) -> dict:
    raw_path = re.sub(r"\{([^}]+)\}", r":\1", path)
    query = []
    for parameter in parameters:
        if parameter.get("in") == "query":
            query.append(
                {
                    "key": parameter["name"],
                    "value": "",
                    "description": parameter.get("description", ""),
                    "disabled": not parameter.get("required", False),
                }
            )
    url = {
        "raw": "{{baseUrl}}" + raw_path,
        "host": ["{{baseUrl}}"],
        "path": raw_path.strip("/").split("/"),
    }
    if query:
        url["query"] = query
    return url


groups = defaultdict(list)
for (path, method), operation in operations.items():
    parameters = spec["paths"][path].get("parameters", []) + operation.get("parameters", [])
    mode = operation["x-counso-auth"]
    auth = (
        {"type": "noauth"}
        if mode == "webhook"
        else {
            "type": "bearer",
            "bearer": [{"key": "token", "value": "{{apiKey}}", "type": "string"}],
        }
    )
    request = {
        "method": method.upper(),
        "header": [{"key": "Accept", "value": "application/json"}],
        "auth": auth,
        "url": postman_url(path, parameters),
        "description": operation.get("description", ""),
    }
    if operation.get("requestBody"):
        request["header"].append({"key": "Content-Type", "value": "application/json"})
        request["body"] = {"mode": "raw", "raw": "{}", "options": {"raw": {"language": "json"}}}
    tag = (operation.get("tags") or ["Other"])[0]
    groups[tag].append({"name": operation.get("summary") or f"{method.upper()} {path}", "request": request})

collection = {
    "info": {
        "name": "Counso API",
        "description": "Postman collection generated from the published Counso OpenAPI specification.",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    },
    "item": [{"name": tag, "item": items} for tag, items in sorted(groups.items())],
}
environment = {
    "name": "Counso",
    "values": [
        {"key": "baseUrl", "value": "https://app.counso.ai", "enabled": True},
        {"key": "apiKey", "value": "", "enabled": True, "type": "secret"},
        {"key": "userAccessToken", "value": "", "enabled": True, "type": "secret"},
    ],
    "_postman_variable_scope": "environment",
}

for language in ("en", "zh-cn"):
    target = ROOT / language / "docs/developer-platform/counso-api-documentation"
    target.mkdir(parents=True, exist_ok=True)
    for name in ("openapi.json", "swagger.json"):
        (target / name).write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (target / "postman.collection.json").write_text(
        json.dumps(collection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (target / "postman.environment.json").write_text(
        json.dumps(environment, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

print(json.dumps({"paths": len(spec["paths"]), "operations": len(operations)}, indent=2))
