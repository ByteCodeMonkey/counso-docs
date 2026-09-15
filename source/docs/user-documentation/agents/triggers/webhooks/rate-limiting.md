> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate Limiting

Rate limits cap how often a webhook trigger can run, so a busy webhook source does not consume your whole workspace allowance. They control frequency only. For whose credits pay for the runs, see [Credits usage](/docs/user-documentation/agents/triggers/credits-usage).

## Per-trigger limit

Each webhook trigger runs at most **42 times per 24 hours** by default. The window slides: it does not reset at midnight.

Editors change the limit in the **Rate limits** field of the trigger sheet. Raise it for a trigger that legitimately fires often, such as a PR review bot on a busy repository. Lower it while you test a new webhook source.

Scheduled triggers have no such limit, since their schedule already sets their frequency.

## Workspace limit

On legacy plans, which use message quotas instead of credits, all webhook triggers together can use at most half of your workspace's message allowance for the period. The other half stays available for conversations. Raising one trigger's limit does not lift this ceiling.

Credit-priced plans have no message quota. A trigger there is limited by the credit balance it charges to, described in [Credits usage](/docs/user-documentation/agents/triggers/credits-usage).

## Reaching a limit

Dust refuses the incoming request and marks the trigger as rate-limited, which you see as a chip in the trigger details. Requests that arrive while the limit is reached are dropped rather than queued, so nothing is replayed once the window frees up. The trigger runs again on the next request it accepts.

If a trigger hits its limit often, raise it in the trigger sheet, or send fewer requests to Dust in the first place with a [payload filter](/docs/user-documentation/agents/triggers/webhooks/filter-webhooks-payload).
