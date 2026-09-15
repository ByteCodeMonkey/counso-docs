# Front

Front MCP 工具可让 Agent 搜索会话、读取消息和联系人、查看收件箱和队友、创建草稿或会话、添加备注与标签、分配会话并发送回复。工作区配置的 Personal Access Token 会让获准使用该工具的用户共享令牌所有者在 Front 中的访问权限。

## 连接 Front

在 **Front → Settings → Integrations → API** 中为目标账号创建 Personal Access Token。只按需授予读取权限：`conversations:read`、`messages:read`、`contacts:read`、`tags:read` 和 `teammates:read`。需要写入时，只添加对应权限：`messages:send`、`comments:write`、`drafts:write`、`conversations:write` 或 `tags:write`。只读 Agent 不应获得写入权限。

在 **Spaces → Tools** 中添加 Front 并填写令牌，再分享给相关 Space。将工具加入 Agent 后，先检查一个收件箱和一条已知会话，并确认令牌所有者有权访问该收件箱。

## 可用操作

读取和查询操作包括 `search_conversations`、`get_conversation`、`get_conversation_messages`、`get_contact`、`get_customer_history`、`list_tags`、`list_teammates` 和 `list_inboxes`。写入操作包括 `create_conversation`、`create_draft`、`add_comment`、`add_tags`、`add_links`、`send_message`、`update_conversation_status` 和 `assign_conversation`。

按具体操作配置写入范围。如果创建草稿即可满足需求，不要授予发送消息权限。区分内部备注、草稿和已发送的客户回复。回复前核对收件人和正文，发送后回到 Front 确认消息。
