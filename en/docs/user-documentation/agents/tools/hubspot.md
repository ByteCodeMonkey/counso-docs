# HubSpot

HubSpot tools let an Agent read CRM objects and, where the granted scopes allow, create or update contacts, companies, deals, tickets, and custom objects. The exact tool list changes with the provider account and authorization; inspect available tools in the current Agent builder.

A workspace administrator adds HubSpot under **Spaces → Tools → Add Tools**, selects the intended HubSpot account, and completes OAuth. Grant only the CRM object scopes needed for the Agent's tasks. Share the tool with the appropriate Space, then add it to an Agent.

Start by using **Get Object Properties** for the target object type, then read one known record by ID. The properties response helps identify the field names that can be written. Before an update or creation, confirm the target object and values; read the same record back afterward. Authentication with no object results commonly indicates a missing app scope, object permission, or private-app policy. Avoid broad write scopes for Agents that only answer questions.

## Available operations

Depending on the enabled scopes, the tool list can include object-property discovery; contact, company, deal, lead, task, ticket, note, communication, and meeting creation; contact/company/deal/meeting retrieval; object counts and latest-object queries; file public URL lookup; associated meeting lookup; and CRM object search. Creating an object requires the corresponding object scope and writable properties. Inspect the property list before writing custom fields.
