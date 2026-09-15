# Microsoft SharePoint 和 OneDrive 工具

SharePoint 和 OneDrive 工具可让 Agent 查找并读取实际操作用户有权访问的站点、驱动器、文件夹和文件。根据配置，也可能上传或更新文件。它是实时工具，与用于同步资料的 Microsoft Connection 不同。

Microsoft Entra 管理员和工作区管理员在 **Spaces → Tools** 中添加工具，并授予当前表单要求的 delegated scopes。原设置中包括 `User.Read`、`Files.ReadWrite.All`、`Sites.Read.All`、`ExternalItem.Read.All` 和 `offline_access`；最终应以当前授权界面为准。实际操作用户完成登录后，还必须有权访问目标站点或驱动器。

将工具加入 Agent，先从一个已知站点、文档库和文件开始。上传或更新前，读取目标位置并确认路径；完成后按同一文件 ID 检查内容。如果找不到文件，除直接权限外也要检查通过组继承的站点成员身份。如果 Connection 可见而 Tool 看不到，则对比服务账号与实际操作用户的权限。

## 可用操作与限制

工具列表包含 **Search In Files**、**Search Drive Items**、**Get File Content**、**Update Word Document** 和 **Upload File**。搜索结果受 Microsoft 用户身份可见范围限制；读取和上传还要求该用户有权访问具体站点、驱动器或文件夹。该工具面向文件操作，不能取代用于同步检索的 SharePoint Connection。

已记录的 delegated scopes 包括 `Files.ReadWrite.All`、`Sites.Read.All`、`ExternalItem.Read.All`、`User.Read` 和 `offline_access`；最终以当前管理员同意界面为准。通过 Microsoft 365 组继承的 SharePoint 成员权限也会影响可见性，不仅是站点直接权限。访问外部数据集还要求用户和租户支持相应权限。
