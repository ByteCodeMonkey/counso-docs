---
title: "Export agent configuration as YAML"
---
Produces a downloadable YAML copy of the agent configuration selected by {sId}.

```http
GET /api/v1/w/{wId}/assistant/agent_configurations/{sId}/export/yaml
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | ID of the workspace |
| `sId` | path | string | Yes | ID of the agent configuration |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | The agent configuration as a downloadable YAML file |
| 400 | Bad Request. Invalid or missing parameters. |
| 401 | Unauthorized. Invalid or missing authentication token. |
| 404 | Agent configuration not found. |
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
    "/api/v1/w/{wId}/assistant/agent_configurations/{sId}/export/yaml": {
      "get": {
        "summary": "Export agent configuration as YAML",
        "description": "Produces a downloadable YAML copy of the agent configuration selected by {sId}.",
        "tags": [
          "Agents"
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
            "name": "sId",
            "required": true,
            "description": "ID of the agent configuration",
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
        "responses": {
          "200": {
            "description": "The agent configuration as a downloadable YAML file",
            "content": {
              "text/yaml": {
                "schema": {
                  "type": "string"
                }
              }
            },
            "headers": {
              "Content-Disposition": {
                "description": "Attachment with suggested filename",
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "400": {
            "description": "Bad Request. Invalid or missing parameters."
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
          },
          "404": {
            "description": "Agent configuration not found."
          },
          "500": {
            "description": "Internal Server Error."
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
