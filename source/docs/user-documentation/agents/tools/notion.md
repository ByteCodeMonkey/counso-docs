> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Notion

## Overview

Connect Notion to Dust agents to read documents, search your workspace, and write new content.

This document provides general information about our Notion tools (available tools, setup, and authentication).

## Setting up the Connection

The setup process **requires a Notion Admin** who is also a Dust Admin. This ensures full access to the necessary pages and databases that need to be shared with Dust. Follow these steps:

1. Under **Spaces** > **Tools**, select **Add Tools**. Then select **Notion**.
2. A modal will show to allow you to select the data you want Dust to have access to.

**Managing Permissions**

* Use Notion's **Top Page selection** to share entire sections that are 100% sharable.
* Apply a more **granular approach** for sensitive pages.
* Selecting a page will give Dust the permission to read and write to the page.

<Warning>
  **Permissions:** Each connection reflects the permissions of the last user to
  set it up. To prevent disruptions, avoid changing the designated admin or
  their permissions in Notion without reviewing the impact on Dust.
</Warning>

## Adding Notion Tools to Agents

After admin set-up, Notion tools can be added to an agent by selecting them in the agent builder. They require no configuration. Note that when connecting a tool, you can define the provided tools as high stake or low stake.

## Available Tools

### Page Operations

| Tool                 | Description                                                                                                                                                                                                 |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Create Page**      | Create a new Notion page.                                                                                                                                                                                   |
| **Retrieve Page**    | Retrieve a Notion page by its ID.                                                                                                                                                                           |
| **Update Page**      | Update a Notion page's properties.                                                                                                                                                                          |
| **Add Page Content** | Add a single content block to a Notion page. For multiple blocks, call this action multiple times. Supports child-containing blocks: page, toggle, to-do, bulleted list, numbered list, callout, and quote. |

### Database Operations

| Tool                          | Description                                                                                                                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Create Database**           | Create a new Notion database (table).                                                                                                                                        |
| **Query Database**            | Query a Notion database.                                                                                                                                                     |
| **Retrieve Database Schema**  | Retrieve a Notion database's schema by its ID.                                                                                                                               |
| **Retrieve Database Content** | Retrieve the content (pages) of a Notion database by its ID.                                                                                                                 |
| **Insert Row Into Database**  | Create a new Notion page in a database.                                                                                                                                      |
| **Update Row Database**       | Update a specific property value in a row (page) of a Notion database. Value formats depend on the property type (text, number, select, date, people, URL, files, checkbox). |
| **Update Schema Database**    | Update the schema (columns/properties) of an existing Notion database.                                                                                                       |

### Block Management

| Tool                        | Description                                                                                                           |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Retrieve Block**          | Retrieve a Notion block by its ID.                                                                                    |
| **Retrieve Block Children** | Retrieve the children of a Notion block or page by its ID.                                                            |
| **Delete Block**            | Archive (delete) a block, page, or database in Notion. Moves the block to 'trash' where it can be restored if needed. |

### Search & Discovery

| Tool       | Description                                       |
| ---------- | ------------------------------------------------- |
| **Search** | Search for pages, databases, or blocks in Notion. |

### Comments & Collaboration

| Tool               | Description                                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Create Comment** | Create a comment on a Notion page or in an existing discussion thread. Requires parent page ID or discussion ID. |
| **Fetch Comments** | Retrieve a list of unresolved comment objects from a specified page or block in Notion.                          |

### User Management

| Tool               | Description                                      |
| ------------------ | ------------------------------------------------ |
| **List Users**     | List all users in the Notion workspace.          |
| **Get About User** | Get information about a specific user by userId. |
