# 管理 Microsoft 工具

Microsoft 工具采用 delegated access：Agent 通过已登录的 Microsoft 用户执行操作，范围受该用户权限和工具启用能力限制。首次管理员同意可能需要 Microsoft Entra Privileged Role Administrator 或 Application Administrator，同时还要有 Counso 工作区管理员配合。

## 完成管理员同意

从 **Spaces → Tools → Add Tools** 选择 Microsoft 工具并启动授权流程。如果出现 **Consent on behalf of your organization**，由 Entra 管理员代表组织同意。如果没有该选项，请提交管理员同意请求，并由 Entra 管理员在对应的请求面板中批准。审批显示可能有延迟；获批后重新运行工具设置流程。

Entra 管理员也可以自行注册和管理企业应用。此时仅使用当前 Counso 设置表单显示的客户端及回调值，不要复用其他环境的应用 ID 或回调网址。

## 各工具的权限范围

所需 delegated scopes 取决于具体能力。常见范围包括 `User.Read` 和 `offline_access`。Outlook 邮件可能需要 `Mail.ReadWrite`、`Mail.Send`，使用共享邮箱时还要相应共享邮箱权限；日历可能需要 `Calendars.ReadWrite`、`Calendars.ReadWrite.Shared` 和 `MailboxSettings.Read`。Drive/SharePoint 可能需要 `Files.ReadWrite.All`、`Sites.Read.All` 和 `ExternalItem.Read.All`；Excel 需要文件和站点访问；Teams 可能需要团队、频道、聊天、消息及用户的读取或发送权限。请检查实际同意界面，只批准工作区计划使用的能力。

Microsoft scopes 本身不会让所有文件或消息自动可见；登录用户仍需在第三方系统中有相应访问权。每种工具先测试一条允许访问的记录，并在开放写入前确认操作身份。
