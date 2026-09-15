> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Conversations

The **Conversations tab** lists all conversations created inside the Pod. Every Pod member can see and contribute to them.

## How to start a conversation in a Pod

**As a human:**

1. Open the Pod and click the **Conversations** tab
2. Type your message in the composer and mention an agent with `@`
3. Press **Enter**. The conversation is created inside the Pod and visible to all members

**As an agent:**

Agents can create and post to conversations in a Pod directly, for example to share a progress update, post a weekly summary, or surface findings from a background task. These conversations appear in the same list and are visible to all members. This is made possible by the **Pods skill**, which is available to all agents by default. See [Agent tools](/docs/user-documentation/pods/agent-tools) for the full list of tools the skill provides.

<Info>
  **Every conversation in a Pod is automatically indexed. Agents can search and reference past conversations as context, without you doing anything.**

  **Mentioning people**
</Info>

Use `@` to mention both agents and teammates in a conversation.

* **Mentioning an agent** triggers the agent to respond in the conversation
* **Mentioning a teammate** sends them a notification and draws their attention to the message

If you mention someone who is not yet a member of the Pod, Dust will prompt you to add them. See [Members and roles](/docs/user-documentation/pods/members-and-roles) for details on who can add members.

## Triggering a conversation from an external source

It is possible to have an external event (a ticket, a webhook, a scheduled trigger, a Slack message) automatically create a conversation inside a specific Pod.

This is done by setting up a **triggered agent** and instructing it to create or post to a specific Pod:

1. Create a triggered agent (e.g. from a Jira webhook, a Slack trigger, or the wake-up tool)
2. In the agent's instructions, specify which Pod to post into. The agent can look it up by name using the Pods skill's `list_pods` tool
3. When triggered, the agent creates a conversation in the target Pod with the relevant context

Common patterns:

* **From a ticketing system**: a new Jira ticket or Plain thread triggers an agent that opens a conversation in the Support Pod with the ticket details
* **On a schedule**: the wake-up tool triggers an agent each morning to post a daily brief into a Pod
* **From a Slack message**: a Slack trigger fires an agent that posts the message (or a summary of it) into the relevant Pod

<Info>
  **The Pods skill is available to all agents by default, including the global Dust agent, agents invoked inside a Pod, and triggered agents.**

  **Finding conversations**
</Info>

In multi-member Pods, a filter bar lets you narrow the list:

| Filter             | Shows                                                          |
| ------------------ | -------------------------------------------------------------- |
| **Mine**           | Conversations where you have sent a message                    |
| **Group**          | Conversations involving more than one person                   |
| **All**            | Every conversation in this Pod                                 |
| **Hide triggered** | Hides conversations created by triggered agents from your list |

**Hide triggered** is a per-user, per-Pod preference. It only changes the conversations shown in your own list; it does not hide them from other Pod members.

Triggered conversations are marked with a **⚡** at the start of their title, so you can identify conversations created by automations.

A search bar above the list lets you search conversation content across the whole Pod.

## Joining an Open Pod

If you are not yet a member of an Open Pod, you will see a prompt at the bottom of the Conversations tab:

* **Open Pod:** "Join this Pod to participate in conversations." Click **Join the \[Pod name] Pod** to join instantly
* **Restricted Pod:** "You need to be invited to participate in this Pod." There is no join button; an Editor must invite you

## Notification preferences

Each member can configure their notification preferences independently, per Pod.

**How to configure notifications for a Pod:**

1. Open the Pod
2. Click the `...` button in the top-right header
3. Select your preferences:
   * **New conversations**: `All` or `Never`
   * **New messages**: `All`, `Mentions only`, or `Never`

Notification channels (in-app, Slack, email) are configured once globally in your profile settings.
