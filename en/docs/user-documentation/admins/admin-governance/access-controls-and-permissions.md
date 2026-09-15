# Plan access to workspace data

Access depends on both the connected source and the Space where the source is made available. A connection can synchronize data without making that data available to every member. Administrators should choose the source scope and intended audience before sharing it.

## The main access layers

- **Workspace membership and role** determine which workspace actions a person can perform.
- **Groups and granted permissions** can delegate selected administrative capabilities.
- **Space membership** determines who can use data placed in an open or restricted Space.
- **Agent access** determines which Spaces, data sources, Tools, and Knowledge an Agent can use.

A user needs access to the relevant source through the Agent's configured Space and their own permissions. Publishing an Agent does not by itself expose its private sources to everyone.

## Configure a connection safely

1. Authorize the required service connection with the appropriate account.
2. Select only the folders, channels, or other source areas needed for the intended work.
3. Check the source's sync status and confirm which content was selected.
4. Add the source to a Space whose membership matches the intended audience.
5. Check source-level permissions as well; a workspace Space does not broaden access beyond what the original provider grants.

## Manage access over time

Create separate Spaces when teams need different data boundaries. Review membership when people change roles, and remove sources or members when access is no longer needed. Before an Agent is shared, check its source list and the access of the people who will use it. After a change, ask a representative member to confirm they can reach intended content and cannot reach unrelated restricted material.

For role and group controls, see [Workspace roles, groups, and permissions](workspace-governance-roles-groups-and-permissions.md).
