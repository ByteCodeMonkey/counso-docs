# 搜索工作区节点

在工作区中搜索内容节点。

```http
POST /api/v1/w/{wId}/search
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `query` | string | 是 |
| `includeDataSources` | boolean | 否 |
| `viewType` | string | 否 |
| `spaceIds` | array[string] | 否 |
| `nodeIds` | array[string] | 否 |
| `searchSourceUrls` | boolean | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已成功获取搜索结果 |
| 400 | 请求错误 |
| 401 | 未授权 |
| 404 | 未找到 Space |

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
    "/api/v1/w/{wId}/search": {
      "post": {
        "summary": "Search for nodes in the workspace",
        "description": "Finds nodes in the workspace that match the supplied search criteria.",
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
                  "query"
                ],
                "properties": {
                  "query": {
                    "type": "string",
                    "description": "The search query"
                  },
                  "includeDataSources": {
                    "type": "boolean",
                    "description": "List of data source IDs to include in search"
                  },
                  "viewType": {
                    "type": "string",
                    "description": "Type of view to filter results"
                  },
                  "spaceIds": {
                    "type": "array",
                    "description": "List of space IDs to search in",
                    "items": {
                      "type": "string"
                    }
                  },
                  "nodeIds": {
                    "type": "array",
                    "description": "List of specific node IDs to search",
                    "items": {
                      "type": "string"
                    }
                  },
                  "searchSourceUrls": {
                    "type": "boolean",
                    "description": "Whether to search source URLs"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Search results retrieved successfully"
          },
          "400": {
            "description": "Bad request"
          },
          "401": {
            "description": "Unauthorized"
          },
          "404": {
            "description": "Space not found"
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
