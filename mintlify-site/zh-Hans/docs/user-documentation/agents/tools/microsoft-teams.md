---
title: "Microsoft Teams"
---
Teams 工具使用 Microsoft 身份为 Agent 提供 Teams 数据和消息能力。根据授权，可查找团队和频道、搜索或读取聊天与消息，也可发送消息。Teams Bot 或频道集成属于另一项功能，使用不同身份并需单独配置事件范围。

Microsoft Entra 管理员和工作区管理员在 **Spaces → Tools** 中添加 Teams 工具，并批准当前表单要求的 delegated permissions。已记录的权限包括团队和频道基本信息、聊天与消息读写、消息发送、用户资料访问以及 `offline_access`；实际范围取决于启用的操作。若表单采用个人凭据，每位用户都需授权自己的账号。

将工具加入 Agent 后，在该用户已有权限的频道或聊天中测试。发送前确认目标团队、频道或聊天、收件人和消息正文；完成后在 Teams 中检查结果。如果消息使用了意外身份，或频道缺失，应区分实时 Tool 与 Teams Bot，并检查实际用户的成员权限和管理员授权。

## 可用操作与限制

工具列表包含 **Search Messages Content**、**List Teams**、**List Users**、**List Channels**、**List Chats**、**List Messages** 和 **Post Message**。搜索使用关键词匹配，不是语义搜索。授权用户必须属于相应团队或聊天，才能查看其中内容。

根据启用的操作，所需 delegated permissions 可能包括 `Team.ReadBasic.All`、`Channel.ReadBasic.All`、`Chat.Read`、`Chat.ReadWrite`、`ChatMessage.Read`、`ChatMessage.Send`、`ChannelMessage.Read.All`、`ChannelMessage.Send`、`User.Read`、`User.ReadBasic.All` 和 `offline_access`。Entra 管理员可能需要在企业应用权限面板中授予同意，或审批待处理的同意请求。

## 搜索与消息

`Search Messages Content` 使用关键词搜索，不是语义检索。**List Teams**、**List Channels** 和 **List Chats** 用于确认目标；**List Messages** 读取频道消息及回复；**List Users** 查询收件人；**Post Message** 向频道、聊天或线程发送消息。操作范围受当前用户可访问的团队和聊天限制，发送前应明确目标。
