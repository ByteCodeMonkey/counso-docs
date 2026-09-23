# 导出消费分析数据

导出工作区中逐次调用的消费分析数据。每一行代表一次计费的 LLM 调用或工具调用。

```http
POST /api/v1/w/{wId}/analytics/consumption/export
```

服务地址：`https://app.counso.ai`

## 认证

在 `Authorization: Bearer <token>` 中传入工作区 API key 或用户 access token。该凭据必须有权访问目标工作区。

## 路径参数

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `wId` | string | 是 | 工作区唯一标识符 |

## 请求体

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `startDate` | string / date-time | 是 | ISO 8601 格式的起始时间，包含该时刻 |
| `endDate` | string / date-time | 是 | ISO 8601 格式的结束时间，不包含该时刻；必须晚于 `startDate`，且间隔不超过 30 天 |
| `format` | `csv` 或 `ndjson` | 否 | 输出格式，默认为 `csv` |
| `filter` | object | 否 | 可选筛选条件，见下文 |

`filter` 支持 `agents`、`users`、`api_keys`、`groups`、`models`、`tools`、`skills`、`sources` 和 `tags` 数组。每个值最长 256 个字符，所有维度合计最多 500 个值。

## 响应

| HTTP 状态 | 说明 |
| --- | --- |
| 200 | 流式 CSV 或 NDJSON 导出结果 |
| 400 | 日期、格式或筛选条件无效，或者时间范围超过 30 天 |
| 401 | 缺少认证或凭据无效 |
| 403 | 当前凭据无权访问该工作区 |

请求会在 10 秒后超时。如果结果过大，请缩短日期范围或增加筛选条件。如果流式传输开始后发生错误，响应会在关闭前追加错误信息。

## 接口规范

精确的 Schema 和响应头定义见完整的 [OpenAPI / Postman](../../docs/developer-platform/counso-api-documentation/openapi-and-postman.md) 文件。
