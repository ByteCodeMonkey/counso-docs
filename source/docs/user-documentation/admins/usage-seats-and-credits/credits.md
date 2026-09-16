> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Credits

Credits are the unit of usage on Dust. Every AI interaction (sending a message, running an agent, using a tool) consumes credits. This page explains what credits are, how they're calculated, and when usage is free.

## What is a credit?

A credit represents a unit of AI work performed on Dust. Credits are consumed whenever you interact with agents, use tools, or run automated workflows.

Credits are not transferable between users, do not roll over to the next billing period, and are not refundable.

## How credits are calculated

Each interaction consumes credits based on two components that are added together:

`total credits = token credits + action credits`

### Token credits

Token credits are proportional to the amount of AI processing involved in generating a response. More complex queries, longer contexts, and more capable models consume more token credits.

### Action credits

Action credits are a fixed amount charged per tool action, regardless of response length. Tools are grouped into 3 tiers:

| Tier         | Credits per action | Tools                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Free**     | 0 credit           | **Internal tools:** memory, agent routing, common utilities<br />**Most Orchestration helpers:** ask user question, close/edit plan, cancel wakeup, mentions<br />**Skills management:** create, update, enable skills<br />**Most Files management:** read, write, copy, move, delete files<br />**Most Pods tools:** create conversations, manage tasks, list members                                                                                                                 |
| **Basic**    | 1 credit           | **Orchestration:** run agent, create plan, schedule wakeup, create schedule<br />**Web Search:** browse a list of websites, google web search from query<br />**MiniApps:** editing, exporting, publishing, retrieving, reverting a MiniApp<br />**Pods:** create pod, semantic search, retrieve recent documents, start task agent<br />**Analytics:** usage, credits, top agents/users/skills/tools                                                                                       |
| **Advanced** | 3 credits          | **Knowledge & Retrieval:** Search, Query Tables, Data Warehouses, Include Data, Extract Data, Files, HTTP Client<br />**MiniApp Creation**<br />**Output Generation:** File Generation, Image Generation, Sound Studio, Speech Generator, Interactive Content (MiniApps), Slideshow<br />**3rd party MCP integration:** Gmail, Slack, GitHub, Notion, Google Drive, Jira, HubSpot, Salesforce, Zendesk, Fathom, Gong, Monday, Confluence, Ashby, and more<br />**All external MCP Servers** |

### Sub-agent costs

When an agent runs sub-agents in the background, each sub-agent's credit cost is added to the total. Costs accumulate across the full agent chain and are displayed alongside the main agent cost.

## When credits are not consumed

Some interactions are exempt from credit consumption:

* **Sidekick**: all Sidekick interactions (Tokens and Actions) are free and do not consume credits.

## Credit cost display

After each message, Dust shows the credit cost of that interaction directly in the conversation. This lets every member track their usage in real time without navigating to the Usage page.

The display includes the cost of the main agent response and any sub-agents that ran in the background as part of that interaction.

## Credit allocations by seat type

Each seat type includes a credit allocation (see [Seat management](/docs/user-documentation/admins/usage-seats-and-credits/seat-management) for details on seat types and how to assign them):

| Seat type     | Credits                                    |
| ------------- | ------------------------------------------ |
| **Free seat** | 500 credits (one-time lifetime allocation) |
| **Pro seat**  | 8,000 credits/month                        |
| **Max seat**  | 40,000 credits/month                       |

Credits are tied to the individual user, not the seat. Changing or unassigning a seat does not revoke credits already allocated: the user retains them and can continue consuming them until the end of their current period.

For details on how credits are drawn from different sources (individual allocation, workspace pool, overage), see [Credit management](/docs/user-documentation/admins/usage-seats-and-credits/credit-management).

## Credit reset

Individual seat credits reset monthly, on the anniversary of your subscription start date. Unused credits do not carry over to the following month.

**Free seat credits** are a one-time lifetime allocation and do not reset.
