# 接收用于触发流程的外部 Webhook

接收为指定 Webhook 来源发送的 JSON 事件，并触发与之关联的流程。

```http
POST /api/v1/w/{wId}/triggers/hooks/{webhookSourceId}
```

服务地址：`https://app.counso.ai`

## 认证

此端点不使用工作区 API key。请使用为该来源生成的 Webhook URL。如果配置了签名校验，请携带要求的签名请求头，并基于实际发送的原始请求体计算签名。

## 路径参数

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `wId` | string | 是 | 工作区 ID |
| `webhookSourceId` | string | 是 | Webhook 来源 ID |

## 请求体

使用 `application/json` 发送事件。允许的嵌套结构取决于触发器配置。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 已收到 Webhook |
| 400 | 请求或签名无效 |
| 404 | 未找到工作区或 Webhook 来源 |

请妥善保管生成的 Webhook URL；如果 URL 泄露，应轮换对应来源。

## 接口规范

精确的请求和响应 Schema 见完整的 [OpenAPI / Postman](../../docs/developer-platform/counso-api-documentation/openapi-and-postman.md) 文件。
