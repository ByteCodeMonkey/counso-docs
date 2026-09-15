# Upload a tool file

Moves a file returned by an MCP server tool into the workspace by downloading and uploading its contents.

```http
POST /api/v1/w/{wId}/search/tools/upload
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `serverViewId` | string | Yes |
| `externalId` | string | Yes |
| `conversationId` | string | No |
| `serverName` | string | No |
| `serverIcon` | string | No |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | File uploaded successfully |
| 400 | Bad request |
| 401 | Unauthorized |
| 500 | Internal server error |

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
    "/api/v1/w/{wId}/search/tools/upload": {
      "post": {
        "summary": "Upload a tool file",
        "description": "Moves a file returned by an MCP server tool into the workspace by downloading and uploading its contents.",
        "tags": [
          "Search"
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
          }
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "serverViewId",
                  "externalId"
                ],
                "properties": {
                  "serverViewId": {
                    "type": "string",
                    "description": "The MCP server view ID"
                  },
                  "externalId": {
                    "type": "string",
                    "description": "The external ID of the file in the tool"
                  },
                  "conversationId": {
                    "type": "string",
                    "description": "Optional conversation ID for context"
                  },
                  "serverName": {
                    "type": "string",
                    "description": "Optional name of the MCP server (e.g., \"Notion\", \"GitHub\")"
                  },
                  "serverIcon": {
                    "type": "string",
                    "description": "Optional icon identifier for the MCP server"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "File uploaded successfully"
          },
          "400": {
            "description": "Bad request"
          },
          "401": {
            "description": "Unauthorized"
          },
          "500": {
            "description": "Internal server error"
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
    }
  }
}
```
