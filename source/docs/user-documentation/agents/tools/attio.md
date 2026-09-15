> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Attio

## Overview

Attio MCP is a hosted Model Context Protocol server by Attio that lets agents search, create, and update CRM data (people, companies, deals, tasks, notes, meetings, calls, and emails) directly in your Attio workspace. Authentication is handled via OAuth, so actions are performed as the connected user.

## Connection Setup (Admin)

Set up Attio as a Remote MCP Server in Dust.

1. In Dust, go to **Spaces Tools** and click **Add Tool**.
2. Click **Add MCP Server**.
3. In the **MCP server URL** field, enter: `https://mcp.attio.com/mcp`
4. For **Authentication**, choose **Automatic (OAuth)** and complete the OAuth authorization flow to connect your Attio account.
5. After the sync finishes, the Attio toolset will appear and can be added to spaces and agents.

## Available Tools

The Attio MCP exposes a range of CRM capabilities. For the authoritative, up-to-date tool list and full schema details, see [Attio's official MCP documentation](https://docs.attio.com/mcp/overview).

### Records & Objects

| Tool                         | Description                                                                |
| ---------------------------- | -------------------------------------------------------------------------- |
| `search-records`             | Search for records (people, companies, deals, etc.) across your workspace. |
| `get-records-by-ids`         | Retrieve one or more records by their IDs.                                 |
| `create-record`              | Create a new record in an Attio object (e.g., a new company or person).    |
| `upsert-record`              | Create or update a record based on a matching attribute.                   |
| `list-attribute-definitions` | List the attribute definitions for an Attio object.                        |

### Notes

| Tool                       | Description                                            |
| -------------------------- | ------------------------------------------------------ |
| `create-note`              | Add a note to a record.                                |
| `search-notes-by-metadata` | Search notes by metadata filters.                      |
| `semantic-search-notes`    | Search notes using semantic (natural language) search. |
| `get-note-body`            | Retrieve the full content of a specific note.          |

### Tasks

* **create-task**: Create a task in Attio.
* **update-task**: Update an existing task (e.g., mark as complete, change assignee).

### Meetings & Calls

| Tool                                 | Description                                        |
| ------------------------------------ | -------------------------------------------------- |
| `search-meetings`                    | Search for meeting records.                        |
| `search-call-recordings-by-metadata` | Find call recordings by metadata.                  |
| `semantic-search-call-recordings`    | Search call recordings using semantic search.      |
| `get-call-recording`                 | Retrieve the details of a specific call recording. |

### Emails

| Tool                        | Description                                    |
| --------------------------- | ---------------------------------------------- |
| `search-emails-by-metadata` | Find emails by metadata filters.               |
| `semantic-search-emails`    | Search emails using semantic search.           |
| `get-email-content`         | Retrieve the full content of a specific email. |

### Workspace

| Tool                     | Description                                                |
| ------------------------ | ---------------------------------------------------------- |
| `list-workspace-members` | List all members of the Attio workspace.                   |
| `list-workspace-teams`   | List all teams in the workspace.                           |
| `whoami`                 | Return information about the currently authenticated user. |

## Security & Approvals

Configure tool stakes in **Tools Management** to match your workspace policy:

* **Read operations** (search, get, list) are typically low-risk and can be set to **Low stake** or **Never ask**.
* **Write operations** (creating/updating records, creating tasks, adding notes) modify CRM data and should be set to **High stake** so users approve calls before they execute.

## Troubleshooting

* If the OAuth flow fails or the Attio tools don't appear after setup, re-run the **Add MCP Server** flow from **Spaces Tools Add Tool Add MCP Server**.
* If tools still don't appear, check whether your workspace has any feature restrictions that may be blocking the integration.
