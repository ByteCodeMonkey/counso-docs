> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Developer platform

Dust is a platform powered by the top frontier models on the market, from providers including OpenAI, Anthropic, Google, and Mistral, alongside open-source models. It's designed to help teams work better with AI: agents help anyone in the company answer questions in your company's context, draft documents, analyze data, and act in connected systems.

Our mission: we think people don't get up to go to work to use the enterprise search portal or to have a better knowledge solution but to get stuff done. We build Dust to make work work better. You can [read more here](https://blog.dust.tt/2023-05-11-work-doesnt-work).

The developer platform lets you build on Dust programmatically through the [Dust API](/docs/developer-platform/dust-api-documentation/openapi-and-postman), the [JavaScript SDK](/docs/developer-platform/overview/javascript-sdk), and the [Dust CLI](/docs/developer-platform/dust-cli/dust-cli).

### Agents

An agent combines a model with instructions, tools, and company knowledge. Every workspace includes the default `@dust` agent, and members can build [custom agents](/docs/user-documentation/agents/create-your-first-agent) for specific tasks, like answering support questions or generating SQL from company data. Several agents can work together in the same conversation.

### Models

Every agent runs on a model. The [model picker](/docs/user-documentation/agents/model-selection) offers specific models from each provider plus three auto models (Basic, Standard, Premium) that Dust benchmarks and keeps up to date. Admins can restrict which models members can use with [model access tiers](/docs/user-documentation/admins/usage-seats-and-credits/model-access-tiers).

### Conversations

You interact with agents through conversations, where you ask questions or make requests. Share a conversation to let colleagues join and work with you and the agents. Create a new conversation for each new topic to keep agents focused.

### Workspaces

A workspace is where members talk to agents and customize Dust for their team's needs. Admins invite members, assign roles (Admin, Manager, Member), and organize data access through open or restricted [spaces](/docs/user-documentation/admins/spaces-management).

### Data sources

Data sources make company knowledge available to agents:

* **Connections**: managed integrations (Google Drive, Notion, Slack, Confluence, and more), synced automatically.
* **Tools**: access and act on third-party systems (Slack, Salesforce, Gmail, HubSpot, and more) via MCP servers.
* **Public websites**: content ingested with the Dust web crawler.
* **Folders**: static documents and tables, uploaded manually or by API.
* **Custom connections**: connections you build yourself with the Dust API or ready-made scripts.

Learn more in the [data sources overview](/docs/user-documentation/data-sources/overview).

### Synchronizing

[Connections](/docs/user-documentation/data-sources/connections) sync automatically, and updates usually appear in Dust within a few minutes. Admins have granular control over what is synced, down to specific Slack channels, Google Drive folders, or Notion pages.

### Retrieve

Agents retrieve information from data sources using [Knowledge](/docs/user-documentation/agents/knowledge/index) tools:

* **Search**: semantic search across selected data sources (RAG).
* **Include data**: include documents exhaustively, most recent first, up to the context window limit.
* **Query tables**: turn a question into a SQL query against structured data.
* **Extract data**: pull structured information following a schema you define.
