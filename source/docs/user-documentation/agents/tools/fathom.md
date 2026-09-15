> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Fathom

## Overview

The Fathom MCP lets agents access your Fathom meeting data without leaving the conversation. It supports:

* Listing meetings with filters (date range, teams, recorded by, domains)
* Optionally including AI summary, action items, and CRM matches in the meeting results
* Retrieving the full transcript for a specific recording

This connector is read-only and designed for safe retrieval of meeting context.

## Connection Setup (Admin)

1. In Dust, go to **Spaces Tools** and click **Add Tools**.
2. Select **Fathom** from the list of available tools.
3. Complete the OAuth flow to connect your Fathom account.
4. Choose whether to use **Shared** (workspace) or **Personal** credentials based on your policy.
5. Share the tool to the spaces where you want it available.

Once connected, the Fathom toolset will be available to add to agents in the spaces you grant access to.

## Authentication

Fathom uses **OAuth**. An admin must complete the initial OAuth flow during setup. You can then operate with either:

* **Shared credentials**: all users share the same connection.
* **Personal credentials**: each user authenticates the first time they use the tool.

Choose based on your organization's security model. See [Personal vs Shared Credentials](https://docs.dust.tt) for guidance.

## Available Tools

| Tool                | Description                                                                                                                             |
| :------------------ | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **list\_meetings**  | List Fathom meetings with filters (date range, recorded by, teams, domains) and optional includes (summary, action items, CRM matches). |
| **get\_transcript** | Get the full transcript of a Fathom meeting recording by `recording_id`. Large transcripts are saved as conversation files.             |

All tools are read-only.

## Tool Parameters

### list\_meetings

| Parameter                        | Type      | Required | Description                                                                                                                                          |
| :------------------------------- | :-------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor`                         | string    | No       | Pagination cursor returned as `next_cursor` in a previous response. Omit to start from the beginning.                                                |
| `start_date`                     | string    | No       | Filter meetings created after this ISO 8601 timestamp (e.g. `2024-01-01T00:00:00Z`).                                                                 |
| `end_date`                       | string    | No       | Filter meetings created before this ISO 8601 timestamp (e.g. `2024-12-31T23:59:59Z`).                                                                |
| `recording_id`                   | number    | No       | Filter the current page to a specific recording by its numeric ID. If not found on this page, paginate using `next_cursor`.                          |
| `calendar_invitees_domains`      | string\[] | No       | Filter by company domains in the calendar invitee list (exact match). Returns meetings where any domain appears (e.g. `["acme.com", "client.com"]`). |
| `calendar_invitees_domains_type` | enum      | No       | Filter by whether calendar invitees include external email domains. One of: `all` (default), `only_internal`, `one_or_more_external`.                |
| `recorded_by`                    | string\[] | No       | Filter by email addresses of users who recorded meetings. Returns meetings recorded by any specified user (e.g. `["ceo@acme.com", "pm@acme.com"]`).  |
| `teams`                          | string\[] | No       | Filter by team names. Returns meetings that belong to any of the specified teams (e.g. `["Sales", "Engineering"]`).                                  |
| `include_action_items`           | boolean   | No       | Include AI-extracted action items for each meeting.                                                                                                  |
| `include_crm_matches`            | boolean   | No       | Include CRM matches (contacts, companies, deals) for each meeting. Only returns data from your connected CRM.                                        |
| `include_summary`                | boolean   | No       | Fetch the AI-generated summary for each meeting via the recordings API. Most useful combined with `recording_id`.                                    |

### get\_transcript

| Parameter      | Type   | Required | Description                                                                          |
| :------------- | :----- | :------- | :----------------------------------------------------------------------------------- |
| `recording_id` | number | Yes      | The numeric recording ID (e.g. the `recordingId` field returned by `list_meetings`). |

## Adding Fathom Tools to Agents

After admin setup, the Fathom toolset can be added to an agent by selecting it in the Agent Builder. Admins can make it available to specific spaces or organization-wide.

## Tips

* **Find a specific call:** Use `recording_id` with `include_summary: true` in `list_meetings` to fetch a single meeting's metadata and summary, then call `get_transcript` for the full text.
* **Large transcripts:** Results are saved as files. Open the transcript file and scroll or load progressively. For programmatic reads, use chunked reads.

## Troubleshooting

* **Authentication prompts keep appearing:** If using Personal credentials, each user must authenticate on first use. Admins should complete the initial OAuth flow during setup.
* **Tool not visible in a space:** Confirm the Fathom tool is shared with that space under the tool's **Sharing** tab.
