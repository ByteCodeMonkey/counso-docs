---
title: "Get an app run"
---
Looks up a previously created app run by its ID in the specified Space.

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/apps/{aId}/runs/{runId}
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Unique string identifier for the workspace |
| `spaceId` | path | string | Yes | ID of the space |
| `aId` | path | string | Yes | ID of the app |
| `runId` | path | string | Yes | ID of the run |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | The run |
| 400 | Bad Request. Missing or invalid parameters. |
| 401 | Unauthorized. Invalid or missing authentication token. |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/apps/{aId}/runs/{runId}": {
      "get": {
        "summary": "Get an app run",
        "description": "Looks up a previously created app run by its ID in the specified Space.",
        "tags": [
          "Apps"
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
            "name": "aId",
            "required": true,
            "description": "ID of the app",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "runId",
            "required": true,
            "description": "ID of the run",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The run",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "run": {
                      "$ref": "#/components/schemas/Run"
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
      "Run": {
        "type": "object",
        "properties": {
          "run_id": {
            "type": "string",
            "description": "The ID of the run",
            "example": "4a2c6e8b0d"
          },
          "app_id": {
            "type": "string",
            "description": "The ID of the app",
            "example": "9f1d3b5a7c"
          },
          "status": {
            "type": "object",
            "properties": {
              "run": {
                "type": "string",
                "description": "The status of the run",
                "example": "succeeded"
              },
              "build": {
                "type": "string",
                "description": "The status of the build",
                "example": "succeeded"
              }
            }
          },
          "results": {
            "type": "object",
            "description": "The results of the run",
            "example": {}
          },
          "specification_hash": {
            "type": "string",
            "description": "The hash of the app specification",
            "example": "8c0a4e6d2f"
          },
          "traces": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "timestamp": {
                    "type": "number",
                    "description": "The timestamp of the trace",
                    "example": 1234567890
                  },
                  "trace": {
                    "type": "object",
                    "description": "The trace",
                    "example": {}
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```
