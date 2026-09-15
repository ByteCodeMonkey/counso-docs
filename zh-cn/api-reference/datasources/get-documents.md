# 列出数据源文档

获取指定工作区数据源中的文档列表。

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents
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
| `document_ids` | 查询 | array[string] | 否 | 要获取的文档 ID 列表（可选） |
| `limit` | 查询 | integer | 否 | 返回文档数量上限 |
| `offset` | 查询 | integer | 否 | 返回文档的偏移量 |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 文档列表 |
| 404 | 未找到该数据源 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents": {
      "get": {
        "summary": "Get documents",
        "description": "Lists documents belonging to data source {dsId} in workspace {wId}.",
        "tags": [
          "Datasources"
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
            "name": "dsId",
            "required": true,
            "description": "ID of the data source",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "document_ids",
            "description": "The IDs of the documents to fetch (optional)",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          {
            "in": "query",
            "name": "limit",
            "description": "Limit the number of documents returned",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "offset",
            "description": "Offset the returned documents",
            "schema": {
              "type": "integer"
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
                        "$ref": "#/components/schemas/Document"
                      }
                    },
                    "total": {
                      "type": "integer"
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "The data source was not found"
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
    },
    "schemas": {
      "Document": {
        "type": "object",
        "properties": {
          "data_source_id": {
            "type": "string",
            "example": "3b7d9f1e5a"
          },
          "created": {
            "type": "number",
            "example": 1625097600
          },
          "document_id": {
            "type": "string",
            "example": "2c4a6e8d0f"
          },
          "title": {
            "type": "string",
            "description": "Title of the document",
            "example": "Customer Support FAQ"
          },
          "mime_type": {
            "type": "string",
            "description": "MIME type of the table",
            "example": "text/md"
          },
          "timestamp": {
            "type": "number",
            "example": 1625097600
          },
          "tags": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              "customer_support",
              "faq"
            ]
          },
          "parent_id": {
            "type": "string",
            "description": "ID of the document parent",
            "items": {
              "type": "string"
            },
            "example": "1234f4567c"
          },
          "parents": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "example": [
              "7b9d1f3e5a",
              "2c4a6e8d0f"
            ]
          },
          "source_url": {
            "type": "string",
            "nullable": true,
            "example": "https://example.com/support/article1"
          },
          "hash": {
            "type": "string",
            "example": "a1b2c3d4e5"
          },
          "text_size": {
            "type": "number",
            "example": 1024
          },
          "chunk_count": {
            "type": "number",
            "example": 5
          },
          "chunks": {
            "type": "array",
            "items": {
              "type": "object"
            },
            "example": [
              {
                "chunk_id": "9f1d3b5a7c",
                "text": "This is the first chunk of the document.",
                "embedding": [
                  0.1,
                  0.2,
                  0.3,
                  0.4
                ]
              },
              {
                "chunk_id": "4a2c6e8b0d",
                "text": "This is the second chunk of the document.",
                "embedding": [
                  0.5,
                  0.6,
                  0.7,
                  0.8
                ]
              }
            ]
          },
          "text": {
            "type": "string",
            "example": "This is the full text content of the document. It contains multiple paragraphs and covers various topics related to customer support."
          },
          "token_count": {
            "type": "number",
            "nullable": true,
            "example": 150
          }
        }
      }
    }
  }
}
```
