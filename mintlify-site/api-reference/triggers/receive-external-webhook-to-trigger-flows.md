---
title: "Receive external webhook to trigger flows"
---
Accepts a JSON event at the source-specific webhook URL, which contains a secret. When signature verification is enabled for that source, the request must carry a valid signature over the raw request body.

```http
POST /api/v1/w/{wId}/triggers/hooks/{webhookSourceId}/{webhookSourceUrlSecret}
```

Base URL: `https://app.counso.ai`

## Authentication

Use the complete webhook URL generated for this source, including its URL secret. This endpoint does not use an API key. If signature verification is configured, include the configured signature header and sign the exact raw request body. Keep the generated URL private.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Workspace ID |
| `webhookSourceId` | path | string | Yes | Webhook source ID |
| `webhookSourceUrlSecret` | path | string | Yes | Secret included in the generated webhook URL |

## Request body

`Content-Type: application/json`

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Webhook received |
| 400 | Invalid request |
| 404 | Workspace or webhook source not found |
| 401 | Invalid webhook URL secret |

## Specification

Download the complete [OpenAPI / Postman](/docs/developer-platform/counso-api-documentation/openapi-and-postman) files.

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Counso API",
    "version": "1.0.2",
    "description": "API reference for Counso workspaces, Agents, conversations and data sources.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    }
  },
  "servers": [
    {
      "url": "https://app.counso.ai",
      "description": "Counso"
    }
  ],
  "paths": {
    "/api/v1/w/{wId}/triggers/hooks/{webhookSourceId}/{webhookSourceUrlSecret}": {
      "post": {
        "summary": "Receive external webhook to trigger flows",
        "description": "Accepts a JSON event at the source-specific webhook URL, which contains a secret. When signature verification is enabled for that source, the request must carry a valid signature over the raw request body.",
        "tags": [
          "Triggers"
        ],
        "security": [],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "description": "Workspace ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "webhookSourceId",
            "required": true,
            "description": "Webhook source ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "webhookSourceUrlSecret",
            "required": true,
            "description": "Secret included in the generated webhook URL",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Webhook received",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "required": [
                    "success"
                  ],
                  "properties": {
                    "success": {
                      "type": "boolean"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request"
          },
          "404": {
            "description": "Workspace or webhook source not found"
          },
          "401": {
            "description": "Invalid webhook URL secret"
          }
        },
        "x-counso-auth": "webhook"
      }
    }
  },
  "components": {
    "securitySchemes": {
      "WorkspaceApiKey": {
        "type": "http",
        "scheme": "bearer",
        "description": "A workspace API key issued by this Counso deployment. Permissions and resource access are checked for each operation."
      },
      "UserAccessToken": {
        "type": "http",
        "scheme": "bearer",
        "description": "A user OAuth access token issued for this Counso deployment. A workspace API key is not a substitute for a user token."
      },
      "BrowserSession": {
        "type": "apiKey",
        "in": "cookie",
        "name": "workos_session",
        "description": "The signed-in Counso browser session. External clients should use a user access token."
      }
    }
  }
}
```
