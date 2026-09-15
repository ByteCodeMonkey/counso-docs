---
title: "Salesforce query limits and access"
---
The Salesforce tool runs provider queries when an Agent requests Salesforce information. It does not need to import all Salesforce records into the workspace, but each query and metadata refresh can consume Salesforce API capacity. Usage allowances vary by Salesforce edition, licenses, purchased add-ons, and organisation settings; use Salesforce Setup to inspect the current 24-hour usage and limit rather than relying on a generic number.

## Control the data boundary

Queries run with the connected Salesforce identity. Use a dedicated service account for shared credentials and give it only the object, field, and record access required. For personal credentials, Salesforce applies each user's permissions. Also restrict which Salesforce objects are queryable in each Space, so Space membership and provider permissions jointly define access.

Not every object or field is automatically available. Salesforce may require object permissions, field-level security, custom permissions, or configuration before a field can be queried. Custom field API names commonly end in `__c`; document business-specific relationships and mappings in the Agent instructions.

## Improve query reliability

Ask for a clear object, date range, and result limit. When multiple Accounts share a name, use an Account Number or external ID, or ask the Agent to confirm which record is intended. For large result sets, narrow filters to reduce latency and API usage. Monitor usage in Salesforce Setup and configure threshold notifications there if needed.

Check record IDs, filters, field access, and the acting identity before relying on the answer. A successful login does not prove that the user can see every object or field.
