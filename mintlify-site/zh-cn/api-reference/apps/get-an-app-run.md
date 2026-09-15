---
title: "获取应用运行记录"
---
获取指定 Space 中某个应用运行的结果。

```http
GET /api/v1/w/{wId}/spaces/{spaceId}/apps/{aId}/runs/{runId}
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区的唯一字符串标识符 |
| `spaceId` | 路径 | string | 是 | Space ID |
| `aId` | 路径 | string | 是 | 应用 ID |
| `runId` | 路径 | string | 是 | 运行 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 该运行 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/apps/{aId}/runs/{runId}": {
      "get": {
        "summary": "Get an app run",
        "description": "Looks up a previously created app run by its ID in the specified Space.",
        "tags": [
          "Apps"
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
            "name": "aId",
            "required": true,
            "description": "ID of the app",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "runId",
            "required": true,
            "description": "ID of the run",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "The run",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "run": {
                      "$ref": "#/components/schemas/Run"
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
      "Run": {
        "type": "object",
        "properties": {
          "run_id": {
            "type": "string",
            "description": "The ID of the run",
            "example": "4a2c6e8b0d"
          },
          "app_id": {
            "type": "string",
            "description": "The ID of the app",
            "example": "9f1d3b5a7c"
          },
          "status": {
            "type": "object",
            "properties": {
              "run": {
                "type": "string",
                "description": "The status of the run",
                "example": "succeeded"
              },
              "build": {
                "type": "string",
                "description": "The status of the build",
                "example": "succeeded"
              }
            }
          },
          "results": {
            "type": "object",
            "description": "The results of the run",
            "example": {}
          },
          "specification_hash": {
            "type": "string",
            "description": "The hash of the app specification",
            "example": "8c0a4e6d2f"
          },
          "traces": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "timestamp": {
                    "type": "number",
                    "description": "The timestamp of the trace",
                    "example": 1234567890
                  },
                  "trace": {
                    "type": "object",
                    "description": "The trace",
                    "example": {}
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```
