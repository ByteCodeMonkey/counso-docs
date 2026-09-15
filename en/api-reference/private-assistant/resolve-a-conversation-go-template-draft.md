# Resolve a conversation go template draft

Private session interface. Resolves a Contentful conversation template from its slug and prepares a composer-ready draft, with optional attachments uploaded in advance.

```http
GET /api/w/{wId}/assistant/go-template
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `slug` | query | string | Yes | Contentful template slug |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Composer draft resolved from the template |
| 404 | Template not found or disabled |
| 422 | Missing slug query parameter |

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
    "/api/w/{wId}/assistant/go-template": {
      "get": {
        "summary": "Resolve a conversation go template draft",
        "description": "Private session interface. Resolves a Contentful conversation template from its slug and prepares a composer-ready draft, with optional attachments uploaded in advance.",
        "tags": [
          "Private Assistant"
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
            "in": "query",
            "name": "slug",
            "required": true,
            "description": "Contentful template slug",
            "schema": {
              "type": "string"
            }
          }
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
            "description": "Composer draft resolved from the template",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetGoTemplateDraftResponseBody"
                }
              }
            }
          },
          "404": {
            "description": "Template not found or disabled"
          },
          "422": {
            "description": "Missing slug query parameter"
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
      "GetGoTemplateDraftResponseBody": {
        "type": "object",
        "description": "Composer draft resolved from a Contentful conversation go template.",
        "required": [
          "title",
          "prompt",
          "attachments",
          "attachmentErrors"
        ],
        "properties": {
          "title": {
            "type": "string"
          },
          "prompt": {
            "type": "string"
          },
          "attachments": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "fileId",
                "name",
                "contentType",
                "size",
                "url"
              ],
              "properties": {
                "fileId": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "contentType": {
                  "type": "string"
                },
                "size": {
                  "type": "integer"
                },
                "url": {
                  "type": "string"
                }
              }
            }
          },
          "attachmentErrors": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "url",
                "message"
              ],
              "properties": {
                "url": {
                  "type": "string"
                },
                "message": {
                  "type": "string"
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
