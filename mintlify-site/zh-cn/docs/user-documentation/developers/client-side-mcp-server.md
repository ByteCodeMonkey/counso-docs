---
title: "客户端 MCP Server"
---
客户端 MCP Server 允许应用在 Counso 会话中提供工具，同时让工具在应用自己的运行环境中执行，例如已登录的浏览器会话。适合需要沿用用户在应用内身份或上下文的场景，比如查询工单，或通过内部服务准备一项更新。它面向基于 Counso Conversations API 开发的自有应用；在 Counso 网页应用或扩展中添加工具，不能通过这种方式完成。

应用决定某个会话可以使用哪些工具，并负责实现每项工具的行为。它可以根据当前用户和任务选择工具，再将活动服务 ID 放入会话上下文的 `clientSideMCPServerIds` 字段。工具在应用本地会话和状态中执行。工具范围应尽量精简，每次执行操作时仍要重新检查用户权限。按会话注册有助于限定工具范围，但不能替代应用自身的权限校验。

由于工具在客户端执行，每个浏览器标签页或应用窗口都有独立的服务实例；只有客户端会话仍能处理请求时，工具才可用。需要考虑浏览器标签关闭、连接中断或用户会话过期的情况，并在工具无法完成时返回清楚的错误信息。客户端 MCP 工具默认按低风险处理，用户可以选择记住审批决定；应用仍应在每次操作时自行校验权限。

## 注册和处理客户端服务

MCP 注册需要当前登录用户的 OAuth access token；这些路由不支持 API key。默认 `baseUrl` 为 `https://app.counso.ai`；如应用使用其他 Counso 环境，请替换为相应基础地址。

| 步骤 | 方法与路由 | 请求或响应 |
| --- | --- | --- |
| 注册 | `POST {baseUrl}/api/v1/w/{wId}/mcp/register` | 发送 `{"serverName":"ticket-tools"}`；保存响应中的 `serverId` 和 `expiresAt`。 |
| 保持活动 | `POST {baseUrl}/api/v1/w/{wId}/mcp/heartbeat` | 发送 `{"serverId":"..."}`，并在注册过期前续期。 |
| 接收工具请求 | `GET {baseUrl}/api/v1/w/{wId}/mcp/requests?serverId={serverId}` | 保持 `text/event-stream` 连接以接收请求。恢复连接时可提供 `lastEventId`。 |
| 返回结果 | `POST {baseUrl}/api/v1/w/{wId}/mcp/results` | 执行所请求的工具后发送 `{"serverId":"...","result":{...}}`。 |
| 注销 | `POST {baseUrl}/api/v1/w/{wId}/mcp/deregister` | 客户端服务关闭时发送 `{"serverId":"..."}`。 |

注册范围绑定当前用户和工作区。若不续期，注册会在五分钟后过期；心跳间隔不能超过五分钟，并应使用 `expiresAt` 跟踪注册状态。在 `requests` 事件流中收到工具请求后，将其交给 MCP server transport 处理，再由 transport 通过 `results` 端点提交执行结果。客户端关闭时注销服务。

SDK transport 可以代为处理注册和消息传递。自行实现其他 transport 时，应保持每个客户端独立：以已登录用户注册，通过 Server-Sent Events 接收请求，将事件交给 MCP transport 处理，再提交执行结果。端点结构见[Counso API 参考](/zh-cn/docs/developer-platform/counso-api-documentation/openapi-and-postman)。
