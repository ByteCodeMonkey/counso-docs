> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Slack

<Info>
  **Feature availability**

  The self-created Slack app connection is not available on all plans. If you do not see the Slack connection option in your workspace, contact [support@dust.tt](mailto:support@dust.tt) to check availability for your plan. Private channel indexing requires separate enablement; mention it in the same request.
</Info>

<Warning>
  **Slack API changes (May 2025)**

  Slack updated its API and Terms of Service in May 2025. Bulk data indexing via a shared Dust app is no longer permitted. All workspaces must use a **self-created Slack app** to maintain the Slack connection. Connections set up before December 2024 must be migrated. See [Slack Troubleshooting](/docs/user-documentation/admins/admin-troubleshooting/slack-troubleshooting) for migration steps.
</Warning>

Dust synchronizes with Slack to bring your workspace conversations into Dust, enabling agents to search and retrieve messages from selected channels.

<Info>
  **Two separate Slack integrations**

  The **Slack connection** (this page) syncs channel messages as a data source for your agents. The **Dust in Slack** integration lets your team call Dust agents directly inside Slack. See [Dust in Slack](https://dust.tt/home/slack/slack-integration) for the interactive bot setup.
</Info>

## Prerequisites

* A **Slack Owner or Admin** account (required to create and install Slack apps)
* A **Dust workspace admin** account
* The region your Dust workspace runs in: **US** (`https://dust.tt`) or **EU** (`https://eu.dust.tt`). The app manifest is different for each region.

Setup takes about 2 minutes: you create a dedicated `Dust Data Sync` app in Slack from the manifest below, then paste its credentials into Dust.

## Step 1: Create your Slack app

1. Go to [api.slack.com/apps](https://api.slack.com/apps) and click **Create New App** -> **From a manifest**
2. Select the Slack workspace you want to connect
3. Select the **JSON** tab. Slack pre-fills a placeholder manifest: delete it entirely and paste the Dust manifest for your region (see [App manifest](#app-manifest) below)
4. Click **Next**, review the requested permissions, then click **Create**
5. Open the app's **Install App** page and click **Install to Workspace**

<Warning>
  **Use the manifest that matches your region**

  The manifest contains a region-specific OAuth redirect URL. Use the **US** manifest if your Dust workspace is on `https://dust.tt`, and the **EU** manifest if it is on `https://eu.dust.tt`. Using the wrong one will fail the authorization step.
</Warning>

### App manifest

<AccordionGroup>
  <Accordion title="US app manifest (dust.tt)">
    ```json theme={null}
    {
      "display_information": {
        "name": "Dust Data Sync",
        "description": "Secure AI agent with your company's knowledge",
        "background_color": "#0f172a",
        "long_description": "The Dust Data Sync Slack app enables seamless synchronization of your Slack workspace data with Dust. Connect channels to make conversations searchable and accessible to your AI assistants."
      },
      "features": {
        "bot_user": {
          "display_name": "Dust Data Sync",
          "always_online": false
        }
      },
      "oauth_config": {
        "redirect_urls": [
          "https://dust.tt/oauth/slack/finalize"
        ],
        "scopes": {
          "user": [
            "channels:read",
            "users:read",
            "chat:write",
            "search:read"
          ],
          "bot": [
            "app_mentions:read",
            "channels:history",
            "channels:join",
            "channels:read",
            "chat:write",
            "files:read",
            "groups:history",
            "groups:read",
            "im:history",
            "im:read",
            "metadata.message:read",
            "mpim:history",
            "mpim:read",
            "team:read",
            "users:read",
            "users:read.email",
            "channels:manage"
          ]
        }
      },
      "settings": {
        "event_subscriptions": {
          "request_url": "https://webhook-router.dust.tt/slack_data_sync/events",
          "bot_events": [
            "channel_deleted",
            "channel_left",
            "channel_created",
            "member_joined_channel",
            "message.channels",
            "message.im",
            "message_metadata_deleted"
          ],
          "metadata_subscriptions": [
            {
              "app_id": "*",
              "event_type": "message_metadata_deleted"
            }
          ]
        },
        "interactivity": {
          "is_enabled": true,
          "request_url": "https://webhook-router.dust.tt/slack_data_sync/interactions"
        },
        "org_deploy_enabled": false,
        "socket_mode_enabled": false,
        "token_rotation_enabled": false
      }
    }
    ```
  </Accordion>

  <Accordion title="EU app manifest (eu.dust.tt)">
    ```json theme={null}
    {
      "display_information": {
        "name": "Dust Data Sync",
        "description": "Secure AI agent with your company's knowledge",
        "background_color": "#0f172a",
        "long_description": "The Dust Data Sync Slack app enables seamless synchronization of your Slack workspace data with Dust. Connect channels to make conversations searchable and accessible to your AI assistants."
      },
      "features": {
        "bot_user": {
          "display_name": "Dust Data Sync",
          "always_online": false
        }
      },
      "oauth_config": {
        "redirect_urls": [
          "https://eu.dust.tt/oauth/slack/finalize"
        ],
        "scopes": {
          "user": [
            "channels:read",
            "users:read",
            "chat:write",
            "search:read"
          ],
          "bot": [
            "app_mentions:read",
            "channels:history",
            "channels:join",
            "channels:read",
            "chat:write",
            "files:read",
            "groups:history",
            "groups:read",
            "im:history",
            "im:read",
            "metadata.message:read",
            "mpim:history",
            "mpim:read",
            "team:read",
            "users:read",
            "users:read.email",
            "channels:manage"
          ]
        }
      },
      "settings": {
        "event_subscriptions": {
          "request_url": "https://webhook-router.dust.tt/slack_data_sync/events",
          "bot_events": [
            "channel_deleted",
            "channel_left",
            "channel_created",
            "member_joined_channel",
            "message.channels",
            "message.im",
            "message_metadata_deleted"
          ],
          "metadata_subscriptions": [
            {
              "app_id": "*",
              "event_type": "message_metadata_deleted"
            }
          ]
        },
        "interactivity": {
          "is_enabled": true,
          "request_url": "https://webhook-router.dust.tt/slack_data_sync/interactions"
        },
        "org_deploy_enabled": false,
        "socket_mode_enabled": false,
        "token_rotation_enabled": false
      }
    }
    ```
  </Accordion>
</AccordionGroup>

<Warning>
  **Do not modify the manifest**

  Use the manifest exactly as provided above. Changing OAuth scopes, redirect URLs, event subscription URLs, or credentials will break the connection.
</Warning>

## Step 2: Copy your app credentials

Open your app's **Basic Information** page on api.slack.com and copy the three values under **App Credentials**:

1. **Client ID**
2. **Client Secret** (click **Show** to reveal it)
3. **Signing Secret** (click **Show** to reveal it)

## Step 3: Connect to Dust

1. In Dust, go to **Spaces** -> **Connections** and select **Slack**
2. Fill in **Slack App Client ID**, **Slack App Client Secret**, and **Slack App Signing Secret** with the values from Step 2
3. Click **Connect**
4. Authorize the app when Slack prompts you. Dust installs the `@Dust Data Sync` bot in your workspace.

<Info>
  **App approval workflows**

  If your Slack workspace requires admin approval for new apps, the installation stays pending until a Slack admin approves it in **Slack Admin** -> **Manage Apps** -> **App Requests**.
</Info>

## Step 4: Select channels to sync

1. In Dust, go to **Spaces** -> **Connections** -> **Slack** -> **Add / Remove data**
2. Select the channels you want Dust to sync
3. Save. Dust will start syncing immediately.

<Info>
  **Private channels**

  Private channels are not visible to the bot by default. To sync a private channel, first invite the bot: open the channel in Slack and type `/invite @Dust Data Sync`. The channel will then appear in the Dust connection manager.

  Private channel indexing requires a separate feature flag. Contact [support@dust.tt](mailto:support@dust.tt) to request access.
</Info>

## What Dust syncs

* Messages and threads from selected channels
* Channel metadata (name, topic)

**Not synced:**

* Messages from bots (including `@Dust` itself and Slack workflows)
* Messages from private channels unless the bot has been explicitly invited
* Direct messages
* External files

## Labels

Dust syncs the name and ID of the Slack channel and includes them in the document, above the message content. They are available as `channelId:xxxxxxxx` and `channelName:my-channel`.

These labels allow additional filtering on the data sources selected in the [Search data sources](/docs/user-documentation/agents/knowledge/search-data-sources) tool.

## Data freshness

New messages are available in Dust almost immediately after being posted. Changes to your channel selection in **Add / Remove data** are reflected within a few seconds to a few minutes, depending on the volume of data.

Historical messages are available from the moment the bot joined the channel. Slack does not provide history from before a bot's first invite.

<Info>
  **Best practice: use threads**

  When messages are not threaded, Dust links to the approximate location in the channel rather than the exact message. Post your topic as the first message, then continue the conversation in a thread. This improves retrieval quality and gives accurate message links.
</Info>

## Managing permissions

* Adopt a **shared-by-default** approach: share everything except the data you explicitly want to keep out of Dust.
* Admins can update which spaces receive Slack data from **Spaces** -> **Connections** -> **Slack** -> **Manage Permissions**.

## Managing the connection

To add or remove channels, go to **Spaces** -> **Connections** -> **Slack** -> **Add / Remove data**.

To update your app credentials (e.g. after rotating secrets), go to **Spaces** -> **Connections** -> **Slack** -> **Manage** -> **Edit**.

<Warning>
  **Avoid editing your Slack app after setup**

  Once your Slack app is created and connected to Dust, editing some app parameters breaks the connection. In particular, do not:

  * update scopes or permissions
  * modify redirect URLs
  * rotate credentials manually

  If one of your secrets is compromised and you must rotate it, update the new values **immediately** in **Spaces** -> **Connections** -> **Slack** -> **Manage** -> **Edit**. The connection resumes once the new credentials are saved.
</Warning>

## Related

* [Slack Troubleshooting](/docs/user-documentation/admins/admin-troubleshooting/slack-troubleshooting)
* [Dust in Slack](https://dust.tt/home/slack/slack-integration)
* [Slack Tools](/docs/user-documentation/agents/tools/slack-tools)
