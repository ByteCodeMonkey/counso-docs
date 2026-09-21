---
title: "生成对话模板草稿"
---
会话接口：按 slug 获取 Contentful 对话模板，并返回可直接用于撰写消息的草稿，可包含预先上传的附件。

```http
GET /api/w/{wId}/assistant/go-template
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `slug` | 查询 | string | 是 | Contentful 模板的 slug |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已根据模板生成可用于撰写消息的草稿 |
| 404 | 未找到模板，或模板已停用 |
| 422 | 缺少 slug 查询参数 |

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
    "/api/w/{wId}/assistant/go-template": {
      "get": {
        "summary": "Resolve a conversation go template draft",
        "description": "Private session interface. Resolves a Contentful conversation template from its slug and prepares a composer-ready draft, with optional attachments uploaded in advance.",
        "tags": [
          "Private Assistant"
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
            "in": "query",
            "name": "slug",
            "required": true,
            "description": "Contentful template slug",
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
            "description": "Composer draft resolved from the template",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetGoTemplateDraftResponseBody"
                }
              }
            }
          },
          "404": {
            "description": "Template not found or disabled"
          },
          "422": {
            "description": "Missing slug query parameter"
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
      "GetGoTemplateDraftResponseBody": {
        "type": "object",
        "description": "Composer draft resolved from a Contentful conversation go template.",
        "required": [
          "title",
          "prompt",
          "attachments",
          "attachmentErrors"
        ],
        "properties": {
          "title": {
            "type": "string"
          },
          "prompt": {
            "type": "string"
          },
          "attachments": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "fileId",
                "name",
                "contentType",
                "size",
                "url"
              ],
              "properties": {
                "fileId": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "contentType": {
                  "type": "string"
                },
                "size": {
                  "type": "integer"
                },
                "url": {
                  "type": "string"
                }
              }
            }
          },
          "attachmentErrors": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "url",
                "message"
              ],
              "properties": {
                "url": {
                  "type": "string"
                },
                "message": {
                  "type": "string"
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
