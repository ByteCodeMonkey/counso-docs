# Slack tools

The Slack Tool lets an Agent search messages and channels, read threads, find users, and—when permitted—post or schedule messages. It uses the connected user's Slack identity.

A workspace administrator adds Slack under **Spaces → Tools → Add Tools** and completes OAuth. Each user may need to authorize their own account. Share the tool with the intended Space and add it to the Agent. Available operations include message search, semantic search where supported by the account, conversation/thread retrieval, user lookup, posting, and scheduling.

For precise writes, use channel and user IDs when available, and include the thread timestamp when replying in a thread. Scheduled posts may not support attachments. Read the channel or message back in Slack after sending. A private channel may be absent because the acting user or configured app was never added. Check the tool permissions and channel membership.

## Available operations

Available tools include message search, semantic message search where available, posting and scheduling a message, listing/searching channels, listing and retrieving users, and conversation/thread lookup. The exact names shown in the Agent builder are the actions available to your workspace. Scheduled posts may not include attachments; posting requires the correct channel or user identifier and a thread timestamp when replying in a thread.
