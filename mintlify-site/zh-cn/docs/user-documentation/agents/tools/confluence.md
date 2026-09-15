---
title: "Confluence"
---
Confluence 工具可让 Agent 搜索和读取页面、使用 CQL 进行高级搜索；获得授权后也可创建、更新或移动页面，并查询用户信息。管理员可选择个人身份或工作区共享账号。

在 **Spaces → Tools** 中添加 Confluence，并按表单提示完成第三方 OAuth。选择个人凭据时，每位用户授权自己的账号，操作和结果遵循该用户的 Confluence 权限。选择工作区凭据时，所有能使用工具的人共享服务账号，因此应将其限制在相关 Space。完成设置后，在 Agent 构建器中加入 Confluence。

## 能力范围

- **Knowledge Management**：读取、创建、更新和移动页面。
- **Advanced Search**：使用 Confluence Query Language（CQL）搜索页面；Agent 可以协助组织查询条件。
- **User Management**：读取 Confluence 用户信息。

先使用一篇已知页面进行查询并确认其空间。编辑时明确目标页面和改动内容，之后回到 Confluence 重新打开该页检查。找不到页面可能是连接身份尚未获得分享权限。账号也可能有读取权限但没有页面编辑权限。
