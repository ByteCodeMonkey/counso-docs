# Confluence

The Confluence tool lets an Agent search and read pages, use CQL for advanced searches, and—when authorized—create, update, or move pages. It also supports user lookup. The tool can use either the connected user's identity or a workspace-level account, depending on the credential model selected by the administrator.

In **Spaces → Tools**, add Confluence and complete the provider OAuth setup. Personal credentials mean each user authorizes their own account; actions and results follow that user's Confluence access. Workspace credentials use a service account for all users who can access the tool, so restrict it to the relevant Spaces. After setup, add Confluence in the Agent builder.

## Capabilities

- **Knowledge Management**: read, create, update, and move pages.
- **Advanced Search**: search pages using Confluence Query Language (CQL); the Agent can help formulate the query.
- **User Management**: retrieve information about Confluence users.

Start with a known page and confirm its space. For edits, identify the destination and intended page change, then reopen the same page in Confluence. Missing pages may not have been shared with the connected identity. The account may be able to read but not edit a page.
