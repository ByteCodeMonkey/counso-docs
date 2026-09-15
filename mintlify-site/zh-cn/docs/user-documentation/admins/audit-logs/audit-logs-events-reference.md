---
title: "审计日志事件参考"
---
审计日志记录工作区配置、数据访问、成员和智能体活动等事件。具体事件取决于工作区配置。结合事件名称和元数据查看发生了什么，以及由谁或什么操作触发。

## 智能体和工具

| 事件 | 说明 |
|---|---|
| `agent.created` | 创建了智能体。 |
| `agent.updated` | 修改了智能体配置。 |
| `agent.archived` / `agent.restored` | 归档或恢复了智能体。 |
| `agent.scope_changed` | 更改了智能体可见范围。 |
| `agent.executed` | 在对话中调用了智能体。 |
| `tool.executed` | 智能体或用户运行了工具；元数据可能包含工具、服务器、来源和执行上下文。 |

## 触发器和唤醒

| 事件 | 说明 |
|---|---|
| `trigger.created` / `trigger.deleted` | 创建或删除了触发器。 |
| `trigger.enabled` / `trigger.disabled` | 启用或停用了触发器。 |
| `trigger.fired` | 触发器启动了智能体运行。 |
| `trigger.email_received` | 触发器收到了一封邮件。 |
| `wake_up.created` / `wake_up.cancelled` / `wake_up.expired` / `wake_up.fired` | 创建、取消、过期或触发了一项定时后续任务。 |

## Spaces 和数据源

| 事件 | 说明 |
|---|---|
| `space.created` / `space.deleted` | 创建或删除了 Space。 |
| `space.accessed` | 访问了 Space。 |
| `space.permissions_updated` | 修改了 Space 权限。 |
| `datasource.created` / `datasource.updated` / `datasource.deleted` | 创建、修改或删除了数据源。 |
| `datasource.deleted_admin` | 管理员删除了数据源。 |
| `datasource.reauthorized` | 重新授权了数据源的 OAuth 凭据。 |

## 成员、邀请和用户

| 事件 | 说明 |
|---|---|
| `member.invited` / `member.bulk_invited` | 邀请了一名或多名成员。 |
| `member.bulk_revoked` | 批量撤销了成员资格。 |
| `membership.created` / `membership.revoked` | 创建或撤销了工作区成员资格。 |
| `membership.role_updated` | 修改了成员角色。 |
| `membership.origin_updated` | 更改了成员资格来源，例如手动管理或目录同步。 |
| `invitation.revoked` / `invitation.role_updated` | 撤销待处理邀请，或修改了邀请指定的角色。 |
| `user.login` / `user.login_failed` / `user.logout` | 用户登录、登录失败或退出登录。 |
| `user.identity_merged` | 合并了两个用户身份。 |
| `user.relocated` | 将用户移动到了另一个工作区。 |

## OAuth、工具和凭据

| 事件 | 说明 |
|---|---|
| `oauth.initiated` / `oauth.authorized` / `oauth.revoked` | 发起、完成或撤销了 OAuth 授权。 |
| `mcp_connection.created` / `mcp_connection.deleted` | 建立或移除了工具服务器连接。 |
| `credentials.created` / `credentials.updated` / `credentials.revoked` / `credentials.invalidated` | 创建、修改、撤销或使凭据失效；例如服务提供方侧凭据过期。 |

## 域名、登录和目录同步

| 事件 | 说明 |
|---|---|
| `domain.verified` / `domain.verification_failed` / `domain.removed` | 验证或移除了域名，或域名验证失败。 |
| `sso.connection_deleted` | 删除了 SSO 连接。 |
| `dsync.connection_deleted` | 删除了目录同步连接。 |
| `scim.user_provisioned` / `scim.user_updated` / `scim.user_deprovisioned` | 通过目录同步配置、更新或停用了用户。 |
| `scim.group_created` / `scim.group_deleted` | 创建或删除了同步群组。 |
| `scim.group_user_added` / `scim.group_user_removed` | 将用户添加到同步群组或从中移除。 |

## 对话、审计设置和模型访问

| 事件 | 说明 |
|---|---|
| `conversation.accessed` | 访问了对话。 |
| `audit_log.viewed` | 管理员打开了审计日志查看器。 |
| `audit_log.export_configured` | 配置了审计日志导出或日志流。 |
| `workspace.advanced_model_access_updated` | 修改了工作区模型访问等级。 |
| `group.advanced_model_access_updated` | 修改了群组模型访问覆盖设置。 |
| `user.advanced_model_access_updated` | 修改了成员模型访问覆盖设置。 |
| `workspace.deleted` | 删除了工作区。 |

此事件列表不代表每个工作区都启用了所有事件类别。调查变更时，请查看事件详情及其前后记录。
