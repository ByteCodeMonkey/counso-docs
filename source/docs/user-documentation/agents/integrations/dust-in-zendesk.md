> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Dust in Zendesk

<Info>
  This page covers adding the Dust extension to Zendesk. If you want to import
  Zendesk data into Dust, see the [Zendesk
  connection](/docs/user-documentation/admins/connections-management/zendesk).
</Info>

## Install from the marketplace

The Dust application is available from the [Zendesk marketplace](https://www.zendesk.com/marketplace/apps/support/1070957/dust).

Click on the **Install** button at the top right, then select the Zendesk workspace you want to install it in.

## Set up your Workspace ID and API key

You will need to have created a Dust API key. Only Dust administrators can create API keys.

Once you have your workspace ID and API key, add them to the Dust application parameters.

## Defining default agents (optional)

If you want to limit the list of agents available to your support team, you can do so in the **Default Agent IDs** option. Add a comma separated list of agent IDs to limit the view of available agents.

More info about [How can I find the ID of an agent?](/docs/user-documentation/getting-started/faq/managing-agents/how-can-i-find-the-id-of-an-agent)

## Removing PII (optional)

If you don't want your agents to know anything about the metadata of your customer (name, email) but only what's present in the conversation itself, you can tick the **Hide customer information** box.

## Restricting access

You can decide to restrict access to the app to certain groups or roles within Zendesk.

## Dust accounts

Please note that the Zendesk user needs to have a Dust account with the same email for the extension to be active.
