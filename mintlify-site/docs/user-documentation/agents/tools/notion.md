---
title: "Notion"
---
The Notion tool lets an Agent search pages and databases and, where permitted, create or update pages, database entries, blocks, and comments. Search results are limited to the pages and databases shared with the connected Notion integration and authorized identity.

An administrator adds Notion from **Spaces → Tools → Add Tools** and completes the provider authorization. In Notion, share the specific pages or databases the integration should access; workspace membership alone does not grant access to every page. Share the configured tool with the intended Space and add it to the Agent.

Start with a search for a known page and confirm the page path. For database work, inspect the database properties before creating or updating an entry. When editing page blocks, preserve existing content and read the page back afterward. If a page is missing, check that it was explicitly shared with the integration and that the connected account can open it. Keep write actions limited to the pages and databases the Agent needs.

## Available operations

Notion operations cover page creation/retrieval/update and content insertion; database creation, schema retrieval, querying, content retrieval, and row insert/update; block retrieval, child listing, and deletion; search; comments; and user/about-user lookup. Page and database sharing is configured in Notion itself. A database may be visible while a specific page or block is not, so check the target sharing boundary before expanding tool access.
