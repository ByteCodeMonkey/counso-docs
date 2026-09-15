---
title: "将 Google Sheets 工作迁移到 Google Drive"
---
这篇旧设置说明中的独立 Google Sheets 工具已弃用。请改用 Google Drive 工具执行当前支持的表格读取和编辑。本页仅帮助工作区管理员识别旧工具并迁移现有 Agent 配置。

## 迁移步骤

1. 在 Agent 构建器中，从仍使用旧功能的 Agent 上移除已弃用的 Google Sheets 工具。
2. 请工作区管理员按当前配置表单设置原生 Google Drive 工具。
3. 将 Google Drive 加入相关 Agent，并连接拥有目标表格或有权访问它的 Google 账号。
4. 修改 Agent 指令，明确指定电子表格、工作表和范围，并要求编辑后回读核验。
5. 用一份已知表格进行测试，在 Google Drive 中确认返回值；不再使用旧配置后，再移除旧工具。

请区分 Google Drive Connection 和实时 Drive Tool：Connection 用于同步检索，Tool 用于精确文件和表格操作。如果工作区当前没有 Drive 工具，请先让管理员确认是否启用，再决定迁移安排。
