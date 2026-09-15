# 添加对话参与者

会话接口：将当前已认证用户加入指定对话。

```http
POST /api/w/{wId}/assistant/conversations/{cId}/participants
```

服务地址：`https://app.counso.ai`

## 认证

此接口需要用户身份：外部客户端通过 `Authorization: Bearer <token>` 传入用户 OAuth access token；已登录的浏览器也可使用 Counso 会话 Cookie。工作区 API key 不能代替用户身份。

## 请求参数

| 参数 | 位置 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- | --- |
| `wId` | 路径 | string | 是 | 工作区 ID |
| `cId` | 路径 | string | 是 | 对话 ID |

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 201 | 已成功添加参与者 |
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
    "/api/w/{wId}/assistant/conversations/{cId}/participants": {
      "post": {
        "summary": "Add a participant to a conversation",
        "description": "Private session interface. Adds the signed-in user to the participant list for the specified conversation.",
        "tags": [
          "Private Conversations"
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
            "name": "cId",
            "required": true,
            "description": "ID of the conversation",
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
          "201": {
            "description": "Successfully added participant"
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
    }
  }
}
```
