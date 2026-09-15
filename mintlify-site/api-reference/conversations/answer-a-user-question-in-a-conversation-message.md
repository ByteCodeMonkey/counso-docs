---
title: "Answer a user question in a conversation message"
---
Submits the user's response to a question an Agent placed in a particular conversation message.

```http
POST /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/answer-question
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Workspace ID |
| `cId` | path | string | Yes | Conversation ID |
| `mId` | path | string | Yes | Message ID |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `actionId` | string | Yes |
| `answer` | object | Yes |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Answer submitted successfully |
| 400 | Invalid request body or action not blocked |
| 403 | User not authorized to answer this question |
| 404 | Conversation, message, or action not found |
| 500 | Internal server error |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/answer-question": {
      "post": {
        "summary": "Answer a user question in a conversation message",
        "description": "Submits the user's response to a question an Agent placed in a particular conversation message.",
        "tags": [
          "Conversations"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Workspace ID"
          },
          {
            "in": "path",
            "name": "cId",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Conversation ID"
          },
          {
            "in": "path",
            "name": "mId",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Message ID"
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "actionId",
                  "answer"
                ],
                "properties": {
                  "actionId": {
                    "type": "string",
                    "description": "ID of the action to answer"
                  },
                  "answer": {
                    "type": "object",
                    "required": [
                      "selectedOptions"
                    ],
                    "properties": {
                      "selectedOptions": {
                        "type": "array",
                        "items": {
                          "type": "integer"
                        },
                        "description": "Indices of selected options"
                      },
                      "customResponse": {
                        "type": "string",
                        "description": "Optional free-text response"
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
            "description": "Answer submitted successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
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
            "description": "Invalid request body or action not blocked"
          },
          "403": {
            "description": "User not authorized to answer this question"
          },
          "404": {
            "description": "Conversation, message, or action not found"
          },
          "500": {
            "description": "Internal server error"
          }
        },
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "x-counso-auth": "workspace"
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
