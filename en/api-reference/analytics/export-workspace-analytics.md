# Export workspace analytics

Generates a workspace analytics export for {wId}, encoded as either CSV or JSON.

```http
GET /api/v1/w/{wId}/analytics/export
```

Base URL: `https://app.counso.ai`

## Authentication

Send a workspace API key or a user OAuth access token in `Authorization: Bearer <token>`. The credential must belong to this Counso deployment and have access to the requested workspace and resources.

## Parameters

| Parameter | Location | Type | Required | Description |
| --- | --- | --- | --- | --- |
| `wId` | path | string | Yes | Unique string identifier for the workspace |
| `table` | query | string | Yes | The analytics table to export:<br>- "usage_metrics": Messages, conversations, and active users over time.<br>- "active_users": Daily, weekly, and monthly active user counts.<br>- "source": Message volume by context origin (web, slack, etc.).<br>- "agents": Top agents by message count, including credits.<br>- "users": Top users by message count, including credits, last login date and membership status (active, revoked, unregistered).<br>- "skills": Skill metadata catalog.<br>- "skill_usage": Skill executions and unique users over time.<br>- "tool_usage": Tool executions and unique users over time.<br>- "messages": Detailed message-level logs, including comma-separated lists of tools (as "server__tool") and skills used per message, and the cost in credits of each message.<br>- "feedback": Detailed message-level feedback (thumbs, content, conversation URL).<br> Values: `usage_metrics`, `active_users`, `source`, `agents`, `users`, `skills`, `skill_usage`, `tool_usage`, `messages`, `feedback` |
| `startDate` | query | string / date | Yes | Start date in YYYY-MM-DD format |
| `endDate` | query | string / date | Yes | End date in YYYY-MM-DD format |
| `timezone` | query | string | No | IANA timezone name (defaults to UTC) |
| `format` | query | string | No | Output format (defaults to csv) Values: `csv`, `json` |

## Responses

| HTTP status | Description |
| --- | --- |
| 200 | The analytics data in CSV or JSON format |
| 400 | Invalid request query parameters |
| 403 | Requires an API key with admin scope |

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
    "/api/v1/w/{wId}/analytics/export": {
      "get": {
        "summary": "Export workspace analytics",
        "description": "Generates a workspace analytics export for {wId}, encoded as either CSV or JSON.",
        "tags": [
          "Analytics"
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "description": "Unique string identifier for the workspace",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "table",
            "required": true,
            "description": "The analytics table to export:\n- \"usage_metrics\": Messages, conversations, and active users over time.\n- \"active_users\": Daily, weekly, and monthly active user counts.\n- \"source\": Message volume by context origin (web, slack, etc.).\n- \"agents\": Top agents by message count, including credits.\n- \"users\": Top users by message count, including credits, last login date and membership status (active, revoked, unregistered).\n- \"skills\": Skill metadata catalog.\n- \"skill_usage\": Skill executions and unique users over time.\n- \"tool_usage\": Tool executions and unique users over time.\n- \"messages\": Detailed message-level logs, including comma-separated lists of tools (as \"server__tool\") and skills used per message, and the cost in credits of each message.\n- \"feedback\": Detailed message-level feedback (thumbs, content, conversation URL).\n",
            "schema": {
              "type": "string",
              "enum": [
                "usage_metrics",
                "active_users",
                "source",
                "agents",
                "users",
                "skills",
                "skill_usage",
                "tool_usage",
                "messages",
                "feedback"
              ]
            }
          },
          {
            "in": "query",
            "name": "startDate",
            "required": true,
            "description": "Start date in YYYY-MM-DD format",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "in": "query",
            "name": "endDate",
            "required": true,
            "description": "End date in YYYY-MM-DD format",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "in": "query",
            "name": "timezone",
            "required": false,
            "description": "IANA timezone name (defaults to UTC)",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "format",
            "required": false,
            "description": "Output format (defaults to csv)",
            "schema": {
              "type": "string",
              "enum": [
                "csv",
                "json"
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The analytics data in CSV or JSON format",
            "content": {
              "text/csv": {
                "schema": {
                  "type": "string"
                }
              },
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object"
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request query parameters"
          },
          "403": {
            "description": "Requires an API key with admin scope"
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
