---
title: "API 规范与 Postman"
---
Counso API 定义文件用于查看请求与响应结构；将请求集合导入 Postman 后，可以逐个选择接口并发送请求。

- [Postman 请求集合](/zh-cn/docs/developer-platform/counso-api-documentation/postman.collection.json)
- [Postman 环境文件](/zh-cn/docs/developer-platform/counso-api-documentation/postman.environment.json)
- [OpenAPI 3.0 规范](/zh-cn/docs/developer-platform/counso-api-documentation/openapi.json)
- [swagger.json 格式文件](/zh-cn/docs/developer-platform/counso-api-documentation/swagger.json)

## 使用请求集合

1. 打开 [Postman](https://web.postman.co)，选择 **Import**，导入请求集合和环境文件。
2. 选择 **Counso** 环境。`baseUrl` 默认为 `https://app.counso.ai`；连接其他 Counso 环境时再修改。填写目标工作区的 `workspaceId`。
3. 在本地密钥变量中填写凭据：工作区 API 请求使用 `apiKey`，以登录用户身份执行的请求使用 `userAccessToken`。共享的环境文件不包含任何凭据。
4. 选择一个请求，填写路径参数和请求体，再发送。可以先列出智能体，确认工作区和连接是否正确。

集合按认证方式分组：

| 请求分组 | 所需凭据 |
| --- | --- |
| Workspace API | 工作区 API key，并满足接口列出的角色与权限要求。接口支持时，也可使用用户 OAuth token。 |
| User session API | 用户 OAuth access token；同源浏览器也可使用已登录的会话 Cookie。 |
| Client-side MCP | 用户 OAuth access token，不接受工作区 API key。 |
| Sign-in flow | 相应登录步骤要求的授权码、刷新令牌、PKCE 参数或会话 ID，不要求已有的 Bearer token。 |
| Webhook receiver | 为该来源生成的完整 URL，包含 URL 密钥；若已启用签名校验，还需传入对应签名。 |

Postman 也支持通过 URL 导入。使用这种方式时，复制上方集合或环境文件的原始下载链接即可。发送前请核对工作区、凭据和请求体；写入操作会修改所选工作区中的内容。
