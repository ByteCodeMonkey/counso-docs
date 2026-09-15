> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Zapier

In this article, we will guide you through how to use the Dust block in Zapier to automatically trigger your Dust Agent from any other application.

## 1. First, go to [Zapier](https://zapier.com/apps/dust/integrations) and create a new Zap

Create a new Zap on Zapier, and choose what event should trigger your Dust Agent.

A common example of a trigger for a Dust Agent is: `A new row inserted in a Google Spreadsheet`

## 2. Add your `Action` event

* To do so, search for Dust among Zapier integrations:\\

* Then in the `App & event`tab, select **“Talk to an Agent”:**

* In the `Account`tab, **follow the instructions to connect Zapier with your Dust account:** you will need your **Workspace ID** (which can be found in your Dust tab URL, right after *dust.tt/w/*), as well as your **Dust API key**, which a workspace admin can create from **Admin > API & Programmatic > API Keys > Create an API Key**\\

* In the `Action`tab, you’ll be prompted to fill the following fields:
  * **The message to send to the Agent**: this is the message to send to the agent
  * **Timezone**: this is the timezone in which you want to operate, you can choose from the list (eg: `Europe/Paris` or `America/Los_Angeles`)
  * **username**: put the name to be displayed in the conversation. eg: `Daily summary Zap`
  * **email**: This one is optional, put an email if needed.
  * **Agent**: Select the name of your Agent from the list. Your Dust Agent must be a "Shared" or "Company" Agent. Personal Agents are not visible in this list.

## 5. Run the Tests, and Publish your Zap

You’re all set!

Once launched, new content in the *Trigger* will automatically run your Agent. To extract the output of the Agent and send it to your next block, you must use the `AgentMessage` property from the Dust block.
