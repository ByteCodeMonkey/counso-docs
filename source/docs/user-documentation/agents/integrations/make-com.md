> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Make.com

In this article, we will guide you through how to use the Dust block in Make.com to automatically trigger your Dust agents from any other application.

## 1. Go to [Make](https://make.com) and create a new scenario

Create a new scenario on Make and choose what event should trigger your Dust Agent.

A common example of a trigger for a Dust Agent is: `A new row inserted in a Google Spreadsheet`

## 2. Add your `Dust` module action

* To do so, search for **Dust** among apps:

**You will be asked to create a connection to Dust:**

You will need your **Workspace ID** (which can be found in your Dust tab URL, right after *dust.tt/w/*), as well as your **Dust API key**, which a workspace admin can create from **Admin > API & Programmatic > API Keys > Create an API Key**

* Once your connection is created, fill in all the necessary fields

* **Agent**: Pick the agent you want to talk to from the list. Only *Company* and *Shared* agents will be available (you won't find *Personal* agents)

* **The message to send to the Agent**: this is the message to send to the agent

* **Timezone**: this is the timezone in which you want to operate, you can choose from the list (eg: `Europe/Paris` or `America/Los_Angeles`)

* **username**: put the name to be displayed in the conversation. eg: `Daily summary Zap`

* **email**: This one is optional, put an email if needed.

## 5. Run and Publish your scenario

You’re all set!

Once launched, new content in the Google Sheet will automatically run your Agent. To extract the output of the Agent and send it to your next module, you must use the `content` part of the output
