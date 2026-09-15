> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Dust provides the ability for LLMs to access **knowledge bases** in order to make their answers more relevant. This is done via **data sources**.

There are various types of Data Sources:

* **Connections:** your main communication and knowledge tools (e.g. Google Drive, Notion, Slack, etc.), they get synchronized automatically, so Dust can always have access to recent information.
* **Tools:** access information from third-party systems (Slack, Salesforce, Gmail, Hubspot, Stripe, Linear etc) via MCP servers.
* **Public Websites:** ingest data from public websites (e.g. docs.dust.tt) with our web crawler, which you can refresh at the cadence you want.
* **Folders:** store static information in a folder, just like you would on your computer.
* **Conversation Files:** dynamically created under the hood when you upload files, behave like if you had created a folder for a specific conversation and stored the files in it.
* **Custom Connections**: connections you can build yourself using our API or already-made scripts.

If you want to add a tool as a Connection, ask your admin to look for [Connections Management](/docs/user-documentation/data-sources/overview)
