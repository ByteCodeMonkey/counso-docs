# Get mention suggestions

Private session interface. Provides mention suggestions available in the workspace.

```http
GET /api/w/{wId}/assistant/mentions/suggestions
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `query` | query | string | No | Search query to filter suggestions |
| `select` | query | string | No | Filter by type (agents, users, or both) Values: `agents`, `users` |
| `current` | query | string | No | Whether to include only current mentions Values: `true`, `false` |
| `spaceId` | query | string | No | Filter suggestions by space |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Success |
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
    "/api/w/{wId}/assistant/mentions/suggestions": {
      "get": {
        "summary": "Get mention suggestions",
        "description": "Private session interface. Provides mention suggestions available in the workspace.",
        "tags": [
          "Private Mentions"
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
            "in": "query",
            "name": "query",
            "required": false,
            "description": "Search query to filter suggestions",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "select",
            "required": false,
            "description": "Filter by type (agents, users, or both)",
            "schema": {
              "type": "string",
              "enum": [
                "agents",
                "users"
              ]
            }
          },
          {
            "in": "query",
            "name": "current",
            "required": false,
            "description": "Whether to include only current mentions",
            "schema": {
              "type": "string",
              "enum": [
                "true",
                "false"
              ]
            }
          },
          {
            "in": "query",
            "name": "spaceId",
            "required": false,
            "description": "Filter suggestions by space",
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
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "suggestions": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/PrivateMentionSuggestion"
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
      "PrivateMentionSuggestion": {
        "type": "object",
        "description": "A rich mention suggestion for agents or users.",
        "required": [
          "id",
          "type",
          "label",
          "pictureUrl",
          "description"
        ],
        "properties": {
          "id": {
            "type": "string",
            "description": "Agent sId or user sId"
          },
          "type": {
            "type": "string",
            "enum": [
              "agent",
              "user"
            ]
          },
          "label": {
            "type": "string",
            "description": "Display name"
          },
          "pictureUrl": {
            "type": "string"
          },
          "description": {
            "type": "string",
            "description": "Agent description or user email"
          },
          "userFavorite": {
            "type": "boolean",
            "description": "Whether the agent is a user favorite (agent mentions only)"
          }
        }
      }
    }
  }
}
```
