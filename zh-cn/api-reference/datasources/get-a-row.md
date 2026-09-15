# 获取表格行

读取指定工作区数据源表格中的一行。

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables/{tId}/rows/{rId}
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
| `tId` | 路径 | string | 是 | 表格 ID |
| `rId` | 路径 | string | 是 | 行 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 该行 |
| 404 | 未找到该行 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables/{tId}/rows/{rId}": {
      "get": {
        "summary": "Get a row",
        "description": "Reads row {rId} from table {tId} in data source {dsId} under workspace {wId}.",
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
          },
          {
            "in": "path",
            "name": "tId",
            "required": true,
            "description": "ID of the table",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "rId",
            "required": true,
            "description": "ID of the row",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The row",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Datasource"
                }
              }
            }
          },
          "404": {
            "description": "The row was not found"
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
      }
    }
  }
}
```
