# Use Counso from Raycast

The Raycast extension can run a Counso Agent on text selected anywhere on macOS. For supported commands, the Agent's response replaces the selected text in place, so you do not need to switch applications or copy and paste manually.

## Installation and sign-in

Install the extension supplied for your Counso deployment. Open its sign-in command, verify the Counso workspace address, and complete authorization with your Counso account. Do not install an upstream-branded extension unless it has been configured to use the Counso service URL and OAuth client.

## Agent shortcuts

The **Agent Quicklink** command lets you bind a keyboard shortcut to one Agent:

1. Open **Agent Quicklink** in Raycast.
2. Select a Counso Agent.
3. Create a Quicklink and assign a shortcut.

You can use a different shortcut for each Agent. Select text in any macOS application, press the shortcut, and review the replacement produced by the Agent. Raycast reports progress or errors through notifications.

For a regular chat that does not replace selected text, assign a Raycast alias or hotkey to the general Counso command or an Agent command.

## Publication requirement

Publish this page only after the extension package, service URL, OAuth configuration, workspace selection, and in-place text replacement have been verified against the Counso deployment.
