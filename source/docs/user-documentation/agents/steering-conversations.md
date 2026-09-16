> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Steering: Conversations that keep up with you

Conversations in Dust just got a major upgrade. Instead of the back-and-forth of sending a message, waiting for the agent to finish, reading the reply, and sending another, you can now interact with agents in real time. This is what’s commonly known as “steering”.

### **See what the agent is doing**

While the agent works, every step now appears live in the conversation. Thinking blocks, tool calls, searches, file operations: they show up one after another as they happen, instead of hiding behind a single activity indicator.

You can follow the agent's reasoning in real time and click on any individual action to inspect its details.

<Info>
  Every step appears as it happens. The difference:

  * **Trust the process.** When you can watch the agent work in real time, you let it run longer instead of stopping it out of uncertainty. That means better outputs.
  * **Catch issues early.** If the agent is pulling the wrong data or misreading your intent, you see it immediately, not after it's finished.
  * **Debug faster.** For agent builders, watching the reasoning unfold is the fastest way to spot where instructions are unclear or where the agent gets stuck.
</Info>

### **Redirect the agent without starting over**

You can now send a message while the agent is still working. No need to wait for it to finish. No need to cancel and lose all progress.

When you send a message mid-run:

1. Your message appears as pending in the conversation.
2. The agent finishes its current round of actions (for example, if it launched three web searches in parallel, it completes all three).
3. It picks up your message with the full context of everything before. You can even send multiple messages while the agent is running. They all get queued and picked up together.
4. It keeps going, adjusted to your new direction.

<Info>
  No waiting, no losing progress, no starting over.

  * **Think out loud.** Send additional context the moment it crosses your mind. The agent picks it up in its next step.
  * **Steer early, save time.** A quick nudge mid-run is cheaper than a full rewrite at the end.
  * **Collaborate, don't just review.** The output is shaped together, not handed off and corrected.
</Info>

<Info>
  ***Why does it finish its current step first?** Cutting the agent off mid-action would leave its reasoning in an inconsistent state. Completing the current round first means your correction actually lands cleanly.*
</Info>

### **One agent per conversation**

Conversations are now scoped to one agent at a time. The active agent is shown in the composer, so you always know who you're talking to. Just type your message, no @mention needed.

This is what makes mid-run redirection possible. For your messages to reliably reach the agent, only one can be working at a time. Previously, you could start a second agent while the first was still processing, which was a common source of confusion. That's no longer the case.

### **Stop without losing progress**

When you stop an agent, everything it's already done is kept. You only stop what comes next, you don't lose work just because you hit stop.

**Iterating on a MiniApp.** You ask an agent to build a dashboard showing monthly revenue by region. As it pulls data and starts generating the visualization, a new idea clicks: you want the APAC breakdown split out, and a bar chart would read better than a line chart. You type "make it a bar chart and split out APAC" while it's still working. The agent picks up your message and adjusts on the fly.

**Narrowing a research task.** You ask an agent for a competitor analysis. As you watch it pull sources, you decide you want to zoom in on the European market specifically. You type "focus on Europe only" while it's still searching. It finishes its current batch, reads your message, and narrows the scope, no need to start over.

**Building on a support response.** You ask an agent to draft a reply to a technical customer email. While it searches documentation, you remember the customer mentioned they're on the legacy API during yesterday's call. You type "they're on v1, not v2" to add that context. The agent folds it in and adjusts the response.

**Layering onto a data request.** You ask an agent to pull monthly churn numbers. As you watch the results take shape, you realize a retention cohort view would complete the picture. You type "add a retention cohort breakdown too" while it's still formatting. It finishes the current query and builds on what it already has.

**Sharpening a meeting briefing.** You ask an agent to prepare a briefing doc for a sales call. While it pulls account data, you think of something: the prospect mentioned a specific pain point around onboarding last quarter. You type "highlight the onboarding friction they raised in Q4." The agent weaves it in without losing the structure it already built.
