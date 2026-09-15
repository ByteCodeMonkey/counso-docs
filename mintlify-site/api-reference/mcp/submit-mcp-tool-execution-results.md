---
title: "Submit MCP tool execution results"
---
Sends back the output produced by tools that a client-side MCP server ran locally.

```http
POST /api/v1/w/{wId}/mcp/results
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
| `result` | object | Yes |
| `serverId` | string | Yes |

Field constraints and nested structures are defined in the specification below.

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Tool execution results successfully submitted |
| 400 | Bad Request. Missing or invalid parameters. |
| 401 | Unauthorized. Invalid or missing authentication token. |
| 403 | Forbidden. You don't have access to this workspace or MCP server. |
| 404 | Conversation or message not found. |
| 500 | Internal Server Error. |

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
    "/api/v1/w/{wId}/mcp/results": {
      "post": {
        "summary": "Submit MCP tool execution results",
        "description": "Sends back the output produced by tools that a client-side MCP server ran locally.",
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
                  "result",
                  "serverId"
                ],
                "properties": {
                  "result": {
                    "type": "object",
                    "description": "The result data from the tool execution"
                  },
                  "serverId": {
                    "type": "string",
                    "description": "ID of the MCP server submitting the results"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Tool execution results successfully submitted"
          },
          "400": {
            "description": "Bad Request. Missing or invalid parameters."
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
          },
          "403": {
            "description": "Forbidden. You don't have access to this workspace or MCP server."
          },
          "404": {
            "description": "Conversation or message not found."
          },
          "500": {
            "description": "Internal Server Error."
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
