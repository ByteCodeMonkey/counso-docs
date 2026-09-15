> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Table queries

Table queries enable agents to generate and execute SQL queries on structured data before replying (Snowflake, BigQuery, CSVs, Notion Databases, Google Sheets). This comes as complement of the Search Data Source agent action which generally falls short on quantitative questions (semantic search presents chunk of data ordered by pertinence to the agent that make it impossible for the agent to properly answer quantitative questions since it does not have access to the entire data). Instead Table Queries allow the agent to query these structured data sources using SQL (query language), enabling the agent to answer analytical questions.

There are multiple ways to use Table Queries:

* On Tables manually created in **Folders (CSV upload, or API)**
* On Tables automatically discovered by Dust from **Google Drive (Sheets)**, **Notion (Databases)**, **Microsoft (Sheets)**, **Snowflake**, **BigQuery** (beta)
* On Tables uploaded in the conversation (**CSV upload**).

Table queries are suited for quantitative questions. Conversely to semantic search, they are not suited for questions on unstructured / raw text data. Both actions (Data Source Search and Table Queries) should be use complementary based on your use-case.

## Example

| cars       | production\_year | color | description                                           |
| ---------- | ---------------- | ----- | ----------------------------------------------------- |
| toyota     | 2001             | red   | Perfect car for young people who love the city        |
| mercedes   | 2004             | red   | perfect car if you love fancy things                  |
| volkswagen | 2008             | blue  | a great car if you like the countryside               |
| renault    | 2012             | brown | ideal car if you like going to your local repair shop |
| citroen    | 2020             | green | a great car if you don’t like cars                    |

The following question is **well suited** for a Table Query but poorly suited for Data Source search:

What is the most common color for cars produced between 2000 and 2010 ?

The following question is **poorly suited** for a Table Query but well suited for Data Source search:

What is the best car to buy if I live in NYC ?

## Creating agents with Table Queries

When creating or editing an agent, in the `Action & Data sources` section select `Add a tool` with the `Query Tables` method.

Select one or more tables that you would like your agent to use.

### Joining tables together (advanced)

Agents have the ability to use data from multiple tables at once, and even join tables together, even if the tables come from different data sources.

To enable this, you can simply pick several tables when creating your agent.

If you want your agent to join data between tables, it is useful to explain how to join the tables in the agen's instructions.

Consider this example with a `users` table and an `orders` table:

| name        | email                               |
| ----------- | ----------------------------------- |
| john powell | [john@acme.co](mailto:john@acme.co) |
| tom peralta | [tom@acme.co](mailto:tom@acme.co)   |

| product\_name              | user\_email                         |
| -------------------------- | ----------------------------------- |
| solid gold lint roller     | [john@acme.co](mailto:john@acme.co) |
| tungsten toothbrush handle | [tom@acme.co](mailto:tom@acme.co)   |

To help the agent properly join data between these tables it is desirable to add something like this in the instructions:

You can join data between the users and orders tables using respectively the email and user\_email columns

This is especially true in more complex use-cases where the ideal join columns are not obvious.

## Creating Tables

### Creating Tables from CSV files

1. Make sure you have `builder` rights on your Dust workspace.
2. Go to the `Knowledge` tab and go to `Folders` into the space of your choice. Pick the folder you want to add your table to, or create a new folder by clicking on `Add a new folder` at the top of the page.
3. Go to the `Tables` tab and click on `Add table`.
4. Upload a file in CSV format, and enter a good description for your table. **Providing a detailed description for your table will help the AI generate better queries !**

| name             | date       | stage    |
| ---------------- | ---------- | -------- |
| ACME CORP        | 20/10/2022 | lead     |
| STARK CORP       | 21/11/2023 | closing  |
| PERMUTATION LABS | 19/08/2020 | customer |

Based on this example, a good table description would be:

This table is an extract from our CRM. Each line represents a potential customer, and includes the date of the last meeting we had with them and what stage they are at in our sales pipeline.

### Creating Tables from API

You can create Tables from API on existing Folders Data Sources. Please refer to our API documentation available here: [Upsert a table](/docs/developer-platform/dust-api-documentation/upsert-a-table)

### Tables from Google Sheets and Notion Databases

Dust automatically creates a table for every Google Sheet and Notion Database that we find in your connections.

Make sure the Notion and Google Sheet connections are setup, and that the Dust integration has access to the Google Sheets or Notion Databases that you want to use.

### Tables from BigQuery

For BigQuery connections, table and column descriptions set in BigQuery can be automatically used when describing tables to agents. This feature can be enabled in the BigQuery connection management screen.
