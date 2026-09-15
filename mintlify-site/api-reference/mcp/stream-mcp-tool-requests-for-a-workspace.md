---
title: "Stream MCP tool requests for a workspace"
---
Opens an SSE stream that delivers workspace tool requests to connected client-side MCP servers as they are issued.

```http
GET /api/v1/w/{wId}/mcp/requests
```

Base URL: `https://app.counso.ai`

## Authentication

Use a user OAuth access token in `Authorization: Bearer <token>`. Workspace API keys are not accepted by client-side MCP registration and transport endpoints.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `serverId` | query | string | Yes | ID of the MCP server to filter events for |
| `lastEventId` | query | string | No | ID of the last event to filter events for |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | Connection established successfully. Events will be streamed in Server-Sent Events format.<br />Each event will contain a tool request that needs to be processed by the MCP server.<br /> |
| 400 | Bad Request. Missing or invalid parameters. |
| 401 | Unauthorized. Invalid or missing authentication token. |
| 403 | Forbidden. You don't have access to this workspace or MCP server. |
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
    "/api/v1/w/{wId}/mcp/requests": {
      "get": {
        "summary": "Stream MCP tool requests for a workspace",
        "description": "Opens an SSE stream that delivers workspace tool requests to connected client-side MCP servers as they are issued.",
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
          },
          {
            "in": "query",
            "name": "serverId",
            "required": true,
            "description": "ID of the MCP server to filter events for",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "lastEventId",
            "required": false,
            "description": "ID of the last event to filter events for",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Connection established successfully. Events will be streamed in Server-Sent Events format.\nEach event will contain a tool request that needs to be processed by the MCP server.\n",
            "content": {
              "text/event-stream": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string",
                      "description": "Type of the event (e.g. \"tool_request\")"
                    },
                    "data": {
                      "type": "object",
                      "description": "The tool request data"
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
          "403": {
            "description": "Forbidden. You don't have access to this workspace or MCP server."
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
