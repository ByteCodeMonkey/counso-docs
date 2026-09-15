> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# [Beta] Slack Auto-Join

The Slack auto-join channel feature allows automatic synchronization of new public Slack channels with Dust based on predefined patterns. This removes the need for manual intervention each time a relevant channel is created.

## How to Use

1. Write to [support@dust.tt](mailto:support@dust.tt) to enable this feature on your workspace.
2. **Define Pattern**: Set a pattern in the Dust Slack settings. Any new channel that matches this pattern will be automatically synchronized.
3. **Channel Creation**: When a channel is created in Slack and it matches the predefined pattern, Dust's bot automatically joins this channel.
4. **Data Aggregation**: Once joined, the bot starts aggregating data from the channel for use within Dust.

## Tips

* **Pattern Specificity**: Ensure the pattern is specific to avoid unnecessary channel joins.
* **Check Permissions**: Admin permissions in Slack may be required to set up and modify integration settings.

## Example of Use

If you set a pattern like "support-\*," any new channel created, such as "support-query" or "support-feedback," will be automatically added to Dust's synchronized channels. Dust starts aggregating data from these channels without manual setup each time a related channel is created.
