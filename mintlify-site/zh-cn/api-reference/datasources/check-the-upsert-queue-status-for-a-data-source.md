---
title: "检查数据源的写入队列状态"
---
查看数据源中正在运行的文档 upsert 工作流数量。此接口仅供系统 API key 使用，例如连接器调用。

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/check_upsert_queue
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `spaceId` | 路径 | string | 是 | Space ID |
| `dsId` | 路径 | string | 是 | 数据源 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | upsert 队列状态 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 403 | 禁止访问：此接口仅允许 system key 调用。 |
| 404 | 未找到数据源。 |
| 500 | 内部服务器错误。 |

## 接口规范

可下载完整的[OpenAPI / Postman](/zh-cn/docs/developer-platform/counso-api-documentation/openapi-and-postman) 文件。

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/check_upsert_queue": {
      "get": {
        "summary": "Check the upsert queue status for a data source",
        "description": "Reports how many document upsert workflows are currently running for the data source. Calls are restricted to system API keys, such as those used by connectors.",
        "tags": [
          "Datasources"
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
            "name": "spaceId",
            "required": true,
            "description": "ID of the space",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "dsId",
            "required": true,
            "description": "ID of the data source",
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
            "description": "Status of the upsert queue",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "running_count": {
                      "type": "number",
                      "description": "Number of currently running upsert workflows"
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
            "description": "Forbidden. Only system keys can access this endpoint."
          },
          "404": {
            "description": "Data source not found."
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
