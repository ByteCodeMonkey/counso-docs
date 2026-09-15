> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Computer admin setup

This page explains how workspace admins can configure Computer. For an overview of what Computer does for users and builders, see [Computer](/docs/user-documentation/agents/tools/computer).

The Computer admin page controls workspace-level network access and environment variables for Computer. Only workspace admins can manage these settings.

If Computer administration is not enabled for your workspace, the page will show a message explaining that Computer administration is not enabled.

## What admins can configure

Admins can configure two areas:

* **Network access**, which controls which websites and APIs Computer can contact.
* **Environment variables**, which provide configuration values or HTTPS secrets to Computer.

## Configure network access

Computer does not have open internet access by default. The Network section lets admins decide which domains are trusted for the workspace.

To add a domain:

1. Open the **Computer** admin page.
2. Go to the **Network** section.
3. Find **Allowed domains**.
4. Enter a trusted domain.
5. Click **Add domain**.

You can add exact domains such as:

```text theme={null}
api.openai.com
```

You can also add wildcard domains such as:

```text theme={null}
*.mistral.ai
```

Allowed domains apply to every Computer in the workspace. Changes are typically picked up within around 60 seconds. Invalid or duplicate domains are rejected before saving.

To remove a domain, use the delete action next to that domain in the allowed domains list.

<details>
  <summary>Technical detail: wildcard domains</summary>

  Use exact domains such as `api.openai.com` or wildcard subdomains such as `*.mistral.ai`. A wildcard covers subdomains. For example, `*.github.com` covers `api.github.com` and `a.b.github.com`, but not `github.com` itself. Add both entries if both are needed.
</details>

## Allow or disable user-approved domains

The **Agent-requested domains** toggle controls whether agents can ask users to approve additional domains during a conversation.

When this setting is disabled, agents cannot request new domains. They must rely on the workspace allowed domains configured by admins.

When this setting is enabled, an agent using Computer can ask the user to approve an additional domain during the conversation. Each request is approval-gated. If the user approves, that domain becomes available only for the current Computer. It does not change the workspace allowlist.

<Warning>
  When Agent-requested domains is enabled, a non-admin user can grant temporary network access to a domain that admins did not preapprove. Enable it when you want users to unblock one-off API or website access during a conversation. Keep it disabled when every allowed domain should be reviewed by an admin first.
</Warning>

To change this setting:

1. Open the **Computer** admin page.
2. Go to the **Network** section.
3. Find **Agent-requested domains**.
4. Turn the toggle on or off.
5. When turning it on, confirm that users will be able to grant temporary access to additional domains.

## Add configuration variables

Configuration variables are for non-sensitive values that Computer can read directly, such as public endpoints, regions, identifiers, feature flags, or model names.

Do not use configuration variables for credentials. They are mounted as plain environment variables on every new Computer and can be read by the agent and by code running in Computer. Anything you put in a configuration variable should be safe to log.

To add a configuration variable:

1. Open the **Computer** admin page.
2. Go to **Environment variables**.
3. Click **Add variable**.
4. Choose **Config**.
5. Enter a name suffix using uppercase letters, digits, and underscores.
6. Paste the value.
7. Save.

Configuration variable names use the `DST_` prefix.

Example use cases:

* A public API base URL.
* A region name.
* A non-secret identifier.
* A default model name.

## Add HTTPS secrets

HTTPS secrets are for credentials such as API keys and tokens. They are safer than configuration variables because Computer does not see the raw secret value.

Inside Computer, an HTTPS secret appears as a placeholder. When Computer makes an approved HTTPS request to a domain configured for that secret, Dust substitutes the real secret on the way out.

To add an HTTPS secret:

1. Open the **Computer** admin page.
2. Go to **Environment variables**.
3. Click **Add variable**.
4. Choose **HTTPS secret**.
5. Enter a name suffix using uppercase letters, digits, and underscores.
6. Paste the secret value.
7. Add at least one allowed domain, for example `api.openai.com` or `*.mistral.ai`.
8. Save.

HTTPS secret names use the `DSEC_` prefix.

<Info>
  Values are write-only after saving. Admins can replace or delete them, but cannot view the saved value.
</Info>

<details>
  <summary>Technical detail: how HTTPS secrets are used</summary>

  Config values are mounted as normal environment variables. HTTPS secrets are represented as placeholders inside Computer. The raw secret is not available to code running in Computer. Dust substitutes the real value only for approved outbound HTTPS requests to domains configured for that secret.
</details>

## Promote a configuration variable to an HTTPS secret

If you already created a configuration variable that should be treated as a credential, promote it to an HTTPS secret by configuring allowed domains for it.

Promotion is one-way: use HTTPS secrets for credentials going forward.

<Info>
  Promotion takes effect for new Computers. Already-running Computers keep their previous environment values until they are restarted.
</Info>

## Rotate or delete variables

Saved values cannot be viewed after saving. To update a value, replace it. To remove a value, delete it.

New Computers receive the latest settings. Already-running Computers keep the values they started with.

<details>
  <summary>Technical detail: when settings apply</summary>

  Workspace allowed domain changes are typically picked up within around 60 seconds. Environment variables are snapshotted when a Computer starts. A running Computer keeps its original variables, while new Computers pick up the latest settings.
</details>

## Troubleshooting

### The agent says a domain is blocked

Add the domain to **Allowed domains**, or enable **Agent-requested domains** so the user can approve it for the current conversation.

### A request returns `401` or `403`

This usually means the external service rejected the credentials or permissions. It does not usually mean Dust blocked the domain. Check the credentials, scopes, and permissions for the external service.

### A newly added domain still fails

Wait around 60 seconds and retry. Domain allowlist changes may take a short time to apply.

### A new environment variable is not visible in an existing conversation

Environment variables are loaded when a Computer starts. Start a new conversation or restart Computer so it picks up the latest values.

### A secret cannot be added

Make sure the secret has at least one allowed domain. HTTPS secrets require allowed domains because the credential should only be sent to the services it is meant for.

### The admin page is unavailable

Make sure Computer administration is enabled for the workspace and that you are a workspace admin.
