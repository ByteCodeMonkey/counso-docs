> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Dust CLI

## Installation

Install the Dust CLI globally via `npm`:

```
npm install -g @dust-tt/dust-cli
```

### Linux

The CLI depends on [`keytar`](https://www.npmjs.com/package/keytar) for storing credentials. On Linux, `keytar` requires `libsecret`:

* **Debian / Ubuntu:** `sudo apt-get install libsecret-1-dev`
* **Red Hat-based:** `sudo yum install libsecret-devel`
* **Arch Linux:** `sudo pacman -S libsecret`

## Usage

```
dust [command] [options]
```

When no command is provided, the `chat` command runs by default, opening an interactive chat with `@Dust` with access to your local filesystem.

## Available commands

### `login`

Authenticate with your Dust account.

```
dust login
dust login --force    # Force re-authentication even if already logged in
```

### `status`

Check your current authentication status.

```
dust status
```

### `logout`

Log out from your Dust account.

```
dust logout
```

### `chat`

Chat with a Dust agent. This is the **default command**: running `dust` with no arguments opens an interactive chat session.

```
dust chat
dust              # equivalent
```

**Flags:**

| Flag                    | Short | Description                                                                             |
| ----------------------- | ----- | --------------------------------------------------------------------------------------- |
| `--sId <sId>`           | `-s`  | Select an agent by its sId (system identifier).                                         |
| `--agent <name>`        | `-a`  | Select an agent by name (e.g. `--agent "My Agent"`).                                    |
| `--auto`                |       | Automatically accept all file edit operations without prompting.                        |
| `--message <text>`      | `-m`  | Send a single message in **non-interactive mode** and return a JSON response to stdout. |
| `--conversationId <id>` | `-c`  | Continue an existing conversation (non-interactive mode only).                          |

**Examples:**

```bash theme={null}
# Interactive: pick an agent by name
dust chat --agent "My Agent"

# Non-interactive: single message, JSON response on stdout
dust chat --agent "My Agent" --message "Summarize Q4 metrics"

# Non-interactive: continue an existing conversation
dust chat -a "My Agent" -m "Add a bullet for next steps" -c <conversationId>
```

<Info>
  **Billing note:** Interactive CLI chat (typing in the terminal UI) counts as regular human usage. Non-interactive messages (`--message`) count as [programmatic usage](/docs/user-documentation/admins/usage-seats-and-credits/credit-management#programmatic-usage) and consume credits.
</Info>

### `skill:init`

Set up a [Claude Code / Anthropic skill](https://code.claude.com/docs/en/skills) on your local coding agent (Claude Code, Codex, etc.) that teaches it how to use the Dust CLI to talk to Dust agents.

```
dust skill:init
```

Running this scaffolds a `SKILL.md` in the appropriate `.claude/skills/` directory. Once installed, your coding agent gains a skill explaining how to call Dust agents non-interactively (e.g. `dust chat -a <agent> -m "..."`), making it easy to pull context from Dust, post Slack messages, read Notion pages, and more, all from within your coding workflow.

<Note>
  For more on how Dust Skills relate to Anthropic/Claude Skills, see the [Skills documentation](/docs/user-documentation/agents/skills/skill-examples) and the [Anthropic skills repository](https://github.com/anthropics/skills).
</Note>

### `cache:clear`

Clear the local CLI cache used for faster startup.

```
dust cache:clear
```

### `help`

Display help information.

```
dust help
```

## In-chat commands

While in an interactive chat session, type these with a forward slash:

| Command        | Description                                                                   |
| -------------- | ----------------------------------------------------------------------------- |
| `/exit`        | Exit the chat session.                                                        |
| `/switch`      | Switch to a different agent.                                                  |
| `/resume`      | Resume a previous conversation.                                               |
| `/attach`      | Open a file selector to attach a local file.                                  |
| `/clear-files` | Clear any attached files.                                                     |
| `/auto`        | Toggle auto-approval of file edits on/off (also available via **Shift+Tab**). |

## Global options

| Flag              | Description                               |
| ----------------- | ----------------------------------------- |
| `-v`, `--version` | Display the installed CLI version.        |
| `--help`          | Display help information for any command. |

## Headless authentication

For automated workflows, CI/CD pipelines, or environments without interactive terminals, the CLI supports headless authentication.

### Method 1: Environment variables (recommended)

```bash theme={null}
export DUST_API_KEY="sk_your_api_key_here"
export DUST_WORKSPACE_ID="ws_abc123"

dust chat                          # uses env vars automatically
```

### Method 2: Command-line flags

```bash theme={null}
dust chat --wId ws_abc123 --api-key sk_your_api_key_here
```

| Parameter    | Env variable        | CLI flag    | Description                      |
| ------------ | ------------------- | ----------- | -------------------------------- |
| API key      | `DUST_API_KEY`      | `--api-key` | Your API key for authentication. |
| Workspace ID | `DUST_WORKSPACE_ID` | `--wId`     | Your workspace ID.               |

<Note>
  Command-line flags take precedence over environment variables.
</Note>

### Security considerations

* Prefer environment variables over CLI flags; flags may be visible in process listings.
* Store API keys securely; avoid committing them to version control.
* Use `.env` files locally and proper secrets management in CI/CD.
