---
title: "Microsoft Excel"
---
Excel 工具可让 Agent 处理实际操作用户在 Microsoft 365 中有权访问的工作簿。它能检查工作簿和工作表、读取单元格范围，并更新受支持的范围。这是实时工具，不是文件同步 Connection。

Microsoft Entra 管理员和工作区管理员在 **Spaces → Tools** 中添加 Excel，并批准当前设置表单显示的 delegated permissions。已记录的范围包括 `User.Read`、`Files.ReadWrite.All`、`Sites.Read.All` 和 `offline_access`。实际操作用户需使用自己的 Microsoft 身份登录，并有权访问目标工作簿。

查询时明确工作簿、工作表和准确范围。写入前让 Agent 检查工作表，并保留请求范围之外的公式和格式。更新后，重新打开同一工作簿和单元格范围，核对值、公式及文件身份。如果 Excel 找不到或无法更新工作簿，确认文件位于用户可访问的 OneDrive 或 SharePoint 位置，并检查用户的 Microsoft 操作权限。

## 可用操作

工具列表包括 **List Excel Files**（查找 `.xlsx` 和 `.xlsm` 文件）、**Get Worksheets**、**Read Worksheet**、**Write Worksheet**、**Create Worksheet** 和 **Clear Range**。文件来自实际操作用户有权访问的 SharePoint 或 OneDrive。写入除工具设置成功外，还需要 Microsoft 文件编辑权限。

指定工作表前先使用 **Get Worksheets**，写入前先读取准确范围。找不到工作簿或范围时，检查文件是否位于用户有权访问的 SharePoint 或 OneDrive，以及用户是否有编辑权限。设置时已记录的 delegated scopes 包括 `User.Read`、`Files.ReadWrite.All`、`Sites.Read.All` 和 `offline_access`；请在当前同意界面确认。
