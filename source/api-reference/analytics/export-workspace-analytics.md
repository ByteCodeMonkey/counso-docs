> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Export workspace analytics

> Export analytics data for the workspace identified by {wId} in CSV or JSON format.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/analytics/export
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
  - name: Agents
    description: Agent configurations
  - name: Apps
    description: Dust apps
  - name: Conversations
    description: Conversations
  - name: DatasourceViews
    description: Data source views
  - name: Datasources
    description: Data sources
  - name: Feedbacks
    description: Message feedbacks
  - name: MCP
    description: MCP servers
  - name: Mentions
    description: Mentions
  - name: Search
    description: Search
  - name: Tools
    description: Tools
  - name: Triggers
    description: Triggers
  - name: Skills
    description: Skills
  - name: Spaces
    description: Spaces
  - name: Workspace
    description: Workspace
  - name: Private User
    description: Private API - User
  - name: Private Authentication
    description: Private API - Authentication (WorkOS)
  - name: Private Agents
    description: Private API - Agent configurations
  - name: Private Conversations
    description: Private API - Conversations
  - name: Private Messages
    description: Private API - Messages
  - name: Private Events
    description: Private API - SSE event streams
  - name: Private Files
    description: Private API - File uploads
  - name: Private Mentions
    description: Private API - Mention suggestions
  - name: Private Spaces
    description: Private API - Spaces and data source views
  - name: Private Extension
    description: Private API - Extension configuration
  - name: Private Workspace
    description: Private API - Workspace settings
paths:
  /api/v1/w/{wId}/analytics/export:
    get:
      tags:
        - Analytics
      summary: Export workspace analytics
      description: >-
        Export analytics data for the workspace identified by {wId} in CSV or
        JSON format.
      parameters:
        - in: path
          name: wId
          required: true
          description: Unique string identifier for the workspace
          schema:
            type: string
        - in: query
          name: table
          required: true
          description: >
            The analytics table to export:

            - "usage_metrics": Messages, conversations, and active users over
            time.

            - "active_users": Daily, weekly, and monthly active user counts.

            - "source": Message volume by context origin (web, slack, etc.).

            - "agents": Top agents by message count, including credits.

            - "users": Top users by message count, including credits, last login
            date and membership status (active, revoked, unregistered).

            - "skills": Skill metadata catalog.

            - "skill_usage": Skill executions and unique users over time.

            - "tool_usage": Tool executions and unique users over time.

            - "messages": Detailed message-level logs, including comma-separated
            lists of tools (as "server__tool") and skills used per message, and
            the cost in credits of each message.

            - "feedback": Detailed message-level feedback (thumbs, content,
            conversation URL).
          schema:
            type: string
            enum:
              - usage_metrics
              - active_users
              - source
              - agents
              - users
              - skills
              - skill_usage
              - tool_usage
              - messages
              - feedback
        - in: query
          name: startDate
          required: true
          description: Start date in YYYY-MM-DD format
          schema:
            type: string
            format: date
        - in: query
          name: endDate
          required: true
          description: End date in YYYY-MM-DD format
          schema:
            type: string
            format: date
        - in: query
          name: timezone
          required: false
          description: IANA timezone name (defaults to UTC)
          schema:
            type: string
        - in: query
          name: format
          required: false
          description: Output format (defaults to csv)
          schema:
            type: string
            enum:
              - csv
              - json
      responses:
        '200':
          description: The analytics data in CSV or JSON format
          content:
            text/csv:
              schema:
                type: string
            application/json:
              schema:
                type: array
                items:
                  type: object
        '400':
          description: Invalid request query parameters
        '403':
          description: Requires an API key with admin scope
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````