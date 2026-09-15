# Zendesk

Zendesk 工具使用工作区级 OAuth 凭据搜索和读取客服工单，并创建回复草稿。工作区管理员在 **Spaces → Tools → Add Tools** 中完成 OAuth，将工具分享给适当的 Space，再加入 Agent。共享账号的 Zendesk 权限决定了可见工单范围。

## 可用操作

- **Get Ticket**：按 ID 读取工单，包括主题、描述、状态、优先级、负责人和元数据；也可按需读取指标或完整评论历史。
- **Search Tickets**：使用 Zendesk 查询语法搜索，例如 `status:open`、`priority:high`、`assignee:me` 和 `tags:bug`。
- **Draft Reply**：创建仅内部可见的私密评论草稿，供发布前复核，不会直接显示给最终用户。

用于同步检索的 Zendesk Connection 与实时 Tool 不同。工单缺失时检查共享身份和品牌。将草稿公开发布前，先检查内容。
