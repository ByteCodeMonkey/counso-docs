---
title: "Airtable"
---
The Airtable remote tool lets an Agent inspect base schemas and search, read, create, or update records and record comments. Choose a credential model before setup: a Personal Access Token is shared by everyone who can use that configured tool; OAuth lets each person act with their own Airtable account and permissions.

## Configure Airtable

For a token, create one at [airtable.com/create/tokens](https://airtable.com/create/tokens). Select only the bases the Agent needs. Start with `data.records:read`, `schema.bases:read`, and `user.email:read`; add `data.records:write`, `data.recordComments:read/write`, or `schema.bases:write` only when the intended work requires them. Copy the token when created and store it in the tool configuration.

For per-user OAuth, register an integration at [airtable.com/create/oauth](https://airtable.com/create/oauth). Use Counso as the integration name, set the public homepage to `https://counso.ai`, and use the callback URL displayed in the current connection form. Configure the scopes and token authentication method required by Airtable and the form. Connect to Airtable's MCP endpoint `https://mcp.airtable.com/mcp` using the selected authentication mode.

After setup, add Airtable to the Agent and verify one base schema and one known record. If authentication works but tables are missing, check the allowed bases and schema scopes. Keep write scopes off unless the Agent needs to change records.

## OAuth values

Airtable's OAuth endpoints are `https://airtable.com/oauth2/v1/authorize` and `https://airtable.com/oauth2/v1/token`; its token endpoint uses Basic authentication. The recommended scopes are `data.records:read`, `data.records:write`, `data.recordComments:read`, `data.recordComments:write`, `schema.bases:read`, `schema.bases:write`, and `user.email:read`. Match the registered scopes to the work and the current connection form. Airtable may request a support email and public privacy/terms links when registering the OAuth application; use Counso's own current contact and legal pages rather than third-party platform links.
