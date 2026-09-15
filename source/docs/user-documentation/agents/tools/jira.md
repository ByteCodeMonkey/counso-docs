> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Jira

## Overview

Jira tools let your agents manage Jira projects and issues from Dust. Agents can create and update tickets, track projects, and move issues through workflow transitions without leaving Dust.

## Key Features

| Tool               | Description                                                                       |
| ------------------ | --------------------------------------------------------------------------------- |
| `Issue Management` | Read, create, update, comment and move Jira issues                                |
| `Project Access`   | Browse and manage accessible Jira projects                                        |
| `Advanced Search`  | Search issues with multiple filter criteria including custom fields or JQL syntax |
| `User Management`  | Retrieve and work with Jira users                                                 |

## Use case examples

<Cards columns={3}>
  <Card title="Create issues automatically" icon="fa-wand-sparkles" target="_blank">
    Automate the creation of Jira Issues from a Customer Success agent
  </Card>

  <Card title="JQL made simple" icon="fa-magnifying-glass">
    Search through Jira issues without knowing the JQL syntax
  </Card>

  <Card title="Write good User Stories" icon="fa-pencil">
    Create User Stories that match your company's preferred syntax
  </Card>
</Cards>

Go to Spaces > Tools in your Dust workspace, click `Add Tools`, and select Jira.

## Personal credentials vs Workspace credentials

|                                    | Description                                                                                                                                              | Benefits                                   |
| :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------- |
| Personal credentials (recommended) | Each user will use their own credentials to Jira. Agents using the Jira tool will only be able to perform actions that the current user can also perform | More secure                                |
| Workspace credentials              | The workspace admin logs in to Jira with a service account, all agents (no matter which user calls them) use that service account                        | No need for Jira credentials for each user |

You will then be redirected to an oAuth flow to connect an admin Jira. By default this tool is added to the Company data Space, so accessible in all the workspace.

## Usage in Dust

Once the tool has been configured by the admin as described before, it can be selected on any agent: in the Agent Builder, click on `Add Tool` and select Jira.

## Personal credentials usage

When users use an agent with the Jira tool for the first time, they will get this message:

Click on the `Connect` button to connect your own Jira credentials. And then, click on the `Retry` button to replay the agent answer.

From then on, requests will use the user's personal credentials, automatically inheriting their Jira permissions.
