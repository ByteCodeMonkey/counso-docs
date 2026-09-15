---
title: "Delete a document from a data source"
---
Removes the chosen document from a workspace data source.

```http
DELETE /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `spaceId` | path | string | Yes | ID of the space |
| `dsId` | path | string | Yes | ID of the data source |
| `documentId` | path | string | Yes | ID of the document |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | The document |
| 401 | Unauthorized. Invalid or missing authentication token. |
| 403 | Forbidden. The data source is managed. |
| 404 | Data source or document not found. |
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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}": {
      "delete": {
        "summary": "Delete a document from a data source",
        "description": "Removes the chosen document from a workspace data source.",
        "tags": [
          "Datasources"
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
            "name": "dsId",
            "required": true,
            "description": "ID of the data source",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "documentId",
            "required": true,
            "description": "ID of the document",
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
        "responses": {
          "200": {
            "description": "The document",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "document": {
                      "type": "object",
                      "properties": {
                        "document_id": {
                          "type": "string"
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
          },
          "403": {
            "description": "Forbidden. The data source is managed."
          },
          "404": {
            "description": "Data source or document not found."
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
    }
  }
}
```
