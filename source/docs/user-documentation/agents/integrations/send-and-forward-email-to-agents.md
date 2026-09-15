> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Send and Forward Email to Agents

This feature lets you involve any Dust agent in an email thread, just like you would email or cc a human colleague. Forward a message, reply to a thread, or start a fresh email: the agent reads the thread and responds in the thread (only to you).

<Info>
  **Feature activation**

  Send Email to Agents is an opt-in feature, not activated by default. You can enable it in Workspace Settings  Capabilities.
</Info>

## How it works

Once the feature is enabled by an admin, every agent in your workspace becomes reachable at the address: `agent-name@dust.team`, where `agent-name` is the agent's name in Dust, the same name you use to @mention it. Dust uses best‑effort matching, so exact spelling isn't required.

When you send or forward an email to an agent:

* The agent reads the thread, including any attachments directly present in the email you sent.
* It replies in‑thread only to you. Other to/cc recipients do not see the agent's answer.
* If the agent needs to use a tool that modifies something (e.g., creating a ticket, updating a record), it will send you a confirmation request first.

Think of email as another interface to interact with a Dust agent, similar in spirit to Slack or Teams. Once Dust matches your email to an agent, that agent keeps its usual instructions, tools, and permissions. The main difference: in addition to replying in Dust, the completed response is emailed back to you (just as a response to a message sent via Slack/Teams is propagated back there).

## Getting started

### For admins: enabling Send Email to Agents

Send Email to Agents must be explicitly activated by a workspace admin:

1. Go to Workspace Settings
2. Navigate to the Capabilities section
3. Enable "Email Agents" under Capabilities
4. Read and acknowledge the security notice

Once enabled, every agent in your workspace is reachable by email.

### For users: emailing an agent

To involve an agent in a thread:

* Direct email: Send directly to `agent-name@dust.team`
* CC on an existing thread: Add `agent-name@dust.team` to CC and reply‑all
* Forward: Forward any email to `agent-name@dust.team`, with optional instructions in the forward body

The agent will reply in‑thread, only to you.

<Warning>
  **Important**

  The agent uses your email address to verify your identity and your workspace membership. Only workspace members can trigger agents this way. Emails from non‑members are not processed.
</Warning>

## Example use cases

* Investigation: Forward a customer bug report to `incidentq@dust.team`: "investigate and summarize the root cause"
* Issue creation: CC `issuebot@dust.team`: "create a ticket for this thread with context from the linked Notion doc, assign to Jacky"
* Scheduling: CC `philassistant@dust.team`: "can you find a few available times this week?"
* CRM / ops: Send to `saleslogistics@dust.team`: "register this contract in our systems"
* Executive summary: Send to `projectbutler@dust.team`: "give an exec summary highlighting expected revenue and potential risks"

## Behavior reference

* Thread context: The agent reads the email thread and any attachments directly present in the email you sent. It does not have access to attachments from earlier messages in the thread.
* Recipients: The agent replies only to you, and cannot change the recipient list.
* Tool validation: When an action requires confirmation (e.g., writing to an external system), the agent sends the sender a private email with secure Accept / Reject links before proceeding. Other recipients are not notified.
* Errors: If something goes wrong, the agent will email the error message (only to you).
* Reply‑To: The agent always replies to the actual sender, not to a custom Reply‑To address.
* Name matching: Dust uses best‑effort matching on the agent name. `issuebot@dust.team`, `issue-bot@dust.team`, and `IssueBot@dust.team` will all resolve to the same agent, unless you actually have different agents named `issuebot` and `issue-bot` respectively.

## Security

### How your identity is verified

Dust uses standard email authentication protocols (DKIM and SPF) to verify that an email was genuinely sent from the address it claims to be from. Only emails that pass these checks are processed. This means:

* The sender must be a member of the workspace associated with the agent's address.
* Emails cannot be spoofed by a third party to impersonate a workspace member.

### What the agent can access

The agent acts with the same permissions as any Dust agent run by the sender. It reads the thread body and any attachments you forwarded to it.

### A note on security

Just as it's risky to open attachments from unknown senders, forwarding emails from untrusted sources to an agent carries risk: the agent will read and act on whatever you send it. Apply the same judgment you would before forwarding a thread to a naïve colleague.

## Restrictions & Limitations

* Prior thread attachments: The agent can read the full forwarded thread body, but only has access to attachments directly included in the email you sent, not attachments from earlier messages.
* No outbound initiation: Agents cannot initiate emails on their own. They only respond when directly addressed.
* Workspace membership required: Only emails sent by workspace members are processed. Emails from unrecognized senders are silently dropped.
* One workspace per user email: An agent address resolves to a single workspace. If a user belongs to multiple workspaces with the same email, then the most recently used paying workspace is chosen.

## FAQ

### Which agents can be reached by email?

Any active agent in your workspace, once the admin has enabled Send Email to Agents. This includes custom agents and global agents like `@dust`.

### Does an agent behave differently over email?

No. Once Dust matches your email to an agent, it runs with that agent's usual instructions, tools, and access rights. Email is just the entry and return channel: Dust turns your email into a conversation for that agent, then sends the completed answer back to you by email. The email-specific limitations on this page still apply, especially around recipients, attachments, and agent name matching.

### What if I make a typo in the agent name?

Dust uses best‑effort matching. If the name is close enough to an existing agent's name, it will resolve correctly. If no match is found, you'll receive an error email.

### Can I address multiple agents in the same email?

Yes. Add multiple agent addresses in To or CC. Each agent will process the thread independently and reply separately.

### Can my customers email agents directly?

No. Only workspace members can trigger agents via email. Emails from non‑members are silently dropped, with no error sent back to the external sender.

### Is the email content stored by Dust?

Email content is processed to generate the agent's response and is subject to Dust's standard data handling and retention policies.

### Is email usage counted as programmatic usage?

No. Emails sent by workspace members to agents are counted as regular usage, not programmatic usage, and are covered by your plan.

### Can I create a fresh email to an agent (not an existing thread)?

Yes. Sending a new email to an agent creates a fresh thread. Replies stay in that thread.

### Do agents remember the whole thread?

They process the message you send and any text your email client quotes. They don't have access to older attachments unless you re‑attach them. If you forward a thread, attachments from the last message are automatically included (but not previous ones).
