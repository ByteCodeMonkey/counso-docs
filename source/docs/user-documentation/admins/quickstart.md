> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

Welcome to Dust! If you are here, it's because you are an Admin of your workspace. As an Admin, you have full admin rights. See more about [Memberships & Roles](/docs/user-documentation/getting-started/dust-rollout-guide/admin-guide-set-up-your-dust-workspace).

You can set-up multiple parameters for your workspace by going to the Admin Panel.

In order to make the most out of Dust, here are the steps we recommend.

You can use Dust without data sources, but Dust is most useful when connected to your knowledge bases. As an admin, you have the ability to manage data sources and make them available for all members of your workspace.

There are various types of Data Sources:

* **Managed Connections:** your main communication and knowledge tools, they get synchronized automatically, so Dust can always have access to recent information
* **Public Websites:** ingest data from public websites with our web crawler, which you can refresh at the cadence you want
* **Folders:** store static information in a folder, just like you would on your computer.

<Danger>
  **About sharing data and permissions**

  * Even once synchronized, your data is not yet shared nor usable with your workspace members. You can make the connected data available to other people in your workspace by adding it to a [space](/docs/user-documentation/data-sources/overview).
  * When adding a connection, you can select exactly which channels or folders you want Dust to have access to.
</Danger>

**How to add my first connection**

Go to **Spaces** > **Connections**, select the desired Connection, click **Connect > Authenticate your account**, and select the data you wish to synchronize with Dust.

To get help on how to set-up the various connections, you can refer directly to [Connections](/docs/user-documentation/data-sources/connections).

Now that you have built the first steps of your connections, you can start putting Dust to work. A very useful agent in your journey is the**@dust** agent.

**@dust** is created to help you **answer questions by looking into your company data**. Think about it as your company data researcher, or "Perplexity for internal data". It works using [Retrieval Augmented Generation](/docs/user-documentation/agents/llm-best-practices/understanding-rag).

**How to set-up Dust**

* Go to **Chat >  Manage Agents > Default>@dust** and click on **Manage**. From there, you will be able to choose which data sources @dust has access to.
* Select the data sources you want to give **@dust** access to.

One great use of Dust is to call the agents directly in Slack. The agent can use the ongoing conversation as context, and anybody in the Slack channel will be able to see the answer.

1. [Install and authorize the Dust app in Slack](/docs/user-documentation/agents/integrations/dust-in-slack/slack-workflows).
2. Add the Dust app to your Slack channels.
3. You're all set! All workspace members can interact with @dust directly in Slack.

<Danger>
  **About Slack Settings**

  * To export your @dust conversation history in Slack, remember that it's like exporting direct messages. You can only do this if you're an Owner or admin of a Slack Business+ or Enterprise Grid account.
</Danger>

That's it! You're all set to make the most out of Dust!
