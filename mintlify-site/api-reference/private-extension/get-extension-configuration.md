---
title: "Get extension configuration"
---
Private session interface. Returns extension settings for the workspace, including its blocked-domain list.

```http
GET /api/w/{wId}/extension/config
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Extension configuration |
| 401 | Unauthorized |

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
    "/api/w/{wId}/extension/config": {
      "get": {
        "summary": "Get extension configuration",
        "description": "Private session interface. Returns extension settings for the workspace, including its blocked-domain list.",
        "tags": [
          "Private Extension"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "description": "ID of the workspace",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "UserAccessToken": []
          },
          {
            "BrowserSession": []
          }
        ],
        "responses": {
          "200": {
            "description": "Extension configuration",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateExtensionConfig"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "x-counso-auth": "user"
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
    },
    "schemas": {
      "PrivateExtensionConfig": {
        "type": "object",
        "description": "Extension configuration for the workspace.",
        "required": [
          "blacklistedDomains"
        ],
        "properties": {
          "blacklistedDomains": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Domains where the extension should not activate"
          }
        }
      }
    }
  }
}
```
