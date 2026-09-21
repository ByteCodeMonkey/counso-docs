---
title: "Power BI"
---
Power BI MCP 可让 Agent 读取获准访问的 Power BI 工作区、仪表板、报表和语义模型。配置需要 Microsoft Entra 应用、Power BI delegated permissions，以及租户中启用的 MCP 端点。仅创建 Entra 应用并不会自动授予报表或模型权限。

## 注册应用

Entra 管理员为**仅本组织目录中的账号**注册应用，并记录 Application (client) ID 和 Directory (tenant) ID。Web redirect URI 使用 Counso 工具表单显示的回调地址；启用 **Allow public client flows**，并创建客户端密钥。然后添加 Power BI Service delegated permissions：`Dataset.Read.All`、`Report.Read.All`、`Dashboard.Read.All` 和 `Workspace.Read.All`，并授予管理员同意。

在 Power BI/Fabric 管理门户中，针对目标用户或组启用 **Users can use the Power BI Model Context Protocol server endpoint**。远程 MCP 端点为 `https://api.fabric.microsoft.com/v1/mcp/powerbi`。

## 添加远程服务器

在 **Spaces → Tools → Add Tools → Add MCP Server** 中填写 Power BI 端点并选择 OAuth。使用 Entra 客户端 ID 和密钥；授权及令牌网址采用对应租户的 Microsoft Identity v2 端点；scope 为 `https://analysis.windows.net/powerbi/api/.default offline_access`。该 scope 指向 Power BI API 资源，而不是 Fabric MCP 主机。保存并完成用户授权后，将可用 Power BI 工具加入目标 Space 中的 Agent。

找不到应用时，确认填写的是 Application ID，而不是 Secret ID 或 Object ID。MCP 功能不可用时检查租户开关；连接发现失败时检查是否启用了 XMLA 端点。遇到个人登录提示时，完成授权后重试 Agent 请求。
