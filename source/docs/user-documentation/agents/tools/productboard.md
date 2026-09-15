> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Productboard

## Use Case Examples

<Cards columns={3}>
  <Card title="Capture Feedback & Notes">
    Create Productboard notes from conversations, and link them to users, companies, and features for structured triage.
  </Card>

  <Card title="Backlog Prioritization">
    Filter and sort features by status, impact, owner, or timeframe, then update fields to keep your backlog healthy.
  </Card>

  <Card title="Roadmap & Release Planning">
    Pull entities by objective or release, review relationships, and set statuses or timelines to prepare roadmap updates.
  </Card>

  <Card title="Research & Insights">
    Query notes by date range, owner, tags, or source to surface themes, trends, and product opportunities.
  </Card>

  <Card title="Dependencies & Relationships">
    Inspect parent/child and blocking links between entities to assess scope, sequencing, and delivery risk.
  </Card>

  <Card title="Customer & Company Context">
    Explore linked customers and related work to understand impact, prioritize requests, and close the loop.
  </Card>
</Cards>

## Admin Setup in Dust

Go to Spaces > Administration > Tools in your Dust workspace, click Add Tools, and select Productboard.

### Authentication

Productboard uses OAuth-based authentication. You’ll be redirected to sign in and grant access. The tools support  workspace-level credentials or individual user credentials.

## Available Tools

| **Name**          | **Description**                                                                                                                                      |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| Get Configuration | Discover configuration for note and entity types, including required fields, supported values, and allowed operations.                               |
| Create Note       | Create a Productboard note (simple or conversation) with optional relationships to customers (users/companies) or external links.                    |
| Update Note       | Update an existing note using full field replacement or granular patch operations (e.g., owner, tags, archived, processed, name, content).           |
| Get Note          | Retrieve a note by ID with optional field selection to limit the returned data.                                                                      |
| Query Notes       | Search notes (newest first) with filters for archived/processed, owner/creator, dates, source record, and pagination.                                |
| Query Entity      | Search entities (product, component, feature, subfeature, initiative, objective, keyResult, release, releaseGroup, company, user) with rich filters. |
| Create Entity     | Create entities across the Productboard hierarchy; optionally set relationships (parent, child, link, isBlockedBy, isBlocking).                      |
| Update Entity     | Update entities via full field replacement or patch operations, following the per-field capabilities defined by configuration.                       |
| Get Relationships | Retrieve relationships for an entity (e.g., parent, child, link, blocking) with pagination support to explore the product graph.                     |
