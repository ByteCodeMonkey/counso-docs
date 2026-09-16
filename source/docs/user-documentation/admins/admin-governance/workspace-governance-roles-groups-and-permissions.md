> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Workspace Governance: Roles, Groups & Permissions 

Dust gives you three workspace roles and a set of granular permissions. Together, they control what people can manage, create, publish, and access in your workspace.

## Roles

### Admin

Admins have full workspace administration access. They can configure workspace settings, manage members and groups, and control permissions.

Admins always retain access to capabilities set to **Admin only**.

By default, Admins can:

* Manage billing and subscriptions
* Manage security settings, user access, identity verification, and provisioning
* Configure governance permissions
* Enable or disable the policy for sharing MiniApps externally
* Enable or disable audit logs

### Manager

Managers are delegated workspace administrators. They can:

* Invite and remove members
* Change the roles of non-admin members
* Assign the Manager and Member roles
* View workspace analytics and usage page
* Review and act on credit upgrade requests from members
* Choose which groups can create and publish agents and skills

Managers do not receive billing or security access by default. Admins can grant these permissions to groups when needed.

Managers cannot manage the policy for sharing MiniApps externally or audit logs. When the external MiniApp sharing policy is enabled, Managers can configure which groups may invite users to MiniApps and make them public.

### Member

Members use Dust according to their seat, group memberships, resource access, and granted permissions. Members do not have administrative access by default.

Admins can grant Members additional permissions through groups.

## Groups and permissions

Dust supports two types of groups:

* **Provisioned groups**, synchronized from your identity provider through SCIM
* **Manual groups**, created and managed in Dust

Permissions are granted to groups rather than directly to individual people. To grant a permission to one person, create a manual group, add that person to it, and grant the permission to the group.

Permissions are additive. If a person belongs to several groups, they receive the combined permissions granted by those groups. A group grant adds access and does not remove access granted elsewhere.

Each permission uses one of three modes:

| Mode       | Who receives access            |
| ---------- | ------------------------------ |
| Everyone   | All workspace members          |
| Groups     | Members of the selected groups |
| Admin only | Admins only                    |

## Permission matrix

The following permissions are available in the workspace governance settings.

| Permission                       | Admin                      | Manager                           | Member                            |
| -------------------------------- | -------------------------- | --------------------------------- | --------------------------------- |
| Create agents                    | Yes                        | When granted                      | When granted                      |
| Publish agents                   | Yes                        | When granted                      | When granted                      |
| Create skills                    | Yes                        | When granted                      | When granted                      |
| View and export audit logs       | Yes                        | When granted                      | When granted                      |
| Manage billing and subscriptions | Yes by default             | When granted                      | When granted                      |
| Manage security and provisioning | Yes by default             | When granted                      | When granted                      |
| Manage workspace model providers | Yes                        | No                                | No                                |
| Invite external users to MiniApps  | Yes when the policy allows | When granted if the policy allows | When granted if the policy allows |
| Publish MiniApps                   | Yes when the policy allows | When granted if the policy allows | When granted if the policy allows |
| View workspace analytics         | Yes                        | Yes                               | No                                |

## Workspace governance settings

Workspace settings and permission controls are managed under **Settings & Governance**.

Billing and security are permissions, not separate roles. Admins receive access by default. Admins can delegate either permission to selected groups without changing those members' workspace roles.

## The Builder role

The Builder role is being replaced by separate permissions for creating and publishing agents and skills.

During the transition, workspaces that used the Builder role receive a **Builders** group. Existing builders are added to that group, which preserves their agent and skill creation access without preserving a broad Builder role.

API keys using the `builder` role receive the legacy Builders group instead. The API key role is removed in the end state.

Admins can move those permissions to other manual or provisioned groups as their workspace model evolves.

## How access is determined

A person's effective access combines:

1. Their workspace role
2. The permissions granted to their groups
3. Their access to specific resources, such as spaces, agents, skills, and other workspace content

These sources of access are additive. A permission granted through one group does not remove access granted through another group or through the person's workspace role.
