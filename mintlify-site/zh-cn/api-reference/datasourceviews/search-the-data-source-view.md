---
title: "搜索数据源视图"
---
在指定工作区的数据源视图中搜索内容。

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}/search
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `spaceId` | 路径 | string | 是 | Space ID |
| `dsvId` | 路径 | string | 是 | 数据源视图 ID |
| `query` | 查询 | string | 是 | 搜索词 |
| `top_k` | 查询 | number | 是 | 要返回的结果数 |
| `full_text` | 查询 | boolean | 是 | 是否返回完整文档内容 |
| `target_document_tokens` | 查询 | number | 否 | 目标文档中的 token 数 |
| `timestamp_gt` | 查询 | number | 否 | 用于筛选的时间戳 |
| `timestamp_lt` | 查询 | number | 否 | 用于筛选的时间戳 |
| `tags_in` | 查询 | string | 否 | 用于筛选的标签 |
| `tags_not` | 查询 | string | 否 | 用于筛选的标签 |
| `parents_in` | 查询 | string | 否 | 用于筛选的父级 |
| `parents_not` | 查询 | string | 否 | 用于筛选的父级 |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 文档列表 |
| 400 | 请求无效错误 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}/search": {
      "get": {
        "summary": "Search the data source view",
        "description": "Searches within view {dsvId} in workspace {wId}.",
        "tags": [
          "DatasourceViews"
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
            "name": "dsvId",
            "required": true,
            "description": "ID of the data source view",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "query",
            "required": true,
            "description": "The search query",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "top_k",
            "required": true,
            "description": "The number of results to return",
            "schema": {
              "type": "number"
            }
          },
          {
            "in": "query",
            "name": "full_text",
            "required": true,
            "description": "Whether to return the full document content",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "in": "query",
            "name": "target_document_tokens",
            "required": false,
            "description": "The number of tokens in the target document",
            "schema": {
              "type": "number"
            }
          },
          {
            "in": "query",
            "name": "timestamp_gt",
            "required": false,
            "description": "The timestamp to filter by",
            "schema": {
              "type": "number"
            }
          },
          {
            "in": "query",
            "name": "timestamp_lt",
            "required": false,
            "description": "The timestamp to filter by",
            "schema": {
              "type": "number"
            }
          },
          {
            "in": "query",
            "name": "tags_in",
            "required": false,
            "description": "The tags to filter by",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "tags_not",
            "required": false,
            "description": "The tags to filter by",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "parents_in",
            "required": false,
            "description": "The parents to filter by",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "parents_not",
            "required": false,
            "description": "The parents to filter by",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The documents",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "documents": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "ID of the document"
                          },
                          "title": {
                            "type": "string",
                            "description": "Title of the document"
                          },
                          "content": {
                            "type": "string",
                            "description": "Content of the document"
                          },
                          "tags": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": "Tags of the document"
                          },
                          "parents": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": "Parents of the document"
                          },
                          "timestamp": {
                            "type": "number",
                            "description": "Timestamp of the document"
                          },
                          "data": {
                            "type": "object",
                            "description": "Data of the document"
                          },
                          "score": {
                            "type": "number",
                            "description": "Score of the document"
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request error"
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
