> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Miro

## Overview

Miro MCP is a remote MCP server provided by Miro that allows your Dust agents to interact directly with your Miro boards.

<Info>
  **Remote MCP Server:** Miro MCP is a **remote MCP server** provided and
  maintained by Miro, not by Dust. Dust does not provide support for this
  integration. For any issue, question, or feature request related to Miro MCP,
  please contact **Miro directly** or refer to the [official Miro MCP
  documentation](https://developers.miro.com/docs/miro-mcp).
</Info>

Miro MCP connects your Dust agents to your Miro boards via the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro), an open standard for AI tool interoperability. It enables agents to read board content, generate diagrams, and interact with your visual workspace.

## Admin: Setup in Dust

Navigate to **Spaces > Tools** in your Dust workspace, click `Add Tools`, and select **Miro MCP**.

The setup uses **OAuth 2.1** to authenticate against Miro's hosted MCP server. Once connected, the tool is added to your Space and becomes accessible to agents in that Space.

<Warning>
  **Miro Enterprise Plan:** If your organization is on Miro's Enterprise plan,
  an admin must first enable Miro's MCP Server for the org before it can be
  used. See [Miro's Admin
  guide](https://help.miro.com/hc/en-us/articles/31625761037202-Miro-MCP-Server-admin-guide)
  for details.
</Warning>

## Usage

In the **Agent Builder**, click `Add Tool` and select **Miro MCP**.

Agents will be able to read and write to the Miro boards accessible from the connected account.

## List of tools

For the full and up-to-date list of tools and their capabilities, refer directly to the **[Miro MCP documentation](https://developers.miro.com/docs/miro-mcp)**.

## Support

<Warning>
  **Dust does not provide support for Miro MCP.** This is a remote MCP server
  operated by Miro. If you encounter issues or need help, please refer to the
  [Miro MCP documentation](https://developers.miro.com/docs/miro-mcp) or contact
  Miro support directly
</Warning>
