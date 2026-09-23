# ServiceNow

ServiceNow 工具允许 Counso 智能体通过 ServiceNow Table API 读取和写入记录，包括事件、变更、问题、请求、知识文章以及自定义表。

## 发布此集成前

请先确认 Counso 部署已经提供 ServiceNow 工具及对应的 OAuth 回调地址。应使用当前部署实际显示的回调地址，不要沿用其他托管服务的回调地址。

连接使用 OAuth 2.0 Authorization Code 流程访问客户自己的 ServiceNow 实例。ServiceNow 管理员需要创建面向外部客户端的 OAuth API Endpoint；用于连接的集成账号还必须具备所需角色、表级和字段级 ACL、REST API Access Policy 及 Data Policy 权限。

## ServiceNow 配置要求

1. 打开 **System OAuth > Application Registry**，创建面向外部客户端的 OAuth API Endpoint。
2. 填写准确的 Counso 回调地址，启用 Authorization Code，并保持应用为 Active。
3. 保存生成的 `Client ID` 和 `Client Secret`。
4. 为部署所需的 Table API 方法授权：`GET`、`POST` 和 `PATCH`。
5. 只向专用集成账号开放需要使用的表和字段。

在 Counso 中填写实例 URL、Client ID 和 Client Secret，然后使用集成账号完成授权。读取、创建和更新应分别测试，因为 ServiceNow 会独立授权每种操作。

## 可用操作

连接器可以列出记录、按 `sys_id` 获取记录、创建记录和更新记录。实际可访问的表仍由 ServiceNow 控制。字段级 ACL 隐藏的字段可能直接从响应中省略，而不会单独报错。

建议创建配套 Skill，记录允许访问的表、必填字段、状态转换、选项值、引用字段查询规则、自定义 `u_*` 字段以及禁止写入的系统字段。不要在 Skill 中保存凭据。

## 当前限制

连接器仅覆盖 Table API，不提供 Catalog 下单流程、附件或 Knowledge Management API，也不支持删除。只有在 Counso 工具、回调地址、凭据流程以及代表性的读写测试全部验证后，才应发布本页。
