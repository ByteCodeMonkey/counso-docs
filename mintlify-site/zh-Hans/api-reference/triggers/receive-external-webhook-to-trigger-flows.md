---
title: "接收用于触发流程的外部 Webhook"
---
接收发往该来源专属 Webhook URL 的 JSON 事件。URL 中包含 secret；若该来源配置了签名校验，请求必须携带基于原始请求正文生成的有效签名，事件才会被接收。

```http
POST /api/v1/w/{wId}/triggers/hooks/{webhookSourceId}/{webhookSourceUrlSecret}
```

服务地址：`https://app.counso.ai`

## 认证

使用该来源生成的完整 Webhook URL，保留其中的密钥路径。此接口不使用 API key。若已配置签名校验，请使用对应请求头，并对实际发送的原始请求体计算签名。不要公开生成的 Webhook URL。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `webhookSourceId` | 路径 | string | 是 | Webhook 来源 ID |
| `webhookSourceUrlSecret` | 路径 | string | 是 | 生成的 Webhook URL 中包含的密钥 |

## 请求体

`Content-Type: application/json`

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已收到 Webhook |
| 400 | 请求无效 |
| 404 | 未找到工作区或 Webhook 来源 |
| 401 | Webhook URL 密钥无效 |

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
    "/api/v1/w/{wId}/triggers/hooks/{webhookSourceId}/{webhookSourceUrlSecret}": {
      "post": {
        "summary": "Receive external webhook to trigger flows",
        "description": "Accepts a JSON event at the source-specific webhook URL, which contains a secret. When signature verification is enabled for that source, the request must carry a valid signature over the raw request body.",
        "tags": [
          "Triggers"
        ],
        "security": [],
        "parameters": [
          {
            "in": "path",
            "name": "wId",
            "required": true,
            "description": "Workspace ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "webhookSourceId",
            "required": true,
            "description": "Webhook source ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "path",
            "name": "webhookSourceUrlSecret",
            "required": true,
            "description": "Secret included in the generated webhook URL",
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
                "type": "object"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Webhook received",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "required": [
                    "success"
                  ],
                  "properties": {
                    "success": {
                      "type": "boolean"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request"
          },
          "404": {
            "description": "Workspace or webhook source not found"
          },
          "401": {
            "description": "Invalid webhook URL secret"
          }
        },
        "x-counso-auth": "webhook"
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
