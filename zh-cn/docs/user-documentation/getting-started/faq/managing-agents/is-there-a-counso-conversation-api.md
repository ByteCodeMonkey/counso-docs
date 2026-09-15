# Counso 提供 Conversations API 吗？

提供。Counso Conversations API 允许应用以编程方式创建与 Counso Agent 的会话，并向会话发送消息。你可以将 Agent 接入产品流程，例如客服工作区或内部运营工具。

公开 API 的默认基础地址是 `https://app.counso.ai`。如果使用其他 Counso 环境，请替换为该环境的基础地址，路由保持不变。常用会话路由如下：

| 操作 | 方法与路径 | 用途 |
| --- | --- | --- |
| 创建会话 | `POST /api/v1/w/{wId}/assistant/conversations` | 通过初始消息创建会话。 |
| 添加消息 | `POST /api/v1/w/{wId}/assistant/conversations/{cId}/messages` | 向已有会话发送消息。 |
| 读取会话 | `GET /api/v1/w/{wId}/assistant/conversations/{cId}` | 按 ID 获取会话。 |

将 `{wId}` 替换为工作区 ID，将 `{cId}` 替换为会话 ID。请求使用的 JSON 字段见 API 参考。

API 操作受调用身份在相应工作区和 Agent 中的权限约束。接入应用仍需负责自身的登录、用户权限和发送信息的范围。不要将服务端凭据放进浏览器代码，也不要把会话 ID 当作访问权限校验。

身份验证、请求结构、事件流和响应处理方式，请参阅[开发者平台概览](../../../../developer-platform/overview/developer-platform.md)及 Counso API 参考。
