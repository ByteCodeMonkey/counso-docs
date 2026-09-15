> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Dust in Teams

## Installation

### Linking Teams to your Dust Workspace

To set up the Dust app for Microsoft Teams, you'll need admin-level permissions in your
Dust workspace.

1. Navigate to your Dust workspace settings
2. Go to the Integrations section
3. Enable "Microsoft Teams Bot"
4. Follow the authentication flow to connect your Teams organization

### Adding the Dust App to Teams

Note: Only workspace administrators can install the Teams integration. Once installed,
all team members can interact with agents. Custom apps must be enabled to allow the upload of Dust app.

1. Download the teams integration from [https://office-addins.dust.tt/teams/teams-app.zip](https://office-addins.dust.tt/teams/teams-app.zip)
2. Go to the [https://admin.teams.microsoft.com/](https://admin.teams.microsoft.com/)
3. Sign in with your admin credentials
4. In the left navigation, go to Teams apps > Manage apps
5. Click Upload new app in the top menu
6. Select Upload and choose the Dust app .zip file
7. Review the app details and permissions
8. Click Add to upload the app to your organization

If your organization blocks custom apps by default:

1. In the top menu, select "Org-wide app settings"
2. Turn on Upload custom apps
3. Save the policy changes

## Interacting with Agents

### Simple agent interaction

Use the following syntax to call your agents in a channel: **@dust +agent\_name your question** or **@dust \~agent\_name your question** . If no agent name is specified, the question will go to the default agent (dust).

Examples:

* @dust What are the key points from our last quarterly review?
* @dust +code\_reviewer Please review this code snippet

### Multiple Agent Interactions

You can use multiple agents in the same conversation thread:

@dust +data\_analyst Review our sales metrics
@dust +report\_writer Create a summary based on the analysis above

### Thread Context

Dust agents understand the context of Teams conversations:

* Thread awareness: Agents can reference previous messages in the thread
* File attachments: Agents can analyze documents shared in the conversation
* Multi-participant conversations: Agents understand who said what in group chats

Privacy and Permissions

* Agents only have access to conversations where they are explicitly mentioned or linked
* All interactions follow your organization's Teams permissions and security policies

### Supported Teams Features

Team channels: Full support for public and private channels

Direct messages: One-on-one conversations with agents

File sharing: Agents can analyze shared documents

Thread replies: Contextual responses in conversation threads

Meeting integration: Not currently supported

Voice/video calls: Text-only interactions
