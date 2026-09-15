---
title: "Provision workspace users and groups"
---
Where directory provisioning is available, an administrator can connect an identity provider (IdP) using SCIM 2.0 to create, update, and deactivate workspace users and groups. Both workspace administration access and IdP administration access are required. The setup steps vary by provider, so follow its current SCIM instructions alongside the workspace setup flow.

## Set up directory sync

1. In workspace administration, open **People & Security**, then **Domain and Members**.
2. Under **User provisioning**, choose **Setup Directory sync**.
3. Select the identity provider offered by the setup flow and follow the generated instructions in both systems.
4. Start with a test user and group. Verify that a user creation, an attribute update, a group membership change, and a deactivation are reflected as intended before provisioning the broader directory.

Some identity providers use separate applications for SSO and directory sync. Check the provider's documentation for its requirements rather than assuming one configuration completes both. If directory sync is unavailable in the workspace, confirm the feature and administrator permissions before changing the IdP.

## Map groups to workspace roles

An administrator can map a workspace group to an **Admin** or **Manager** role from **Settings & Governance > Roles**. The group can be provisioned from the IdP or managed manually in the workspace.

- A member inherits the role mapped to each group they belong to.
- Each group can grant at most one role.
- A member who receives roles from several groups keeps the highest role.

For an IdP-managed group, create and populate the group in the IdP, synchronize it, and then map that workspace group to the intended role. Review membership and role changes with a test account before applying them to the full organization.
