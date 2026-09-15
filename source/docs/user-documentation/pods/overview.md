> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Pods are shared workspaces where humans and agents collaborate around conversations, tasks, and files.

A **Pod** is a shared workspace inside Dust where a team (humans and agents together) collaborates around a common goal. Each Pod brings together three things in one place:

* **Conversations**: discussions with agents and teammates, visible to all Pod members and automatically indexed so agents can reference them as context
* **Tasks**: lightweight work items that anyone (human or agent) can create, assign, start an agent on, and mark done
* **Files**: the shared knowledge library of the Pod: uploaded files, folders, data linked from Company Data, and agent-generated artifacts such as [Frames](/docs/user-documentation/pods/frames)

A core principle of Pods: **everything a human can do, an agent can do**. Agents can start conversations, create and complete tasks, and save files in a Pod, with or without a human in the loop.

## The Pods skill

Agents interact with Pods through the **Pods skill**, which is available to all agents by default, including the global Dust agent, agents invoked inside a Pod, and triggered agents. The skill provides a set of tools that let agents:

* List and look up Pods by name
* Create and post to conversations in a Pod
* Create, pick up, progress, and complete tasks
* Upload and read files in the Pod's Files tab
* Search the Pod's knowledge and link data from Company Data
* Create Pods and manage members, settings, and the pinned Frame (with Editor permissions)

For the complete list of tools and what each one does, see [Agent tools](/docs/user-documentation/pods/agent-tools).

This makes Pods a natural target for automations: a triggered agent can post a daily brief into a Pod, open a conversation when a ticket arrives, or keep Pod tasks in sync with an external tool. See [Conversations](/docs/user-documentation/pods/conversations) and [Tasks](/docs/user-documentation/pods/tasks) for concrete patterns.

## Visibility: Open and Restricted Pods

| Visibility     | Who can access                                                       |
| -------------- | -------------------------------------------------------------------- |
| **Open**       | Any workspace member can browse the Pod's content and join instantly |
| **Restricted** | Only invited members can see and participate; an Editor must add you |

Workspace admins can restrict Pod creation to Restricted Pods only. See [Admin controls](/docs/user-documentation/pods/admin-controls).

## Members and roles

Every Pod member is either a **Member** or an **Editor**. Members participate in conversations, tasks, and files; Editors additionally manage membership, settings, visibility, and can pin Frames as the Pod banner. See [Members and roles](/docs/user-documentation/pods/members-and-roles).

## Where to go next

* [Getting started](/docs/user-documentation/pods/getting-started): create your first Pod
* [Conversations](/docs/user-documentation/pods/conversations): collaborate with agents and teammates
* [Tasks](/docs/user-documentation/pods/tasks): define, assign, and automate work
* [Files](/docs/user-documentation/pods/files): build the Pod's shared knowledge library
* [Frames](/docs/user-documentation/pods/frames): pin live dashboards as the Pod banner
* [Agent tools](/docs/user-documentation/pods/agent-tools): the full list of tools agents get through the Pods skill
* Examples: [Shared asset library](/docs/user-documentation/pods/examples/shared-asset-library), [One Pod per customer](/docs/user-documentation/pods/examples/one-pod-per-customer), [Initiative and project management](/docs/user-documentation/pods/examples/initiative-and-project-management), and more
