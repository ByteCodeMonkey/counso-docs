# NetSuite

NetSuite 远程 MCP 使用 Oracle 的 **MCP Standard Tools SuiteApp** 和 OAuth 2.0。需要 NetSuite 管理员启用 SuiteCloud 功能、安装 SuiteApp、创建专用角色并注册集成。此 MCP 服务器不能使用 Administrator 角色。

## 准备 NetSuite 账号

1. 在 **Setup → Company → Enable Features → SuiteCloud** 中启用 **Server SuiteScript**、**REST Web Services**、**Token-Based Authentication** 和 **OAuth 2.0**。
2. 在 **Customization → SuiteBundler → Search & Install Bundles** 中找到并安装 **MCP Standard Tools**。
3. 在 **Setup → Users/Roles → Manage Roles → New** 中创建专用角色，并授予 **MCP Server Connection**、**Log in using OAuth 2.0 Access Tokens**、**REST Web Services** 和 **Perform Search** 权限。仅分配给需要使用的用户。
4. 在 **Setup → Integration → Manage Integrations → New** 中启用集成，并开启 **Authorization Code Grant**、**Public Client** 和 **Dynamic Client Registration**。回调地址使用 Counso 设置表单显示的值；scope 选择 **NetSuite AI Connector Service**。保存后安全复制 Consumer Key/Client ID 和密钥。若表单要求原始密钥值，输入时去掉展示前缀（例如 `ID`）。

## 连接 MCP 服务器

在 **Spaces → Tools → Add Tools → Add MCP Server** 中选择 **Static OAuth**。服务器 URL 使用当前账号对应的 NetSuite MCP Standard Tools SuiteApp 端点：

`https://<accountid>.suitetalk.api.netsuite.com/services/mcp/v1/suiteapp/com.netsuite.mcpstandardtools`

将 `<accountid>` 替换为 NetSuite 账户 ID。OAuth 授权端点为 `https://<accountid>.app.netsuite.com/app/login/oauth2/authorize`；令牌端点为 `https://<accountid>.suitetalk.api.netsuite.com/services/rest/auth/oauth2/v1/token`；scope 为 `mcp`。填写集成记录中的密钥，保存后使用自定义 MCP 角色授权。将服务器提供的工具加入获批的 Agent 和 Space。

登录失败时，确认选择的是自定义角色而非 Administrator。找不到 **MCP Server Connection** 权限时检查 SuiteApp 是否安装。密钥被拒绝时，如果表单需要原始 Consumer Key，去掉 `ID` 等前缀。回调校验失败时，对照当前 Counso 表单检查提供方中的登记值。
