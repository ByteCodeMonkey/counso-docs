# Attio

Attio's hosted MCP server lets an Agent search and manage CRM records, including people, companies, deals, tasks, notes, meetings, calls, and emails. Authentication uses OAuth; actions run with the connected user's Attio access.

## Connect Attio

In the current tool configuration flow, add a remote MCP server at `https://mcp.attio.com/mcp` and choose the available OAuth option. Share the tool only with the Spaces that need it, then add it to the intended Agent. The exact authorization fields and callback are supplied by the connection flow; complete consent as the user whose Attio identity should act.

Useful first checks include `whoami` to confirm the connected identity, `list-attribute-definitions` to inspect fields, and a search for one known record. Available operations may include creating and updating records or tasks, so limit write actions to users and Spaces with an approved business need. If the server connects but its tools do not appear, re-open the server's sharing settings and confirm the Agent's Space has access.

## Available operations

The tool list includes `search-records`, `get-records-by-ids`, `create-record`, `upsert-record`, `list-attribute-definitions`, note creation and search, meeting and call recording search/retrieval, email search/content retrieval, workspace member/team lists, and `whoami`. Record creation, upsert, and note creation change CRM data; keep those operations limited to the appropriate Agent and review owner.
