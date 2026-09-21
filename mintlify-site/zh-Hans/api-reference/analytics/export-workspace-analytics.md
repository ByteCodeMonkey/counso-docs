---
title: "导出工作区分析数据"
---
将指定工作区的分析数据导出为 CSV 或 JSON。

```http
GET /api/v1/w/{wId}/analytics/export
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区的唯一字符串标识符 |
| `table` | 查询 | string | 是 | 要导出的分析表：usage_metrics：随时间变化的消息数、对话数和活跃用户；active_users：日、周、月活跃用户数；source：按上下文来源（web、slack 等）统计的消息量；agents：按消息数排序的热门智能体及其 credits；users：按消息数排序的用户及其 credits、最近登录日期和成员状态（active、revoked、unregistered）；skills：Skill 元数据目录；skill_usage：随时间变化的 Skill 执行次数和独立用户数；tool_usage：随时间变化的工具执行次数和独立用户数；messages：消息级明细日志，包括每条消息调用的工具（格式为 server__tool）和 Skills 列表，以及每条消息的 credits 成本；feedback：消息级详细反馈，包括评分、内容和对话 URL。 可选值：`usage_metrics`, `active_users`, `source`, `agents`, `users`, `skills`, `skill_usage`, `tool_usage`, `messages`, `feedback` |
| `startDate` | 查询 | string / date | 是 | 开始日期，格式为 YYYY-MM-DD |
| `endDate` | 查询 | string / date | 是 | 结束日期，格式为 YYYY-MM-DD |
| `timezone` | 查询 | string | 否 | IANA 时区名称（默认值为 UTC） |
| `format` | 查询 | string | 否 | 输出格式（默认值为 csv） 可选值：`csv`, `json` |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | CSV 或 JSON 格式的分析数据 |
| 400 | 请求查询参数无效 |
| 403 | 需要具有 admin scope 的 API key |

## 接口规范

可下载完整的[OpenAPI / Postman](/zh-Hans/docs/developer-platform/counso-api-documentation/openapi-and-postman) 文件。

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
