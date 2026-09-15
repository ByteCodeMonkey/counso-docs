---
title: "Microsoft Outlook"
---
Outlook 工具可搜索和读取邮件、查看文件夹与附件、创建草稿、发送或移动邮件、管理联系人，以及创建或更新日历事件。邮件和日历权限相互独立，只申请 Agent 实际需要的能力。

Microsoft Entra 管理员和工作区管理员在 **Spaces → Tools** 中配置工具，并授予当前表单要求的 delegated permissions。随后由实际操作用户连接 Microsoft 账号。邮件操作通常需要 `Mail.ReadWrite`，发送邮件还需 `Mail.Send`；共享邮箱可能需要 `Mail.ReadWrite.Shared` 和 `Mail.Send.Shared`。联系人操作可能需要 `Contacts.ReadWrite`，共享联系人还需 `Contacts.ReadWrite.Shared`。日历需要 `Calendars.ReadWrite`，必要时添加共享日历权限及账户、邮箱设置读取权限。

先从读取邮件或创建草稿开始。确认 Agent 正在使用的邮箱、文件夹、日历和用户身份。发送或修改日程前，核对收件人和时间；操作后在 Outlook 中验证同一邮件或事件。若能读取但无法写入，分别检查委派授权和目标邮箱权限。

## 可用操作

邮件操作包括 **Get Messages**、**Get Message Body**、**List Folders**、**List Attachments**、**Get Attachment**、**Get Attachments**、**Get Drafts**、**Create Draft**、**Delete Draft**、**Send Mail** 和 **Move Messages**。邮件预览短于完整正文；长邮件可分段读取。附件列表返回元数据，下载操作才会获取文件本身。

联系人操作包括 **Get Contacts**、**Create Contact** 和 **Update Contact**。日历操作包括 **Get User Timezone**、**List Calendars**、**List Events**、**Get Event**、**Create Event**、**Update Event**、**Delete Event**、**Check Availability** 和 **Check Self Availability**。日历工具使用个人凭据；共享邮箱场景适用于邮件，不能据此推断日历也有同等共享访问。

邮件按需使用 delegated `Mail.ReadWrite`、`Mail.Send`、`User.Read`、`SensitivityLabel.Read` 和 `offline_access`；共享邮箱可能还需要 `Mail.ReadWrite.Shared` 和 `Mail.Send.Shared`；联系人可能需要 `Contacts.ReadWrite` 和 `Contacts.ReadWrite.Shared`。日历需要 `Calendars.ReadWrite`，共享日历按需增加 `Calendars.ReadWrite.Shared`，并配合 `MailboxSettings.Read`、`User.Read` 和 `offline_access`。请以实际同意请求和启用的操作为准。

## 操作确认

在工具的 **Available tools** 面板中检查每项操作的确认级别。原界面说明：High 每次都要求确认；Medium 可为特定输入保存确认；Low 允许用户关闭确认；Never ask 则自动执行。发送邮件或修改日程不应与只读搜索同等处理；请按组织政策设置确认级别。
