# Statuspage

Statuspage 工具可让 Agent 读取页面和组件信息；获得授权后也可新建或更新事件。实际操作账号必须能访问目标 Statuspage 站点，写入权限应仅授予负责事件发布的人员。

管理员在 **Spaces → Tools** 中添加 Statuspage，填写当前表单要求的页面、账号信息和认证资料，再分享给受限 Space。根据任务选择凭据角色。将工具加入 Agent 后，先读取页面和组件状态。

新建事件或发布更新前，确认页面、组件、状态、影响范围和公开文案。操作后通过事件 ID 重新读取并核验发布状态。页面缺失或无法编辑时，检查 API 密钥、账号角色和页面所有权。不要让通用 Agent 绕过人工复核直接发布事件通告。

## 可用操作

工具提供 **Get Page**、**List Components**、**Get Component**、**List Incidents**、**Get Incident**、**Create Incident** 和 **Update Incident**。读取页面或组件需要标准页面访问权限；创建或更新事件需要 **Incident Manager** 角色；计划维护可能需要 **Maintenance Manager**。API 密钥归属于 Statuspage 用户，应确认该用户在目标页面上的角色。
