> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Notion

<Danger>
  **Heads up**

  Ensure to do the Initial Connection Setup once and then Manage the Connection by adding or unselecting pages directly from Notion.
  The recommended approach to creating a Notion Connection is to provision a user [dust-admin@yourdomain.com](mailto:dust-admin@yourdomain.com) in your Google workspace and use that identity to connect Dust to your various data sources. The IT/CISO/(name the right function here) will update Dust data access using that account.
  You will have to ensure that this new 'admin user' has access to the pages/teamspaces that you want to connect.
  This will help them control what Dust has access to by managing the permission of that account on Notion.
  If you cannot locate a specific Notion page in Dust, add it directly through Notion. To guarantee proper indexing and organization, link all parent pages to reestablish the page hierarchy.
  Notion connections are unique per user, and replacing an existing connection with a new user's permissions disrupts the current data access.
</Danger>

Dust integrates with Notion to bring your workspace's pages and databases into Dust, so agents can search and use that content. Due to permission restrictions, only Notion Admins can set up this connection.

### Initial Connection Setup

<Info>
  **User provisionning**

  The recommended approach to creating a Notion Connection is to provision a user `dust-admin@yourdomain.com` in your Google workspace and use that identity to connect Dust to your various data sources. The IT/CISO/(name the right function here) will update Dust data access using that account.
  You will have to ensure that this new 'admin user' has access to the pages/teamspaces that you want to connect.
  This will help them control what Dust has access to by managing the permission of that account on Notion.
</Info>

The setup process **requires a Notion Admin** who is also a Dust Admin. This ensures full access to the necessary pages and databases that need to be shared with Dust. Follow these steps:

1. A Notion popup to give Dust your Notion workspace data (Teamspace selection).
2. A modal to select the exact data you want to sync with Dust.

**Managing Permissions**

* Adopt a **shared-by-default** approach: share everything except for the data you want to exclude from Dust.
* Use Notion's **Top Page selection** to share entire sections that are 100% sharable.
* Apply a more **granular approach** for sensitive pages, which will be classified under an Orphaned Pages folder in Dust.

<Danger>
  **Permissions**

  Each connection reflects the permissions of the last user to set it up. To prevent disruptions, avoid changing the designated admin or their permissions in Notion without reviewing the impact on Dust.
</Danger>

### Updating the connection

* From Notion, navigate to the settings or page you wish to connect.
* Select the `...` option, then choose `Connect to` and select `Dust`.

<Danger>
  **Missing pages**

  Notion API isn't designed to ease sync with 3rd parties; some pages you think should be indexed can be missing.
  Should a Notion **page remain missing in Dust a few hours after direct addition**: to guarantee proper indexing and organization, link all parent pages to reestablish the page hierarchy and check the permission of the page.
  **Check for unlinked share settings:** A Notion page may not sync if its share settings are unlinked from its parent page

  1. Open the page in Notion
  2. Click **Share**
  3. Look for "Share settings on this page are unlinked from the parent page" button
  4. Click the three dots (`...`) menu
  5. Select **Reset to inherited permissions**
     See the Best Practice section below.
</Danger>

* **For new top pages:** Refresh occurs once daily.
* **For new pages within a synced top page or changes in an already synced page:** Refresh is immediate, with a few seconds to minutes latency.

<Danger>
  **Large workspaces**

  Large Notion workspaces can take several days for the initial sync. Plan accordingly and monitor the process.
</Danger>

* **Restrict Permission Management:** To avoid accidental data access changes, limit the ability to manage Notion permissions to a single identified admin.

* **Check if the page or Teamspace is restricted:** Ensure the page or Teamspace is not restricted, otherwise Dust wont be able to index the data. If the Notion Teamspace is restricted, then all the child pages are as well.
  Note: when everyone has access to the page but not in full access, the page is considered as restricted. The eye icon at the top of the Notion page can help you identify whether a page is restricted or not.

* **Admin Role Consistency:** Ensure the designated admin has appropriate roles in Notion and Dust, with access to all necessary data.

* **Orphaned Resources:** Be mindful when adding pages without top pages to avoid misclassification under Orphaned Resources in Dust.

* **Avoid Multiple Notion Connections:** Ensure the designated admin is the only person to have a connection with the Dust app in Notion. Go to `Setting & member` > `Connections` > `All connections`. If you see `your name +X`, click on `...`and delete all connections except from your admin connections.

## Notion FAQ

### **How to correctly share a page with Dust**

For a page to be shared with Dust, two conditions need to be true:

1. The user who created the connection (whether it's an admin or a [dust-admin@yourdomain.com](mailto:dust-admin@yourdomain.com) account) needs to have at least commenting access to that page.
2. When logged in to Notion as the user who created the connection, you need to see the black Dust icon under '...' / Connections. Note that you may not see Dust there if you're logged in as a different user, and that is normal.

### **Why do I see pages in Orphaned Resources?**

When adding pages to Dust without their respective top pages, these get categorized as "Orphaned Resources" within Dust. This helps identify and manage pages that might not fit into the general hierarchy but still require syncing.

### I added/deleted a Page or a Database, and I can’t/still see it.

Dust performs synchronization tasks based on the setup and permissions granted by the Notion Admin. The refresh rate varies depending on the type of content, its size, the size of the Notion workspace, and its location within the Notion workspace.

As an admin, go to the page and check Dust is connected.

From Notion, select the `...` option (top right), then choose `Connect to` and select `Dust`. Read [the guide here](/docs/user-documentation/admins/connections-management/notion#updating-the-connection).

If the page is connected but you can’t see it 24 hours later:

* ping Dust at [support@dust.tt](mailto:support@dust.tt);
* [write an email to Notion](https://www.notion.so/Notion-Email-Template-3d9baee6c99140cebb8fa41f52fe66f5?pvs=21). This will help nudge them to improve their APIs to ensure their users can use third-party applications.

By following these guidelines, you can ensure a smooth integration between Dust and Notion, allowing for efficient data sharing and collaboration across your teams.

### Database with multiple data sources are not supported

This is a feature that Notion added in October 2025 ([https://www.notion.com/help/data-sources-and-linked-databases](https://www.notion.com/help/data-sources-and-linked-databases)), and Dust does not support it. If syncing these with Dust is important to you, it's best to keep each datasource as a separate database.

## Labels

Dust syncs the custom labels set on the pages from Notion databases and includes them in the documents synced above the content itself. It also automatically adds a label with the name of the author and last editor of the document in `author:Firstname LastName` and `lastEditor:Firstname LastName`.

**Labels**  allow for additional filtering on data sources selected on the [semantic search](/docs/user-documentation/agents/knowledge/search-data-sources) tool.

<Info>
  **Labels support was added Feb 13 2025**

  Notion pages that have been synced before this date won't have those labels available for filtering. If you update the pages, then the labels will be synced on the next sync in Dust.
</Info>
