---
title: "在 Slack Workflow 中使用智能体"
---
Slack Workflow 可以自动执行定时消息、表单提交等日常任务。Workflow 可以提及 Counso 智能体，并把智能体回答发送到指定频道。

例如，可以让 Workflow：

- 每个工作日早上调用摘要智能体整理最新动态；
- 有人使用指定表情回应消息时调用智能体。

## 工作方式

1. 在 Slack 中创建 Workflow，并选择定时、表单提交或表情回应等触发方式。
2. 添加发送消息步骤，提及已配置的 Counso 应用和智能体名称，例如 `@Counso +highlights Summarize the updates since yesterday`。
3. 在 Counso 中允许该 Workflow，并只授予智能体所需的 Space。
4. 使用不含敏感信息的内容测试，确认预期智能体在正确频道中回复。

Counso 根据 Slack 消息中显示的发送者名称识别 Workflow，大小写和表情也必须完全匹配。在 Slack 中重命名 Workflow 后，需要按新名称重新允许。

Workflow 始终可以访问通过 Company Data 提供的智能体和数据。其他 Space 必须明确授权。如果智能体需要访问 Workflow 未获授权的 Space，它不会响应该 Workflow 消息。

<Warning>
  所有可以运行该 Slack Workflow 的人（包括访客）都可能调用所选智能体。只授予 Workflow 必需的 Space，并确认目标频道适合接收智能体回答。
</Warning>

## 允许 Workflow

如果工作区提供自助管理功能：

1. 打开 **Programmatic Usage > Automations**。
2. 选择 **Slack workflows** 标签页。
3. 点击 **Allow a workflow**。
4. 输入 Slack 中显示的准确 Workflow 发送者名称。
5. 在 **Spaces it can reach** 中添加智能体所需数据所在的 Space。Company Data 始终包含在内。
6. 保存后从 Slack 运行测试。

表格会显示已允许的 Workflow、可访问的 Space 以及添加时间。页面也可能按所选时间范围显示 Slack Workflow 消耗的 credits。

如果当前部署中没有 Slack workflows 标签页，请让部署管理员登记 Workflow 名称和允许访问的 Space。不要把工作区标识或访问配置信息发送给上游厂商。

## 更改或撤销权限

从表格中移除 Workflow，即可阻止它继续调用智能体。要更改名称或 Space 访问范围，请使用新值重新登记。如果工作区启用了审计日志，Workflow 授权变更会记录在工作区审计日志中。
