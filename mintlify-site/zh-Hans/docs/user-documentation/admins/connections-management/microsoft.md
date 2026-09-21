---
title: "连接 Microsoft"
---
Microsoft 连接索引指定的 SharePoint 文档、电子表格和演示文稿。需要使用组织 Microsoft 账号，不支持个人账号。

## 使用组织账号授权

1. 打开 **Spaces > Connections > Microsoft**，开始连接。
2. 登录并核对所需 Microsoft 权限。
3. 如果租户要求管理员同意，提交请求。Entra 管理员批准后，再执行一次登录步骤完成连接。
4. 选择需要同步的站点和文件。

用户委托授权使用 `Files.Read.All`、`Sites.Read.All`、`User.Read` 和 `offline_access`，分别用于读取文件和站点、识别用户及刷新访问。应用身份和回调地址应使用当前 Counso 配置页面提供的值。

使用专门的集成账号，便于维护持续访问。账号直接获得的权限及通过群组继承的权限，共同决定可见的 SharePoint 站点和 Teams 文件。请检查公共站点、账号作为成员加入的私人站点，以及所加入的标准、共享或私人 Teams 频道。在 Counso 选择数据不会替代 Microsoft 本身的权限。

## 使用服务主体授权

如果连接提供服务主体认证，可在 Entra 创建应用注册，授予相应的 Microsoft Graph **应用权限**，取得管理员同意，并创建客户端密钥。然后在 Counso 填入租户 ID、客户端 ID 和密钥值。

如果只允许访问部分站点，使用 `Sites.Selected`，并明确给应用授予每个指定站点的访问权限；仅完成管理员同意，不会自动获得任何站点访问。按连接要求填写允许的站点 ID。这个仅应用身份的流程，不应与交互登录的用户委托权限混用。站点授权步骤参见 [Microsoft 所选权限说明](https://learn.microsoft.com/en-us/graph/permissions-selected-overview)。

## 文件与刷新

支持包含文字的 DOCX、PPTX、TXT 等文档。如需 PDF，请在 Microsoft 连接的 **Manage** 设置中开启索引。XLSX 会按工作表解析，供表格查询使用。提取文字超过约 800 KB 的文档会被跳过。

连接大约每五分钟检查变化。文件新增、修改或删除，需要等同步完成后才会反映，大批量变更可能更久。文件缺失时，请检查账号或应用权限、所选站点、文件格式和同步状态。

SharePoint 列表的自定义列会作为文件标签同步，可用于关键词筛选和[知识搜索](/zh-Hans/docs/user-documentation/agents/knowledge/search-data-sources)。
