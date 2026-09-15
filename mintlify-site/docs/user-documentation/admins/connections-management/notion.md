---
title: "Connect Notion"
---
The Notion connection indexes selected pages and databases. Set it up with a designated administrator who can administer both Counso and the relevant Notion workspace. The account must retain access to the pages and teamspaces you want to synchronize.

## Connect the workspace

1. Open the Notion connection in **Spaces > Connections**.
2. Authorize the connection with the designated Notion account.
3. Select the pages to share. Choosing a top-level page includes its accessible descendants; select sensitive sections individually when appropriate.
4. Save the selection and allow the initial synchronization to finish. Large workspaces can take several days.

The connection reflects the permissions of the account used to configure it. Replacing it with another person's authorization may change the existing scope. Review the connection before switching accounts or removing page access.

## Add or remove pages

Manage subsequent page access in Notion. Open a page's **...** menu, choose **Connect to**, and select the installed Counso integration. Ensure the connection owner has at least commenting access and can see the integration under that page's connections while signed in with the correct account.

New top-level pages are checked daily. New child pages and edits within an already connected page usually synchronize within seconds or minutes. Changes still need to pass through indexing before an agent can retrieve them.

## Restore a missing page

Check the page's integration access, the connecting account, and the parent hierarchy. Pages connected without their parent pages can appear under **Orphaned Resources**. Connect the appropriate parents when you want the original hierarchy to appear.

A restricted teamspace or independently restricted page can prevent synchronization. In Notion's **Share** panel, look for permissions unlinked from the parent. **Reset to inherited permissions** is useful when the page should have the same audience as its parent; review the resulting access before applying it.

In Notion settings, inspect the integration's connections for overlapping authorizations from different people. Keep the intended connection and review any removal with its owner, rather than repeatedly replacing the connection to fix a single missing page. If an authorized page is still missing after the next daily check, give your workspace administrator its URL and the connection details.

## Databases and labels

Databases containing multiple Notion data sources are not supported by this connection. Keep each data source in a separate database when it needs to be synchronized.

Custom labels from database pages are included with the indexed document. Author and last-editor labels use forms such as `author:Alex Tan` and `lastEditor:Mei Lim`. They can narrow [knowledge searches](/docs/user-documentation/agents/knowledge/search-data-sources). Update and resynchronize an older page if its current labels are missing.
