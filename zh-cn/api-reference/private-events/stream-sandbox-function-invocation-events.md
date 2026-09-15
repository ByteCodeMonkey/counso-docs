# 实时接收 Pod 函数调用事件

会话接口：通过 SSE 实时接收 Pod 函数调用事件，流量会转发到 /api/sse/。

```http
GET /api/w/{wId}/sandbox-functions/{functionId}/invocations/{invocationId}/events
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `functionId` | 路径 | string | 是 | Pod 函数 ID |
| `invocationId` | 路径 | string | 是 | 沙箱函数调用 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | SSE 事件流。每个事件以 data: {json}\n\n 形式发送，并通过 type 字段区分事件类型。 |
| 401 | 未授权 |

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
    "/api/w/{wId}/sandbox-functions/{functionId}/invocations/{invocationId}/events": {
      "get": {
        "summary": "Stream sandbox function invocation events",
        "description": "Private session interface. Streams event updates for a Pod function invocation through SSE.",
        "tags": [
          "Private Events"
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
            "name": "functionId",
            "required": true,
            "description": "ID of the Pod function",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "invocationId",
            "required": true,
            "description": "ID of the sandbox function invocation",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "UserAccessToken": []
          },
          {
            "BrowserSession": []
          }
        ],
        "responses": {
          "200": {
            "description": "SSE event stream. Each event is sent as `data: {json}\\n\\n`.\nEvents are discriminated by the `type` field.\n",
            "content": {
              "text/event-stream": {
                "schema": {
                  "$ref": "#/components/schemas/PrivateSandboxFunctionInvocationEvent"
                }
              }
            }
          },
          "401": {
            "description": "Unauthorized"
          }
        },
        "x-counso-auth": "user"
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
      "PrivateSandboxFunctionInvocationEvent": {
        "type": "object",
        "description": "Server-Sent Event for sandbox function invocation streaming. Discriminated on the `type` field.",
        "discriminator": {
          "propertyName": "type"
        },
        "oneOf": [
          {
            "$ref": "#/components/schemas/PrivateSandboxFunctionInvocationCreatedEvent"
          },
          {
            "$ref": "#/components/schemas/PrivateSandboxFunctionInvocationResultEvent"
          },
          {
            "$ref": "#/components/schemas/PrivateSandboxFunctionInvocationErrorEvent"
          }
        ]
      },
      "PrivateSandboxFunctionInvocationCreatedEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "invocation"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "sandbox_function_invocation_created"
            ]
          },
          "created": {
            "type": "integer"
          },
          "invocation": {
            "type": "object",
            "required": [
              "sId",
              "functionId",
              "status",
              "createdAt"
            ],
            "properties": {
              "sId": {
                "type": "string"
              },
              "functionId": {
                "type": "string"
              },
              "status": {
                "type": "string",
                "enum": [
                  "created"
                ]
              },
              "createdAt": {
                "type": "string",
                "format": "date-time"
              }
            }
          }
        }
      },
      "PrivateSandboxFunctionInvocationErrorEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "invocationId",
          "functionId",
          "error"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "sandbox_function_invocation_error"
            ]
          },
          "created": {
            "type": "integer"
          },
          "invocationId": {
            "type": "string"
          },
          "functionId": {
            "type": "string"
          },
          "error": {
            "type": "object",
            "required": [
              "code",
              "message"
            ],
            "properties": {
              "code": {
                "type": "string",
                "description": "Whatever classified the failure, forwarded as-is (a runner code such as `threw` or `http_error`, or the `type` of the API error that failed the call). Open by design, branch on the codes you handle and treat the rest as generic failures."
              },
              "message": {
                "type": "string"
              },
              "status": {
                "type": "integer"
              }
            },
            "description": "A structured error describing why the invocation failed."
          }
        }
      },
      "PrivateSandboxFunctionInvocationResultEvent": {
        "type": "object",
        "required": [
          "type",
          "created",
          "invocationId",
          "functionId",
          "result"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "sandbox_function_invocation_result"
            ]
          },
          "created": {
            "type": "integer"
          },
          "invocationId": {
            "type": "string"
          },
          "functionId": {
            "type": "string"
          },
          "result": {
            "description": "Parsed result validated against the sandbox function output schema."
          }
        }
      }
    }
  }
}
```
