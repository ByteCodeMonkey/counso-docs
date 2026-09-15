# 写入或更新数据源文档

在指定工作区的数据源中新增文档，或更新已有文档。

```http
POST /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}
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

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `title` | string | 否 |
| `mime_type` | string | 否 |
| `text` | string | 否 |
| `section` | object | 否 |
| `source_url` | string | 否 |
| `tags` | array[string] | 否 |
| `timestamp` | number | 否 |
| `light_document_output` | boolean | 否 |
| `async` | boolean | 否 |
| `upsert_context` | object | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 该文档 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 403 | 禁止访问：该数据源由系统管理。 |
| 404 | 未找到数据源或文档。 |
| 429 | 超出速率限制。 |
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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}": {
      "post": {
        "summary": "Upsert a document in a data source",
        "description": "Creates or replaces a document entry in a workspace data source.",
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
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "title": {
                    "type": "string",
                    "description": "The title of the document to upsert."
                  },
                  "mime_type": {
                    "type": "string",
                    "description": "The MIME type of the document to upsert."
                  },
                  "text": {
                    "type": "string",
                    "description": "The text content of the document to upsert."
                  },
                  "section": {
                    "$ref": "#/components/schemas/Section"
                  },
                  "source_url": {
                    "type": "string",
                    "description": "The source URL for the document to upsert."
                  },
                  "tags": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Tags to associate with the document."
                  },
                  "timestamp": {
                    "type": "number",
                    "description": "Unix timestamp (in milliseconds) for the document (e.g. 1736365559000)."
                  },
                  "light_document_output": {
                    "type": "boolean",
                    "description": "If true, a lightweight version of the document will be returned in the response (excluding the text, chunks and vectors). Defaults to false."
                  },
                  "async": {
                    "type": "boolean",
                    "description": "If true, the upsert operation will be performed asynchronously."
                  },
                  "upsert_context": {
                    "type": "object",
                    "description": "Additional context for the upsert operation."
                  }
                }
              }
            }
          }
        },
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
                    },
                    "data_source": {
                      "$ref": "#/components/schemas/Datasource"
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
            "description": "Forbidden. The data source is managed."
          },
          "404": {
            "description": "Data source or document not found."
          },
          "429": {
            "description": "Rate limit exceeded."
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
      "Datasource": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the datasource",
            "example": 12345
          },
          "createdAt": {
            "type": "integer",
            "description": "Timestamp of when the datasource was created",
            "example": 1625097600
          },
          "name": {
            "type": "string",
            "description": "Name of the datasource",
            "example": "Customer Knowledge Base"
          },
          "description": {
            "type": "string",
            "description": "Description of the datasource",
            "example": "Contains all customer-related information and FAQs"
          },
          "dustAPIProjectId": {
            "type": "string",
            "description": "ID of the associated Counso API project",
            "example": "5e9d8c7b6a"
          },
          "connectorId": {
            "type": "string",
            "description": "ID of the connector used for this datasource",
            "example": "1f3e5d7c9b"
          },
          "connectorProvider": {
            "type": "string",
            "description": "Provider of the connector (e.g., 'webcrawler')",
            "example": "webcrawler"
          },
          "assistantDefaultSelected": {
            "type": "boolean",
            "description": "Whether this datasource is selected by default for agents",
            "example": true
          }
        }
      },
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
      },
      "Section": {
        "type": "object",
        "description": "A section of a document that can contain nested sections",
        "properties": {
          "prefix": {
            "type": "string",
            "nullable": true,
            "description": "Optional prefix text for the section"
          },
          "content": {
            "type": "string",
            "nullable": true,
            "description": "Optional content text for the section"
          },
          "sections": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Section"
            },
            "description": "Array of nested sections"
          }
        }
      }
    }
  }
}
```
