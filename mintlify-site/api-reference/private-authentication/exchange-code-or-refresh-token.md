---
title: "Exchange code or refresh token"
---
Exchanges a WorkOS authorization code or refresh token for user access tokens as part of sign-in or session renewal. An existing Bearer token is not required.

```http
POST /api/workos/authenticate
```

Base URL: `https://app.counso.ai`

## Authentication

Exchange an authorization code (and its PKCE verifier when applicable), or send grant_type=refresh_token with a refresh token. No existing Bearer token is required. JSON and form-encoded request bodies are accepted.

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `code` | string | No |
| `grant_type` | string | No |
| `refresh_token` | string | No |
| `code_verifier` | string | No |

`Content-Type: application/x-www-form-urlencoded`

| Field | Type | Required |
| --- | --- | --- |
| `code` | string | No |
| `grant_type` | string | No |
| `refresh_token` | string | No |
| `code_verifier` | string | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Authentication result with tokens |
| 400 | Invalid request |

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
    "/api/workos/authenticate": {
      "post": {
        "summary": "Exchange code or refresh token",
        "description": "Exchanges a WorkOS authorization code or refresh token for user access tokens as part of sign-in or session renewal. An existing Bearer token is not required.",
        "tags": [
          "Private Authentication"
        ],
        "security": [],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "code": {
                    "type": "string"
                  },
                  "grant_type": {
                    "type": "string",
                    "enum": [
                      "refresh_token"
                    ]
                  },
                  "refresh_token": {
                    "type": "string"
                  },
                  "code_verifier": {
                    "type": "string"
                  }
                }
              },
              "examples": {
                "authorization_code": {
                  "summary": "Exchange an authorization code",
                  "value": {
                    "code": "{{authorizationCode}}",
                    "code_verifier": "{{codeVerifier}}"
                  }
                },
                "refresh_token": {
                  "summary": "Refresh a user session",
                  "value": {
                    "grant_type": "refresh_token",
                    "refresh_token": "{{refreshToken}}"
                  }
                }
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "type": "object",
                "properties": {
                  "code": {
                    "type": "string"
                  },
                  "grant_type": {
                    "type": "string",
                    "enum": [
                      "refresh_token"
                    ]
                  },
                  "refresh_token": {
                    "type": "string"
                  },
                  "code_verifier": {
                    "type": "string"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Authentication result with tokens",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "accessToken": {
                      "type": "string"
                    },
                    "refreshToken": {
                      "type": "string"
                    },
                    "user": {
                      "type": "object"
                    },
                    "expiresIn": {
                      "type": "integer",
                      "description": "Token expiry in seconds"
                    },
                    "expirationDate": {
                      "type": "integer",
                      "description": "Token expiry date in milliseconds"
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
        "x-counso-auth": "login"
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
