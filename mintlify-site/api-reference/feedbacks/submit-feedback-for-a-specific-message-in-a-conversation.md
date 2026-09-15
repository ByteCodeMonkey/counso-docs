---
title: "Submit feedback for a specific message in a conversation"
---
Stores a thumbs-up or thumbs-down rating for a particular conversation message. The authenticated caller must have the update:conversation scope.

```http
POST /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/feedbacks
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
| `thumbDirection` | string | Yes |
| `feedbackContent` | string | No |
| `isConversationShared` | boolean | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Feedback submitted successfully |
| 400 | Invalid request parameters or body |
| 401 | Unauthorized |
| 404 | Conversation or message not found |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/feedbacks": {
      "post": {
        "summary": "Submit feedback for a specific message in a conversation",
        "description": "Stores a thumbs-up or thumbs-down rating for a particular conversation message. The authenticated caller must have the update:conversation scope.",
        "tags": [
          "Feedbacks"
        ],
        "parameters": [
          {
            "name": "wId",
            "in": "path",
            "description": "Workspace ID",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cId",
            "in": "path",
            "description": "Conversation ID",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "mId",
            "in": "path",
            "description": "Message ID",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "thumbDirection"
                ],
                "properties": {
                  "thumbDirection": {
                    "type": "string",
                    "enum": [
                      "up",
                      "down"
                    ],
                    "description": "Direction of the thumb feedback"
                  },
                  "feedbackContent": {
                    "type": "string",
                    "description": "Optional feedback text content"
                  },
                  "isConversationShared": {
                    "type": "boolean",
                    "description": "Whether the conversation is shared"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Feedback submitted successfully",
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
            "description": "Invalid request parameters or body"
          },
          "401": {
            "description": "Unauthorized"
          },
          "404": {
            "description": "Conversation or message not found"
          }
        },
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
