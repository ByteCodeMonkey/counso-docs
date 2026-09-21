---
title: "流式搜索工作区节点"
---
在工作区搜索节点，并通过 SSE 流式返回结果。

```http
GET /api/v1/w/{wId}/search
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `query` | 查询 | string | 是 | 搜索词（至少 3 个字符） |
| `limit` | 查询 | integer | 否 | 每页结果数（1–100，默认 25） |
| `cursor` | 查询 | string | 否 | 分页游标 |
| `viewType` | 查询 | string | 否 | 用于筛选结果的视图类型 可选值：`all`, `document`, `table` |
| `spaceIds` | 查询 | string | 否 | 要搜索的 Space ID 列表，以逗号分隔 |
| `includeDataSources` | 查询 | boolean | 否 | 是否包含数据源 |
| `searchSourceUrls` | 查询 | boolean | 否 | 是否搜索来源 URL |
| `includeTools` | 查询 | boolean | 否 | 是否包含工具结果 |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已成功以流形式返回搜索结果 |
| 400 | 请求错误 |
| 401 | 未授权 |

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
    "/api/v1/w/{wId}/search": {
      "get": {
        "summary": "Search for nodes in the workspace (streaming)",
        "description": "Searches workspace nodes and sends matching results incrementally over SSE.",
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
          },
          {
            "in": "query",
            "name": "query",
            "required": true,
            "description": "The search query (minimum 3 characters)",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "limit",
            "required": false,
            "description": "Number of results per page (1-100, default 25)",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "cursor",
            "required": false,
            "description": "Cursor for pagination",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "viewType",
            "required": false,
            "description": "Type of view to filter results",
            "schema": {
              "type": "string",
              "enum": [
                "all",
                "document",
                "table"
              ]
            }
          },
          {
            "in": "query",
            "name": "spaceIds",
            "required": false,
            "description": "Comma-separated list of space IDs to search in",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "includeDataSources",
            "required": false,
            "description": "Whether to include data sources",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "in": "query",
            "name": "searchSourceUrls",
            "required": false,
            "description": "Whether to search source URLs",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "in": "query",
            "name": "includeTools",
            "required": false,
            "description": "Whether to include tool results",
            "schema": {
              "type": "boolean"
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
            "description": "Search results streamed successfully",
            "content": {
              "text/event-stream": {
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "400": {
            "description": "Bad request"
          },
          "401": {
            "description": "Unauthorized"
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
