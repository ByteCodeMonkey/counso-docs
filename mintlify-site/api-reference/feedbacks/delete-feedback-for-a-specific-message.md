---
title: "Delete feedback for a specific message"
---
Removes a user's feedback entry attached to a message in a conversation. The authenticated caller must have the update:conversation scope.

```http
DELETE /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/feedbacks
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

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Feedback deleted successfully |
| 400 | Invalid request parameters |
| 401 | Unauthorized |
| 404 | Conversation, message or feedback not found |

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
      "delete": {
        "summary": "Delete feedback for a specific message",
        "description": "Removes a user's feedback entry attached to a message in a conversation. The authenticated caller must have the update:conversation scope.",
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
        "responses": {
          "200": {
            "description": "Feedback deleted successfully",
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
            "description": "Invalid request parameters"
          },
          "401": {
            "description": "Unauthorized"
          },
          "404": {
            "description": "Conversation, message or feedback not found"
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
