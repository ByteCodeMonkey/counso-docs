---
title: "解析 Markdown 中的提及"
---
解析粘贴文本中的 @ 提及，并转换为系统可识别的提及格式。

```http
POST /api/v1/w/{wId}/assistant/mentions/parse
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 OAuth access token。凭据须由当前 Counso 环境签发，并有权访问目标工作区与资源。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |

## 请求体

`Content-Type: application/json`

| 字段 | 类型 | 必填 |
| --- | --- | --- |
| `markdown` | string | 是 |

完整字段约束与嵌套结构见下方接口规范。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已将提及转换为规范格式的 Markdown 文本 |
| 400 | 请求错误：请求正文无效或缺失。 |
| 401 | 未授权：身份验证令牌无效或缺失。 |
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
    "/api/v1/w/{wId}/assistant/mentions/parse": {
      "post": {
        "summary": "Parse mentions in markdown text",
        "description": "Converts @ references in pasted Markdown into the structured mention representation.",
        "tags": [
          "Mentions"
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
          }
        ],
        "security": [
          {
            "WorkspaceApiKey": []
          },
          {
            "UserAccessToken": []
          }
        ],
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "markdown"
                ],
                "properties": {
                  "markdown": {
                    "type": "string",
                    "description": "Markdown text containing @ mentions to parse",
                    "example": "Hello @JohnDoe, can you help with @MyAgent?"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Parsed markdown with mentions converted to proper format",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "markdown": {
                      "type": "string",
                      "description": "Processed markdown text with mentions converted to serialized format"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad Request. Missing or invalid request body."
          },
          "401": {
            "description": "Unauthorized. Invalid or missing authentication token."
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
    }
  }
}
```
