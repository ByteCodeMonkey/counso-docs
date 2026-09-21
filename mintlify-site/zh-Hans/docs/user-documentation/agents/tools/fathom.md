---
title: "Fathom"
---
Fathom 工具提供会议和转录文本的只读访问。它可按时间、团队、录制人或邀请者域名筛选会议，附带可用的摘要、行动项或 CRM 匹配信息，并可通过录制 ID 获取转录文本。

管理员从 **Spaces → Tools → Add Tools** 添加 Fathom 并完成 OAuth；若表单提供选择，可使用个人或共享凭据。将工具分享给相关 Space，再加入 Agent。个人凭据以用户自身的第三方访问权限为边界；共享凭据则使用连接账号的权限，供获准调用工具的人使用。

初次检查时，按有限日期范围列出会议，并确认录制 ID 和参与者；随后使用 `recording_id` 获取一份转录。会议结束后，转录文本可能不会立刻生成。较长的转录可能以文件返回，可分段打开或读取。会议、转录、摘要和 CRM 数据的可见性可能不同，分享结论前先确认录制身份。

## 工具参数

`list_meetings` 支持使用 `cursor` 分页；使用 ISO 8601 格式的 `start_date` 和 `end_date`；指定数字类型的 `recording_id`；使用精确匹配的 `calendar_invitees_domains` 及其筛选类型 `calendar_invitees_domains_type`（`all`、`only_internal` 或 `one_or_more_external`）；按邮箱筛选 `recorded_by`；按团队名称筛选 `teams`；并通过 `include_action_items`、`include_crm_matches` 和 `include_summary` 控制附带内容。CRM 匹配仅来自已连接的 CRM。`get_transcript` 必须传入数字类型的 `recording_id`。较长的转录可能以会话文件形式保存，应分段读取。
