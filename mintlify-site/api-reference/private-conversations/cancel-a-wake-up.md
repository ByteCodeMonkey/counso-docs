---
title: "Cancel a wake-up"
---
Private session interface. Cancels a scheduled wake-up when requested by its owner or a workspace administrator.

```http
DELETE /api/w/{wId}/assistant/conversations/{cId}/wakeups/{wuId}
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `cId` | path | string | Yes | ID of the conversation |
| `wuId` | path | string | Yes | sId of the wake-up to cancel |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Successfully cancelled (or already terminal) |
| 403 | Caller is not the wake-up owner or a workspace admin |
| 404 | Wake-up not found in this conversation |

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
    "/api/w/{wId}/assistant/conversations/{cId}/wakeups/{wuId}": {
      "delete": {
        "summary": "Cancel a wake-up",
        "description": "Private session interface. Cancels a scheduled wake-up when requested by its owner or a workspace administrator.",
        "tags": [
          "Private Conversations"
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
          },
          {
            "in": "path",
            "name": "cId",
            "required": true,
            "description": "ID of the conversation",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "wuId",
            "required": true,
            "description": "sId of the wake-up to cancel",
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
            "description": "Successfully cancelled (or already terminal)",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "wakeUp": {
                      "$ref": "#/components/schemas/PrivateWakeUp"
                    }
                  }
                }
              }
            }
          },
          "403": {
            "description": "Caller is not the wake-up owner or a workspace admin"
          },
          "404": {
            "description": "Wake-up not found in this conversation"
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
      "PrivateWakeUp": {
        "type": "object",
        "description": "A wake-up scheduled in a conversation to re-invoke the agent at a later time.",
        "required": [
          "id",
          "sId",
          "createdAt",
          "agentConfigurationId",
          "scheduleConfig",
          "reason",
          "status",
          "fireCount",
          "maxFires"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "sId": {
            "type": "string"
          },
          "createdAt": {
            "type": "integer",
            "description": "Unix timestamp (milliseconds)."
          },
          "agentConfigurationId": {
            "type": "string"
          },
          "scheduleConfig": {
            "oneOf": [
              {
                "type": "object",
                "required": [
                  "type",
                  "fireAt"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "enum": [
                      "one_shot"
                    ]
                  },
                  "fireAt": {
                    "type": "integer",
                    "description": "Unix timestamp (milliseconds) when the wake-up should fire."
                  }
                }
              },
              {
                "type": "object",
                "required": [
                  "type",
                  "cron",
                  "timezone"
                ],
                "properties": {
                  "type": {
                    "type": "string",
                    "enum": [
                      "cron"
                    ]
                  },
                  "cron": {
                    "type": "string",
                    "description": "5-field cron expression."
                  },
                  "timezone": {
                    "type": "string",
                    "description": "IANA timezone name."
                  }
                }
              }
            ]
          },
          "reason": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "enum": [
              "scheduled",
              "fired",
              "cancelled",
              "expired"
            ]
          },
          "fireCount": {
            "type": "integer"
          },
          "maxFires": {
            "type": "integer"
          }
        }
      }
    }
  }
}
```
