# 接收工作区 MCP 工具请求流

通过 SSE 长连接实时接收工作区发给客户端 MCP 服务器的工具请求。

```http
GET /api/v1/w/{wId}/mcp/requests
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入用户 OAuth access token。客户端 MCP 的注册与通信接口不接受工作区 API key。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `serverId` | 查询 | string | 是 | 用于筛选事件的 MCP 服务器 ID |
| `lastEventId` | 查询 | string | 否 | 用于筛选事件的最后一个事件 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 连接成功。事件将以 Server-Sent Events 格式持续发送；每个事件包含一项需要 MCP 服务器处理的工具请求。 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 403 | 禁止访问：你无权访问此工作区或 MCP 服务器。 |
| 500 | 内部服务器错误。 |

## 接口规范

可下载完整的[OpenAPI / Postman](../../docs/developer-platform/counso-api-documentation/openapi-and-postman.md) 文件。

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
