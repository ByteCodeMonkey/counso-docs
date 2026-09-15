---
title: "创建并运行应用"
---
在指定 Space 中创建应用运行并执行。

```http
POST /api/v1/w/{wId}/spaces/{spaceId}/apps/{aId}/runs
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区的唯一字符串标识符 |
| `spaceId` | 路径 | string | 是 | Space ID |
| `aId` | 路径 | string | 是 | 应用的唯一标识符 |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `specification_hash` | string | 是 |
| `config` | object | 是 |
| `inputs` | array[object] | 是 |
| `stream` | boolean | 否 |
| `blocking` | boolean | 否 |
| `block_filter` | array[string] | 否 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 应用运行已创建并执行 |
| 400 | 请求错误：参数无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
| 404 | 未找到工作区或应用。 |
| 500 | 内部服务器错误。 |

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
    "/api/v1/w/{wId}/spaces/{spaceId}/apps/{aId}/runs": {
      "post": {
        "summary": "Create an app run",
        "description": "Starts an execution of app {aId} in Space {spaceId} and returns the resulting run.",
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
            "description": "Unique identifier of the app",
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
                "required": [
                  "specification_hash",
                  "config",
                  "inputs"
                ],
                "properties": {
                  "specification_hash": {
                    "type": "string",
                    "description": "Hash of the app specification. Ensures API compatibility across app iterations."
                  },
                  "config": {
                    "type": "object",
                    "description": "Configuration for the app run",
                    "properties": {
                      "model": {
                        "type": "object",
                        "description": "Model configuration",
                        "properties": {
                          "provider_id": {
                            "type": "string",
                            "description": "ID of the model provider"
                          },
                          "model_id": {
                            "type": "string",
                            "description": "ID of the model"
                          },
                          "use_cache": {
                            "type": "boolean",
                            "description": "Whether to use caching"
                          },
                          "use_stream": {
                            "type": "boolean",
                            "description": "Whether to use streaming"
                          }
                        }
                      }
                    }
                  },
                  "inputs": {
                    "type": "array",
                    "description": "Array of input objects for the app",
                    "items": {
                      "type": "object",
                      "additionalProperties": true
                    }
                  },
                  "stream": {
                    "type": "boolean",
                    "description": "If true, the response will be streamed"
                  },
                  "blocking": {
                    "type": "boolean",
                    "description": "If true, the request will block until the run is complete"
                  },
                  "block_filter": {
                    "type": "array",
                    "items": {
                      "type": "string"
                    },
                    "description": "Array of block names to filter the response"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "App run created and executed successfully",
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
          },
          "404": {
            "description": "Workspace or app not found."
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
