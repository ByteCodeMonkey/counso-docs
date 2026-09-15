> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Folders

In Dust, Folders organize and manage data sources other than connections or websites. Once added to a Folder, the data sources can be plugged into custom agents using tools.

There is no number of files limit to a Folder.

**Admins** and **builders** have the capability to add Folders by navigating to **Spaces > Folders** in the Dust interface.

## 1. Docs

Upload pdf/text files and have your agent use them as inputs using the [Search data sources](/docs/user-documentation/agents/knowledge/search-data-sources), [Most recent data](/docs/user-documentation/agents/knowledge/include-data), [Extract data](/docs/user-documentation/agents/knowledge/extract-data).

Note: PDFs are turned into text before being added to the folder. Tables and images will not properly be extracted.

## 2. Tables

Upload CSV files that you can then analyze using the Table queries  tool in custom agents.

Both file types can be automatically pushed to a folder using the [Dust API](/docs/developer-platform/overview/developer-platform) or using the [Zapier integration](/docs/user-documentation/data-sources/custom-connections/zapier-automatically-add-datasource). Learn more about it in [Custom connections](/docs/user-documentation/data-sources/overview).

* Documents up to 30MB can be uploaded manually via Folders and 10MB directly in the conversation.
* By default, the folders will not be used by the generic **@dust** admin. You can change this from the **@dust** agent settings.
* There is no number of files limit to a Folder.
* Having a detailed description can help your agents understand what is included in your data source, which can increase its accuracy.
