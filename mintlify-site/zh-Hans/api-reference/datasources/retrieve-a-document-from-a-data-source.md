---
title: "从数据源读取文档"
---
按数据源 ID 获取指定工作区中的文档。

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}
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
| `documentId` | 路径 | string | 是 | 文档 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 该文档 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 404 | 未找到数据源或文档。 |
| 500 | 内部服务器错误。 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}": {
      "get": {
        "summary": "Retrieve a document from a data source",
        "description": "Fetches a document by its data-source ID {dsId} from workspace {wId}.",
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
          },
          {
            "in": "path",
            "name": "documentId",
            "required": true,
            "description": "ID of the document",
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
            "description": "The document",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "document": {
                      "$ref": "#/components/schemas/Document"
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
          "404": {
            "description": "Data source or document not found."
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
