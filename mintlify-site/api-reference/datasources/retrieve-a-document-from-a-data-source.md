---
title: "Retrieve a document from a data source"
---
Fetches a document by its data-source ID {dsId} from workspace {wId}.

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}
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
| 400 | Bad Request. Missing or invalid parameters. |
| 401 | Unauthorized. Invalid or missing authentication token. |
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
      "get": {
        "summary": "Retrieve a document from a data source",
        "description": "Fetches a document by its data-source ID {dsId} from workspace {wId}.",
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
                      "$ref": "#/components/schemas/Document"
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
    },
    "schemas": {
      "Document": {
        "type": "object",
        "properties": {
          "data_source_id": {
            "type": "string",
            "example": "3b7d9f1e5a"
          },
          "created": {
            "type": "number",
            "example": 1625097600
          },
          "document_id": {
            "type": "string",
            "example": "2c4a6e8d0f"
          },
          "title": {
            "type": "string",
            "description": "Title of the document",
            "example": "Customer Support FAQ"
          },
          "mime_type": {
            "type": "string",
            "description": "MIME type of the table",
            "example": "text/md"
          },
          "timestamp": {
            "type": "number",
            "example": 1625097600
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              "customer_support",
              "faq"
            ]
          },
          "parent_id": {
            "type": "string",
            "description": "ID of the document parent",
            "items": {
              "type": "string"
            },
            "example": "1234f4567c"
          },
          "parents": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              "7b9d1f3e5a",
              "2c4a6e8d0f"
            ]
          },
          "source_url": {
            "type": "string",
            "nullable": true,
            "example": "https://example.com/support/article1"
          },
          "hash": {
            "type": "string",
            "example": "a1b2c3d4e5"
          },
          "text_size": {
            "type": "number",
            "example": 1024
          },
          "chunk_count": {
            "type": "number",
            "example": 5
          },
          "chunks": {
            "type": "array",
            "items": {
              "type": "object"
            },
            "example": [
              {
                "chunk_id": "9f1d3b5a7c",
                "text": "This is the first chunk of the document.",
                "embedding": [
                  0.1,
                  0.2,
                  0.3,
                  0.4
                ]
              },
              {
                "chunk_id": "4a2c6e8b0d",
                "text": "This is the second chunk of the document.",
                "embedding": [
                  0.5,
                  0.6,
                  0.7,
                  0.8
                ]
              }
            ]
          },
          "text": {
            "type": "string",
            "example": "This is the full text content of the document. It contains multiple paragraphs and covers various topics related to customer support."
          },
          "token_count": {
            "type": "number",
            "nullable": true,
            "example": 150
          }
        }
      }
    }
  }
}
```
