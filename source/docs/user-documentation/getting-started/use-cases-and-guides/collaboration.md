> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# 🧑‍🤝‍🧑 Collaboration

## How to use Dust for team collaboration?

In Dust, users and AI agents work together in shared conversations through mentions, notifications, and conversation sharing. These features keep everyone in the loop and let agents escalate to the right people when needed.

| Use Case                                     | Mission                                                                                                                     |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Mention colleagues in conversations          | Bring team members into a conversation by `@mentioning` them, automatically adding them as participants and notifying them. |
| Share conversations with your team           | Share a conversation with colleagues so they can join, contribute, and work alongside you and the agents.                   |
| Agent escalation to users                    | Configure agents to identify when human input is needed and mention the right person to handle it.                          |
| Track conversations requiring your attention | Use your inbox to see unread conversations and those requiring your action, so nothing falls through the cracks.            |

## Tutorial & Guides

## 1. Mention Colleagues in Conversations

Bring team members into a conversation by `@mentioning` them. When you mention someone, they're automatically added as a participant and receive a notification.

**How to mention a user:**

1. In the composer, type `@` to open the mention picker
2. Search for a colleague by name
3. Select their name to insert the mention
4. Send your message - they'll be notified instantly

## 2. Share Conversations with Your Team

Share a conversation so colleagues can join and collaborate with you and the agents. Shared conversations allow multiple people to interact with the same agents and see the full conversation history.

**How to share:**

1. Go to the conversation you want to share
2. Click **'Copy the link'** at the top right
3. Share the link with your colleagues, to let them access the conversation and participate

**Tip:** Combine sharing with mentions to notify specific people that a conversation needs their attention.

## 3. Agent Escalation to Users

Configure agents to identify situations requiring human input and mention the appropriate team member. This is ideal for support escalations, approval workflows, or when expert knowledge is needed.

**How to set up escalation:**

1. Create or edit an agent
2. Add instructions telling the agent when and whom to mention

**Example instructions:**

```
When you encounter a question you cannot answer confidently, or when the user
explicitly requests human help look for human help

For technical questions, ping @engineer. For billing questions, ping @finance person.
```

## 4. Track Conversations Requiring Your Attention

Your conversation sidebar shows visual indicators to help you quickly identify what needs attention:

| Indicator        | Meaning                                             |
| ---------------- | --------------------------------------------------- |
| Blue dot         | Unread - new messages since you last viewed         |
| Yellow indicator | Action required - someone is waiting for your input |
| No indicator     | Read - you're up to date                            |

**Managing your conversations:**

* Conversations are **automatically marked as read** when you view them
* **Leave** a conversation you no longer need to follow
* **Join** a conversation you want to participate in
* **Delete** a conversation to remove it from your history

  **Email notifications:** If you have unread messages, you'll receive an email digest with links to conversations needing your attention. You can set up your notification preferences in your Profile.

## 5. Who Has Access to My Conversation?

Understanding who can see your conversations helps you work confidently and share appropriately.

### Access Rules

| Scenario                  | Who Can Access                                                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Standard conversation** | Only you, unless you share it or mention someone                                                                       |
| **Shared conversation**   | You + anyone you've shared the link with who joins (they must also have access to the agents used in the conversation) |
| **Mentioned colleagues**  | You are asked to confirm before they are added. Once confirmed, they see the full history and can reply                |

### Key Points

* **Your conversations are private by default.** When you start a conversation, only you can see it.
* **Sharing requires agent access.** When you share a conversation link, colleagues can only join if they have access to the agents used in the conversation.
* **Mentions require your approval.** When an agent mentions a colleague, you'll see a prompt asking "Do you want to invite them?". They are only added once you approve.
* **Participants list.** You can see who has access to a conversation by viewing the participants.

  **Tip:** When sharing a conversation that uses agents from restricted Spaces, make sure the person you're sharing with has access to those Spaces; otherwise they won't be able to join.

### What Admins Can See

Workspace administrators can view aggregate usage analytics (like message counts and active users) but **cannot read the content of your conversations**. Your conversation content remains private.

## Best Practices

**For users:**

* Use mentions sparingly to avoid notification fatigue
* Mention specific people when their expertise is genuinely needed
* Check your inbox regularly for conversations requiring your attention

**For agent builders:**

* Only enable user mention tools when escalation is a key part of the workflow
* Include clear instructions on when agents should mention users
* Consider using mentions for: escalation workflows, approval requests, and expert consultations
