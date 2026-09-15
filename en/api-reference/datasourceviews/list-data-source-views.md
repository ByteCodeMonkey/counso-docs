# List Data Source Views

Enumerates the data source views configured for the selected Space.

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_source_views
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Unique string identifier for the workspace |
| `spaceId` | path | string | Yes | ID of the space |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | List of data source views in the space |
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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_source_views": {
      "get": {
        "summary": "List Data Source Views",
        "description": "Enumerates the data source views configured for the selected Space.",
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
          }
        ],
        "responses": {
          "200": {
            "description": "List of data source views in the space",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "dataSourceViews": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/DatasourceView"
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
      "DatasourceView": {
        "type": "object",
        "properties": {
          "category": {
            "type": "string",
            "enum": [
              "managed",
              "folder",
              "website",
              "apps"
            ],
            "description": "The category of the data source view"
          },
          "createdAt": {
            "type": "number",
            "description": "Timestamp of when the data source view was created"
          },
          "dataSource": {
            "$ref": "#/components/schemas/Datasource"
          },
          "editedByUser": {
            "type": "object",
            "description": "The user who last edited the data source view",
            "properties": {
              "fullName": {
                "type": "string",
                "description": "Full name of the user"
              },
              "editedAt": {
                "type": "number",
                "description": "Timestamp of when the data source view was last edited by the user"
              }
            }
          },
          "id": {
            "type": "number",
            "description": "Unique identifier for the data source view"
          },
          "kind": {
            "type": "string",
            "enum": [
              "default",
              "custom"
            ],
            "description": "The kind of the data source view"
          },
          "parentsIn": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of IDs included in this view, null if complete data source is taken",
            "nullable": true
          },
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the data source view"
          },
          "updatedAt": {
            "type": "number",
            "description": "Timestamp of when the data source view was last updated"
          },
          "spaceId": {
            "type": "string",
            "description": "ID of the space containing the data source view"
          }
        }
      },
      "Datasource": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the datasource",
            "example": 12345
          },
          "createdAt": {
            "type": "integer",
            "description": "Timestamp of when the datasource was created",
            "example": 1625097600
          },
          "name": {
            "type": "string",
            "description": "Name of the datasource",
            "example": "Customer Knowledge Base"
          },
          "description": {
            "type": "string",
            "description": "Description of the datasource",
            "example": "Contains all customer-related information and FAQs"
          },
          "dustAPIProjectId": {
            "type": "string",
            "description": "ID of the associated Counso API project",
            "example": "5e9d8c7b6a"
          },
          "connectorId": {
            "type": "string",
            "description": "ID of the connector used for this datasource",
            "example": "1f3e5d7c9b"
          },
          "connectorProvider": {
            "type": "string",
            "description": "Provider of the connector (e.g., 'webcrawler')",
            "example": "webcrawler"
          },
          "assistantDefaultSelected": {
            "type": "boolean",
            "description": "Whether this datasource is selected by default for agents",
            "example": true
          }
        }
      }
    }
  }
}
```
