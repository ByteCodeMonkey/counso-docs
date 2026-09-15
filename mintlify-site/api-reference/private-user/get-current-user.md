---
title: "Get current user"
---
Private session interface. Returns the signed-in user's profile together with associated workspaces and subscriber hash.

```http
GET /api/user
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | The authenticated user |
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
      "get": {
        "summary": "Get current user",
        "description": "Private session interface. Returns the signed-in user's profile together with associated workspaces and subscriber hash.",
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
        "responses": {
          "200": {
            "description": "The authenticated user",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "user": {
                      "$ref": "#/components/schemas/PrivateUser"
                    }
                  }
                }
              }
            }
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
    },
    "schemas": {
      "PrivateUser": {
        "type": "object",
        "description": "Authenticated user with their workspaces and subscriber hash.",
        "required": [
          "sId",
          "id",
          "createdAt",
          "username",
          "email",
          "firstName",
          "fullName",
          "workspaces"
        ],
        "properties": {
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the user"
          },
          "id": {
            "type": "integer",
            "description": "Numeric model identifier"
          },
          "createdAt": {
            "type": "integer",
            "description": "Unix timestamp of user creation"
          },
          "provider": {
            "type": "string",
            "nullable": true,
            "enum": [
              "auth0",
              "github",
              "google",
              "okta",
              "samlp",
              "waad"
            ],
            "description": "Authentication provider"
          },
          "username": {
            "type": "string"
          },
          "email": {
            "type": "string"
          },
          "firstName": {
            "type": "string"
          },
          "lastName": {
            "type": "string",
            "nullable": true
          },
          "fullName": {
            "type": "string"
          },
          "image": {
            "type": "string",
            "nullable": true,
            "description": "URL of the user's profile image"
          },
          "lastLoginAt": {
            "type": "integer",
            "nullable": true
          },
          "workspaces": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PrivateWorkspace"
            }
          },
          "selectedWorkspace": {
            "type": "string",
            "description": "sId of the currently selected workspace"
          },
          "origin": {
            "type": "string",
            "description": "How the user joined (e.g. invitation, provisioned)"
          },
          "subscriberHash": {
            "type": "string",
            "nullable": true,
            "description": "Hash used for Intercom identity verification"
          }
        }
      },
      "PrivateWorkspace": {
        "type": "object",
        "description": "Workspace as returned by the private API, includes SSO and provider settings.",
        "required": [
          "id",
          "sId",
          "name",
          "role",
          "regionalModelsOnly"
        ],
        "properties": {
          "id": {
            "type": "integer"
          },
          "sId": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "role": {
            "type": "string",
            "enum": [
              "admin",
              "builder",
              "user",
              "none"
            ]
          },
          "segmentation": {
            "type": "string",
            "nullable": true
          },
          "whiteListedProviders": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            },
            "description": "Allowed model provider IDs"
          },
          "defaultEmbeddingProvider": {
            "type": "string",
            "nullable": true
          },
          "ssoEnforced": {
            "type": "boolean"
          },
          "regionalModelsOnly": {
            "type": "boolean",
            "description": "When true, only models whose regionalAvailability includes the workspace's region are usable."
          },
          "metadata": {
            "type": "object",
            "nullable": true,
            "additionalProperties": true
          }
        }
      }
    }
  }
}
```
