# Table queries

A table-query capability lets an Agent ask questions of structured data by generating and running a query, then using the returned rows to answer. It is suited to counts, totals, filters, groupings, and comparisons across a table. Semantic search returns relevant excerpts and may not inspect every row, so it is not a substitute for a complete structured query.

Depending on the connections and features enabled in your workspace, queryable tables can come from CSV files, connected Google Sheets or Notion databases, Microsoft spreadsheets, or a supported data warehouse such as Snowflake or BigQuery. A CSV may also be uploaded directly to a conversation where that option is available. Check the source type and availability shown in your workspace.

## Choose a query for the question

For a table of cars with columns `cars`, `production_year`, `color`, and `description`, “What is the most common color for cars produced between 2000 and 2010?” is a table-query question. “What is the best car to buy if I live in NYC?” needs interpretation of unstructured descriptions and is better suited to search.

Use both methods when the task needs a quantitative result plus explanatory context.

## Add Query Tables to an Agent

When the feature is available, open the Agent Builder and find **Action & Data sources**. Choose **Add a tool**, then select **Query Tables**. Select one or more tables for the Agent to use and save the configuration. The tool can query selected tables together, including tables from different supported sources.

For a join, explain the matching columns in the Agent instructions. For example, if a `users` table has `email` and an `orders` table has `user_email`, say that these columns identify the same user. State whether the relationship is one-to-one or one-to-many when that affects totals, so the Agent can avoid multiplying rows accidentally.

## Create a table from CSV

If your workspace allows manual CSV tables, a Builder can create one in a Knowledge folder:

1. Open **Knowledge**, then **Folders** in the Space where the table should live.
2. Select a folder or choose **Add a new folder**.
3. Open the folder's **Tables** tab and select **Add table**.
4. Upload a CSV file and provide a useful description.

Describe what each row represents and explain important columns. For example: “This table is an extract from our CRM. Each row represents a potential customer and includes the date of the last meeting and the current sales-pipeline stage.” A clear description helps the Agent form queries that match the data's meaning.

Connected Sheets and Notion databases may appear as tables when their connections are set up and have access to the relevant files or databases. For BigQuery, table and column descriptions may be available to the Agent when the connection's metadata option is enabled. Availability depends on the connectors and settings in your workspace.

## Check quantitative answers

State the period, filters, grouping, currency or unit, and treatment of missing or duplicate rows. For joins, provide the key columns. Check the returned table, filters, and row count against the source when completeness matters. A plausible total alone does not prove that the query used every intended row.

Table queries are for structured data, not raw unstructured text. For document meaning or recommendations, use a search capability and verify the cited source.
