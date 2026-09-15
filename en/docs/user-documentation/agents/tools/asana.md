# Asana

The Asana tool lets an Agent search and work with tasks and projects using an authorized Asana identity. Depending on the granted access, actions can include reading project/task data and creating or updating tasks.

## Administrator setup

In the workspace's **Spaces → Tools**, add Asana and select the credential model supported by the current form: **Workspace credentials** use one configured account, while **Personal credentials** require each user to connect their own account. Complete the provider OAuth flow. If you maintain your own Asana OAuth application, use the callback shown in the Counso form rather than copying a callback from another deployment.

An Asana administrator must also open **My Apps → Manage distribution**, select the Asana workspace where the application may be used, and save. Without this distribution step, authorization may appear successful while the Agent returns no workspace data.

Add Asana to the intended Agent and start with one project and task read. Before enabling task creation or updates, confirm the acting identity and project permissions. If the tool is connected but returns no data, check app distribution, workspace membership, and the user's access to the project.
