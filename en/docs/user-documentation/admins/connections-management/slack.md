# Connect Slack knowledge

The Slack connection indexes messages from selected channels for agent knowledge searches. It is separate from the interactive Slack bot and from Slack tools that search or act using a user's account.

## Prepare the Slack app

You need Counso workspace admin access and permission to create and install Slack apps. Ask the administrator responsible for your Counso deployment for the app manifest values: Slack must be able to reach that deployment's OAuth callback, Events Request URL, and Interactivity Request URL. The Slack Connection and its data-sync service must also be enabled for the workspace.

1. Open [Slack's app dashboard](https://api.slack.com/apps), choose **Create New App > From a manifest**, and select the workspace.
2. Paste the manifest supplied for this Counso deployment. Before creating the app, confirm that its OAuth callback and event/interactivity addresses point to the same deployment. Do not reuse addresses from another service or environment.
3. Review the requested permissions and event subscriptions. The app needs the channel, message, user, and file access used by the connection, plus the events required to keep selected channels synchronized. Keep the supplied scopes and event list intact.
4. Create and install the app. If Slack requires approval, a Slack administrator must approve it in the workspace's app management settings.
5. From **Basic Information > App Credentials**, copy the Client ID, Client Secret, and Signing Secret into the matching fields in **Spaces > Connections > Slack**.
6. Choose **Connect** and complete Slack authorization.

## Select channels

In **Spaces > Connections > Slack > Add / Remove data**, select the channels to index and save. For a private channel, invite the configured data-sync bot first so the channel can appear in the selector. Private-channel indexing must also be enabled for your workspace; an invitation alone does not enable the feature.

## Content and freshness

The connection indexes messages, threads, and channel metadata for the selected channels. Bot-generated messages, direct messages, and external files are not indexed. Do not assume historical messages from before the bot joined are included; check the history available for the channel after setup.

New messages normally appear soon after they are posted. Changes to selected channels can take seconds or minutes, depending on volume. Use threads for related discussion: unthreaded content may link to an approximate channel location rather than a precise message.

Channel labels use `channelId:...` and `channelName:...` and can filter the [knowledge search tool](../../agents/knowledge/search-data-sources.md).

## Maintain the connection

Change the channel selection in **Add / Remove data**, and control which Spaces receive Slack knowledge through **Manage Permissions**. If app credentials must be rotated, update the corresponding values immediately in **Manage > Edit** so the connection can resume.

For authorization, migration, or missing-channel problems, see [Slack troubleshooting](../admin-troubleshooting/slack-troubleshooting.md). For live Slack actions, see [Slack tools](../../agents/tools/slack-tools.md).
