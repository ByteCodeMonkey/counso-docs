# ServiceNow

The ServiceNow tool lets Counso Agents read and write records through the ServiceNow Table API, including incidents, changes, problems, requests, knowledge articles, and custom tables.

## Before you publish this integration

Confirm that the Counso deployment provides the ServiceNow tool and its OAuth callback. Use the callback shown by the deployment; do not reuse a callback belonging to another hosted service.

The connection uses OAuth 2.0 Authorization Code flow against the customer's own ServiceNow instance. A ServiceNow administrator must create an OAuth API endpoint for external clients, and the connected integration user must have the required roles, table ACLs, field ACLs, REST API access policies, and data-policy permissions.

## Required ServiceNow configuration

1. Open **System OAuth > Application Registry** and create an OAuth API endpoint for external clients.
2. Enter the exact Counso callback URL, enable Authorization Code flow, and keep the application active.
3. Copy the generated `Client ID` and `Client Secret`.
4. Authorize the Table API methods required by the deployment: `GET`, `POST`, and `PATCH`.
5. Give the dedicated integration user access only to the required tables and fields.

In Counso, enter the instance URL, Client ID, and Client Secret, then complete authorization as the integration user. Test read, create, and update separately because ServiceNow authorizes each operation independently.

## Available operations

The connector can list records, get a record by `sys_id`, create records, and update records. Exact table access remains controlled by ServiceNow. Fields hidden by a field-level ACL may be omitted without an explicit error.

Create a companion Skill that records approved tables, mandatory fields, state transitions, choice values, reference-field lookup rules, custom `u_*` fields, and fields that must never be written. Do not put credentials in the Skill.

## Current limitations

The connector covers the Table API. It does not provide catalog ordering flows, attachments, or the Knowledge Management API, and it does not support deletes. Do not publish this article until the Counso tool, callback, credentials flow, and representative read/write tests have been verified.
