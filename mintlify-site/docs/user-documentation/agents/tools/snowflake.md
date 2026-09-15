---
title: "Snowflake"
---
The Snowflake Tool explores databases, schemas, tables, and views and runs read-only SQL under a selected Snowflake role. Available operations are **List Databases**, **List Schemas**, **List Tables**, **Describe Table**, and **Query**. Query accepts only one read-only `SELECT` statement—no semicolon-separated multi-statements or write operations—and returns at most 1,000 rows per query.

## Create an OAuth integration

An Account Administrator creates a confidential custom OAuth Security Integration in Snowflake. Use the callback URI shown by the Counso connection form, enable refresh tokens, and retrieve the client ID and secret through Snowflake's supported secret-display function. Grant usage on the integration to the intended role where required. Do not paste the secret into an Agent prompt.

## Configure the tool

In **Spaces → Tools → Add Tools**, select Snowflake and enter the account identifier, client ID, client secret, warehouse, and role. Choose **Personal** credentials so each user's role controls access, or **Workspace** credentials so the configured service account, role, and warehouse are shared. With personal credentials, a user may select a permitted role during OAuth; with workspace credentials, those values remain fixed.

Start by listing databases and describing the target table before querying. The active role controls accessible objects. Personal credentials can query views and apply per-user permissions; a Snowflake Connection is separately configured for an administrator-selected table list and may support larger retrievals. Use a Tool for role-scoped live queries, a Connection for a fixed synchronized collection. Filter queries to keep results manageable.
