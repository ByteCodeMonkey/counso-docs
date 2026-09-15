# List conversations

Private session interface. Returns the signed-in user's conversations for this workspace as a paginated collection.

```http
GET /api/w/{wId}/assistant/conversations
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
| 200 | Successfully retrieved conversations |
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
    "/api/w/{wId}/assistant/conversations": {
      "get": {
        "summary": "List conversations",
        "description": "Private session interface. Returns the signed-in user's conversations for this workspace as a paginated collection.",
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
            "description": "Successfully retrieved conversations",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "conversations": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/PrivateConversation"
                      }
                    },
                    "hasMore": {
                      "type": "boolean"
                    },
                    "lastValue": {
                      "type": "string",
                      "nullable": true
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
      "PrivateConversation": {
        "type": "object",
        "description": "Conversation without content, used in list responses.",
        "required": [
          "id",
          "created",
          "updated",
          "sId",
          "depth"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "created": {
            "type": "integer",
            "description": "Unix timestamp of creation"
          },
          "updated": {
            "type": "integer",
            "description": "Unix timestamp of last update"
          },
          "unread": {
            "type": "boolean"
          },
          "lastReadMs": {
            "type": "integer",
            "nullable": true
          },
          "actionRequired": {
            "type": "boolean",
            "description": "Whether the conversation requires user action"
          },
          "hasError": {
            "type": "boolean"
          },
          "sId": {
            "type": "string"
          },
          "title": {
            "type": "string",
            "nullable": true
          },
          "spaceId": {
            "type": "string",
            "nullable": true,
            "description": "ID of the space the conversation belongs to (for project conversations)"
          },
          "triggerId": {
            "type": "string",
            "nullable": true
          },
          "depth": {
            "type": "integer",
            "description": "Conversation depth (for agent handover chains)"
          },
          "metadata": {
            "type": "object",
            "additionalProperties": true
          },
          "requestedSpaceIds": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "forkingData": {
            "$ref": "#/components/schemas/PrivateConversationForkingData"
          }
        }
      },
      "PrivateConversationForkingData": {
        "type": "object",
        "properties": {
          "forkedFrom": {
            "$ref": "#/components/schemas/PrivateConversationForkedFrom"
          },
          "forkedChildren": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateConversationForkedChild"
            }
          }
        }
      },
      "PrivateConversationForkedChild": {
        "type": "object",
        "properties": {
          "childConversationId": {
            "type": "string"
          },
          "childConversationTitle": {
            "type": "string",
            "nullable": true
          },
          "sourceMessageId": {
            "type": "string"
          },
          "branchedAt": {
            "type": "integer"
          },
          "user": {
            "$ref": "#/components/schemas/PrivateConversationForkUser"
          }
        }
      },
      "PrivateConversationForkUser": {
        "type": "object",
        "properties": {
          "sId": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "createdAt": {
            "type": "integer"
          },
          "provider": {
            "type": "string",
            "nullable": true,
            "enum": [
              "auth0",
              "github",
              "google",
              "okta",
              "samlp",
              "waad"
            ]
          },
          "username": {
            "type": "string"
          },
          "email": {
            "type": "string"
          },
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string",
            "nullable": true
          },
          "fullName": {
            "type": "string"
          },
          "image": {
            "type": "string",
            "nullable": true
          },
          "lastLoginAt": {
            "type": "integer",
            "nullable": true
          }
        }
      },
      "PrivateConversationForkedFrom": {
        "type": "object",
        "required": [
          "parentConversationId",
          "parentConversationTitle",
          "sourceMessageId",
          "branchedAt",
          "user",
          "fileCopyStatus"
        ],
        "properties": {
          "parentConversationId": {
            "type": "string"
          },
          "parentConversationTitle": {
            "type": "string",
            "nullable": true
          },
          "sourceMessageId": {
            "type": "string"
          },
          "branchedAt": {
            "type": "integer"
          },
          "user": {
            "$ref": "#/components/schemas/PrivateConversationForkUser"
          },
          "fileCopyStatus": {
            "type": "string",
            "enum": [
              "pending",
              "done"
            ]
          }
        }
      }
    }
  }
}
```
