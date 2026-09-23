---
title: "Export consumption analytics"
---
Exports per-call consumption analytics for a workspace. Each row represents one billed LLM call or tool call.

```http
POST /api/v1/w/{wId}/analytics/consumption/export
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or user access token in `Authorization: Bearer <token>`. The credential must have access to the requested workspace.

## Path parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `wId` | string | Yes | Unique workspace identifier |

## Request body

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `startDate` | string / date-time | Yes | Inclusive start time in ISO 8601 format |
| `endDate` | string / date-time | Yes | Exclusive end time in ISO 8601 format; must be after `startDate` and no more than 30 days later |
| `format` | `csv` or `ndjson` | No | Output format; defaults to `csv` |
| `filter` | object | No | Optional filters described below |

`filter` accepts arrays for `agents`, `users`, `api_keys`, `groups`, `models`, `tools`, `skills`, `sources`, and `tags`. Each value is limited to 256 characters, with at most 500 values across all dimensions.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Streaming CSV or NDJSON export |
| 400 | Invalid dates, format, filters, or a range longer than 30 days |
| 401 | Missing or invalid authentication |
| 403 | The credential cannot access the workspace |

The request times out after 10 seconds. Reduce the date range or add filters if the result is too large. If an error occurs after streaming starts, an error message is appended before the stream closes.

## Specification

Download the complete [OpenAPI / Postman](/docs/developer-platform/counso-api-documentation/openapi-and-postman) files for exact schemas and response headers.
