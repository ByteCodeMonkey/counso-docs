---
title: "Get mention suggestions"
---
Returns agent and user mention candidates matching the supplied query.

```http
GET /api/v1/w/{wId}/assistant/mentions/suggestions
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `query` | query | string | Yes | Search query string to filter suggestions |
| `select` | query | array[string] | No | Array of mention types to include. Can be "agents", "users", or both. If not provided, defaults to agents and users. |
| `current` | query | boolean | No | Whether to include the current user in the suggestions. |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | List of mention suggestions |
| 400 | Bad Request. Missing or invalid parameters. |
| 401 | Unauthorized. Invalid or missing authentication token. |
| 500 | Internal Server Error. |

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
    "/api/v1/w/{wId}/assistant/mentions/suggestions": {
      "get": {
        "summary": "Get mention suggestions",
        "description": "Returns agent and user mention candidates matching the supplied query.",
        "tags": [
          "Mentions"
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
            "required": true,
            "description": "Search query string to filter suggestions",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "select",
            "required": false,
            "description": "Array of mention types to include. Can be \"agents\", \"users\", or both. If not provided, defaults to agents and users.",
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "agents",
                  "users"
                ]
              }
            }
          },
          {
            "in": "query",
            "name": "current",
            "required": false,
            "description": "Whether to include the current user in the suggestions.",
            "schema": {
              "type": "boolean"
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
            "description": "List of mention suggestions",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "suggestions": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/RichMention"
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request. Missing or invalid parameters."
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
          },
          "500": {
            "description": "Internal Server Error."
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
    },
    "schemas": {
      "RichMention": {
        "type": "object",
        "description": "A rich mention suggestion containing detailed information about an agent or user",
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
            "description": "Unique identifier for the mention (agent sId or user sId)",
            "example": "7f3a9c2b1e"
          },
          "type": {
            "type": "string",
            "enum": [
              "agent",
              "user"
            ],
            "description": "Type of the mention",
            "example": "agent"
          },
          "label": {
            "type": "string",
            "description": "Display label for the mention",
            "example": "My Assistant"
          },
          "pictureUrl": {
            "type": "string",
            "description": "URL of the profile picture",
            "example": "https://example.com/avatar.png"
          },
          "description": {
            "type": "string",
            "description": "Description of the mention (agent description or user email)",
            "example": "A helpful AI assistant"
          },
          "userFavorite": {
            "type": "boolean",
            "nullable": true,
            "description": "Whether the agent is marked as a favorite by the user (only for agent mentions)",
            "example": true
          }
        }
      }
    }
  }
}
```
