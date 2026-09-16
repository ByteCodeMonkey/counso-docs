> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Wake-ups

Wake-ups enable your agents to schedule wake-up calls in the future. They are available to agents through a set of tools that they can discover automatically.

## In practice

* **Ask an agent to perform a task repeatedly**: Simply ask an agent to perform something periodically and they will set-up a wake-up based on a schedule (check a website to update internal data, or keep a MiniApp up to date every monday morning).

* **Agent ask questions and wait for answers**: Imagine an agent asks a question to soneone on Slack or Teams. Wake-ups enable them to schedule a trigger in the future to check for the answer and potentially continue their work.

* **Keep MiniApps up to date**: Ask the agent to keep the MiniApp up to date on a daily/weekly/monthly basis.

## How to create a Wake-up

Wake-ups are created by agents automatically.

<Info>
  There is nothing to do other than ask your agent.
</Info>

Agents will create wake-ups by discovering the tools automatically and deciding how to get waken-up. they can query a particular date in the future or a (cron) schedule (as an example, every Mondays and Tuesdays at 9a). You can also add the tool explicitly to an agent or from the composer to save the tool discovery work.

<Info>
  Once a wake-up is created it will be visible at all time above the composer. Conversations with a pending wake-up are also visible in the list of conversation in the left side-bar.
</Info>

## List of tools

The following tools are available to agents to manage wake-ups:

| Tool                  | Description                                                                      | Stake Level |
| --------------------- | -------------------------------------------------------------------------------- | ----------- |
| **`schedule_wakeup`** | Schedule a wake-up (with a reason) that will trigger the agent at a future time. | High        |
| **`list_wakeups`**    | List wake-ups with their status, schedule and reason.                            | Never ask   |
| **`cancel_wakeup`**   | Cancel a previously scheduled wake-up.                                           | Never ask   |

## Authentication

In the rest of this document we call the **wake-up's user** the user whose message led to the creation of a wake-up.

The authentication of the wake-up's user is used by the agent when it gets triggered in the future.

## Administration

### Setup

There is no admin setup. Wake-ups are available and enabled by default.

### Billing

Wake-ups agent executions are billed normally against the wake-up's user quota.

## Restrictions

* Other users than the wake-up's user are prevented from posting to a conversation with an active wake-up. This is to prevent steering the behavior of the agent once it gets triggered with the credentials of the wake-up's user.
* Agents can set up at most one wake-up per conversation. This is not really a restriction as the agent will be able to set up subsequent wake-ups once the current one gets triggered.
* Wake-ups based on a schedule are executed at most 32 times. This restrictions is exposed to the agent and the agent is warned when executed for the last time so that it can decide to set up a new wake-up as needed.
* Wake-ups scheduling is high-stake and require user confirmation to prevent uncontrolled blow-out usage.
