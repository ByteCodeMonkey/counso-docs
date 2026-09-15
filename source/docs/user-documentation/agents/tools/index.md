> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Tools

**Tools** add abilities to an agent, allowing it to tackle complex scenarios by carrying out multiple tasks at the same time.

* **If you choose to build an agent with no capability or knowledge:** The agent uses only the model to generate an answer.
* **If you build an agent with several capabilities:** The agent evaluates the user request and deploys an appropriate combination of tools
* **If you upload files:** The agent evaluates the user request and, based on the file types, deploy an appropriate combination of dynamic tools

## What tools can you choose from?

Default tools are already available in your Dust workspace, they do not require any Data Source to run, and will augment your agents:

| Tool name           | What the agent will do                                                                                                 |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Data visualization  | Become able to build graphs using the data it gathered                                                                 |
| Web search & Browse | Perform web searches to gather information and use it to generate responses                                            |
| Create Files        | Generate and convert files in various formats ( [Learn more →](/docs/user-documentation/agents/tools/file-generation)) |
| Create Images       | Generate images from a text prompt ( [Learn more →](/docs/user-documentation/agents/tools/image-generation))           |
| Agent Memory        | Remember past conversations from the user to improve itself                                                            |
| Run an agent        | Call another specialised agent to delegate a part of the execution                                                     |

Tools can also perform actions in third-party platforms, based on Personal or Workspace credentials. These tools must be configured at the Admin level.

| Tool name       | What the agent will be able to do                                                                         | Type of credentials   |
| --------------- | --------------------------------------------------------------------------------------------------------- | --------------------- |
| Notion          | Ability to search info, update and create pages in Notion.                                                | Workspace             |
| Slack           | Ability to search info and post messages in Slack.                                                        | Personal              |
| GitHub          | Ability to search, update, comment, and create pull requests and issues in GitHub.                        | Workspace             |
| Confluence      | Ability to search, create, and update pages in Confluence.                                                | Personal or Workspace |
| HubSpot         | Ability to search, update and create info in Hubspot.                                                     | Personal              |
| Salesforce      | Ability to search, update and create info in Salesforce.                                                  | Personal              |
| Gmail           | Ability to search emails in Gmail and create drafts.                                                      | Personal              |
| Google Calendar | Ability to search, update and create events in Google Calendar.                                           | Personal              |
| Outlook         | Ability to search emails in Outlook and create drafts.                                                    | Personal              |
| Zendesk         | Ability to search and retrieve support tickets, view ticket metrics and conversations, and draft replies. | Workspace             |

<Tip>
  Define the tools and let the agent decide which are relevant to your specific
  request.
</Tip>

## Tips & tricks to maximize capabilities' performance

Here are the things you can check as you go through the agent building flow, from `Instructions` to `Tools & Knowledge`:

### Instructions screen

**Clear and detailed instructions will ensure that your agent selects the appropriate tools for each situation.**

Consider describing potential scenarios your agent might encounter and specifying which action should be used in each case, even when it feels obvious.

If you've enabled the Github connections and want to allow your agent to access the code:

> If someone asks you a question that requires understanding our internal codebase, you must search our internal codebase before answering.

If you've enabled some Data sources tools and Websearch:

> If someone asks you about information related to the company (i.e., information that is not public knowledge that you already know about, or that is available on the public internet), you must retrieve it from the internal data sources. If someone asks about general/public knowledge that might require information that is more recent than your knowledge cutoff date, it is very important that you execute a Google search first.

If you've enabled the Browse action:

> You may use your 'Browse' action to read the actual content of web pages to gain more information. It is usually a good idea to read content from several relevant pages before attempting to reply. You should browse several pages simultaneously.

<Tip>
  Use instructions to "script" your agent. Take care not to overestimate the
  model's intuitive understanding; instead, treat it as if it were a highly
  informed yet naive child who requires detailed and clear explanations.
</Tip>

### Tools & Knowledge screen

