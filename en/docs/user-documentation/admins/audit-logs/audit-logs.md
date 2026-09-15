# Review workspace audit logs

Audit Logs provide a time-ordered record of significant workspace actions. When the feature is enabled, Admins have access by default; Managers or Members need the corresponding view and export permission.

## Before you begin

Define what you need to investigate, such as a failed login, an Agent change, a membership change, an unexpected tool call, or a directory-sync event. Note the approximate time, actor, resource, and action. If Audit Logs is not available in the administration area, ask an administrator to confirm that the feature is enabled and check your role or delegated permission; an empty view alone does not show that no events occurred.

## Find relevant events

1. Open the administration area and select **Audit Logs** when available.
2. Set the narrowest useful time range. Search for a known actor, resource, action, or identifier, then widen the range if needed.
3. Filter by event family, such as Agent creation or execution, tool execution, trigger and wake-up changes, Space permissions, member and role changes, data-source authorization, login, OAuth, SSO or directory sync, and conversation access.
4. Open an event and review its action, timestamp, actor, targets, context, and metadata together. The actor can be a user or system process. Agent and tool event metadata can show whether the action was user-driven or AI-driven.
5. Compare nearby events for the same actor and target to distinguish a configuration change from the execution that followed.

Opening the viewer is itself recorded as `audit_log.viewed`. Include it when documenting an investigation.

## Export and stream logs

When the viewer provides CSV export, export the filtered results and check the time range, row count, and representative events. Keep the filter and export time with the file so another administrator can reproduce the selection.

If the workspace's Audit Logs settings provide continuous log streaming, an administrator can configure a supported destination there, such as Datadog, Splunk, AWS S3, GCP GCS, or a custom HTTPS endpoint. Follow the destination settings shown in the workspace and verify receipt at the destination. Streaming availability and destination options depend on workspace configuration; an administrator must enable the feature.

## Common questions

### Why can't I open Audit Logs?

Ask a workspace administrator to confirm the feature is enabled and check your Admin role or delegated view/export permission.

### Does the actor field show whether AI was involved?

For Agent and tool events, inspect the metadata as well as the actor. The initiating user can remain the actor while the metadata identifies the action as AI-driven.

### Why did opening the viewer add an event?

Viewer access is recorded as `audit_log.viewed`, so an investigation should expect that event near the time it began.
