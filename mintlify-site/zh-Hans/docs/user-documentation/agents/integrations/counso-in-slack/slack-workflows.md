---
title: "在 Slack Workflow 中使用智能体"
---
Slack Workflow 可以在事件发生时向智能体发送消息，例如到达设定时间或有人对消息添加表情。它适合定期摘要或消息分流等工作，智能体回答会出现在共享频道中。

## 配置 Workflow

1. 在 Slack 中创建 Workflow，并选择触发方式，例如定时或表情反应。
2. 添加一个步骤，将提示发到智能体应回复的频道。提及已配置的 Counso 应用并指定智能体，例如 `@Counso +weekly-summary Summarize the updates since yesterday`。如果工作区使用不同的机器人名称，请从 Slack 提及选择器中选择该应用。
3. 请让工作区管理员登记准确的 Workflow 名称，以及智能体使用的受限 Space。按授权流程提供所需的工作区标识。
4. 用无敏感信息的提示运行一次测试，确认预期智能体在指定频道回复。

授权可能与准确的 Workflow 名称及智能体的受限数据范围绑定。重命名 Workflow 或增加受限 Space 后，可能需要管理员更新授权。工作区的 Workflow 授权由部署管理员管理。

向更多人开放 Workflow 前，确认频道中的所有参与者都是智能体回答的预期接收者，并确保智能体只访问完成任务所需的来源。
