> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Audit Logs

<Info>
  **Enterprise feature.** Audit Logs are only available to workspaces on the
  Enterprise plan.
</Info>

Audit Logs give security and compliance teams a tamper-evident, time-ordered record of every significant action that occurs in your Dust workspace. Every log entry answers: *who did what, to which resource, from where, and when.*

A key capability is the ability to **distinguish between actions taken by human users and actions taken by AI agents**, making it possible to attribute data access, tool executions, and configuration changes to their true originator.

## Accessing Audit Logs

Audit Logs are available to **workspace admins** only. Navigate to:

**Admin > IT & Security > Audit Logs**

The UI provides full-text search, time-range filtering, and CSV export.

<Note>
  Accessing the Audit Logs viewer itself generates an `audit_log.viewed` event.
</Note>

## Log Entry Structure

Each event contains the following fields:

| Field               | Description                                                                      |
| ------------------- | -------------------------------------------------------------------------------- |
| `action`            | The event type (e.g. `agent.executed`, `space.deleted`)                          |
| `occurredAt`        | ISO 8601 timestamp of the event                                                  |
| `actor`             | Identity that triggered the action (see below)                                   |
| `targets`           | Resources affected (workspace, agent, data source, etc.)                         |
| `context.location`  | Client IP address at time of action, or `"internal"` for system-generated events |
| `context.userAgent` | Client user agent string                                                         |
| `metadata`          | Event-specific fields (agent name, conversation ID, etc.)                        |

### Actor Types

| Type      | Description                                                            |
| --------- | ---------------------------------------------------------------------- |
| `user`    | A human user authenticated via the UI or SSO                           |
| `api_key` | A request made using a workspace API key                               |
| `system`  | An automated system process (e.g. SCIM sync, Directory Sync, Temporal) |

<Note>
  For `agent.executed` and `tool.executed` events, the actor reflects the
  identity that initiated the action (user or API key). Whether the action was
  AI-driven is captured in the event's `metadata.actor_type`,
  `metadata.initiating_user_id`, and `metadata.initiating_user_email` fields.
</Note>

## Export and SIEM Integration

Audit Logs can be exported as CSV from the admin UI.
Continuous streaming to a SIEM is supported for log stream destinations such as **Datadog**, **Splunk**, **AWS S3**, **GCP GCS**, and any **custom HTTPS endpoint**.

### IP Allowlist

If your SIEM or log stream endpoint restricts inbound traffic by IP, allowlist the following addresses.

**WorkOS delivery IPs** (used to deliver audit log events to your log stream endpoint):

```
3.217.146.166
23.21.184.92
34.204.154.149
44.213.245.178
44.215.236.82
50.16.203.9
52.1.251.34
52.21.49.187
174.129.36.47
```

For the canonical and up-to-date list, refer to the [WorkOS IP allowlist documentation](https://workos.com/docs/events/data-syncing/webhooks).

## Related

* See the [Events Reference](/docs/user-documentation/admins/audit-logs/audit-logs-events-reference) for the full list of emitted events.
* [Single Sign-On (SSO)](/docs/user-documentation/admins/admin-governance/single-sign-on-sso/single-sign-on-sso)
* [Users and Groups Provisioning](/docs/user-documentation/admins/admin-governance/users-and-groups-provisioning)
* [Access Controls and Permissions](/docs/user-documentation/admins/admin-governance/access-controls-and-permissions)
