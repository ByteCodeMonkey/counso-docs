> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Gmail

## Overview

Connect Gmail to Dust agents to read messages, create drafts, and send emails using user credentials.

<Info>
  The Gmail tool interacts with Gmail using each user's account, adapting to
  individual access permissions.
</Info>

Navigate to Spaces > Tools in your Dust workspace, click `Add Tools`, and select Gmail.

The setup redirects you to an `OAuth flow` to connect an admin Gmail account. Dust uses the admin account only during setup. Users cannot query Gmail from the admin account.

The Gmail tool is added to the Company data Space, making it accessible across the entire workspace.

In the @Agent Builder, click `Add Tool` and select Gmail.

When users first use an agent with the Gmail tool, a connection error appears:

Click the `Connect` button.

\*\* Note:\*\* Gmail tools with High or Medium stake levels require user approval. See the "Tool Control & Automation" section below for more information on managing approvals.

The Gmail tool provides the following capabilities:

| Tool                     | Description                                                               | Stake Level |
| ------------------------ | ------------------------------------------------------------------------- | ----------- |
| **`get_messages`**       | Retrieves messages from Gmail inbox with support for Gmail search queries | Never ask   |
| **`get_attachment`**     | Retrieves the content of a specific attachment from a Gmail message       | Never ask   |
| **`get_drafts`**         | Retrieves all drafts from Gmail                                           | Never ask   |
| **`create_draft`**       | Creates a new email draft in Gmail                                        | Medium      |
| **`create_reply_draft`** | Creates a reply draft to an existing email thread in Gmail                | Medium      |
| **`delete_draft`**       | Deletes a draft email from Gmail                                          | Low         |
| **`send_mail`**          | Sends an email directly from Gmail *(new)*                                | High\*      |

\*\* Note:\*\*`send_mail` is disabled by default on existing workspaces. Admins must manually enable it in **Spaces > Tools > Gmail**. It is enabled by default on new Gmail tool installations.

Gmail tools use specific approval levels ("stakes") to control automation:

* **High stake** (e.g., `send_mail`): Requires explicit user approval every time the tool is used
* **Medium stake** (e.g., `create_draft`, `create_reply_draft`): Requires approval once per agent + recipient combination. Once approved, the agent can repeat the action without interruption for that specific combination
* **Low stake** (e.g., `delete_draft`): Users can disable confirmations
* **Never ask** (e.g., `get_messages`, `get_drafts`): Executes automatically without confirmation

Admins can modify the stake level of each tool in **Spaces > Tools > Gmail** to match their team's workflows and risk tolerance.

**Learn more about tool management and stake levels in the [Tools Management documentation](/docs/user-documentation/admins/tools-management/adding-an-mcp-server).**

<Warning>
  Dust is not designed for bulk email campaigns. Using it for mass outreach can
  harm your domain's email reputation, affecting deliverability across your
  entire organization. Keep automation targeted and workflow-driven for best
  results.
</Warning>
