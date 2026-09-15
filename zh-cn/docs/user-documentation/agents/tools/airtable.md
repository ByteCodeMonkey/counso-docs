# Airtable

Airtable 远程工具可让 Agent 查看 Base 结构，并搜索、读取、新建或更新记录和记录评论。配置前先选凭据模式：Personal Access Token 会由所有能使用该工具的人共用；OAuth 则让每个人使用自己的 Airtable 账号和权限。

## 配置 Airtable

使用令牌时，在 [airtable.com/create/tokens](https://airtable.com/create/tokens) 创建 Personal Access Token。只选择 Agent 需要访问的 Base。先授予 `data.records:read`、`schema.bases:read` 和 `user.email:read`；仅在确有需要时再添加 `data.records:write`、`data.recordComments:read/write` 或 `schema.bases:write`。创建时复制令牌并保存到工具配置中。

使用个人 OAuth 时，在 [airtable.com/create/oauth](https://airtable.com/create/oauth) 注册集成。集成名称可填 Counso，公开主页填 `https://counso.ai`，回调地址使用当前连接表单显示的值。按 Airtable 要求和表单提示设置权限范围及令牌认证方式。连接到 Airtable 的 MCP 地址 `https://mcp.airtable.com/mcp`，并选择对应的认证方式。

配置完成后，将 Airtable 加入 Agent，并验证一个 Base 结构和一条已知记录。若认证成功但看不到表格，检查允许访问的 Base 和结构读取权限。除非 Agent 需要修改记录，否则不要开启写入权限。

## OAuth 参数

Airtable OAuth 端点为 `https://airtable.com/oauth2/v1/authorize` 和 `https://airtable.com/oauth2/v1/token`；令牌端点使用 Basic authentication。建议权限范围包括 `data.records:read`、`data.records:write`、`data.recordComments:read`、`data.recordComments:write`、`schema.bases:read`、`schema.bases:write` 和 `user.email:read`。按实际工作与当前连接表单选择对应范围。注册 OAuth 应用时，Airtable 可能要求支持邮箱以及公开的隐私和服务条款链接；请使用 Counso 当前的联系与法律页面，不要填写第三方平台页面。
