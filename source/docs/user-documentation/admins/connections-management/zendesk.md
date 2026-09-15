> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Zendesk

At the moment, Dust is able to sync **Help Center Articles** and **Tickets**.

<Info>
  **Zendesk extension**

  We also have a Dust extension available on the Zendesk marketplace that enables access to Dust agents by your support team directly within Zendesk. Check out the documentation at [Zendesk extension](/docs/user-documentation/admins/connections-management/zendesk).
</Info>

This page talks about importing Zendesk data to Dust. If you want to install the Dust Zendesk app, please visit this article: [Dust in Zendesk](/docs/user-documentation/admins/connections-management/zendesk)

Setting up the Zendesk connection involves the following steps that must be completed by an individual with admin rights on both Dust and Zendesk (in *Support* and *Guide* at least).

1. On dust.tt, navigate to **Spaces** > **Connections** and select Zendesk in the list.

2. Enter the subdomain of your Zendesk instance, it can be found in every Zendesk URL: https\://**subdomain**.zendesk.com/agent/dashboard.

3. Authenticate on Zendesk, you will then be redirected to Zendesk in order to give Dust access your Zendesk instance data (only data from *Support* and *Guide*).

4. The connection should appear under **Spaces > Connections**. You can then manage the connection by selecting the exact data you want to sync with Dust.

Dust modal to select the data you want to sync with your Dust workspace.

<Info>
  **How to check if you are an admin in Zendesk**

  1. Click on your profile picture/icon in the top right corner of your Zendesk interface
  2. Select "View Profile"
  3. Look at your role information - it will show whether you are an: Admin, Agent, End-user, Light agent or Custom role (Enterprise accounts only).
</Info>

### Permission granularity: Brands

When setting up the connection you can select individual Brand’s Tickets or select whole Brands, which will select their Tickets and Help Center.

### Tickets synced in a Brand

By default, we synchronize only the tickets meeting all the following conditions:

* were last updated **in the past 180 days.**
* are **solved** or **closed**.

### Sync Options

These options can be turned on in **Spaces** > **Connections** > **Zendesk** > **Manage**.

#### Sync Unresolved Tickets

If activated, Dust will also sync tickets that are not yet solved or closed. Be aware that enabling this option will significantly increase the number of tickets synchronized, which may slow down the sync and potentially add noise to agent responses.

***

#### Hide Customer Information

Enable this option to prevent customer names and email addresses from being synced with Dust. This does not impact the data *within* tickets, only the metadata attached to tickets (e.g. requester name, email).

***

#### Data Retention Period

Set the retention period in days. Tickets older than the configured period will not be synced with Dust and will be cleaned on a daily basis. The default retention period is 120 days.

***

#### Ticket Tag Filters

Configure tags to include or exclude specific tickets from the sync based on their Zendesk tags.

* Add **Included** tags to sync *only* tickets that have those tags.
* Add **Excluded** tags to filter out tickets that have those tags.

<Warning>
  These filters only apply to **future syncing** and will not retroactively remove already-synced tickets.
</Warning>

***

#### Organization Tag Filters

Configure tags to include or exclude tickets based on the Zendesk organization they are associated with.

* Add **Included** tags to sync only tickets from organizations with those tags.
* Add **Excluded** tags to filter out tickets from organizations with specific tags.

<Warning>
  These filters only apply to **future syncing** and will not retroactively remove already-synced tickets.
</Warning>

***

#### Custom Field Tags

Configure custom Zendesk ticket fields to be included as tags when syncing tickets. Custom field values will be added as labels in the format `fieldName:value`, making them available for filtering in Dust's [semantic search](/docs/user-documentation/agents/knowledge/search-data-sources) tool.

To add a custom field:

1. Find the numeric ID of the custom field in your **Zendesk Admin** settings under **Fields**.
2. Enter the ID in the input and click **Add Field**.

<Info>
  Custom field tags follow the same `fieldName:value` format as other Dust labels and can be used to filter data sources on the semantic search tool.
</Info>

***

#### Rate Limit Transactions Per Second

Set a transaction-per-second (TPS) limit to manage Zendesk API rate restrictions. This is useful if your Zendesk plan has strict API rate limits and you want to avoid hitting them. Leave this field empty (disabled) to apply no rate limit.

### Data synced in a Ticket

We synchronize the following in a ticket:

* All the **comments** of the ticket (with the **author**’s name and email address for each).
* The list of **tags** attached to the ticket.
* The **priority**, **type**, **channel**, **organization** ID, **group** ID, **satisfaction** rating and comment and the**due date** of the ticket.

### How fresh is the Data in Dust?

If you select a **Brand** or only it’s **Tickets** we immediately launch an action to sync the added data. This can take up to a few minutes to complete, depending on the amount of tickets to process.

When a new ticket is solved or deleted in a Brand you’ve selected, it takes up to 30 min to be synced with Dust.

Outdated tickets (older than the retention period) and tickets that were unselected in the UI are cleaned on a daily basis.

<Danger>
  **Quantitative use-cases**

  The connection is tailored around qualitative analyses such as retrieving key information inside tickets based on semantic meaning. As of now quantitative questions such as *how many tickets about X topic have been assigned to Y* are not supported out of the box (but could be in the future, stay tuned!).
</Danger>

## Sync of Help Center articles

### **Permission granularity: Brands and Categories**

When setting up the connection you pick from the list of Categories in your Help Center that you want to sync with Dust or can select whole Help Centers. Selecting a Brand will automatically select its Help Center and Tickets.

### Articles synced in a Category or Help Center

We synchronize the articles that are published if they belong to either a selected Category or a selected Help Center.

### Data synced in an Article

We synchronize the following in an article:

* The **title** and **body** of the article.
* The **category**’s name and description.
* The **section**’s name and description.
* The **author**’s name and mail address.
* The **labels** attached to the article.
* The sum of upvotes (+1) and downvotes (-1).

### How fresh is the Data?

If you select a **Category**, **Brand** or only its **Help Center** we immediately launch an action to sync the added data. It can take up to a few minutes to be completed, depending on the amount of articles to process.

If a new article is published on either a selected **Category** or **Brand** **Help Center**, it can take up to 30 min to be available on Dust. Note that this means that if you wish to sync newly created **Categories**, you should select the whole **Help Center**.

Articles that were unselected in the UI or deleted in Zendesk are cleaned on a daily basis.

<Info>
  **Hiding names and email addresses**

  By default the names and email addresses of the users involved in a ticket or an article are included in the synced metadata, making them available to Dust agents.
  This option can be disabled in **Spaces** > **Connections** > **Zendesk** > **Manage**.
  :warning: Doing so will result in the agents having no knowledge of who the users are.
</Info>

## Labels

Dust syncs the custom labels (tags) set on tickets in Zendesk and include them in the document above the content itself. It also automatically adds those labels:

* `priority`
* `ticketType`
* `channel`
* `status`
* `groupId`
* `organizationId`
* `dueDate`
* `satisfactionRating`
* `hasIncidents`

**Labels**  allow for additional filtering on data sources selected on the [semantic search](/docs/user-documentation/agents/knowledge/search-data-sources) tool.
