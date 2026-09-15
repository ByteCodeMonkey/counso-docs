# Upsert a table

Creates a table in data source {dsId}, or applies updates to its existing definition, in workspace {wId}.

```http
POST /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Unique string identifier for the workspace |
| `spaceId` | path | string | Yes | ID of the space |
| `dsId` | path | string | Yes | ID of the data source |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `name` | string | No |
| `title` | string | No |
| `table_id` | string | No |
| `description` | string | No |
| `timestamp` | number | No |
| `tags` | array[string] | No |
| `mime_type` | string | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | The table |
| 400 | Invalid request |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables": {
      "post": {
        "summary": "Upsert a table",
        "description": "Creates a table in data source {dsId}, or applies updates to its existing definition, in workspace {wId}.",
        "tags": [
          "Datasources"
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
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Name of the table"
                  },
                  "title": {
                    "type": "string",
                    "description": "Title of the table"
                  },
                  "table_id": {
                    "type": "string",
                    "description": "Unique identifier for the table"
                  },
                  "description": {
                    "type": "string",
                    "description": "Description of the table"
                  },
                  "timestamp": {
                    "type": "number",
                    "description": "Unix timestamp (in milliseconds) for the table (e.g. 1736365559000)."
                  },
                  "tags": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Tags associated with the table"
                  },
                  "mime_type": {
                    "type": "string",
                    "description": "Reserved for internal use, should not be set. Mime type of the table"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "The table",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "table": {
                      "$ref": "#/components/schemas/Table"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request"
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
      "Table": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the table",
            "example": "Roi data",
            "deprecated": true
          },
          "title": {
            "type": "string",
            "description": "Title of the table",
            "example": "ROI Data"
          },
          "table_id": {
            "type": "string",
            "description": "Unique identifier for the table",
            "example": "1234f4567c"
          },
          "description": {
            "type": "string",
            "description": "Description of the table",
            "example": "roi data for Q1"
          },
          "mime_type": {
            "type": "string",
            "description": "MIME type of the table",
            "example": "text/csv"
          },
          "schema": {
            "type": "array",
            "description": "Array of column definitions",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "Name of the column",
                  "example": "roi"
                },
                "value_type": {
                  "type": "string",
                  "description": "Data type of the column",
                  "enum": [
                    "text",
                    "int",
                    "float",
                    "bool",
                    "date"
                  ],
                  "example": "int"
                },
                "possible_values": {
                  "type": "array",
                  "description": "Array of possible values for the column (null if unrestricted)",
                  "items": {
                    "type": "string"
                  },
                  "nullable": true,
                  "example": [
                    "1",
                    "2",
                    "3"
                  ]
                }
              }
            }
          },
          "timestamp": {
            "type": "number",
            "description": "Unix timestamp of table creation/modification",
            "example": 1732810375150
          },
          "tags": {
            "type": "array",
            "description": "Array of tags associated with the table",
            "items": {
              "type": "string"
            }
          },
          "parent_id": {
            "type": "string",
            "description": "ID of the table parent",
            "items": {
              "type": "string"
            },
            "example": "1234f4567c"
          },
          "parents": {
            "type": "array",
            "description": "Array of parent table IDs",
            "items": {
              "type": "string"
            },
            "example": [
              "1234f4567c"
            ]
          }
        }
      }
    }
  }
}
```
