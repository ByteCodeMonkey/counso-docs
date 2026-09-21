---
title: "Google Drive"
---
Google Drive 工具会使用实际操作用户有权访问的文件执行实时操作。它采用个人凭据：工作区管理员先完成应用设置，之后每位用户连接自己的 Google 账号。它与用于同步文件供检索的 Drive Connection 不同，也不同于已弃用的独立 Sheets 工具。

管理员打开 **Spaces → Tools → Add Tools → Google Drive**，填写表单要求的客户端 ID 和密钥，并完成首次 OAuth。将工具加入 Agent；用户首次使用时点击 **Connect** 授权自己的 Google 账号。如果写入时提示权限不足，重新连接 Google Drive 并授予所请求的写入权限。

## 可用操作

- **List Drives** 和 **Search Files**：查找个人云端硬盘或共享云端硬盘中的内容。
- **Get File Content**：读取支持的 Docs、Sheets、Slides、文本、Markdown 和 CSV 内容。较大响应可通过 offset/limit 分页。
- **Get Document Structure**、**Get Spreadsheet**、**Get Worksheet** 和 **Get Presentation Structure**：在修改前读取文档结构、电子表格属性或单元格范围、演示文稿对象。
- **List Comments**、**Create Comment** 和 **Create Reply**：处理文件评论。
- **Create Document**、**Create Spreadsheet**、**Create Presentation** 和 **Copy File**：新建或复制文件。
- **Update Document**、**Append to Spreadsheet**、**Update Spreadsheet** 和 **Update Presentation**：编辑内容。应先读取结构，确保索引、单元格范围和对象 ID 正确。

该工具不提供对整个 Drive 内容的语义搜索；需要索引检索时应使用 Drive Connection。原始说明给出的文件上限为 64 MB，每次读取最多返回 32,000 个字符；较长内容可分页获取。使用时仍应查看当前界面的限制。编辑后，回到 Drive 重新打开同一文件和范围检查结果。
