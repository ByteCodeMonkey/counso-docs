> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Confluence

## Overview

## Key Features

| Tool                   | Description                                    |
| ---------------------- | ---------------------------------------------- |
| `Knowledge Management` | Read, create, update and move Confluence pages |
| `Advanced Search`      | Search pages with CQL syntax                   |
| `User Management`      | Retrieve and work with Confluence users        |

### Use case examples

| Tool                         | Description                                                            |
| ---------------------------- | ---------------------------------------------------------------------- |
| `Create pages automatically` | Automate the update of your documentation                              |
| `CQL made simple`            | Search through Confluence pages without knowing the CQL syntax         |
| `Write better documentation` | Create documentation that match your company's preferred writing style |

## Admin: Setup in Dust

Go to **Spaces > Tools** in your Dust workspace, click `Add Tools`, and select Confluence.

### Personal credentials vs Workspace credentials

|                                    | Description                                                                                                                                                          | Benefits                                         |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Personal credentials (recommended) | Each user will use their own credentials to Confluence. Agents using the Confluence tool will only be able to perform actions that the current user can also perform | More secure                                      |
| Workspace credentials              | The workspace admin logs in to Confluence with a service account, all agents (no matter which user calls them) use that service account                              | No need for Confluence credentials for each user |

You will then be redirected to an oAuth flow to connect an admin Confluence. By default this tool is added to the Company data Space, so accessible in all the workspace.

## User: Usage in Dust

Once the tool has been configured by the admin as described before, it can be selected on any agent: in the Agent Builder, simply click on `Add Tool` and select Confluence.

### Personal credentials usage

When users use an agent with the Confluence tool for the first time, they will get this message: `The agent took an action that requires personal authentication`

Click on the `Connect` button to connect your own Confluence credentials. And then, click on the `Retry` button to replay the agent answer.

From then on, requests will use the user's personal credentials, automatically inheriting their Confluence permissions.