**Choose data sources judiciously for each action to ensure high-quality, relevant results, and provide a thorough description of the data you selected.**

The agent will provide better results if you carefully select the exact data it might need vs a large amount of data.

For example if you're working on a customer service related agent, you can add a "Search" action and select the Customer Service documentation from your Notion Connection, and describe the data as is:

> "This is the customer service documentation. Every thing here is the ground truth and this documentation is kept up to date. If you found some information here to answer a request, you can answer with confidence."

And then add another "Search" action and select your Intercom Connection to give it access to some specific categories of conversations, and say:

> "This contains the closed Intercom conversations with your members. Keep in mind that especially if the conversation is old our process might have changed, and it concerns only a single member. The data in the Intercom notes are usually relevant, it's usually that the customer service person asked help from a more experience colleague."

**Using Dust apps as tools? Make sure it holds a clear name and description so the agent knows how to use it.**

If you plan on using a Dust app in an action, we highly recommend carefully setting its name and description so it's not a complete black box for your agent. You can do so via the `Settings` of your Dust app. The agent won't know when and why to use it if it does not understand its purpose.

Also note that if the Dust app has no description at all, it won't be selectable from the Agent Builder.

<Tip>
  The more context you provide your agent regarding its prompt and action
  descriptions, the smarter it will operate! Easily iterate on your agent's
  configuration using the preview area next to the builder (with Sidekick
  guidance).
</Tip>

## What use cases do Capabilities support?

Here are a couple of examples of agents using multiple tools to execute complex tasks. You can start from scratch or from a template; Sidekick will guide the setup either way.

### Examples of agents using multiple tools

* [@salesOutboundDraft an agent able to dig through internal documentation and browse the web for the latest news to help draft the perfect outreach email](https://www.notion.so/dust-tt/Write-highly-personalized-outbound-messages-68b60e17c3ad40ae8740368263036b7c)
* [@postmortemDraft an agent that can parse through incident threads, extract key information and present it in a predefined template](https://www.notion.so/dust-tt/Postmortem-Drafter-87c553c1f2684597ae414d365fb255e0)

### Examples of Dust Apps (deprecated)

<Tip>
  Dust Apps allows you to execute code that can be run by agents, which allows
  you to create custom tools for your agents.
</Tip>

Please refer to our [Developer Platform overview](/docs/developer-platform/overview/developer-platform) if you want to learn more about Dust Apps.

* Creating Google Calendar events from a Dust agent
* Allowing an agent to send an email

Tools extend your agents' capabilities by connecting them to external services. They are managed, and made available to spaces by your workspace Admins.

### Overview

Tools in Dust let your agents interact with services like GitHub, GitLab, and many more to come. Tool management is available to workspace administrators through the Spaces > Tools menu.

### Adding and configuring Tools

You can add predefined tools by doing the following :

1. Navigate to the Tools page in your workspace settings
2. Click the "+ Add Tools" button
3. Select your desired tools from the available options
4. Complete any required configuration:

<Info>
  Some tools need authentication credentials. You'll have to login to the
  external service.
</Info>

<Warning>
  These credentials will be used by all users who have access to the tool.
</Warning>

By clicking on a set of tools, you can see the details, including the available tools, manage authentication, and remove it.

It is also possible to add remote MCP servers - check Remote MCP Server documentation.

### Managing Access

By default, tools are workspace-wide and available to all users. You can control access in two ways:

Workspace-wide tools (those in Company Space) won't appear in individual spaces' "Add Tools" dropdown, this is expected behavior. The tool IS accessible to all users; it doesn't need to be added again.

If you want a tool to be available only in specific spaces rather than workspace-wide:

1. First remove the tool from Company Space
2. Then add it to the specific spaces where you want it available

### Space-Based Restrictions

* Click the "Sharing" tab on any tool.
* Enable "Restricted Access".
* Select which spaces can use the tool.
* Only members of those spaces will be able to use the tool.

### Checking available tools

Users can see their available tools in the sidebar of each space under the "Tools" section.
