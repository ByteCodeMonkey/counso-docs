---
title: "Receive external webhook to trigger flows"
---
Accepts a JSON event for a configured webhook source and triggers the associated flows.

```http
POST /api/v1/w/{wId}/triggers/hooks/{webhookSourceId}
```

Base URL: `https://app.counso.ai`

## Authentication

This endpoint does not use a workspace API key. Use the webhook URL generated for the source. If signature verification is configured, include the required signature header and calculate it from the exact raw request body.

## Path parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `wId` | string | Yes | Workspace ID |
| `webhookSourceId` | string | Yes | Webhook source ID |

## Request body

Send the event as `application/json`. The accepted nested structure depends on the trigger configuration.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Webhook received |
| 400 | Invalid request or signature |
| 404 | Workspace or webhook source not found |

Keep generated webhook URLs private and rotate the source if a URL is exposed.

## Specification

See the complete [OpenAPI / Postman](/docs/developer-platform/counso-api-documentation/openapi-and-postman) files for the exact request and response schemas.
