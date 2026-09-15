---
title: "Compact a conversation"
---
Private session interface. Summarizes earlier messages into a compaction entry using the model supplied for summarization.

```http
POST /api/w/{wId}/assistant/conversations/{cId}/compactions
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `cId` | path | string | Yes | ID of the conversation |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `model` | object | Yes |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Compaction started |
| 400 | Invalid request body |
| 404 | Conversation not found |
| 409 | Conflict — compaction or agent message is already running |

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
    "/api/w/{wId}/assistant/conversations/{cId}/compactions": {
      "post": {
        "summary": "Compact a conversation",
        "description": "Private session interface. Summarizes earlier messages into a compaction entry using the model supplied for summarization.",
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
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "model"
                ],
                "properties": {
                  "model": {
                    "type": "object",
                    "required": [
                      "providerId",
                      "modelId"
                    ],
                    "properties": {
                      "providerId": {
                        "type": "string"
                      },
                      "modelId": {
                        "type": "string"
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Compaction started",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "compactionMessage": {
                      "$ref": "#/components/schemas/PrivateCompactionMessage"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request body"
          },
          "404": {
            "description": "Conversation not found"
          },
          "409": {
            "description": "Conflict — compaction or agent message is already running"
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
      "PrivateCompactionMessage": {
        "type": "object",
        "description": "A compaction message summarizing earlier conversation content.",
        "required": [
          "type",
          "sId",
          "status",
          "version",
          "rank",
          "created"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "compaction_message"
            ]
          },
          "id": {
            "type": "integer"
          },
          "compactionMessageId": {
            "type": "integer"
          },
          "sId": {
            "type": "string"
          },
          "created": {
            "type": "integer"
          },
          "visibility": {
            "type": "string",
            "enum": [
              "visible",
              "deleted"
            ]
          },
          "version": {
            "type": "integer"
          },
          "rank": {
            "type": "integer"
          },
          "branchId": {
            "type": "string",
            "nullable": true,
            "description": "Legacy, always null. Branches were removed."
          },
          "sourceConversationId": {
            "type": "string",
            "nullable": true
          },
          "status": {
            "type": "string",
            "enum": [
              "created",
              "succeeded",
              "failed"
            ]
          },
          "content": {
            "type": "string",
            "nullable": true,
            "description": "Compacted summary. Null while status is \"created\"."
          }
        }
      }
    }
  }
}
```
