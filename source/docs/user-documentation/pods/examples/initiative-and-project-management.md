> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Initiative and project management

**Audience:** Cross-functional teams

**Goal:** Organise a strategic initiative (product launch, hiring sprint, OKR cycle) with tasks, shared knowledge, and automated progress tracking.

## Setup

* One Pod per initiative (e.g. "Q3 Product Launch")
* Members: all DRIs and contributors
* Visibility: Restricted or Open depending on sensitivity
* Files tab: attach the brief, roadmap, and design specs; link relevant pages from Company Data
* Pod description: state the goal and success criteria clearly; agents use this as context

## Usage

**Light: shared context, manual coordination**

Use the Pod as a shared home for the initiative. Drop all relevant documents into the Files tab. Create tasks for each deliverable, assign them to DRIs, and use conversations to discuss, make decisions, and track open questions.

Anyone who joins the Pod has the full history immediately. No more "who has the latest version" or "what was decided in that meeting."

**Medium: weekly summary, Slack integration**

* Set up an agent triggered from the initiative's Slack channel to route key updates and decisions into the Pod as conversations
* Schedule a weekly agent (using the wake-up tool) to read all Pod activity and post a structured progress summary: what shipped, what's in progress, what's blocked, and what's next
* Share the weekly summary link in Slack or by email so stakeholders who are not Pod members stay informed without joining

**Heavy: fully automated initiative operating system**

* Connect your project management tools: agents create tasks in the Pod from GitHub issues, Jira tickets, or Linear items, keeping everything in sync
* Set up a pre-meeting agent that reads all open tasks and recent conversations 30 minutes before a recurring sync, and posts a ready-made agenda
* Set up a post-meeting agent triggered from a Fathom or Granola transcript to extract decisions and action items, create tasks in the Pod, and assign them to the right DRIs
* Schedule an end-of-initiative retrospective agent that reads the full Pod history and generates a structured post-mortem

## Outcome

Everyone has the same view of what's happening, what's done, and what's blocked. The Pod becomes the living record of the initiative, from kickoff to retrospective.
