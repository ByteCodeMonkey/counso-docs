# Set up automatic replies in Slack channels

An Agent can be configured to respond in selected Slack channels without a member mentioning the workspace bot. This is useful for a dedicated question-and-answer channel, but can create noise in a general discussion channel. Before setting this up, a workspace administrator must register and connect the Slack bot app for this Counso deployment, using the callback and event addresses provided for that deployment. The bot app is separate from the Slack data connection and from the personal Slack Tool. The Agent must be published before changing its channel settings.

## Choose where it replies

An administrator configures the behavior for each Agent in its **Slack Channel Settings**. Select the channel and enable **Respond to all messages in channel**. If the settings offer **Top-level posts only**, enable it to skip replies inside threads. Otherwise, the Agent may respond to both new channel posts and thread replies.

Messages that explicitly mention the bot continue to follow the mention behavior. Messages posted by other bots are ignored to avoid bot-to-bot reply loops.

## Private channels

A private channel appears in the Agent's channel list after the workspace bot app has access to it. Invite the bot to the channel and confirm that the connected integration can read its messages. Adding a personal Slack Tool does not grant the workspace bot access, and connecting the data-sync app is a separate setup.

## Check the result

Post a short test message in the selected channel, then test a thread reply if the mode allows it. Confirm that the intended Agent responded, that the audience can access its sources, and that unrelated channels remain unchanged. To change the behavior, return to the Agent's channel settings and save the updated selection.
