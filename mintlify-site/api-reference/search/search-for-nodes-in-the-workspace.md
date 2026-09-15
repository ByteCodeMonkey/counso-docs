---
title: "Search for nodes in the workspace"
---
Finds nodes in the workspace that match the supplied search criteria.

```http
POST /api/v1/w/{wId}/search
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `query` | string | Yes |
| `includeDataSources` | boolean | No |
| `viewType` | string | No |
| `spaceIds` | array[string] | No |
| `nodeIds` | array[string] | No |
| `searchSourceUrls` | boolean | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Search results retrieved successfully |
| 400 | Bad request |
| 401 | Unauthorized |
| 404 | Space not found |

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
    "/api/v1/w/{wId}/search": {
      "post": {
        "summary": "Search for nodes in the workspace",
        "description": "Finds nodes in the workspace that match the supplied search criteria.",
        "tags": [
          "Search"
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
                  "query"
                ],
                "properties": {
                  "query": {
                    "type": "string",
                    "description": "The search query"
                  },
                  "includeDataSources": {
                    "type": "boolean",
                    "description": "List of data source IDs to include in search"
                  },
                  "viewType": {
                    "type": "string",
                    "description": "Type of view to filter results"
                  },
                  "spaceIds": {
                    "type": "array",
                    "description": "List of space IDs to search in",
                    "items": {
                      "type": "string"
                    }
                  },
                  "nodeIds": {
                    "type": "array",
                    "description": "List of specific node IDs to search",
                    "items": {
                      "type": "string"
                    }
                  },
                  "searchSourceUrls": {
                    "type": "boolean",
                    "description": "Whether to search source URLs"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Search results retrieved successfully"
          },
          "400": {
            "description": "Bad request"
          },
          "401": {
            "description": "Unauthorized"
          },
          "404": {
            "description": "Space not found"
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
