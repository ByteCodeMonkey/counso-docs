---
title: "Search the data source view"
---
Searches within view {dsvId} in workspace {wId}.

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}/search
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `spaceId` | path | string | Yes | ID of the space |
| `dsvId` | path | string | Yes | ID of the data source view |
| `query` | query | string | Yes | The search query |
| `top_k` | query | number | Yes | The number of results to return |
| `full_text` | query | boolean | Yes | Whether to return the full document content |
| `target_document_tokens` | query | number | No | The number of tokens in the target document |
| `timestamp_gt` | query | number | No | The timestamp to filter by |
| `timestamp_lt` | query | number | No | The timestamp to filter by |
| `tags_in` | query | string | No | The tags to filter by |
| `tags_not` | query | string | No | The tags to filter by |
| `parents_in` | query | string | No | The parents to filter by |
| `parents_not` | query | string | No | The parents to filter by |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | The documents |
| 400 | Invalid request error |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}/search": {
      "get": {
        "summary": "Search the data source view",
        "description": "Searches within view {dsvId} in workspace {wId}.",
        "tags": [
          "DatasourceViews"
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
            "description": "ID of the workspace",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "spaceId",
            "required": true,
            "description": "ID of the space",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "dsvId",
            "required": true,
            "description": "ID of the data source view",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "query",
            "required": true,
            "description": "The search query",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "top_k",
            "required": true,
            "description": "The number of results to return",
            "schema": {
              "type": "number"
            }
          },
          {
            "in": "query",
            "name": "full_text",
            "required": true,
            "description": "Whether to return the full document content",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "in": "query",
            "name": "target_document_tokens",
            "required": false,
            "description": "The number of tokens in the target document",
            "schema": {
              "type": "number"
            }
          },
          {
            "in": "query",
            "name": "timestamp_gt",
            "required": false,
            "description": "The timestamp to filter by",
            "schema": {
              "type": "number"
            }
          },
          {
            "in": "query",
            "name": "timestamp_lt",
            "required": false,
            "description": "The timestamp to filter by",
            "schema": {
              "type": "number"
            }
          },
          {
            "in": "query",
            "name": "tags_in",
            "required": false,
            "description": "The tags to filter by",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "tags_not",
            "required": false,
            "description": "The tags to filter by",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "parents_in",
            "required": false,
            "description": "The parents to filter by",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "parents_not",
            "required": false,
            "description": "The parents to filter by",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The documents",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "documents": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "ID of the document"
                          },
                          "title": {
                            "type": "string",
                            "description": "Title of the document"
                          },
                          "content": {
                            "type": "string",
                            "description": "Content of the document"
                          },
                          "tags": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": "Tags of the document"
                          },
                          "parents": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": "Parents of the document"
                          },
                          "timestamp": {
                            "type": "number",
                            "description": "Timestamp of the document"
                          },
                          "data": {
                            "type": "object",
                            "description": "Data of the document"
                          },
                          "score": {
                            "type": "number",
                            "description": "Score of the document"
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
            "description": "Invalid request error"
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
