> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# HubSpot

## Overview

HubSpot tools give your agents access to a wide range of HubSpot objects. Agents can make account summaries and create contacts, deals, opportunities, tickets, and more.

This document provides general information about our HubSpot tools (available tools, setup and authentication) but as the tool will likely evolve, the fresh list of available tools can be found when you are actually connecting the Hubspot tool in your workspace.

## Available Tools

| Tool                        | Description                                                                                                                                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Get Object Properties       | Lists all available properties for a HubSpot object. When creatableOnly is true, returns only properties that can be modified through forms (excludes hidden, calculated, read-only and file upload fields). |
| Create Contact              | Creates a new contact in Hubspot, with optional associations.                                                                                                                                                |
| Get Object By Email         | Retrieves a Hubspot object using an email address. Supports contacts, companies, deals, owners.                                                                                                              |
| Count Objects By Properties | Count objects in Hubspot with matching properties. Supports contacts, companies, deals. Max limit is 10000 objects.                                                                                          |
| Get Latest Objects          | Get latest objects from Hubspot. Supports contacts, companies, deals. Limit is 50.                                                                                                                           |
| Create Company              | Creates a new company in Hubspot, with optional associations.                                                                                                                                                |
| Create Deal                 | Creates a new deal in Hubspot, with optional associations.                                                                                                                                                   |
| Create Lead                 | Creates a new lead in Hubspot (as a Deal), with optional associations. Ensure properties correctly define it as a lead.                                                                                      |
| Create Task                 | Creates a new task in Hubspot, with optional associations.                                                                                                                                                   |
| Create Ticket               | Creates a new ticket in Hubspot, with optional associations.                                                                                                                                                 |
| Create Note                 | Creates a new note in Hubspot, with optional associations.                                                                                                                                                   |
| Create Communication        | Creates a new communication (WhatsApp, LinkedIn, SMS) in Hubspot as an engagement. Requires hs\_communication\_channel\_type in properties.                                                                  |
| Create Meeting              | Creates a new meeting in Hubspot as an engagement. Ensure hs\_engagement\_type='MEETING' and meeting details are in properties.                                                                              |
| Get Contact                 | Retrieves a Hubspot contact by its ID.                                                                                                                                                                       |
| Get Company                 | Retrieves a Hubspot company by its ID.                                                                                                                                                                       |
| Get Deal                    | Retrieves a Hubspot deal by its ID.                                                                                                                                                                          |
| Get Meeting                 | Retrieves a Hubspot meeting (engagement) by its ID.                                                                                                                                                          |
| Get File Public Url         | Retrieves a publicly available URL for a file in HubSpot.                                                                                                                                                    |
| Get Associated Meetings     | Retrieves meetings associated with a specific object (contact, company, or deal).                                                                                                                            |
| Search Crm Objects          | Searches CRM objects of a specific type based on filters, query, and properties.                                                                                                                             |

## Workspace Setup and Authentication

See [Managing Tools](/docs/user-documentation/admins/tools-management/adding-an-mcp-server) for details on how to make HubSpot tools available to your workspace. The setup will require authentication to HubSpot by the admin. Through the OAuth flow the admin will select that will be accessible by this integration.

When connecting the tool as an admin, you will be able to pick between **Personal** and **Workspace** authentication.

* **Workspace** means all agents will use the connecting admin's account when querying Hubspot
* **Personal** means users will need to authenticate the first time they use an agent that has Hubspot access and the actions will then be taken through their account (permissions, audit, etc)

## Adding HubSpot Tools to agents

HubSpot tools can be added to an agent by selecting them in the agent builder. They require no configuration. Note that when connecting a tool, you can define the provided tools as high stake or low stake.

<Warning>
  We highly recommend leaving any tool that can modify data in your CRM in HIGH
  STAKE.
</Warning>

In general you will want to mention in the instructions of your agents the objects you want them to interact with. Example instructions:

```text theme={null}
From the transcripts you are receiving, create a contact if you can't find any existing contact with the interlocutor's name or email, and if a deal has been set create a deal to attach to the current account.
```
