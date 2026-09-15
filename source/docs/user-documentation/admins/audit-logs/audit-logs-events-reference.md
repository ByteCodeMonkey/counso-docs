> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Audit Logs: Events Reference

<Info>
  **Enterprise feature.**

  Audit Logs are only available to workspaces on the Enterprise plan.
</Info>

This page lists all events currently emitted by Dust.

***

## Agents

| Event                 | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| `agent.created`       | An agent was created                                              |
| `agent.updated`       | An agent's configuration was updated                              |
| `agent.archived`      | An agent was archived                                             |
| `agent.restored`      | An archived agent was restored                                    |
| `agent.scope_changed` | An agent's visibility scope was changed (e.g. private  workspace) |
| `agent.executed`      | An agent was invoked in a conversation                            |

## Tools

| Event           | Description                                                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tool.executed` | A tool was executed by an agent; metadata includes the tool name, MCP server name, data sources accessed, and whether the action was AI-driven or directly user-initiated |

## Triggers

| Event                    | Description                                |
| ------------------------ | ------------------------------------------ |
| `trigger.created`        | A trigger was created                      |
| `trigger.deleted`        | A trigger was deleted                      |
| `trigger.enabled`        | A trigger was enabled                      |
| `trigger.disabled`       | A trigger was disabled                     |
| `trigger.fired`          | A trigger fired and initiated an agent run |
| `trigger.email_received` | An inbound email was received by a trigger |

## Wake-ups

| Event               | Description             |
| ------------------- | ----------------------- |
| `wake_up.cancelled` | A wake-up was cancelled |
| `wake_up.created`   | A wake-up was created   |
| `wake_up.expired`   | A wake-up expired       |
| `wake_up.fired`     | A wake-up fired         |

## Spaces

| Event                       | Description                         |
| --------------------------- | ----------------------------------- |
| `space.created`             | A space was created                 |
| `space.deleted`             | A space was deleted                 |
| `space.accessed`            | A space was accessed                |
| `space.permissions_updated` | A space's permissions were modified |

## Data Sources

| Event                      | Description                                         |
| -------------------------- | --------------------------------------------------- |
| `datasource.created`       | A data source was created                           |
| `datasource.updated`       | A data source's configuration was updated           |
| `datasource.deleted`       | A data source was deleted                           |
| `datasource.deleted_admin` | A data source was deleted by an admin               |
| `datasource.reauthorized`  | A data source's OAuth credentials were reauthorized |

## Members & Memberships

| Event                       | Description                                                |
| --------------------------- | ---------------------------------------------------------- |
| `member.invited`            | A member was invited to the workspace                      |
| `member.bulk_invited`       | Multiple members were invited in bulk                      |
| `member.bulk_revoked`       | Multiple members were revoked in bulk                      |
| `membership.created`        | A workspace membership was created                         |
| `membership.revoked`        | A workspace membership was revoked                         |
| `membership.role_updated`   | A member's role was changed                                |
| `membership.origin_updated` | The origin of a membership was updated (e.g. manual  SCIM) |

## Invitations

| Event                     | Description                                           |
| ------------------------- | ----------------------------------------------------- |
| `invitation.revoked`      | A pending invitation was revoked                      |
| `invitation.role_updated` | The role assigned to a pending invitation was changed |

## Users

| Event                  | Description                                   |
| ---------------------- | --------------------------------------------- |
| `user.login`           | A user logged in                              |
| `user.login_failed`    | A login attempt failed                        |
| `user.logout`          | A user logged out                             |
| `user.identity_merged` | Two user identities were merged               |
| `user.relocated`       | A user was relocated to a different workspace |

## API Keys

| Event             | Description            |
| ----------------- | ---------------------- |
| `api_key.created` | An API key was created |
| `api_key.updated` | An API key was updated |
| `api_key.revoked` | An API key was revoked |

## OAuth

| Event              | Description                             |
| ------------------ | --------------------------------------- |
| `oauth.initiated`  | An OAuth authorization flow was started |
| `oauth.authorized` | An OAuth authorization was completed    |
| `oauth.revoked`    | An OAuth token was revoked              |

## MCP Connections

| Event                    | Description                              |
| ------------------------ | ---------------------------------------- |
| `mcp_connection.created` | An MCP server connection was established |
| `mcp_connection.deleted` | An MCP server connection was removed     |

## Credentials (BYOK)

| Event                     | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| `credentials.created`     | A credential set was created                                 |
| `credentials.updated`     | A credential set was updated                                 |
| `credentials.revoked`     | A credential set was revoked                                 |
| `credentials.invalidated` | A credential set was invalidated (e.g. provider-side expiry) |

## Domains

| Event                        | Description                                      |
| ---------------------------- | ------------------------------------------------ |
| `domain.removed`             | A verified domain was removed from the workspace |
| `domain.verified`            | A domain was verified                            |
| `domain.verification_failed` | A domain verification attempt failed             |

## SSO & Directory Sync

| Event                      | Description                                       |
| -------------------------- | ------------------------------------------------- |
| `sso.connection_deleted`   | An SSO connection was deleted                     |
| `dsync.connection_deleted` | A Directory Sync connection was deleted           |
| `scim.user_provisioned`    | A user was provisioned via SCIM                   |
| `scim.user_updated`        | A SCIM-provisioned user's attributes were updated |
| `scim.user_deprovisioned`  | A user was deprovisioned via SCIM                 |
| `scim.group_created`       | A group was created via SCIM                      |
| `scim.group_deleted`       | A group was deleted via SCIM                      |
| `scim.group_user_added`    | A user was added to a SCIM group                  |
| `scim.group_user_removed`  | A user was removed from a SCIM group              |

## Conversations

| Event                   | Description                 |
| ----------------------- | --------------------------- |
| `conversation.accessed` | A conversation was accessed |

## Audit Logs (Meta)

| Event                         | Description                                      |
| ----------------------------- | ------------------------------------------------ |
| `audit_log.viewed`            | The Audit Logs viewer was accessed by an admin   |
| `audit_log.export_configured` | An audit log export or log stream was configured |

## Model Access Tiers

| Event                                     | Description                                  |
| ----------------------------------------- | -------------------------------------------- |
| `workspace.advanced_model_access_updated` | The workspace model tier ceiling was changed |
| `group.advanced_model_access_updated`     | A group's model tier override was changed    |
| `user.advanced_model_access_updated`      | A member's model tier override was changed   |

## Workspace

| Event               | Description               |
| ------------------- | ------------------------- |
| `workspace.deleted` | The workspace was deleted |
