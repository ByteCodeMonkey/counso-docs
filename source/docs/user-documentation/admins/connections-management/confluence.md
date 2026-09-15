> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Confluence

<Danger>
  **Heads up**

  The initial user’s Confluence permissions bind the synchronization between Dust and Confluence. If permissions are edited by another user, the synchronization scope may change, potentially breaking connections to data no longer in the new user's scope.
  Dust does not ingest private spaces. Dust does not access pages with view limitations and will not capture any content from a restricted page. This restriction also applies to all the child pages of such pages.
</Danger>

Dust synchronizes with Confluence to bring your workspace documentation into Dust, enabling easy access and retrieval of information directly through your Dust workspace.

## Initial Connection Setup

To connect Confluence with Dust:

1. **Identify an Admin**: Choose an admin with comprehensive access to Confluence global spaces and also a Dust admin. This ensures a broad and relevant data scope for synchronization.

2. **Connect to Confluence**: Navigate to `Spaces` > `Connections` in Dust, select Confluence, and follow the prompts to authenticate and grant Dust access to Confluence.

3. **Select Global Spaces**: During the connection setup, the admin can choose which global spaces in Confluence to synchronize with Dust. Only those selected will be accessible in Dust.

<Danger>
  **About the admin user**

  Dust recommends using a single, identified admin (or a virtual user like [**dust@workspace.com**](mailto:dust@workspace.com)) for managing Confluence permissions to ensure consistent access and avoid accidental permission overwrites.
</Danger>

### Managing Permissions

To manage or update the permissions:

* **Add/Remove Global Spaces**: The identified admin can add or remove global spaces for synchronization in Dust without resetting the entire connection.

## Updating the Connection

If you need to update the connection, such as adding more global spaces or changing the admin permissions, follow the same steps under Initial Connection Setup. Remember, changes in permissions might affect the data scope available in Dust.

* **Scope**: Dust synchronizes content from the selected global spaces in Confluence. Private spaces and pages with view restrictions are not included.

* Limit permission management to a single identified admin to maintain consistent synchronization scope.

* Regularly review and update the selected global spaces to ensure the most relevant and up-to-date information is available in Dust.

## Refresh and Sync Details

* **Immediate Sync**: Changes within selected global spaces are synchronized with Dust almost immediately, with a slight latency of a few seconds to minutes.
* **Hourly Check**: Dust checks for new or updated content in Confluence approximately every hour to ensure data freshness.

## Labels

Dust syncs the custom labels set on Confluence and include them in the document above the content itself.

**Labels** allow for additional filtering on data sources selected on the [semantic search](/docs/user-documentation/agents/knowledge/search-data-sources) tool.

<Info>
  **Labels support was added Feb 13 2025**

  Prior to that, the labels we were syncing were based on the label id (ex: "labels:36077569") and we now sync the name of the labels without prefix (ex: "deprecated").
</Info>
