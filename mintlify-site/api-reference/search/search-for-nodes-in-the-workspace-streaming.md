---
title: "Search for nodes in the workspace (streaming)"
---
Searches workspace nodes and sends matching results incrementally over SSE.

```http
GET /api/v1/w/{wId}/search
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `query` | query | string | Yes | The search query (minimum 3 characters) |
| `limit` | query | integer | No | Number of results per page (1-100, default 25) |
| `cursor` | query | string | No | Cursor for pagination |
| `viewType` | query | string | No | Type of view to filter results Values: `all`, `document`, `table` |
| `spaceIds` | query | string | No | Comma-separated list of space IDs to search in |
| `includeDataSources` | query | boolean | No | Whether to include data sources |
| `searchSourceUrls` | query | boolean | No | Whether to search source URLs |
| `includeTools` | query | boolean | No | Whether to include tool results |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Search results streamed successfully |
| 400 | Bad request |
| 401 | Unauthorized |

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
      "get": {
        "summary": "Search for nodes in the workspace (streaming)",
        "description": "Searches workspace nodes and sends matching results incrementally over SSE.",
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
          },
          {
            "in": "query",
            "name": "query",
            "required": true,
            "description": "The search query (minimum 3 characters)",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "limit",
            "required": false,
            "description": "Number of results per page (1-100, default 25)",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "cursor",
            "required": false,
            "description": "Cursor for pagination",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "viewType",
            "required": false,
            "description": "Type of view to filter results",
            "schema": {
              "type": "string",
              "enum": [
                "all",
                "document",
                "table"
              ]
            }
          },
          {
            "in": "query",
            "name": "spaceIds",
            "required": false,
            "description": "Comma-separated list of space IDs to search in",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "includeDataSources",
            "required": false,
            "description": "Whether to include data sources",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "in": "query",
            "name": "searchSourceUrls",
            "required": false,
            "description": "Whether to search source URLs",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "in": "query",
            "name": "includeTools",
            "required": false,
            "description": "Whether to include tool results",
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
            "description": "Search results streamed successfully",
            "content": {
              "text/event-stream": {
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "400": {
            "description": "Bad request"
          },
          "401": {
            "description": "Unauthorized"
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
