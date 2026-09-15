> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Gong

## Overview

Tools to list calls, retrieve call details, and fetch transcripts from Gong, supporting sales and go-to-market workflows directly from Dust.

The Gong MCP server lets agents:

* List recent or date-bounded calls
* Retrieve detailed metadata for a specific call (participants, timing, summary fields, and more)
* Retrieve the full transcript for a call, organized by speaker

This is a live, tool-based integration (MCP), distinct from the Gong data sync connection. If you're looking to synchronize transcripts into Dust for semantic search, see [Gong connection](/docs/user-documentation/admins/connections-management/gong).

## Connection Setup (Admin)

1. In Dust, go to **Spaces → Tools** and click **Add Tools**.
2. Select **Gong** from the list of available tools.
3. Complete the OAuth authorization to connect your Gong account.

Once connected and added to a Space, users can add the Gong tool to agents in that Space and start using it in conversations.

## Authentication & Permissions Model

<Danger>
  **Gong's API does not scope results to just the authenticating user's calls.
  It returns all calls for the Gong workspace.** Even if a user connects with
  their personal Gong account, listing or retrieving calls via the Gong MCP
  tools will return calls across the workspace, subject to Gong's own workspace
  permissions and visibility. To control who can use the Gong tools, limit
  access by placing them only in Spaces with appropriate membership. For
  sensitive deployments, create a Space dedicated to specific teams or roles and
  add Gong there.
</Danger>

## Available Tools

The Gong MCP server exposes three tools:

### list\_calls

* Description: List calls recorded in Gong within a date range. Returns call metadata including title, participants, duration, and timing. If no dates are provided, returns the most recent calls.
* Parameters:
  * `fromDateTime` (optional, string): ISO-8601 start (e.g., `2024-01-01T00:00:00Z`)
  * `toDateTime` (optional, string): ISO-8601 end
  * `cursor` (optional, string): Pagination cursor from a previous response
* Notes:
  * Results are paginated; use the returned cursor to fetch the next page (up to 50 calls per page).

### get\_call

* Description: Retrieve detailed information about a specific call by its ID (participants and extended metadata).
* Parameters:
  * `callId` (string): Gong call ID

### get\_call\_transcript

* Description: Retrieve the full transcript of a call, organized by speaker.
* Parameters:
  * `callId` (string): Gong call ID
* Notes:
  * If the call has not been transcribed yet, the tool returns a clear error indicating the transcript is not available. Try again later.

## Usage

After adding Gong to a Space and including it in an agent:

* Ask the agent to list calls (optionally with a date range).
  * Example: "List calls from 2026-04-01 to 2026-04-15."
* Retrieve details for a call by ID returned from `list_calls`.
  * Example: "Get the details for call 1234567890."
* Fetch the transcript for a given call.
  * Example: "Get the transcript for call 1234567890 and summarize the key objections."

<Tip>
  Because Gong's API returns workspace calls, agents may see calls beyond the
  authenticating user's own meetings. Use Space membership to control who can
  invoke these tools.
</Tip>

## Notes and Limitations

* Transcript availability: Newly completed calls may not have transcripts immediately. If you see "No transcript found," wait until Gong finishes processing and try again.
