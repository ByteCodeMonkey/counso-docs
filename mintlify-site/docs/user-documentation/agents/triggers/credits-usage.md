---
title: "Choose the credit pool for a trigger"
---
Every trigger run uses resources. Its **Credits** setting determines whether the run is charged to the Agent editor or to the workspace pool; this choice does not change the trigger's schedule or filter.

## Choose a pool

Open the trigger in Agent Builder and use its **Credits** dropdown:

- **My credits** charges the run to the trigger editor, as if they had sent the request themselves. This suits a low-volume digest or report that mainly serves that person.
- **Workspace credits** charges the workspace pool as shared automated usage. This suits a team service such as alert routing or ticket triage that may run frequently.

To change the setting, you need to edit the Agent and have access to the workspace pool. An administrator can grant that access through workspace governance. Administrators and managers may also be able to change the pool from the Automations page. A saved change applies to future runs.

## What happens when a pool is unavailable

A trigger stops running when its selected pool or applicable spend limit is exhausted. Check the pool balance and current limits in the workspace Usage area. Runs missed while the trigger is blocked are not necessarily replayed when capacity returns; review the trigger's recent runs after making a change.

The workspace pool is billed and monitored according to the workspace's current resource rules. For personal-credit fallback, programmatic usage, and pool limits, check [Credit management](/docs/user-documentation/admins/usage-seats-and-credits/credit-management).

## Review triggers

Administrators and managers can review trigger activity in **Programmatic Usage > Automations** when available. Compare the Agent, selected pool, run volume, and consumption over the same period. The pool setting is separate from a webhook's rate limit; see [Rate limiting](/docs/user-documentation/agents/triggers/webhooks/rate-limiting).
