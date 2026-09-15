# 删除数据表

从指定工作区的数据源中删除一张表。

```http
DELETE /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables/{tId}
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

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 该表格已删除 |
| 404 | 未找到该表格 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables/{tId}": {
      "delete": {
        "summary": "Delete a table",
        "description": "Deletes table {tId} from data source {dsId} in workspace {wId}.",
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
          }
        ],
        "responses": {
          "200": {
            "description": "The table was deleted"
          },
          "404": {
            "description": "The table was not found"
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
