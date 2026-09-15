# List consumption analytics facets

Private session interface. Lists current and historical indexed values for each consumption dimension within the selected period. It disables a facet when other active filters leave no matching document. The workspace route requires a Manager, /me is limited to the signed-in member, and the agent route requires workspace Manager access or editor access to the selected Agent.

```http
POST /api/w/{wId}/analytics/consumption/facets
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes |  |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `period` | string | No |
| `days` | integer | No |
| `scope` | string | No |
| `dimensions` | array[string] | No |
| `filter` | object | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Consumption facets and their contextual availability |
| 400 | Invalid request body |
| 403 | Not authorized for this analytics view |
| 500 | Failed to retrieve consumption facets |

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
    "/api/w/{wId}/analytics/consumption/facets": {
      "post": {
        "summary": "List consumption analytics facets",
        "description": "Private session interface. Lists current and historical indexed values for each consumption dimension within the selected period. It disables a facet when other active filters leave no matching document. The workspace route requires a Manager, /me is limited to the signed-in member, and the agent route requires workspace Manager access or editor access to the selected Agent.",
        "tags": [
          "Private Analytics"
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
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
                  "period": {
                    "type": "string",
                    "enum": [
                      "cycle",
                      "days"
                    ],
                    "default": "cycle"
                  },
                  "days": {
                    "type": "integer",
                    "minimum": 1,
                    "default": 30
                  },
                  "scope": {
                    "type": "string",
                    "enum": [
                      "all",
                      "automations"
                    ],
                    "default": "all",
                    "description": "Restricts which documents the facets are computed over. `automations` counts only trigger-originated runs."
                  },
                  "dimensions": {
                    "type": "array",
                    "description": "Dimensions to compute facets for. Defaults to every dimension. Omitted dimensions come back as empty arrays. The personal route omits user and group dimensions, and the agent route omits the agent dimension.",
                    "items": {
                      "type": "string",
                      "enum": [
                        "agent",
                        "user",
                        "api_key",
                        "group",
                        "model",
                        "tool",
                        "skill",
                        "source"
                      ]
                    }
                  },
                  "filter": {
                    "type": "object",
                    "description": "Map of consumption dimensions to selected values.",
                    "additionalProperties": false,
                    "properties": {
                      "agents": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "users": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "api_keys": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "groups": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "models": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "tools": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "skills": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "sources": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "security": [
          {
            "UserAccessToken": []
          },
          {
            "BrowserSession": []
          }
        ],
        "responses": {
          "200": {
            "description": "Consumption facets and their contextual availability",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "required": [
                    "period",
                    "facets"
                  ],
                  "properties": {
                    "period": {
                      "type": "object",
                      "required": [
                        "startDate",
                        "endDate"
                      ],
                      "properties": {
                        "startDate": {
                          "type": "string",
                          "format": "date-time"
                        },
                        "endDate": {
                          "type": "string",
                          "format": "date-time"
                        }
                      }
                    },
                    "facets": {
                      "type": "object",
                      "required": [
                        "agent",
                        "user",
                        "api_key",
                        "group",
                        "model",
                        "tool",
                        "skill",
                        "source"
                      ],
                      "properties": {
                        "agent": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/PrivateConsumptionFacet"
                          }
                        },
                        "user": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/PrivateConsumptionFacet"
                          }
                        },
                        "api_key": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/PrivateConsumptionFacet"
                          }
                        },
                        "group": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/PrivateConsumptionFacet"
                          }
                        },
                        "model": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/PrivateConsumptionFacet"
                          }
                        },
                        "tool": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/PrivateConsumptionFacet"
                          }
                        },
                        "skill": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/PrivateConsumptionFacet"
                          }
                        },
                        "source": {
                          "type": "array",
                          "items": {
                            "$ref": "#/components/schemas/PrivateConsumptionFacet"
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
            "description": "Invalid request body"
          },
          "403": {
            "description": "Not authorized for this analytics view"
          },
          "500": {
            "description": "Failed to retrieve consumption facets"
          }
        },
        "x-counso-auth": "user"
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
      "PrivateConsumptionFacet": {
        "type": "object",
        "required": [
          "value",
          "label",
          "pictureUrl",
          "documentCount",
          "disabled"
        ],
        "properties": {
          "value": {
            "type": "string",
            "description": "Raw indexed value accepted by the corresponding consumption filter."
          },
          "label": {
            "type": "string",
            "description": "Human-readable label, falling back to the raw value when its resource was deleted."
          },
          "pictureUrl": {
            "type": "string",
            "nullable": true
          },
          "icon": {
            "type": "string",
            "nullable": true,
            "description": "Design-system icon name for tool and skill facets when known."
          },
          "documentCount": {
            "type": "integer",
            "minimum": 0,
            "description": "Number of matching indexed documents after applying the selected period and every other facet."
          },
          "disabled": {
            "type": "boolean",
            "description": "Whether selecting this value would produce no matching indexed document."
          },
          "scope": {
            "type": "string",
            "enum": [
              "global",
              "visible",
              "hidden"
            ],
            "description": "Current agent scope, when the agent still has accessible configuration metadata."
          },
          "maker": {
            "type": "string",
            "description": "Model maker, for known model facets."
          },
          "tier": {
            "type": "string",
            "enum": [
              "cost_efficient",
              "balanced",
              "premium"
            ],
            "description": "Default reasoning-effort tier, for known model facets."
          }
        }
      }
    }
  }
}
```
