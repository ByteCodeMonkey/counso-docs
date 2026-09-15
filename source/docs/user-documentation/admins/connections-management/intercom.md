> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Intercom

At the moment, Dust is able to sync **Help Center Articles** and **Conversations**.

Setting up the Intercom connection involves two steps that must be completed by an individual with admin rights on both Dust and Intercom (need the “Can install, configure and delete apps” right on Intercom):

1. An Intercom popup to give Dust your Intercom workspace data (only conversations, teams & teammates & Help Center data).
2. A modal to select the exact data you want to sync with Dust.

Intercom Authorization popup.

Dust modal, to select the data you want to sync with your Dust workspace.

<Danger>
  **Waiting time**

  We know the Permission modal is quite long to set up the first time you click on Save, we’re working on making it faster!
  **Permission granularity: All conversations OR by picking Teams**
</Danger>

When setting up the connection you pick the list of Teams that you want to sync with Dust. You can either pick “Conversations” to have us sync all conversations from your Intercom workspace, or select some Teams. If you select Teams, we will only sync conversations that are attached to one of the selected Teams.

### Conversations synced in a Team

We synchronize only the conversations meeting all the following conditions:

* were opened in the past 90 days,
* are closed,
* are attached to one of the a selected teams (unless you selected all conversations).

### Data synced in a Conversation

We synchronize the following in a conversation:

* All the **messages and notes** of the conversation (with the name of the **author** for each),
* The list of **tags** attached to the conversation,
* The **source** of the conversation.

You can decide to not sync the Notes from the Connection configuration page.

### How fresh is the Data in Dust?

If you add or remove a Team we immediately launch an action to either sync the new data or remove the one you don’t want to share anymore. This can take a few minutes to complete, depending on the amount of conversations.

When a new conversation is closed in a Team for which you’ve given us access, we get notified within a few seconds by Intercom and process the new closed conversation immediately.

### **Permission granularity: Top-level Collections**

When setting up the connection you pick the list of top-level Collections in your Help Center that you want to sync with Dust. We only sync articles that are published within one of the selected Collections.

### Articles synced in a Collection

We synchronize the articles that are in state **published** in one of the selected **collections**.

### Data synced in an Article

Nothing fancy, we synchronize the title and content of the article.

### How fresh is the Data?

If you add or remove a Collection we immediately launch an action to either sync the new data or remove the one you don’t want to share anymore. It can take a few minutes to be completed, depending on the amount of articles.

Otherwise, data is refreshed every hour. If a new article is published on your Help Center, it can take up to one hour to be available on Dust.

## Labels

Dust syncs the custom attributes set on Intercom conversations (as `attribute:name:value`) and their tags (as `tag:name`.

**Labels**  allow for additional filtering on data sources selected on the [semantic search](/docs/user-documentation/agents/knowledge/search-data-sources) tool.
