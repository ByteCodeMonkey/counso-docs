> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Statuspage

## Overview

The Statuspage MCP lets agents create and update incidents on your Statuspage, as well as retrieve page and component information. This is useful for automating incident management workflows, from opening an incident to posting updates, without leaving your Dust conversation.

## Connection Setup (Admin)

1. In Dust, go to **Spaces  Tools** and click **Add Tools**.
2. Select **Statuspage** from the list of available tools.
3. Provide the following required values:
   * **API Key**: your Statuspage API key.
   * **Page ID**: the ID of the target Statuspage page (found in your Statuspage account settings).
4. Save the configuration.

Once connected, the Statuspage toolset will be available to add to agents in the spaces you grant access to.

## Authentication

Statuspage authenticates requests using an API key passed as an OAuth token:

```
Authorization: OAuth <API_KEY>
```

See the official [Statuspage Authentication documentation](https://developer.statuspage.io/#section/Authentication) for details on generating API keys.

## Required Permissions and Roles

The Statuspage API key is tied to a user account. That user must have the appropriate **page roles** assigned for the target page(s):

| Role                     | Required for                                                                                                                                                                                                            |
| :----------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Incident Manager**     | Creating and updating incidents ([create](https://developer.statuspage.io/#tag/incidents/operation/postPagesPageIdIncidents), [update](https://developer.statuspage.io/#operation/patchPagesPageIdIncidentsIncidentId)) |
| **Maintenance Manager**  | Creating and updating scheduled maintenance                                                                                                                                                                             |
| **Standard page access** | Reading page details and components                                                                                                                                                                                     |

Assign roles to the user in your Statuspage account settings under **Team  Manage team members**.

**References:**

* [Statuspage Authentication and permissions](https://developer.statuspage.io/#section/Authentication)
* [Create incident endpoint](https://developer.statuspage.io/#tag/incidents/operation/postPagesPageIdIncidents)
* [Update incident endpoint](https://developer.statuspage.io/#operation/patchPagesPageIdIncidentsIncidentId)

## Available Tools

| Tool                | Description                                                                 |
| :------------------ | :-------------------------------------------------------------------------- |
| **Get Page**        | Retrieve details about your Statuspage page.                                |
| **List Components** | List all components on the page and their current statuses.                 |
| **Get Component**   | Retrieve details of a specific page component.                              |
| **Create Incident** | Create a new incident on the page, including impact, status, and body text. |
| **Update Incident** | Update an existing incident (e.g., change status, add an update message).   |
| **List Incidents**  | List active or historical incidents on the page.                            |
| **Get Incident**    | Retrieve details of a specific incident.                                    |
