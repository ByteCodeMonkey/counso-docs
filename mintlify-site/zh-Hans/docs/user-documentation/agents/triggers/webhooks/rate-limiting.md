---
title: "设置 Webhook 触发器的频率限制"
---
每个 Webhook 触发器默认在**滚动的 24 小时内最多运行 42 次**。窗口持续向前滚动，不会在午夜重置。此限制控制触发频率，与智能体运行消耗的 credits 分开计算。

## 修改触发器上限

在 Agent Builder 中打开 Webhook 触发器，在触发器设置表单中编辑 **Rate limits**。Editor 可以根据预期事件量调整上限。当前触发器设置中显示的数值是该工作区的实际依据。定时触发器不受此 Webhook 上限约束。

## 达到上限时

收到的请求会被拒绝，触发器会标记为受速率限制。达到上限期间收到的请求会直接丢弃，不会排队，也不会在滚动窗口恢复后重放。触发器会在下一个被接受的请求到达时再次运行。如果经常达到上限，可以用 [payload filter](/zh-Hans/docs/user-documentation/agents/triggers/webhooks/filter-webhooks-payload) 减少无关事件，或在允许时调整该触发器的上限。
