---
title: "Connect Confluence"
---
Connect selected Confluence global spaces so agents can search team documentation. Private spaces and pages with viewing restrictions are excluded, including descendants of a restricted page.

## Choose the account and spaces

1. Use a designated administrator with Counso admin access and access to the required Confluence global spaces.
2. Open **Spaces > Connections**, select Confluence, and complete authorization.
3. Select the global spaces to synchronize and save.

Keep this account as the connection owner. Reauthorizing with a different account can change which content remains accessible. You can add or remove selected global spaces without resetting the whole connection.

## Update the connection

Open the existing connection to change the space selection or renew authorization. Before changing the connecting account's permissions, check whether an agent depends on the affected content. Selecting a space does not override page-level viewing restrictions.

Changes in selected spaces can appear within seconds or minutes; the connection also checks for new and updated content approximately hourly. When a page is missing, check its space selection, restrictions on the page and its parents, the connected account, and the last sync.

## Search with labels

Confluence's custom label names are included with synchronized documents and can be used by the [knowledge search tool](/docs/user-documentation/agents/knowledge/search-data-sources). Use the readable label name, such as `deprecated`, rather than an old numeric label identifier.
