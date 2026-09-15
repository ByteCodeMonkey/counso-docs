> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Ticket handling and support knowledge

**Audience:** Support / Ops

**Goal:** Automatically create one task per incoming ticket, let agents start resolving them, and build a collective memory of resolutions that makes every agent faster over time.

## Setup

* One Pod for the support team (e.g. "Support")
* Members: all support agents and team lead
* Visibility: Restricted
* Files tab: link the product documentation, known issues log, and escalation playbook from Company Data

## Usage

**Light: shared inbox, manual triage**

Use the Pod as a shared space for the support team. Create tasks manually for each incoming ticket and assign them to agents. When an agent hits \*\*\*\* on a task, Dust searches the Pod's Files for relevant documentation and drafts a response for the agent to review and send.

The Pod accumulates resolved tickets as conversations over time, making it progressively easier to find precedents.

**Medium: automated task creation, agent-assisted drafting**

* Set up an agent triggered on each new ticket (from Plain, Zendesk, Front, or Intercom) to create a task in the Pod with the ticket title, priority, and a link to the thread
* When a support agent hits \*\*\*\*, the agent reads the ticket, searches the Pod's files and past resolutions, and drafts a response
* The support agent reviews, adjusts, and sends; the task is marked done
* Post-shift, a scheduled agent scans all tickets resolved that day and flags any recurring patterns to the team lead

**Heavy: fully automated, self-improving support loop**

* Agents handle first-pass triage automatically: classify ticket type, search for known solutions, draft a response, and in some cases send it without human review (for well-defined, low-risk categories)
* A weekly agent reads all resolved conversations and updates the known issues log in the Files tab, keeping documentation fresh without manual effort
* A monthly agent generates a support trends report (top issue categories, resolution times, product areas generating the most friction), posted as a conversation for the team lead and shared with the product team
* New hires onboard by reading the Pod: they have access to every resolved ticket and every piece of documentation from day one

## Outcome

No ticket gets lost. Agents handle first-pass triage and drafting, humans review and send. Resolution patterns accumulate in the Pod and make every future ticket faster.
