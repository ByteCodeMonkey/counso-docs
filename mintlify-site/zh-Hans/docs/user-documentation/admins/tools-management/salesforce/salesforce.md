---
title: "连接 Salesforce"
---
Salesforce 工具让 Agent 使用一个 Salesforce 身份查询记录。记录、对象、字段和 API 访问权限仍由 Salesforce 控制。如果每位用户应使用自己的权限，请选个人凭据；如果希望通过经批准的集成用户共享访问，请选工作区凭据。

## 创建 Salesforce 应用

在 Salesforce Setup 中打开 **External Client App Manager**，创建 External Client App。填写名称，按组织要求设置分发状态，然后启用 OAuth。回调地址使用 Counso Salesforce 工具设置表单显示的值；不同部署环境的回调可能不同。

添加工具所需的身份、API、刷新令牌/离线访问和自定义权限范围。使用以下范围组：`id`、`profile`、`email`、`address`、`phone`；`api`；`refresh_token` / `offline_access`；以及 `custom_permissions`。

在 **Flow Enablement & Security** 中开启该连接器需要的设置：

- **Enable Client Credentials Flow**
- **Enable Authorization Code and Credentials Flow**
- **Require secret for Web Server Flow**
- **Require secret for Refresh Token Flow**
- **Require Proof Key for Code Exchange (PKCE) extension for Supported Authorization Flows**

创建应用后，打开 **Settings > Edit > OAuth Settings > Consumer Key and Secret**，妥善保存这两个值。应用设置用于支持 OAuth 连接；Counso 中的个人或工作区凭据选项，决定实际使用哪个已连接的 Salesforce 账号。

## 配置工具

在 **Spaces > Tools > Add Tools > Salesforce** 中填写 Salesforce 实例网址和应用凭据。选择 **Personal** 或 **Workspace** 凭据，并按 Counso 页面提示完成授权。

使用**个人**凭据时，管理员的初始授权用于初始化集成，并不是每位成员查询时使用的身份。每位用户首次使用时都要连接自己的 Salesforce 账号，然后重新发起请求。使用**工作区**凭据时，查询使用管理员配置时授权的 Salesforce 账号，所有获准使用工具的人共用该账号的 Salesforce 访问权限。仅为它授予完成 Agent 工作所需的对象和字段权限。

只将工具分享给需要的 Space，再加入 Agent。先读取一条已知 Account 或 Contact。资料缺失时，检查当前 Salesforce 身份、对象权限、字段级安全和 API 限额。详细说明见 [Salesforce 查询限额与访问权限](/zh-Hans/docs/user-documentation/admins/tools-management/salesforce/salesforce-notes-on-api-limit-and-permissions)。
