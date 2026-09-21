---
title: "连接 Slack 知识"
---
Slack 数据连接索引所选频道的消息，供助手搜索知识。它与 Slack 中的交互机器人、以及使用用户账号搜索或操作 Slack 的工具是分别配置的能力。

## 准备 Slack 应用

需要 Counso 工作区管理权限，以及在 Slack 工作区创建和安装应用的权限。请向 Counso 部署管理员取得应用清单及配置值：Slack 必须能够访问当前部署的 OAuth 回调、Events Request URL 和 Interactivity Request URL。工作区还需启用 Slack 连接及其数据同步服务。

1. 打开 [Slack 应用管理页](https://api.slack.com/apps)，选择 **Create New App > From a manifest**，再选择工作区。
2. 粘贴适用于当前 Counso 部署的应用清单。创建前确认 OAuth 回调、事件地址和交互地址都指向同一部署；不要复用其他服务或环境的地址。
3. 核对清单中的权限和事件订阅。应用需要连接所用的频道、消息、用户和文件权限，以及同步所选频道所需的事件。保留部署管理员提供的权限和事件列表。
4. 创建并安装应用。如果 Slack 要求审批，由 Slack 管理员在工作区应用管理设置中批准。
5. 在 **Basic Information > App Credentials** 中取得 Client ID、Client Secret 和 Signing Secret，填入 **Spaces > Connections > Slack** 中对应的字段。
6. 点击 **Connect**，完成 Slack 授权。

## 选择频道

在 **Spaces > Connections > Slack > Add / Remove data** 中选择需要索引的频道并保存。私人频道需先邀请已配置的数据同步机器人，才可能出现在选择列表中。工作区还必须启用私人频道索引；仅邀请机器人并不会开启这项功能。

## 内容与刷新

连接索引所选频道的消息、线程和频道元数据。不索引机器人生成的消息、私信和外部文件。不要默认机器人加入前的历史消息已经全部导入，应在配置后检查频道实际可用的历史范围。

新消息通常会较快出现。调整所选频道后，可能需要几秒到几分钟，具体取决于资料量。建议把同一主题的讨论放在线程中；未使用线程时，搜索结果可能链接到频道中的大致位置，而不是精确消息。

频道标签使用 `channelId:...` 和 `channelName:...`，可用于[知识搜索工具](/zh-Hans/docs/user-documentation/agents/knowledge/search-data-sources)的筛选。

## 维护连接

在 **Add / Remove data** 中调整频道，通过 **Manage Permissions** 控制哪些 Space 可使用 Slack 知识。如果需要轮换应用凭据，请立即在 **Manage > Edit** 中更新对应值，使连接能够恢复。

授权、迁移或频道缺失问题可查看 [Slack 故障排查](/zh-Hans/docs/user-documentation/admins/admin-troubleshooting/slack-troubleshooting)；需要实时操作时，查看 [Slack 工具](/zh-Hans/docs/user-documentation/agents/tools/slack-tools)。
