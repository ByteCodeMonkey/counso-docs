# Jira

Jira tools let an Agent browse projects and issues, search, create or update issues, and perform workflow transitions when the connected identity has permission. The provider's project role and workflow conditions apply in addition to the tool configuration.

In **Spaces → Tools**, add Jira and select the site and credential method offered by the current form. Complete OAuth or the supported provider authentication, then share the tool with the intended Space and add it to an Agent. For a custom app, use the callback shown in the connection form. Grant **Browse Projects** and issue-read access for search; add Create/Edit Issues or Transition Issues only when the Agent is expected to write.

Start by reading a known project and issue. Before creating or changing an issue, specify project key, issue type, summary, fields, and desired transition. Read the issue back afterward. A transition may fail even when the issue is readable because workflow conditions, required fields, or project permissions are separate checks.
