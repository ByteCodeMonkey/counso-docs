# Counso CLI

Use the Counso-configured CLI build provided for your workspace. Follow the installation instructions supplied with that build, then confirm it is available in your terminal:

```bash
dust --version
```

For interactive use, authenticate with the account and workspace configured for Counso:

```bash
dust login
dust status
```

The sign-in flow uses the OAuth provider configured for your Counso deployment. If the CLI is being set up by an administrator, its WorkOS domain, client ID, and claim namespace must match that deployment.

To chat with an Agent, start an interactive session and choose an Agent, or name it directly:

```bash
dust chat
dust chat --agent "My Agent"
```

The chat command is also the default when you run `dust` without a subcommand. It can access local files in the terminal session. Use `/attach` to select a file, `/clear-files` to remove attachments, `/switch` to change Agents, `/resume` to continue a conversation, and `/exit` to close the session. `/auto` toggles automatic approval of local file edits; `Shift+Tab` does the same.

For a single non-interactive message, use `--message` (`-m`). The command returns a JSON response to standard output. Add `--conversationId` (`-c`) to continue an existing conversation, and select the Agent with `--agent` (`-a`) or `--sId` (`-s`).

```bash
dust chat --agent "My Agent" --message "Summarize the latest invoices"
dust chat -a "My Agent" -m "Add a note about the next steps" -c <conversationId>
```

For scripts, CI jobs, or terminals without an interactive sign-in, configure a workspace API key and ID in the environment. Keep the key in a secrets manager or other protected configuration; do not pass it in command-line arguments or commit it to source control.

```bash
export DUST_API_KEY="<workspace-api-key>"
export DUST_WORKSPACE_ID="<workspace-id>"
dust chat --agent "My Agent" --message "Summarize the latest invoices"
```

The CLI also includes `dust skill:init`, which creates a local skill that helps coding assistants call Agents through the CLI; `dust cache:clear` clears its local startup cache. See [Skills](../../../../../en/docs/user-documentation/agents/skills/skill-examples.md) for the related concept. Use `dust help` or `dust --help` for command options, and `dust --version` to check the installed build. On Linux, credential storage may require `libsecret`: install `libsecret-1-dev` on Debian/Ubuntu, `libsecret-devel` on Red Hat-based systems, or `libsecret` on Arch Linux.
