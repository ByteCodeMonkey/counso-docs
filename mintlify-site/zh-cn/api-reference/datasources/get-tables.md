---
title: "列出数据源表格"
---
获取指定工作区数据源中的表格列表。

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables
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

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 表格列表 |
| 400 | 请求无效 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables": {
      "get": {
        "summary": "Get tables",
        "description": "Returns the tables available in data source {dsId} for workspace {wId}.",
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
        "responses": {
          "200": {
            "description": "The tables",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "tables": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/Table"
                      }
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
