---
title: "Deregister a client-side MCP server"
---
Removes the registration for a client-side MCP server that was registered earlier.

```http
POST /api/v1/w/{wId}/mcp/deregister
```

Base URL: `https://app.counso.ai`

## Authentication

Use a user OAuth access token in `Authorization: Bearer <token>`. Workspace API keys are not accepted by client-side MCP registration and transport endpoints.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |

## Request body

`Content-Type: application/json`

| Field | Type | Required |
| --- | --- | --- |
| `serverId` | string | Yes |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Server deregistered successfully |
| 401 | Unauthorized. Invalid or missing authentication token. |
| 403 | Forbidden. User does not have access to the workspace. |

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
    "/api/v1/w/{wId}/mcp/deregister": {
      "post": {
        "summary": "Deregister a client-side MCP server",
        "description": "Removes the registration for a client-side MCP server that was registered earlier.",
        "tags": [
          "MCP"
        ],
        "security": [
          {
            "UserAccessToken": []
          }
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
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "serverId"
                ],
                "properties": {
                  "serverId": {
                    "type": "string",
                    "description": "The ID of the registered MCP server"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Server deregistered successfully"
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
          },
          "403": {
            "description": "Forbidden. User does not have access to the workspace."
          }
        },
        "x-counso-auth": "mcp"
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
