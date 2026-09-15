---
title: "Workspace roles, groups, and permissions"
---
Workspace roles provide baseline access. Group permissions add selected capabilities, and access to a specific Space, Agent, or Skill is controlled separately.

## Roles

**Admin** has full workspace administration access. Admins manage settings, members, groups, and permissions; they retain access to permissions set to **Admin only**. By default, Admins can manage billing and security, configure governance, control the external Frame-sharing policy, and enable or disable Audit Logs.

**Manager** can invite and remove members, change roles of non-Admins, assign Manager or Member roles, view analytics and usage, act on credit-upgrade requests, and choose which groups can create or publish Agents and Skills. Managers do not have billing or security access by default. They cannot change the external Frame-sharing policy or enable or disable Audit Logs; when external sharing is enabled, they can configure which groups may invite people to Frames and publish them.

**Member** uses workspace resources according to group permissions, resource access, and other grants. Members have no administrative access by default, but Admins can grant additional permissions through groups.

## Groups and permission modes

Groups can be provisioned from an identity provider through SCIM or created and managed manually. Permissions are granted to groups. To grant a permission to one person, create a manual group for them and grant the permission to that group. Permissions are additive: members of multiple groups receive the combined grants.

Each governance permission can be set to **Everyone**, selected **Groups**, or **Admin only**.

## Permission matrix

| Permission | Admin | Manager | Member |
|---|---|---|---|
| Create Agents | Yes | When granted | When granted |
| Publish Agents | Yes | When granted | When granted |
| Create Skills | Yes | When granted | When granted |
| View and export Audit Logs | Yes | When granted | When granted |
| Manage billing and subscriptions | Yes by default | When granted | When granted |
| Manage security and provisioning | Yes by default | When granted | When granted |
| Manage workspace model providers | Yes | No | No |
| Invite external users to Frames | If policy allows | If granted and policy allows | If granted and policy allows |
| Publish Frames | If policy allows | If granted and policy allows | If granted and policy allows |
| View workspace analytics | Yes | Yes | No |

Billing and security are permissions rather than separate workspace roles. An Admin can delegate either permission to selected groups without changing their members' roles. Effective access combines a person's role, group permissions, and access to the specific resource.

## Earlier Builder roles

Workspaces moving from the earlier Builder role use a **Builders** group to preserve existing Agent and Skill creation permissions. Administrators can review or redistribute those group permissions in **Settings & Governance**. Creating and publishing are separate permissions.
