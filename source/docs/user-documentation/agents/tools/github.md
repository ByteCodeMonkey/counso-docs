> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# GitHub

## Overview

GitHub tools let your agents work with GitHub issues and pull requests. Use them to build agents that file issues when needed, or that review PRs based on internal coding rules.

This document provides general information about our GitHub tools (available tools, setup and authentication) as well as two step-by-step guides covering the creation of:

* Issue creator agents
* PR reviewer agents

## Available Tools

## Workspace Setup and Authentication

See [Managing Tools](/docs/user-documentation/admins/tools-management/adding-an-mcp-server) for details on how to make GitHub tools available to your workspace. The setup will require authentication to GitHub by the admin. Through the OAuth flow, the admin will select which repositories will be accessible by this integration.

The admin will be able to select if the tool users *personal* or *workspace* credentials.

### Workspace Credentials

All actions taken by your agents will be attributed to the [dust-agent](https://github.com/apps/dust-agent) bot.

### Personal Credentials

All actions are taken as the user who invoked the agent.

The tool only has permissions that both the user and the Dust Github app have. If the Dust Github app is installed on a repository and the user has permissions for that repository, the tool is able to take action. If the Dust Github app is not installed or the user cannot access the repository, the tool is not able to take action.

## Adding GitHub Tools to agents

GitHub tools can be added to an agent by selecting them in the agent builder. They require no configuration. Note that they have access to the repositories that were selected by the administrator that set them up for the workspace.

In general you will want to mention in the instructions of your agents the repositories you want them to interact with. Example instructions:

```text theme={null}
Our repositories are the following:
- https://github.com/dust-tt/dust (main code repository, public)
- https://github.com/dust-tt/tasks (repository used for tasks tracking, private)

If not specified the default repository to consider is our main one https://github.com/dust-tt/dust
```
