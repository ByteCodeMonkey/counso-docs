# Set limits for webhook triggers

Each webhook trigger runs at most **42 times in a rolling 24-hour period by default**. The window slides continuously; it does not reset at midnight. The limit controls trigger frequency, separately from the credits used by Agent runs.

## Change a trigger limit

Open the webhook trigger in Agent Builder and edit **Rate limits** in the trigger sheet. Editors can adjust the limit for the expected event volume. The value shown in the current trigger settings is authoritative for that workspace. Scheduled triggers are not subject to this webhook limit.

## When the limit is reached

The incoming request is rejected and the trigger is marked as rate-limited. Requests received while the limit is reached are dropped, not queued, and will not be replayed when the rolling window clears. The trigger runs again on the next request it accepts. If this happens often, reduce unnecessary events with a [payload filter](filter-webhooks-payload.md) or adjust the trigger limit where permitted.
