---
title: "Miro"
---
Miro MCP connects an Agent to boards and board content that the authorized user can access. It can read board content, generate diagrams, and work with visual objects according to the provider's current tool set. The remote MCP service is operated by Miro; consult [Miro's MCP documentation](https://developers.miro.com/docs/miro-mcp) for provider-side capabilities and support.

An administrator adds **Miro MCP** from **Spaces → Tools → Add Tools** and completes Miro's OAuth 2.1 flow. For an Enterprise organisation, a Miro administrator must first enable the MCP server at the organisation level. Share the tool with the intended Space and add it to an Agent.

Start with a board the connected user can open. Ask the Agent to identify the board and inspect its existing items before creating or editing content. If no boards appear, check Miro organisation settings, board sharing, team membership, and the OAuth identity.
