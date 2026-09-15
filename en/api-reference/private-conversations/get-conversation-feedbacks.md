# Get conversation feedbacks

Private session interface. Retrieves feedback that the signed-in user submitted for the specified conversation.

```http
GET /api/w/{wId}/assistant/conversations/{cId}/feedbacks
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `cId` | path | string | Yes | ID of the conversation |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Successfully retrieved feedbacks |
| 401 | Unauthorized |

## Specification

Download the complete [OpenAPI / Postman](../../docs/developer-platform/counso-api-documentation/openapi-and-postman.md) files.

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
    "/api/w/{wId}/assistant/conversations/{cId}/feedbacks": {
      "get": {
        "summary": "Get conversation feedbacks",
        "description": "Private session interface. Retrieves feedback that the signed-in user submitted for the specified conversation.",
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
        "responses": {
          "200": {
            "description": "Successfully retrieved feedbacks",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "feedbacks": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/PrivateFeedback"
                      }
                    }
                  }
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
      "PrivateFeedback": {
        "type": "object",
        "description": "User feedback on an agent message.",
        "required": [
          "id",
          "sId",
          "messageId",
          "agentMessageId",
          "userId",
          "thumbDirection",
          "agentConfigurationId",
          "agentConfigurationVersion",
          "isConversationShared",
          "dismissed",
          "createdAt"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "sId": {
            "type": "string"
          },
          "messageId": {
            "type": "string"
          },
          "agentMessageId": {
            "type": "integer"
          },
          "userId": {
            "type": "integer"
          },
          "thumbDirection": {
            "type": "string",
            "enum": [
              "up",
              "down"
            ]
          },
          "content": {
            "type": "string",
            "nullable": true,
            "description": "Optional text feedback from the user"
          },
          "createdAt": {
            "type": "string",
            "format": "date-time"
          },
          "agentConfigurationId": {
            "type": "string"
          },
          "agentConfigurationVersion": {
            "type": "integer"
          },
          "isConversationShared": {
            "type": "boolean"
          },
          "dismissed": {
            "type": "boolean"
          }
        }
      }
    }
  }
}
```
