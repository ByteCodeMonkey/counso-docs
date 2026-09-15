# Audit log event reference

Audit Logs record events across workspace configuration, data access, membership, and Agent activity. Event availability depends on workspace configuration. Use the event name and its associated metadata to understand what changed and who or what initiated it.

## Agents and tools

| Event | Description |
|---|---|
| `agent.created` | An Agent was created. |
| `agent.updated` | Agent configuration changed. |
| `agent.archived` / `agent.restored` | An Agent was archived or restored. |
| `agent.scope_changed` | Agent visibility changed. |
| `agent.executed` | An Agent was invoked in a conversation. |
| `tool.executed` | An Agent or user ran a Tool; metadata may include the Tool, server, source, and execution context. |

## Triggers and wake-ups

| Event | Description |
|---|---|
| `trigger.created` / `trigger.deleted` | A trigger was created or deleted. |
| `trigger.enabled` / `trigger.disabled` | A trigger was enabled or disabled. |
| `trigger.fired` | A trigger initiated an Agent run. |
| `trigger.email_received` | A trigger received an inbound email. |
| `wake_up.created` / `wake_up.cancelled` / `wake_up.expired` / `wake_up.fired` | A scheduled follow-up was created, cancelled, expired, or fired. |

## Spaces and data sources

| Event | Description |
|---|---|
| `space.created` / `space.deleted` | A Space was created or deleted. |
| `space.accessed` | A Space was accessed. |
| `space.permissions_updated` | Space permissions changed. |
| `datasource.created` / `datasource.updated` / `datasource.deleted` | A data source was created, updated, or deleted. |
| `datasource.deleted_admin` | An administrator deleted a data source. |
| `datasource.reauthorized` | A data source's OAuth credentials were reauthorized. |

## Members, invitations, and users

| Event | Description |
|---|---|
| `member.invited` / `member.bulk_invited` | One or multiple members were invited. |
| `member.bulk_revoked` | Membership was revoked in bulk. |
| `membership.created` / `membership.revoked` | Workspace membership was created or revoked. |
| `membership.role_updated` | A member's role changed. |
| `membership.origin_updated` | Membership origin changed, such as manual or directory-provisioned. |
| `invitation.revoked` / `invitation.role_updated` | A pending invitation was revoked or its assigned role changed. |
| `user.login` / `user.login_failed` / `user.logout` | A user logged in, failed to log in, or logged out. |
| `user.identity_merged` | Two user identities were merged. |
| `user.relocated` | A user was moved to another workspace. |

## OAuth, tools, and credentials

| Event | Description |
|---|---|
| `oauth.initiated` / `oauth.authorized` / `oauth.revoked` | An OAuth authorization was started, completed, or revoked. |
| `mcp_connection.created` / `mcp_connection.deleted` | A tool-server connection was established or removed. |
| `credentials.created` / `credentials.updated` / `credentials.revoked` / `credentials.invalidated` | A credential set was created, changed, revoked, or invalidated, for example after provider-side expiry. |

## Domains, sign-in, and directory sync

| Event | Description |
|---|---|
| `domain.verified` / `domain.verification_failed` / `domain.removed` | A domain was verified, a verification attempt failed, or a domain was removed. |
| `sso.connection_deleted` | An SSO connection was deleted. |
| `dsync.connection_deleted` | A directory-sync connection was deleted. |
| `scim.user_provisioned` / `scim.user_updated` / `scim.user_deprovisioned` | A user was provisioned, updated, or deprovisioned through directory sync. |
| `scim.group_created` / `scim.group_deleted` | A provisioned group was created or deleted. |
| `scim.group_user_added` / `scim.group_user_removed` | A user was added to or removed from a provisioned group. |

## Conversations, audit settings, and model access

| Event | Description |
|---|---|
| `conversation.accessed` | A conversation was accessed. |
| `audit_log.viewed` | An administrator opened the Audit Logs viewer. |
| `audit_log.export_configured` | An audit log export or stream was configured. |
| `workspace.advanced_model_access_updated` | Workspace model access tier changed. |
| `group.advanced_model_access_updated` | A group's model access override changed. |
| `user.advanced_model_access_updated` | A member's model access override changed. |
| `workspace.deleted` | The workspace was deleted. |

The event reference does not imply that every event family is enabled in every workspace. Check the event detail and nearby records when investigating a change.
