> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Ashby

## Overview

The Ashby MCP lets agents interact with your Ashby ATS workspace. It provides the ability to search for candidates and applications, retrieve job listings, look up users, create candidate notes, and submit referrals. All without leaving your Dust conversation.

## Connection Setup (Admin)

1. In Dust, go to **Spaces Tools** and click **Add Tools**.
2. Select **Ashby** from the list of available tools.
3. Paste your **Ashby API key** into the field provided and save.

Once connected, the Ashby toolset will be available to add to agents in the spaces you grant access to.

## Authentication

Ashby uses **HTTP Basic Auth**. The API key is passed as the Basic Auth username, with an empty password. Dust handles this automatically once you provide the API key.

See the official [Ashby Authentication documentation](https://developers.ashbyhq.com/reference/authentication) for details.

## Required API Key Permissions

In **Ashby Admin API Keys**, create or edit your API key and grant at minimum the following permissions:

| Permission area | Access level | Required for                                                                                                                      |
| :-------------- | :----------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| Candidates      | Read + Write | Search candidates, get interview feedback, get candidate notes, get application details, create candidate notes, create referrals |
| Jobs            | Read         | Internal job listing (used when creating referrals                                                                                |
| Reports         | Read         | Get report data                                                                                                                   |
| Organization    | Read         | Internal user lookup (used when creating referrals)                                                                               |
| Hiring Process  | Read         | Get referral form                                                                                                                 |

**Optional toggles**, to enable when your workspace data requires them:

* **Allow access to confidential jobs and projects**: needed if agents must read confidential job postings.
* **Allow access to non-offer private fields**: needed if agents must read private candidate fields.

For the full table of permissions and scopes, see the [Ashby Authentication documentation](https://developers.ashbyhq.com/reference/authentication).

## Available Tools

| Tool                         | Description                                                             |
| :--------------------------- | :---------------------------------------------------------------------- |
| **Search Candidates**        | Search for candidates by name, email, or other criteria.                |
| **List Candidate Notes**     | Retrieve the notes attached to a candidate's profile.                   |
| **Create Candidate Note**    | Add a new note to a candidate's profile.                                |
| **Get Application Details**  | Retrieve details of a specific application, including stage and status. |
| **Get Application Feedback** | Retrieve interview feedback submitted for an application.               |
| **Get Referral Form**        | Retrieve the referral form configuration for a job.                     |
| **Create Referral**          | Submit a new referral for a candidate to a job.                         |
| **List Jobs**                | List active job postings in your Ashby workspace.                       |
| **Run Synchronous Report**   | Execute a synchronous Ashby report and return the results.              |
| **Search Users**             | Search for users (employees/recruiters) in your Ashby organization.     |
