# 连接 Zendesk

该连接将 Support 工单和 Guide 帮助中心文章导入 Counso 知识，不是在 Zendesk 内安装聊天助手。

## 连接并选择品牌

配置人员需要同时拥有 Counso、Zendesk Support 和 Guide 的管理权限。打开 **Spaces > Connections > Zendesk**，填写 Zendesk 子域名并授权。子域名就是 Zendesk 地址中 `.zendesk.com` 前面的部分。

可以只选择某个品牌的工单，也可以选择整个品牌，同时包含它的帮助中心。文章可以按类别选择，也可选择整个帮助中心。只有所选范围内已发布的文章会建立索引；如果希望自动包含后续新建的类别，请选择整个帮助中心。

## 配置工单同步

在 Zendesk 连接中打开 **Manage**，调整以下设置：

| 设置 | 作用 |
| --- | --- |
| Sync Unresolved Tickets | 包含尚未解决或关闭的工单，会增加同步量，也会让未完成的客服讨论进入搜索。 |
| Hide Customer Information | 隐藏附加元数据中的客户姓名和邮箱，但不会涂黑工单消息正文中的这些信息。 |
| Data Retention Period | 决定工单的保留范围，评估覆盖时请核对当前配置值。 |
| Ticket Tag Filters | 按工单标签包含或排除工单。 |
| Organization Tag Filters | 按所属组织的标签包含或排除工单。 |
| Custom Field Tags | 将指定自定义字段加入 `fieldName:value` 标签。在 Zendesk Admin 的 Fields 中找到数字字段 ID，再点击 **Add Field**。 |
| Rate Limit Transactions Per Second | 限制连接请求速度，以适应 Zendesk 限额。留空只表示不开启这一额外限制，Zendesk 自身限额仍然生效。 |

默认聚焦相应时间范围内已解决或已关闭的工单。包含和排除标签仅对后续同步生效，不会追溯移除已索引工单。过期或取消选择的工单按日清理。

## 同步内容

工单包含评论、可用的作者元数据、标签、优先级、类型、渠道、组织和群组 ID、满意度反馈及截止日期。语义搜索用于查找相关内容，不应直接当作完整统计系统来回答某人被分配了多少工单。

文章包含标题、正文、类别和分区描述、作者元数据、标签以及投票净值。隐藏客户信息的设置会影响身份元数据，开启后，助手回答中也会缺少这部分身份背景。

## 刷新与标签

选择内容后即开始同步，耗时取决于资料量。新解决或删除的工单、新发布的文章，可能需要约 30 分钟才能反映。删除或取消选择的文章以及过期工单，会在每日任务中清理。

工单标签，以及 `priority`、`ticketType`、`channel`、`status`、`groupId`、`organizationId`、`dueDate`、`satisfactionRating`、`hasIncidents` 等标签，可用于缩小[知识搜索](../../agents/knowledge/search-data-sources.md)范围。
