> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Export consumption analytics

> Export per-call consumption analytics for the workspace identified by {wId}.
Each row represents one unit of billed credit consumption (an LLM call or a tool call).
The export can be filtered by various dimensions (agents, users, API keys, groups, models, tools, skills, sources, tags).
The export is limited to a maximum of 30 days per request and times out after 10 seconds: reduce the time range
or apply filters to reduce the number of rows if you encounter a timeout.
Results are streamed, if an error occurs, an error message is appended and the stream is closed.




## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/v1/w/{wId}/analytics/consumption/export
openapi: 3.0.0
info:
  title: DUST API Documentation
  version: 1.0.2
  description: The OpenAPI specification for the Dust.tt API
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT
servers:
  - url: https://dust.tt
    description: Dust.tt API (us-central1)
  - url: https://eu.dust.tt
    description: Dust.tt API (europe-west1)
security: []
tags:
  - name: Users
    description: User management
  - name: Agents
    description: Agent configurations
  - name: Analytics
    description: Workspace analytics
  - name: Apps
    description: Dust apps
  - name: Conversations
    description: Conversations
  - name: Datasources
    description: Data sources
  - name: DatasourceViews
    description: Data source views
  - name: Feedbacks
    description: Message feedbacks
  - name: MCP
    description: MCP servers
  - name: Mentions
    description: Mentions
  - name: Search
    description: Search
  - name: Skills
    description: Skills
  - name: Spaces
    description: Spaces
  - name: Tools
    description: Tools
  - name: Triggers
    description: Triggers
  - name: Workspace
    description: Workspace
  - name: Private Agents
    description: Private API - Agent configurations
  - name: Private Authentication
    description: Private API - Authentication (WorkOS)
  - name: Private Conversations
    description: Private API - Conversations
  - name: Private Events
    description: Private API - SSE event streams
  - name: Private Extension
    description: Private API - Extension configuration
  - name: Private Files
    description: Private API - File uploads
  - name: Private Mentions
    description: Private API - Mention suggestions
  - name: Private Messages
    description: Private API - Messages
  - name: Private Spaces
    description: Private API - Spaces and data source views
  - name: Private User
    description: Private API - User
  - name: Private Workspace
    description: Private API - Workspace settings
paths:
  /api/v1/w/{wId}/analytics/consumption/export:
    post:
      tags:
        - Analytics
      summary: Export consumption analytics
      description: >
        Export per-call consumption analytics for the workspace identified by
        {wId}.

        Each row represents one unit of billed credit consumption (an LLM call
        or a tool call).

        The export can be filtered by various dimensions (agents, users, API
        keys, groups, models, tools, skills, sources, tags).

        The export is limited to a maximum of 30 days per request and times out
        after 10 seconds: reduce the time range

        or apply filters to reduce the number of rows if you encounter a
        timeout.

        Results are streamed, if an error occurs, an error message is appended
        and the stream is closed.
      parameters:
        - in: path
          name: wId
          required: true
          description: Unique string identifier for the workspace
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - startDate
                - endDate
              properties:
                startDate:
                  type: string
                  format: date-time
                  description: Start of the time range (inclusive), ISO 8601 datetime
                  example: '2026-01-01T00:00:00Z'
                endDate:
                  type: string
                  format: date-time
                  description: >-
                    End of the time range (exclusive), ISO 8601 datetime. Must
                    be after startDate, at most 30 days apart.
                  example: '2026-01-15T00:00:00Z'
                format:
                  type: string
                  enum:
                    - csv
                    - ndjson
                  description: Output format (defaults to csv)
                filter:
                  type: object
                  description: >
                    Optional dimension filters. Each key maps to an array of
                    string identifiers to include.

                    Each value must be at most 256 characters. The total number
                    of values across all dimensions must not exceed 500.
                  properties:
                    agents:
                      type: array
                      items:
                        type: string
                        maxLength: 256
                      description: Agent sIds to filter on
                    users:
                      type: array
                      items:
                        type: string
                        maxLength: 256
                      description: User IDs to filter on
                    api_keys:
                      type: array
                      items:
                        type: string
                        maxLength: 256
                      description: API key names to filter on
                    groups:
                      type: array
                      items:
                        type: string
                        maxLength: 256
                      description: Group IDs to filter on
                    models:
                      type: array
                      items:
                        type: string
                        maxLength: 256
                      description: Model IDs to filter on
                    tools:
                      type: array
                      items:
                        type: string
                        maxLength: 256
                      description: Tool server names to filter on
                    skills:
                      type: array
                      items:
                        type: string
                        maxLength: 256
                      description: Skill IDs to filter on
                    sources:
                      type: array
                      items:
                        type: string
                        maxLength: 256
                      description: >-
                        Context origins to filter on (e.g. "web", "slack",
                        "api")
                    tags:
                      type: array
                      items:
                        type: string
                        maxLength: 256
                      description: Agent tag IDs to filter on
      responses:
        '200':
          description: The consumption data in CSV or NDJSON format
          content:
            text/csv:
              schema:
                type: string
            application/x-ndjson:
              schema:
                type: string
                description: Newline-delimited JSON, one row object per line
        '400':
          description: >-
            Invalid request body (missing fields, invalid dates, range exceeds
            30 days)
        '403':
          description: Requires an API key with admin scope
        '500':
          description: Internal Server Error
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````