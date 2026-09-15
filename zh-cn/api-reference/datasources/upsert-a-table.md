# 写入或更新数据表

在指定工作区的数据源中新建表格，或更新已有表格。

```http
POST /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区的唯一字符串标识符 |
| `spaceId` | 路径 | string | 是 | Space ID |
| `dsId` | 路径 | string | 是 | 数据源 ID |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `name` | string | 否 |
| `title` | string | 否 |
| `table_id` | string | 否 |
| `description` | string | 否 |
| `timestamp` | number | 否 |
| `tags` | array[string] | 否 |
| `mime_type` | string | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 该表格 |
| 400 | 请求无效 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables": {
      "post": {
        "summary": "Upsert a table",
        "description": "Creates a table in data source {dsId}, or applies updates to its existing definition, in workspace {wId}.",
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
            "description": "Unique string identifier for the workspace",
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
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Name of the table"
                  },
                  "title": {
                    "type": "string",
                    "description": "Title of the table"
                  },
                  "table_id": {
                    "type": "string",
                    "description": "Unique identifier for the table"
                  },
                  "description": {
                    "type": "string",
                    "description": "Description of the table"
                  },
                  "timestamp": {
                    "type": "number",
                    "description": "Unix timestamp (in milliseconds) for the table (e.g. 1736365559000)."
                  },
                  "tags": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Tags associated with the table"
                  },
                  "mime_type": {
                    "type": "string",
                    "description": "Reserved for internal use, should not be set. Mime type of the table"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "The table",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "table": {
                      "$ref": "#/components/schemas/Table"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request"
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
      "Table": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of the table",
            "example": "Roi data",
            "deprecated": true
          },
          "title": {
            "type": "string",
            "description": "Title of the table",
            "example": "ROI Data"
          },
          "table_id": {
            "type": "string",
            "description": "Unique identifier for the table",
            "example": "1234f4567c"
          },
          "description": {
            "type": "string",
            "description": "Description of the table",
            "example": "roi data for Q1"
          },
          "mime_type": {
            "type": "string",
            "description": "MIME type of the table",
            "example": "text/csv"
          },
          "schema": {
            "type": "array",
            "description": "Array of column definitions",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "Name of the column",
                  "example": "roi"
                },
                "value_type": {
                  "type": "string",
                  "description": "Data type of the column",
                  "enum": [
                    "text",
                    "int",
                    "float",
                    "bool",
                    "date"
                  ],
                  "example": "int"
                },
                "possible_values": {
                  "type": "array",
                  "description": "Array of possible values for the column (null if unrestricted)",
                  "items": {
                    "type": "string"
                  },
                  "nullable": true,
                  "example": [
                    "1",
                    "2",
                    "3"
                  ]
                }
              }
            }
          },
          "timestamp": {
            "type": "number",
            "description": "Unix timestamp of table creation/modification",
            "example": 1732810375150
          },
          "tags": {
            "type": "array",
            "description": "Array of tags associated with the table",
            "items": {
              "type": "string"
            }
          },
          "parent_id": {
            "type": "string",
            "description": "ID of the table parent",
            "items": {
              "type": "string"
            },
            "example": "1234f4567c"
          },
          "parents": {
            "type": "array",
            "description": "Array of parent table IDs",
            "items": {
              "type": "string"
            },
            "example": [
              "1234f4567c"
            ]
          }
        }
      }
    }
  }
}
```
