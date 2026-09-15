---
title: "Update current user"
---
Private session interface. Saves profile changes for the current user, including name, job type, favorite platforms, and image.

```http
PATCH /api/user
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `firstName` | string | Yes |
| `lastName` | string | Yes |
| `jobType` | string | No |
| `imageUrl` | string | No |
| `favoritePlatforms` | array[string] | No |
| `emailProvider` | string | No |
| `workspaceId` | string | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | User updated successfully |
| 400 | Invalid request body |
| 404 | User not found |

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
    "/api/user": {
      "patch": {
        "summary": "Update current user",
        "description": "Private session interface. Saves profile changes for the current user, including name, job type, favorite platforms, and image.",
        "tags": [
          "Private User"
        ],
        "security": [
          {
            "UserAccessToken": []
          },
          {
            "BrowserSession": []
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "firstName",
                  "lastName"
                ],
                "properties": {
                  "firstName": {
                    "type": "string"
                  },
                  "lastName": {
                    "type": "string"
                  },
                  "jobType": {
                    "type": "string"
                  },
                  "imageUrl": {
                    "type": "string",
                    "nullable": true
                  },
                  "favoritePlatforms": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    }
                  },
                  "emailProvider": {
                    "type": "string"
                  },
                  "workspaceId": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "User updated successfully",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request body"
          },
          "404": {
            "description": "User not found"
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
    }
  }
}
```
