# Create an app run

Starts an execution of app {aId} in Space {spaceId} and returns the resulting run.

```http
POST /api/v1/w/{wId}/spaces/{spaceId}/apps/{aId}/runs
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Unique string identifier for the workspace |
| `spaceId` | path | string | Yes | ID of the space |
| `aId` | path | string | Yes | Unique identifier of the app |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `specification_hash` | string | Yes |
| `config` | object | Yes |
| `inputs` | array[object] | Yes |
| `stream` | boolean | No |
| `blocking` | boolean | No |
| `block_filter` | array[string] | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | App run created and executed successfully |
| 400 | Bad Request. Missing or invalid parameters. |
| 401 | Unauthorized. Invalid or missing authentication token. |
| 404 | Workspace or app not found. |
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
    "/api/v1/w/{wId}/spaces/{spaceId}/apps/{aId}/runs": {
      "post": {
        "summary": "Create an app run",
        "description": "Starts an execution of app {aId} in Space {spaceId} and returns the resulting run.",
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
            "description": "Unique identifier of the app",
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
                "required": [
                  "specification_hash",
                  "config",
                  "inputs"
                ],
                "properties": {
                  "specification_hash": {
                    "type": "string",
                    "description": "Hash of the app specification. Ensures API compatibility across app iterations."
                  },
                  "config": {
                    "type": "object",
                    "description": "Configuration for the app run",
                    "properties": {
                      "model": {
                        "type": "object",
                        "description": "Model configuration",
                        "properties": {
                          "provider_id": {
                            "type": "string",
                            "description": "ID of the model provider"
                          },
                          "model_id": {
                            "type": "string",
                            "description": "ID of the model"
                          },
                          "use_cache": {
                            "type": "boolean",
                            "description": "Whether to use caching"
                          },
                          "use_stream": {
                            "type": "boolean",
                            "description": "Whether to use streaming"
                          }
                        }
                      }
                    }
                  },
                  "inputs": {
                    "type": "array",
                    "description": "Array of input objects for the app",
                    "items": {
                      "type": "object",
                      "additionalProperties": true
                    }
                  },
                  "stream": {
                    "type": "boolean",
                    "description": "If true, the response will be streamed"
                  },
                  "blocking": {
                    "type": "boolean",
                    "description": "If true, the request will block until the run is complete"
                  },
                  "block_filter": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Array of block names to filter the response"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "App run created and executed successfully",
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
          },
          "404": {
            "description": "Workspace or app not found."
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
