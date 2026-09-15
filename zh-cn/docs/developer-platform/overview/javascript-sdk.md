# JavaScript SDK

安装 [JavaScript 客户端](https://www.npmjs.com/package/@dust-tt/client)：

```bash
npm install @dust-tt/client
```

将客户端指向 Counso，并提供工作区 ID 及 API key 或 OAuth access token：

```typescript
import { DustAPI } from "@dust-tt/client";

const client = new DustAPI(
  { baseUrl: "https://app.counso.ai", workspaceId, apiKey }
);
```

请将凭据保存在应用的密钥管理服务或安全的服务端配置中，不要把工作区 API key 放入公开的浏览器代码。需要以已登录用户身份执行操作时使用 OAuth access token；客户端 MCP 路由必须使用用户 OAuth 身份。

SDK 使用 Result 风格返回结果。读取 `value` 前先检查 `isErr()`，并在继续处理前妥善处理 API 错误。[Conversations API 参考](../counso-api-documentation/openapi-and-postman.md)列出了请求字段和可用操作。
