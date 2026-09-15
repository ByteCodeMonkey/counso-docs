# Get or download a file

Private session interface. Opens or downloads a file. Reading a Skill attachment requires read access to that Skill; version (original, processed, public) and action (view, download) select the returned content and operation.

```http
GET /api/w/{wId}/files/{fileId}
```

Base URL: `https://app.counso.ai`

## Authentication

This operation requires a user OAuth access token in `Authorization: Bearer <token>`. A signed-in browser may use its Counso session cookie. A workspace API key does not supply user identity.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `fileId` | path | string | Yes | ID of the file |
| `version` | query | string | No | File version to retrieve Values: `original`, `processed`, `public` |
| `action` | query | string | No | Action to perform Values: `view`, `download` |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | File content or redirect to download URL |
| 302 | Redirect to signed download URL |
| 404 | File not found |

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
    "/api/w/{wId}/files/{fileId}": {
      "get": {
        "summary": "Get or download a file",
        "description": "Private session interface. Opens or downloads a file. Reading a Skill attachment requires read access to that Skill; version (original, processed, public) and action (view, download) select the returned content and operation.",
        "tags": [
          "Private Files"
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
            "name": "fileId",
            "required": true,
            "description": "ID of the file",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "version",
            "required": false,
            "description": "File version to retrieve",
            "schema": {
              "type": "string",
              "enum": [
                "original",
                "processed",
                "public"
              ]
            }
          },
          {
            "in": "query",
            "name": "action",
            "required": false,
            "description": "Action to perform",
            "schema": {
              "type": "string",
              "enum": [
                "view",
                "download"
              ]
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
            "description": "File content or redirect to download URL",
            "content": {
              "application/octet-stream": {
                "schema": {
                  "type": "string",
                  "format": "binary"
                }
              }
            }
          },
          "302": {
            "description": "Redirect to signed download URL"
          },
          "404": {
            "description": "File not found"
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
