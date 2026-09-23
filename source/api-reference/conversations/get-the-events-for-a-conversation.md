> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get the events for a conversation

> Stream conversation events for the workspace identified by {wId} using Server-Sent Events (SSE).
The stream starts with a `:connect` comment. Event frames carry JSON with `eventId` and `data` fields. A plain-text `data: done` frame ends the current connection; clients may reconnect with `lastEventId`.




## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/assistant/conversations/{cId}/events
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
  /api/v1/w/{wId}/assistant/conversations/{cId}/events:
    get:
      tags:
        - Conversations
      summary: Get the events for a conversation
      description: >
        Stream conversation events for the workspace identified by {wId} using
        Server-Sent Events (SSE).

        The stream starts with a `:connect` comment. Event frames carry JSON
        with `eventId` and `data` fields. A plain-text `data: done` frame ends
        the current connection; clients may reconnect with `lastEventId`.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: path
          name: cId
          required: true
          description: ID of the conversation
          schema:
            type: string
        - in: query
          name: lastEventId
          required: false
          description: >-
            Redis stream ID of the last received conversation event. Omit or
            pass an empty value to start from the available history.
          schema:
            type: string
      responses:
        '200':
          description: >-
            SSE event stream with a `:connect` comment followed by conversation
            frames. Each conversation frame contains JSON with `eventId` and
            `data` fields. The `data` field is the conversation event. View the
            "Events" page from this documentation for more information.
          content:
            text/event-stream:
              schema:
                type: object
                required:
                  - eventId
                  - data
                properties:
                  eventId:
                    type: string
                    description: Redis stream ID used as the resume cursor.
                  data:
                    type: object
                    description: Conversation event discriminated by its type field.
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '404':
          description: Conversation not found.
        '500':
          description: Internal Server Error.
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````