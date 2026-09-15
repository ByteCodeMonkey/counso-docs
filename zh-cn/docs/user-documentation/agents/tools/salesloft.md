# Salesloft

Salesloft 工具可让 Agent 获取销售节奏及相关销售上下文，例如任务和人员。具体操作取决于连接账号、API 密钥范围和当前工具配置。

在 Salesloft 管理界面中，为目标账号所有者创建或选择 API 密钥，只启用任务需要的 cadence、task、people 和 activity 权限。在 **Spaces → Tools** 中添加 Salesloft，输入密钥，按表单选择凭据归属方式，并分享给相关 Space。然后将工具加入 Agent。

先读取一条销售节奏和一项任务。修改活动或任务前，确认账号身份、记录 ID 和预期改动；操作后回读记录。密钥可以通过认证，却仍缺少访问特定 cadence 或 task 的权限。资料缺失时，应检查对应 API 密钥范围和账号归属。

## 可用操作

可用工具包括 `List Actions` 和 `Get Action`。文档列出的读取权限为 `cadences:read`、`people:read`、`team:read` 和 `calls:read`。请连接拥有目标销售节奏资料的账号，并先在限定账号范围内列出操作。
