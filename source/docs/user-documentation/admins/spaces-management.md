> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Spaces management

You can make data available to your Dust workspace via **spaces** that let you organize and [control access](/docs/user-documentation/admins/admin-governance/access-controls-and-permissions) to your data.

<Info>
  **Once Connections are set up, don't forget to create spaces and add data to your spaces.**
</Info>

Spaces are containers for storing information relevant to specific groups or projects. They come in two types:

* **Open spaces:** accessible to all workspace members
* **Restricted spaces**: limited access to designated users

## Open spaces

Open spaces are accessible to all members of your workspace. They're ideal for sharing common resources and fostering collaboration across teams.

<Info>
  **Key Features**

  * Managed by: workspace administrators
  * Accessible to: available to all workspace members
  * Ideal for: organizing team/project data
</Info>

### Company Data

Every workspace includes a default space called "Company Data". This special space cannot be modified or restricted.

## Restricted spaces

Workspace administrators manage which team members have access to a space. Agents that access data from a specific space are only available to members of that space. If you have [Users and groups provisioning](/docs/user-documentation/admins/admin-governance/users-and-groups-provisioning) set up, members can be based on groups coming from your IdP.

<Info>
  **Key features:**

  * Managed by: workspace administrators
  * Accessible to: only to selected members
  * Ideal for: securing sensitive data and controlling who can access it
</Info>

### Using provisioned groups

If you have [Users and groups provisioning](/docs/user-documentation/admins/admin-governance/users-and-groups-provisioning) setup, members can be based on groups coming from your IdP. Select "Provisioned group access" from the combo box, then add the groups you want to associate with the space. The group members will be managed in your IdP - you won't have to manually manage space members in Dust.

## Create a space

Only workspace admins can create and manage spaces:

1. Go to "**Spaces**" tab
2. Click "***New***"
3. Name the Space
4. Choose if it's **Open** or **Restricted**
5. If restricted, add Members
6. Click "**Create**"

## Add data to a space

### From a connection

*Note:* Only admins can add data from "***Connections***" to a space.

To add data from a ***connection*** (connected by an Admin),

1. Click on your Space and click on "***Connected Data.***".
2. Click "***Add data from connections***".
3. From the modal, select only the data that should be available to the space.
4. Click "***Save***."

### From other sources

**For folders, websites, and apps:**

* in Open spaces: only admins and builders can add data
* in Restricted spaces: all members can add data

## Using spaces in agents tools

### Agents visibility

**The space(s) used by an agent determines who can see and use the agent**. Only members of the space(s) used by the agent's tools will be able to see and use it.

The number of spaces you can create depends on your plan.

The number of spaces you can create depends on your plan: Business supports up to 5 spaces, and Enterprise supports up to 100. For more information or assistance with Dust Spaces, please contact our support team at [support@dust.tt](mailto:support@dust.tt).
