> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# n8n

In this article, we will guide you through how to use the Dust node in n8n to automatically trigger your Dust Agents from any other application.

Self-hosted n8n only!
Community nodes are only available on the self-hosted version of n8n for now. If you use n8n cloud, the Dust node will not be available. They are preparing the integration of the community nodes in the cloud version, but we don't know when this will be available.
See their documentation here: [https://docs.n8n.io/integrations/community-nodes/installation/](https://docs.n8n.io/integrations/community-nodes/installation/)

## 1. Install the Dust community node in your n8n environment

In your n8n interface, open your **Settings**

Then in the sidebar click on **Community nodes**, then **Install a community node**

In the **npm package name**, enter: `n8n-nodes-dust`

Create a new scenario on n8n and choose what event should trigger your Dust Agents.

Your Dust node should now be installed

## 2. Trigger your node

A common example of a trigger for a Dust Agent to run it on a schedule:

We will not detail the trigger part here, as it could be anything you wish. We will detail in the next steps the possibilities of the Dust node.

## 3. Add your `Dust` node action

* To do so, search for **Dust** among nodes on the right side of the screen

Then pick the action you want, for now choices are:

* Talk to an agent
* Upload a document

**You will need to create Dust credentials:**

For that you need your Dust Workspace ID, API key and region. Only **admins** can generate API keys.

* Once your connection is created, fill in all the necessary fields

* **Assistant Configuration ID**: Pick the agent you want to talk to from the list. Only *Company* and *Shared* agents will be available (you won't find *Personal* agents). The ID can be found in the "Manage Agents" menu in the app

* **The message to send to the Agent**: this is the message to send to the agent

### Optional:

* **Timezone**: this is the timezone in which you want to operate, you can choose from the list (eg: `Europe/Paris` or `America/Los_Angeles`)
* **username**: put the name to be displayed in the conversation. eg: `Daily summary Zap`
* **email**: This one is optional, put an email if needed.

## 4. Run and Publish your workflow

You’re all set! You can use Dust's reply to continue your workflow.

## Want to contribute?

We're open source, don't hesitate to create a pull request here if you want to add anything to the node:  [https://github.com/dust-tt/dust-n8n-node](https://github.com/dust-tt/dust-n8n-node)
