---
title: "获取数据源视图"
---
读取指定 Space 中数据源视图的详情。

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 |  |
| `spaceId` | 路径 | string | 是 |  |
| `dsvId` | 路径 | string | 是 |  |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 成功响应 |
| 404 | 未找到数据源视图 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}": {
      "get": {
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
        "summary": "Get a data source view",
        "parameters": [
          {
            "name": "wId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "spaceId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "dsvId",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DatasourceView"
                }
              }
            }
          },
          "404": {
            "description": "Data source view not found"
          }
        },
        "x-counso-auth": "workspace",
        "description": "Returns the configuration and details for one data source view in a Space."
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
      "DatasourceView": {
        "type": "object",
        "properties": {
          "category": {
            "type": "string",
            "enum": [
              "managed",
              "folder",
              "website",
              "apps"
            ],
            "description": "The category of the data source view"
          },
          "createdAt": {
            "type": "number",
            "description": "Timestamp of when the data source view was created"
          },
          "dataSource": {
            "$ref": "#/components/schemas/Datasource"
          },
          "editedByUser": {
            "type": "object",
            "description": "The user who last edited the data source view",
            "properties": {
              "fullName": {
                "type": "string",
                "description": "Full name of the user"
              },
              "editedAt": {
                "type": "number",
                "description": "Timestamp of when the data source view was last edited by the user"
              }
            }
          },
          "id": {
            "type": "number",
            "description": "Unique identifier for the data source view"
          },
          "kind": {
            "type": "string",
            "enum": [
              "default",
              "custom"
            ],
            "description": "The kind of the data source view"
          },
          "parentsIn": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of IDs included in this view, null if complete data source is taken",
            "nullable": true
          },
          "sId": {
            "type": "string",
            "description": "Unique string identifier for the data source view"
          },
          "updatedAt": {
            "type": "number",
            "description": "Timestamp of when the data source view was last updated"
          },
          "spaceId": {
            "type": "string",
            "description": "ID of the space containing the data source view"
          }
        }
      },
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
