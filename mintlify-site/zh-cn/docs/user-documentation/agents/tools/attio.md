---
title: "Attio"
---
Attio 托管 MCP 服务可让 Agent 搜索和管理 CRM 记录，包括人员、公司、交易、任务、备注、会议、通话和邮件。它使用 OAuth 认证，操作权限取决于已连接用户在 Attio 中的访问范围。

## 连接 Attio

在当前工具配置流程中添加远程 MCP 服务，地址为 `https://mcp.attio.com/mcp`，并选择界面提供的 OAuth 方式。仅向需要此工具的 Space 分享，然后将其加入目标 Agent。授权表单和回调地址以连接流程显示为准；请使用将实际执行操作的 Attio 账号完成授权。

初步检查可运行 `whoami` 确认连接身份，运行 `list-attribute-definitions` 查看字段定义，并搜索一条已知记录。工具可能支持创建或更新记录、任务等操作，应只向有明确业务需要的用户和 Space 开放写入能力。若服务器已连接但 Agent 中看不到工具，请检查服务器分享设置和 Agent 所在 Space 的访问权限。

## 可用操作

工具列表包括 `search-records`、`get-records-by-ids`、`create-record`、`upsert-record`、`list-attribute-definitions`，以及备注创建与搜索、会议和通话录音搜索/读取、邮件搜索/内容读取、工作区成员和团队列表、`whoami`。创建记录、Upsert 和创建备注会修改 CRM 数据；应只向合适的 Agent 开放，并明确结果复核人。
