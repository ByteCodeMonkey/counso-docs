---
title: "Get feedbacks for a conversation"
---
Returns every feedback entry recorded for the selected conversation. The authenticated caller must have the read:conversation scope.

```http
GET /api/v1/w/{wId}/assistant/conversations/{cId}/feedbacks
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Workspace ID |
| `cId` | path | string | Yes | Conversation ID |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | List of feedback entries for the conversation |
| 400 | Invalid request parameters |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Conversation not found |
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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/feedbacks": {
      "get": {
        "summary": "Get feedbacks for a conversation",
        "description": "Returns every feedback entry recorded for the selected conversation. The authenticated caller must have the read:conversation scope.",
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
            "description": "List of feedback entries for the conversation",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "feedbacks": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "messageId": {
                            "type": "string",
                            "description": "ID of the message that received feedback"
                          },
                          "agentMessageId": {
                            "type": "number",
                            "description": "ID of the agent message"
                          },
                          "userId": {
                            "type": "number",
                            "description": "ID of the user who gave feedback"
                          },
                          "thumbDirection": {
                            "type": "string",
                            "enum": [
                              "up",
                              "down"
                            ],
                            "description": "Direction of the thumb feedback"
                          },
                          "content": {
                            "type": "string",
                            "nullable": true,
                            "description": "Optional feedback content/comment"
                          },
                          "createdAt": {
                            "type": "number",
                            "description": "Timestamp when feedback was created"
                          },
                          "agentConfigurationId": {
                            "type": "string",
                            "description": "ID of the agent configuration"
                          },
                          "agentConfigurationVersion": {
                            "type": "number",
                            "description": "Version of the agent configuration"
                          },
                          "isConversationShared": {
                            "type": "boolean",
                            "description": "Whether the conversation was shared"
                          }
                        }
                      }
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
          "403": {
            "description": "Forbidden"
          },
          "404": {
            "description": "Conversation not found"
          },
          "500": {
            "description": "Internal server error"
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
