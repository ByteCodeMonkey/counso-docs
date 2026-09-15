> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Monday

Monday tools let your agents interact with Monday.com boards, items, groups, and users. Agents can automate CRM workflows, project management, lead tracking, and team coordination: managing sales pipelines, tracking projects, or coordinating team activities.

## Use Case Examples

<Cards columns={3}>
  <Card title="CRM Pipeline Management" icon="fa-chart-line">
    Automatically create and update deals, move leads to opportunities, and track your sales pipeline
  </Card>

  <Card title="Project Tracking" icon="fa-tasks">
    Search items by status, create tasks, add updates, and keep your projects
    organized
  </Card>

  <Card title="Bulk Operations" icon="fa-layer-group">
    Import multiple leads or opportunities efficiently using bulk creation tools
  </Card>
</Cards>

***

Go to Spaces > Tools in your Dust workspace, click `Add Tools`, and select Monday.

## Authentication Setup

To connect Monday.com to Dust:

1. Click on the Monday tool in your workspace
2. Complete the OAuth flow using the installation URL
3. Note: Monday admins need to install the Dust app in their Monday.com workspace first

**Installation URL:** `https://auth.monday.com/oauth2/authorize?client_id=0466cfd3d05df679d21710d32a96cfb4&response_type=install`

## Personal credentials vs Workspace credentials

|                                    | Description                                                                                                                 | Benefits                                  |
| :--------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------- |
| Personal credentials (recommended) | Each user uses their own Monday.com credentials. Agents can only perform actions the current user can perform in Monday.com | More secure, granular permissions         |
| Workspace credentials              | All users share the admin's Monday.com credentials when using Monday tools. All agent actions use the admin's account       | Simpler setup, no per-user authentication |

You will be redirected through an OAuth flow to connect Monday.com. By default, this tool is added to the Company data Space, making it accessible across the workspace.

## Available Tools

### Board Management

| Tool                      | Description                                                       |
| :------------------------ | :---------------------------------------------------------------- |
| **get\_boards**           | Lists all accessible boards (up to 100)                           |
| **get\_board\_values**    | Retrieves detailed board information including columns and groups |
| **create\_board**         | Creates a new board with optional workspace and description       |
| **get\_board\_analytics** | Retrieves analytics and statistics for reporting                  |

### Item Management

| Tool                              | Description                                                                                               |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **get\_board\_items**             | Retrieves items from a specific board (up to 100)                                                         |
| **get\_item\_details**            | Retrieves detailed information about a specific item                                                      |
| **search\_items**                 | Advanced search with filtering by query, board, status, assignee, group, timeframe, with ordering options |
| **create\_item**                  | Creates a new item with optional group and column values                                                  |
| **create\_multiple\_items**       | Bulk creates multiple items across boards                                                                 |
| **update\_item**                  | Updates column values of an existing item                                                                 |
| **update\_item\_name**            | Updates the name of an item                                                                               |
| **delete\_item**                  | Deletes an item                                                                                           |
| **move\_item\_to\_board**         | Moves an item between boards (useful for CRM workflows like converting leads to opportunities)            |
| **get\_items\_by\_column\_value** | Retrieves items filtered by column value                                                                  |

### Group Management

| Tool                    | Description                                            |
| :---------------------- | :----------------------------------------------------- |
| **create\_group**       | Creates a new group in a board                         |
| **get\_group\_details** | Retrieves details about a specific group               |
| **delete\_group**       | Deletes a group from a board                           |
| **duplicate\_group**    | Duplicates a group with optional positioning and title |

### Column Management

| Tool                          | Description                                            |
| :---------------------------- | :----------------------------------------------------- |
| **create\_column**            | Creates a new column with specified type               |
| **get\_column\_values**       | Retrieves column values for a specific item and column |
| **get\_file\_column\_values** | Retrieves file column values                           |
| **upload\_file\_to\_column**  | Uploads a file to a column                             |

### Subitem Management

| Tool                     | Description                            |
| :----------------------- | :------------------------------------- |
| **create\_subitem**      | Creates a new subitem for an item      |
| **update\_subitem**      | Updates column values of a subitem     |
| **get\_subitem\_values** | Retrieves subitems for a specific item |

### Updates & Comments

| Tool               | Description                         |
| :----------------- | :---------------------------------- |
| **create\_update** | Adds an update (comment) to an item |

### User Management

| Tool                     | Description                             |
| :----------------------- | :-------------------------------------- |
| **find\_user\_by\_name** | Finds a user by name                    |
| **get\_user\_details**   | Retrieves details about a specific user |

### Analytics & Activity

| Tool                      | Description                                                                 |
| :------------------------ | :-------------------------------------------------------------------------- |
| **get\_activity\_logs**   | Retrieves activity logs for tracking pipeline velocity and user actions     |
| **get\_board\_analytics** | Retrieves board statistics by status, group, and assignee for CRM reporting |

Once the tool has been configured by the admin as described above, it can be added to any agent in the Agent Builder.

## Adding Monday Tools to Agents

1. In the Agent Builder, click on `Add Tool`
2. Select Monday from the available tools
3. Configure the tool settings as needed

## Personal Credentials Usage

When using **Personal credentials**, users will need to authenticate on their first use:

1. When you first use an agent with the Monday tool, you'll see a connection prompt
2. Click on the `Connect` button to authenticate with your own Monday.com credentials
3. After connecting, click the `Retry` button to replay the agent answer

From then on, requests will use your personal credentials, automatically inheriting your Monday.com permissions and ensuring all actions are performed with appropriate access controls.

<Info>
  **Personal credentials provide better security**

  With personal credentials, each user's actions are tracked individually, and agents can only access what the user can access in Monday.com.
</Info>

## CRM Pipeline Management

* Create a new deal in my sales pipeline for Acme Corp worth \$50,000
* Move the lead "TechStart Inc" to the opportunities board
* Show me all deals in the "Proposal Sent" stage
* Update the status of deal #12345 to "Closed Won"

## Project Tracking

* Create a new task called "Design homepage mockup" in the Marketing board
* Search for all items assigned to me with status "In Progress"
* Get all overdue items from the Development board
* Add an update to task #789 saying "Completed initial review"

## Analytics & Reporting

* Show me the activity logs for the Sales board from last week
* Get analytics on deal distribution by status
* How many items are assigned to each team member?
* Track pipeline velocity for Q4

## Team Coordination

* Find user John Smith in Monday
* Create a task and assign it to Sarah Johnson
* Add a comment to item #456 mentioning the latest update
* Get details about all users in the Sales team

## Best Practices

When building agents with Monday.com tools:

* **Be specific with board names**: Include exact board names in your agent instructions to avoid confusion
* **Use bulk operations wisely**: For importing multiple records, use `create_multiple_items` rather than creating items individually
* **Use search**: The `search_items` tool supports advanced filtering - use it to find exactly what you need
* **Track changes**: Use activity logs to monitor pipeline velocity and team performance
* **Consider permissions**: When using personal credentials, remember that agents inherit the user's permissions

## Example Agent Instructions

Here's an example of how to configure a CRM agent with Monday.com tools:

```text theme={null}
You are a CRM assistant with access to our Monday.com sales boards:
- "Leads" board for new prospects
- "Opportunities" board for qualified deals
- "Customers" board for closed-won accounts

When asked to:
- Add a new lead: Create an item in the Leads board with all provided details
- Qualify a lead: Move the item from Leads to Opportunities board
- Close a deal: Update the status column to "Closed Won" and move to Customers board
- Report on pipeline: Use search_items and get_board_analytics to provide insights

Always confirm actions with the user before making changes to important deals.
```
