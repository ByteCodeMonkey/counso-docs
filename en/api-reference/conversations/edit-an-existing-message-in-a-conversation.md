# Edit an existing message in a conversation

Changes the contents of a message that already exists in the specified conversation.

```http
POST /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/edit
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Workspace ID |
| `cId` | path | string | Yes | Conversation ID |
| `mId` | path | string | Yes | Message ID to edit |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `content` | string | Yes |
| `mentions` | array[object] | Yes |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Message successfully edited |
| 400 | Invalid request (message not found or not a user message) |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/edit": {
      "post": {
        "tags": [
          "Conversations"
        ],
        "summary": "Edit an existing message in a conversation",
        "parameters": [
          {
            "name": "wId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Workspace ID"
          },
          {
            "name": "cId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Conversation ID"
          },
          {
            "name": "mId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Message ID to edit"
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
                  "content",
                  "mentions"
                ],
                "properties": {
                  "content": {
                    "type": "string",
                    "description": "New content for the message"
                  },
                  "mentions": {
                    "type": "array",
                    "description": "List of agent mentions in the message",
                    "items": {
                      "type": "object",
                      "required": [
                        "configurationId"
                      ],
                      "properties": {
                        "configurationId": {
                          "type": "string",
                          "description": "ID of the mentioned agent configuration"
                        }
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
            "description": "Message successfully edited",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "object",
                      "description": "The edited user message"
                    },
                    "agentMessages": {
                      "type": "array",
                      "description": "Optional array of agent messages generated in response"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request (message not found or not a user message)"
          }
        },
        "x-counso-auth": "workspace",
        "description": "Changes the contents of a message that already exists in the specified conversation."
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
