# List available spaces

Enumerates Spaces the authenticated user can access in the current workspace.

```http
GET /api/v1/w/{wId}/spaces
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Unique string identifier for the workspace |
| `kinds` | query | string | No | Comma-separated list of space kinds to filter on, among `system`, `global`, `regular` and `project`. Defaults to `system,global,regular` — projects must be requested explicitly. |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Spaces of the workspace |
| 400 | Bad Request. Missing or invalid parameters. |
| 401 | Unauthorized. Invalid or missing authentication token. |
| 404 | Workspace not found. |
| 500 | Internal Server Error. |

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
    "/api/v1/w/{wId}/spaces": {
      "get": {
        "summary": "List available spaces.",
        "description": "Enumerates Spaces the authenticated user can access in the current workspace.",
        "tags": [
          "Spaces"
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "description": "Unique string identifier for the workspace",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "kinds",
            "required": false,
            "description": "Comma-separated list of space kinds to filter on, among `system`, `global`, `regular` and `project`. Defaults to `system,global,regular` — projects must be requested explicitly.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Spaces of the workspace",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "spaces": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Space"
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
          "404": {
            "description": "Workspace not found."
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
      "Space": {
        "type": "object",
        "properties": {
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the space"
          },
          "name": {
            "type": "string",
            "description": "Name of the space"
          },
          "kind": {
            "type": "string",
            "enum": [
              "regular",
              "global",
              "system",
              "public"
            ],
            "description": "The kind of the space"
          },
          "groupIds": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of group IDs that have access to the space"
          },
          "isRestricted": {
            "type": "boolean",
            "description": "Whether the space is restricted to specific groups"
          }
        }
      }
    }
  }
}
```
