---
title: "为触发器选择 credits 来源"
---
每次触发器运行都会消耗资源。**Credits** 设置决定费用记在智能体编辑者名下，还是记入工作区共享池；它不会改变触发时间表或筛选条件。

## 选择来源

在 Agent Builder 中打开触发器，使用 **Credits** 下拉框：

- **My credits（我的 credits）**：将运行记在触发器编辑者名下，如同由其本人发起。适合主要服务个人、运行量较低的摘要或报告。
- **Workspace credits（工作区 credits）**：将运行计入工作区共享池，作为团队自动化使用量。适合告警路由、工单分类等可能频繁运行的团队服务。

修改此设置需要能够编辑该智能体，并有权使用工作区共享池。管理员可以通过工作区治理授予此权限；管理员和经理也可能可以从 Automations 页面调整来源。保存后的更改适用于后续运行。

## 资源池不足时

所选资源池或适用的支出上限耗尽时，触发器会停止运行。请在工作区 Usage 区域检查余额和当前限制。资源恢复后，受阻期间错过的运行不一定会自动补跑；变更后应查看触发器的最近运行记录。

工作区共享池按工作区当前资源规则计费和监控。个人 credits 的扣减顺序、自动化用量和资源池上限见[Credit 管理](/zh-cn/docs/user-documentation/admins/usage-seats-and-credits/credit-management)。

## 检查触发器

如果工作区提供 **Programmatic Usage > Automations**，管理员和经理可在其中查看触发器活动。用相同时间范围比较智能体、所选资源池、运行次数和消耗量。credits 来源与 Webhook 频率上限彼此独立；另见[速率限制](/zh-cn/docs/user-documentation/agents/triggers/webhooks/rate-limiting)。
