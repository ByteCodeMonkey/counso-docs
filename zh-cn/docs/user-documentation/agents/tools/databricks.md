# Databricks

Databricks 提供 **Databricks SQL** 和 **Databricks Genie** 两种 MCP 工具。SQL 可探索获准访问的 Unity Catalog 数据并查询 SQL Warehouse；Genie 可访问用户有权使用的 Genie 资源及其底层数据。请求会由 Unity Catalog 按权限控制。

## 创建 Databricks 应用连接

使用运行 Notebook 的工作区网址，不要填写 Account Console 网址。在 Databricks Account Console 中打开 **Settings → App Connections**，创建 OAuth 应用连接，并加入 Counso 设置表单显示的回调网址。保持生成客户端密钥选项开启，然后安全复制客户端 ID 和密钥。使用 SQL 时增加 `sql` 和 `offline_access`；使用 Genie 时增加 `genie` 和 `offline_access`；两者都用时同时添加这两组范围。

连接前，确认目标用户能访问所需 Genie 资源；如果用 SQL，则确认其可访问目标 Unity Catalog Catalog、Schema、表和 SQL Warehouse。如果工作区配置了 IP 访问列表，也需要允许该服务的出站访问。

## 连接工具

在 **Spaces → Tools → Add Tools** 中选择 Databricks SQL 或 Databricks Genie。填写工作区网址和应用连接凭据，并完成授权。提供方 MCP 端点根据工作区主机名确定：SQL 使用 `/api/2.0/mcp/sql`，Genie 使用 `/api/2.0/mcp/genie`。将工具加入 Agent 后，先读取一个已知资源并限制查询范围。
