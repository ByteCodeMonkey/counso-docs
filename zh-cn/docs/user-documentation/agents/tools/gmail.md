# Gmail

Gmail 工具使用已连接用户的 Google 身份搜索和读取邮件；获得授权后，也可创建草稿或发送邮件。访问范围遵循该用户的 Gmail 权限，不会自动变成共享邮箱连接。

工作区管理员在 **Spaces → Tools** 中添加 Gmail，并按当前表单完成应用设置。然后由要使用的邮箱所有者登录 Google 并授权。将工具加入目标 Agent 后，先搜索或读取一封已知邮件。创建草稿前，请 Agent 确认邮箱和邮件对象。

撰写邮件时优先保存为草稿以便复核。发送前核对收件人、主题、正文和操作账号，发送后回到 Gmail 验证邮件。如果用户能搜索却不能创建草稿或发送，检查写入授权范围和 Gmail 账号权限。不要在 Agent 指令中保存凭据或私密邮件内容。

## 可用操作

工具集包括用于搜索和读取邮件的 `get_messages`、获取附件的 `get_attachment`、`get_drafts`、`create_draft`、`create_reply_draft`、`delete_draft` 和 `send_mail`。创建、删除草稿及发送邮件需要写入授权。发送前应在 Gmail 中检查草稿和目标邮箱身份。

## 操作与确认

`get_messages`、`get_attachment` 和 `get_drafts` 属于读取操作；`create_draft` 和 `create_reply_draft` 用于准备待审核邮件；`delete_draft` 会删除草稿；`send_mail` 会实际发送。原设置将读取设为 Never ask、创建草稿设为 Medium、删除草稿设为 Low、发送邮件设为 High；管理员可在工具设置中调整。已存在的安装可能需要管理员手动启用 `send_mail`。邮件操作应围绕具体工作，不要用于批量营销发送。
