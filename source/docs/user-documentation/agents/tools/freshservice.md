> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Freshservice

## Overview

The Freshservice tool provides the ability to manage tickets, submit service requests, access knowledge base articles, and handle approvals.

## Connection Setup

Connect Freshservice to Dust with a Freshservice Agent account and OAuth.

Before you start:

In **Freshservice**

1. Use a Freshservice account with the **Agent** role, not **Requester**.

2. Check that the assigned role can access **Tickets**, **Service Catalog**, **Knowledge Base**, and **Approvals**.

3. Make sure the account is not blocked by security restrictions or repeated failed sign-in attempts.

4. Review the official documentation: [Dust Freshservice guide](/docs/user-documentation/agents/tools/freshservice) and [Freshservice authentication docs](https://api.freshservice.com/#authentication).

In **Dust**:

1. go to **Spaces** -> **Tools** and select **Add Tools**.
2. Select **Freshservice** from the available MCP servers.
3. Enter your Freshservice domain URL (for example, `yourcompany.freshservice.com`).
4. Enter your Freshservice organization URL (for example, `yourcompany.myfreshservice.com`).
5. Click **Connect** to start the OAuth flow.
6. Sign in with your Freshservice **Agent** account.
7. Accept all requested OAuth scopes and complete the authorization flow.
8. Assign the tool to the relevant Dust agent so it appears in the agent's available actions.

## Available Tools

Freshservice provides the following tools:

### Ticket Management

| Tool                 | Description                                           |
| -------------------- | ----------------------------------------------------- |
| **List Tickets**     | Lists tickets with optional filtering and pagination. |
| **Get Ticket**       | Gets detailed information about a specific ticket.    |
| **Create Ticket**    | Creates a new ticket in Freshservice.                 |
| **Update Ticket**    | Updates an existing ticket's properties.              |
| **Add Ticket Note**  | Adds an internal note to a ticket.                    |
| **Add Ticket Reply** | Adds a public reply to a ticket conversation.         |

### Task Management

| Tool                   | Description                               |
| ---------------------- | ----------------------------------------- |
| **List Ticket Tasks**  | Lists all tasks associated with a ticket. |
| **Create Ticket Task** | Creates a new task on a ticket.           |
| **Update Ticket Task** | Updates an existing task's properties.    |
| **Delete Ticket Task** | Deletes a task from a ticket.             |

### Service Catalog

| Tool                        | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| **List Service Categories** | Lists all service catalog categories.                    |
| **List Service Items**      | Lists service catalog items.                             |
| **Search Service Items**    | Searches for service items by keyword.                   |
| **Get Service Item**        | Gets detailed information about a specific service item. |
| **Get Service Item Fields** | Gets the field configuration for a service item.         |
| **Request Service Item**    | Submits a service request for a catalog item.            |

### Knowledge Base

| Tool                         | Description                                                      |
| ---------------------------- | ---------------------------------------------------------------- |
| **List Solution Categories** | Lists solution categories used to organize folders and articles. |
| **List Solution Folders**    | Lists solution folders within categories.                        |
| **List Solution Articles**   | Lists articles within a specific folder.                         |
| **Get Solution Article**     | Gets the full content of a specific solution article.            |
| **Create Solution Article**  | Creates a new solution article in a specified folder.            |

### Approvals

| Tool                         | Description                                |
| ---------------------------- | ------------------------------------------ |
| **List Ticket Approvals**    | Lists all approvals for a specific ticket. |
| **Get Ticket Approval**      | Gets details of a specific approval.       |
| **Request Service Approval** | Requests approval for a ticket.            |

### Organizational Data

| Tool                       | Description                                           |
| -------------------------- | ----------------------------------------------------- |
| **List Departments**       | Lists all departments in Freshservice.                |
| **List Products**          | Lists all products/assets.                            |
| **List Requesters**        | Lists requesters with optional filtering.             |
| **Get Requester**          | Gets detailed information about a specific requester. |
| **List On-Call Schedules** | Lists on-call schedules for support teams.            |
| **List SLA Policies**      | Lists SLA policies configured in your instance.       |
| **List Purchase Orders**   | Lists purchase orders.                                |
| **List Canned Responses**  | Lists available canned responses.                     |
| **Get Canned Response**    | Gets the full content of a specific canned response.  |

### Field Discovery

| Tool                        | Description                                                         |
| --------------------------- | ------------------------------------------------------------------- |
| **Get Ticket Read Fields**  | Lists available ticket field IDs for use in read operations.        |
| **Get Ticket Write Fields** | Lists all available ticket fields for create and update operations. |

## Limitations & Considerations

* Standard Freshservice API rate limits apply (typically 1000 requests per hour per API key)
