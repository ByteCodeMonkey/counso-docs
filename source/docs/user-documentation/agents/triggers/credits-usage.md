> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Credits usage

A trigger run costs credits like any other agent run. The **Credits** setting on each trigger decides whose credits pay for it: the trigger editor's, or the workspace. It does not change anything else about how the trigger behaves.

## Set the pool on a trigger

Open the trigger in the Agent Builder and pick from the **Credits** dropdown:

* **My credits**, the default, bills the run to the trigger editor's, as if they had sent the message themselves.
* **Workspace credits** bills the run to the workspace as programmatic usage, alongside API calls and other automations. It is not attributed to any member.

To change the setting you must be an editor of the agent and have access to the workspace pool, which an admin grants (see [Grant access to the workspace pool](#grant-access-to-the-workspace-pool)). Without that access, you can see the setting but not change it. Admins and managers can also change it from the Automations page. Your change are automatically picked up starting from the next run.

## Which pool to pick

Put a trigger on workspace credits when it serves the team rather than one person: PR reviews, ticket triage, alert routing, anything running dozens of times a day. Charging that to one member's seat credits exhausts them on work the team benefits from.

Leave a trigger on personal credits when its editor is also the one who reads the output, like a morning digest or a weekly report. Volume stays low and the cost sits with the person who asked for it.

## Grant access to the workspace pool

Only admins can charge triggers to the workspace by default. Admins and managers change that in **Settings & Governance**, under *Charge automations to the workspace*: everyone, selected groups, or admins only.

Removing the access does not move existing triggers back to personal credits. Triggers already on workspace credits stay there until someone changes them.

## Where the credits come from

On credit-priced plans:

* **My credits** uses the editor's seat credits first, then the workspace credit pool if their seat has access and their personal spend limit allows it. [Credit management](/docs/user-documentation/admins/usage-seats-and-credits/credit-management) covers that order in detail.
* **Workspace credits** uses the workspace credit pool, then Pay As You Go on Enterprise plans. It counts against the monthly programmatic cap in **Admin > Usage** and has no free credit baseline.

On legacy plans, which still use message quotas instead of credits:

* **My credits** counts against the workspace's fair-use message allowance. Webhook triggers can use up to half of it, leaving the rest for people's conversations.
* **Workspace credits** uses programmatic usage credits, the balance shown in **Programmatic Usage > Credits Usage**, and counts against the daily programmatic cap.

<Note>
  A trigger stops running once the pool it charges is out: its editor's credits or personal spend limit on **My credits**, the workspace pool or the monthly programmatic cap on **Workspace credits**. Admins top up the pool or raise the cap in **Admin > Usage**. The trigger starts running again once the limit resets or the balance goes back up, and runs missed in the meantime are not replayed.
</Note>

## Review your triggers

Admins and managers see every trigger in the workspace under **Programmatic Usage > Automations**, with its agent, its credit consumption over the selected period, and a **Pool** column showing *Member* or *Workspace*.

Members can review their own automations from the **Automations** entry under **Tools** in the user menu. This view lists the automations they edit, with filters, an expandable per-trigger credit breakdown for the current billing cycle, and controls to enable, disable, or delete an automation.

Select several rows to move them to another pool in one go, which is the quickest way to migrate a batch of triggers after changing your policy.

## Rate limits

The pool is separate from the rate limit. A webhook trigger keeps its own cap on runs per 24 hours whichever pool it charges. See [Rate limiting](/docs/user-documentation/agents/triggers/webhooks/rate-limiting).
