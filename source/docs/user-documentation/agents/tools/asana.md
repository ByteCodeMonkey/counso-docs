> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Asana

## Overview

Asana tools let your agents work with Asana directly from Dust once an administrator connects the integration. After setup, agents can reference and act on Asana data according to the permissions granted during authentication.

<Info>
  This integration uses OAuth. Workspace admins can choose between
  Workspace-level credentials (shared) and Personal credentials (per-user). See
  the general guidance in [Tools
  management](/docs/user-documentation/admins/tools-management/adding-an-mcp-server).
</Info>

## Admin: Setup in Dust

1. In your Dust workspace, go to **Spaces Tools Add Tools**
2. Select **Asana**
3. Choose the credential type:
   * **Workspace credentials**: A single admin authorizes Asana for everyone who can access the tool
   * **Personal credentials**: Each user authorizes Asana with their own account when they first use an agent with the tool
4. Click **Connect** and complete the Asana OAuth flow
   1. Use your created Asana app credentials
   2. The redirect URL field should be [https://dust.tt/oauth/mcp\_static/finalize](https://dust.tt/oauth/mcp_static/finalize) (or [https://eu.dust.tt/oauth/mcp\_static/finalize](https://eu.dust.tt/oauth/mcp_static/finalize) for EU workspaces)

### Important: Finalize in Asana (Manage Distribution)

After completing the OAuth connection in Dust, an Asana admin must finalize distribution for the app:

1. Open **Asana My Apps**: [https://app.asana.com/0/my-apps](https://app.asana.com/0/my-apps)
2. Select the app you just authorized for Dust
3. Click **Manage distribution**
4. Select the relevant Asana workspace(s) where this app is allowed
5. Save

If this step is skipped, agents may see authorization errors or won’t be able to access any Asana data.

## Usage in Dust (Users)

* Once the tool is configured by an admin, add it to an agent from the Agent Builder (Add Tool Asana)
* If the tool uses Personal credentials, users will be prompted to connect their Asana account on first use

## Troubleshooting

* “Connected but no data” or 403-like authorization errors: Verify the app’s **Manage distribution** setting in Asana includes the intended workspace(s)
* Reconnect flow: If you recently changed Asana permissions, disconnect and reconnect from the tool’s configuration panel, then retry

## Related

* Tools management: [/docs/user-documentation/admins/tools-management/adding-an-mcp-server](/docs/user-documentation/admins/tools-management/adding-an-mcp-server)
* Changelog (Asana):
  * Asana available as tool: [https://docs.dust.tt/changelog/asana-added-to-default-connectors](https://docs.dust.tt/changelog/asana-added-to-default-connectors)
