> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Why isn't my recently updated document showing in agent responses?

If you updated a document but the agent isn't using the new information, here's how to diagnose:

## Check sync timing

1. Verify when the document was last updated
2. Check how long ago the connection last synced (admins only: `Spaces` > `Connection Admin`)
3. Wait for the appropriate sync interval:
   * **Notion**: 15-30 minutes
   * **Google Drive**: 30-60 minutes
   * **Slack**: Within minutes
   * **Confluence**: 1-2 hours

## Verify the document is actually synced

**As an admin:**

* Go to `Spaces` > `Connection Admin` > Select connection > `Manage`
* Navigate to the document in the hierarchy
* If it's not listed, it wasn't selected for syncing

**As a member:**

* Go to `Spaces` > Select space > `Connected Data`
* Look for your document in the list
* If not visible, ask your admin to add it

## Force a conversation refresh

After data has synced:

* **Start a new conversation** - agents don't automatically refresh data mid-conversation
* Old conversations use a snapshot of data from when they started

## Check document format

Some content isn't indexed:

**Notion:**

* External files not indexed
* Content behind URLs not indexed
* Databases must be in table format

**Google Drive:**

* Files over 1MB extracted text not indexed
* Images in documents not read
* Shortcuts to documents not followed

**Slack:**

* External files not indexed
* URLs not indexed
* Workflow messages not indexed

See full limitations: [Connections Management - What kind of data cannot be read](/docs/user-documentation/data-sources/connections#what-kind-of-data-cannot-be-read-by-my-agents)
