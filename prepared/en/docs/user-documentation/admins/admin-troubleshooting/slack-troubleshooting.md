# Troubleshoot Slack connections and tools

First identify which Slack capability is involved. A data connection, a conversational bot, and a personal Tool have different credentials and access settings.

| Capability | First checks |
| --- | --- |
| Message synchronization | Data-sync app installation, selected channels, target Space, and sync status |
| Agent replies in Slack | Bot app installation, channel membership, mentions, and reply settings |
| Personal Slack Tool | Signed-in Slack account, channel access, and Tool assignment to the Agent |

## A channel or message is missing

For a private channel, an authorized member must add the data-sync app before it can discover the channel. Then select the channel for synchronization in the Counso connection. App membership and selection for synchronization are separate steps.

Check the destination Space and whether the Agent and its user can access it. For missing older messages, review the connection's history range and current sync status rather than assuming every message is already indexed. A large channel list may take time to load.

## The bot does not reply

Check that the bot app is installed in the intended Slack workspace and invited to the channel. Mention the app and include the question in the same message or thread. Select the intended Agent using the configured mention syntax or selector.

For replies without a mention, check the channel's automatic-reply settings and the selected Agent. Whether the bot replies to a new channel message or to a thread depends on those settings. Channel synchronization alone does not turn on replies.

## A Tool uses the wrong account

Check the Slack identity in the Tool's authorization settings. Personal Tools act with the connected user's access. If a bot Tool is used, check the bot's channel membership separately. Reconnect with the correct account when necessary and verify which Tool the Agent is using.

## Installation or authorization fails

A Slack administrator may need to approve the app. For a custom app, the deployment administrator should check the registered callback and event addresses, the relevant app credentials, and the webhook service. Update the saved connection when credentials are rotated.

If the issue remains, share the error text, steps, expected result, and channel or thread link with your administrator. Do not include app secrets in the report.
