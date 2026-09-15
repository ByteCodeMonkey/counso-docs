# Connect Snowflake

Connect Snowflake tables for agents to query without importing the warehouse as a document collection. The connection stores schema metadata, and query results are returned to the agent. It exposes tables, not views or materialized views.

## Prepare read-only access

Use a dedicated role, service user, and warehouse. If Snowflake has a network policy, allow the outbound addresses supplied for your Counso deployment. Do not reuse another service's allowlist.

A warehouse provides query compute; databases contain schemas, and schemas contain tables. Grant the role `USAGE` on the warehouse, database, and schema, plus `SELECT` on the required tables. For example, adapt these identifiers to your environment:

```sql
CREATE ROLE counso_reader;
CREATE USER counso_service TYPE = SERVICE DEFAULT_ROLE = counso_reader;
CREATE WAREHOUSE counso_queries
  WAREHOUSE_SIZE = 'XSMALL' AUTO_SUSPEND = 300 AUTO_RESUME = TRUE;
GRANT USAGE ON WAREHOUSE counso_queries TO ROLE counso_reader;
GRANT USAGE ON DATABASE BUSINESS TO ROLE counso_reader;
GRANT USAGE ON SCHEMA BUSINESS.REPORTING TO ROLE counso_reader;
GRANT SELECT ON TABLE BUSINESS.REPORTING.MONTHLY_SALES TO ROLE counso_reader;
GRANT ROLE counso_reader TO USER counso_service;
```

`USAGE` lets the role reach a container; it does not give access to the tables inside. To include a whole schema, replace the individual table grant with `SELECT ON ALL TABLES IN SCHEMA`; add a separate `SELECT ON FUTURE TABLES IN SCHEMA` grant only if new tables should also be available. Keep the role read-only: mutation privileges can cause the connection's permission validation to fail.

## Set up key-pair authentication

Use Snowflake's [key-pair setup](https://docs.snowflake.com/en/user-guide/key-pair-auth) to generate an RSA pair of at least 2048 bits. An encrypted PKCS#8 private key and its public key can be created with:

```sh
openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8
openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
```

Set the service user's `RSA_PUBLIC_KEY` to the public-key contents without the PEM header, footer, or line breaks. Keep the private key private; it belongs in the connection's credential fields, not documentation or a repository.

Password authentication can be used only where the Snowflake account's authentication policy still permits it. Prefer key-pair authentication for a service connection.

## Connect and select tables

In **Spaces > Connections**, add Snowflake and choose the supported authentication method. Provide the account identifier, role, warehouse, and username. For key-pair authentication, paste the full private-key PEM including its header and footer, and enter its passphrase if encrypted. The connection accepts PKCS#8 keys, encrypted PKCS#8 keys, and PKCS#1 RSA keys. For password authentication, enter the permitted service-user password instead.

Select **Connect and select tables**, then choose the tables available to agents. If an expected table is missing, inspect its `SELECT` grant and the enclosing schema and database `USAGE` grants. Views will not appear even when the role has permission to read them.

Ask a [table-query](../../agents/knowledge/table-queries.md) question with a known expected result. **Tools inspection** shows the SQL and result used for the answer, which also helps identify incorrect joins or filters.
