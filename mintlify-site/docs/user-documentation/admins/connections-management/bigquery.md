---
title: "Connect BigQuery"
---
A BigQuery connection lets agents run [table queries](/docs/user-documentation/agents/knowledge/table-queries) against selected warehouse tables. It indexes metadata such as dataset and table names rather than copying the warehouse into Counso. Query results are returned to the agent for answers or visualizations.

## Prepare Google Cloud access

Use a dedicated service account. In **IAM & Admin > Service Accounts**, create the account and give it the permissions needed to run queries and read the selected data. The connection guide uses `roles/bigquery.user` and `roles/bigquery.dataViewer`. Some external storage formats require additional permissions on their underlying storage.

In the account's **Keys** tab, choose **Add Key > Create new key > JSON**. Store the downloaded key securely; it grants access to the account's BigQuery resources.

A project contains datasets, and datasets contain tables. Each dataset has a region or multi-region location. A query cannot combine datasets in different locations, such as US and EU.

## Configure Counso

1. Open **Spaces > Connections**, add BigQuery, and enter the service-account JSON key in the credential field.
2. Select the connection's BigQuery location. Allow a moment for the key to register if the form is still processing it.
3. Choose datasets and tables from that same location.
4. Enable **Use BigQuery descriptions** if agents should use table and column descriptions to understand fields.
5. Make the tables available in the appropriate Spaces and select them for the agent's table-query capability.

A workspace uses one BigQuery connection and one service-account authorization. Its credentials can access every resource granted to that account by Google Cloud IAM; Space selections then narrow the tables available to agents. Keep the account permissions aligned with the datasets you intend to expose.

## Check a query

Ask a question with a defined metric and date range. Use **Tools inspection** to inspect the generated SQL and the query result before relying on a total or chart. Check dataset location, service-account roles, selected tables, and field descriptions if a query cannot run or uses the wrong fields.
