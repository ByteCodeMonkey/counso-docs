# Cancel message generation in a conversation

Stops the in-progress generation associated with the selected conversation.

```http
POST /api/v1/w/{wId}/assistant/conversations/{cId}/cancel
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Workspace ID |
| `cId` | path | string | Yes | Conversation ID |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `messageIds` | array[string] | Yes |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Message generation successfully canceled |
| 400 | Invalid request (invalid query parameters or request body) |

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
    "/api/v1/w/{wId}/assistant/conversations/{cId}/cancel": {
      "post": {
        "tags": [
          "Conversations"
        ],
        "summary": "Cancel message generation in a conversation",
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
                  "messageIds"
                ],
                "properties": {
                  "messageIds": {
                    "type": "array",
                    "description": "List of message IDs to cancel generation for",
                    "items": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Message generation successfully canceled",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean",
                      "description": "Indicates if the cancellation was successful"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request (invalid query parameters or request body)"
          }
        },
        "x-counso-auth": "workspace",
        "description": "Stops the in-progress generation associated with the selected conversation."
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
