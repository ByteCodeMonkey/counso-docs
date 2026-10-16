# Use Agents in Microsoft Teams

If the Microsoft Teams integration is enabled for your workspace, members can interact with Agents in Teams channels and chats. A workspace administrator connects the organization and installs the app package approved for your deployment. Do not install a package from an unverified source.

## Connect Teams

1. In workspace settings, open **Integrations** and enable **Microsoft Teams** if the option is available.
2. Complete the authentication flow for the intended Teams organization.
3. A Teams administrator opens the Teams admin center, goes to **Teams apps > Manage apps**, and uploads or approves the organization-provided Counso app package if custom app upload is required. Review its permissions before allowing the organization to use it.
4. Add the app to the intended team or conversation and test with a non-sensitive question.

## Call an Agent

In a channel or chat, mention the configured Counso app and select the Agent. In workspaces that use the `+` agent syntax, send a message such as `@Counso +data-analyst Review these sales metrics`. If no Agent is selected, the default Agent may answer. The mention label can depend on how the app is installed in Teams.

Agents can use the current Teams thread as context and may analyze supported file attachments. Multiple Agents can be called in sequence in the same thread; each response can use the earlier thread context. Interactions follow the workspace's Agent and data permissions.

## Supported interaction

The integration is designed for text interactions in channels, private channels, and direct chats where enabled. Meeting audio and voice/video calls are not part of this flow. Before using an Agent in a group conversation, confirm that all participants are intended to see its answer and any cited information.
