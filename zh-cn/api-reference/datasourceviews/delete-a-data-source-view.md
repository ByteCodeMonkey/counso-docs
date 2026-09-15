# 删除数据源视图

从指定 Space 中删除指定的数据源视图。

```http
DELETE /api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}
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
| 204 | 数据源视图已成功删除 |
| 401 | 未授权：数据源视图正在使用中，无法删除 |
| 403 | 禁止访问：只有管理员或构建者可以删除数据源视图 |
| 404 | 未找到数据源视图 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}": {
      "delete": {
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
        "summary": "Delete a data source view",
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
          "204": {
            "description": "Data source view successfully deleted"
          },
          "401": {
            "description": "Unauthorized - The data source view is in use and cannot be deleted"
          },
          "403": {
            "description": "Forbidden - Only admins or builders can delete data source views"
          },
          "404": {
            "description": "Data source view not found"
          }
        },
        "x-counso-auth": "workspace",
        "description": "Removes the selected data source view from its Space."
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
