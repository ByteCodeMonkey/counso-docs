> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Stream MCP tool requests for a workspace

> [Documentation](https://docs.dust.tt/docs/client-side-mcp-server)
Server-Sent Events (SSE) endpoint that streams MCP tool requests for a workspace.
This endpoint is used by client-side MCP servers to listen for tool requests in real-time.
Events arrive as new tool requests are made. Reconnect with `lastEventId` after the stream closes to continue receiving events.
The stream starts with a `:connect` comment. Request frames carry JSON with `eventId` and `data` fields. A plain-text `data: done` frame ends the current connection; clients may reconnect with `lastEventId`.




## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/mcp/requests
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
  /api/v1/w/{wId}/mcp/requests:
    get:
      tags:
        - MCP
      summary: Stream MCP tool requests for a workspace
      description: >
        [Documentation](https://docs.dust.tt/docs/client-side-mcp-server)

        Server-Sent Events (SSE) endpoint that streams MCP tool requests for a
        workspace.

        This endpoint is used by client-side MCP servers to listen for tool
        requests in real-time.

        Events arrive as new tool requests are made. Reconnect with
        `lastEventId` after the stream closes to continue receiving events.

        The stream starts with a `:connect` comment. Request frames carry JSON
        with `eventId` and `data` fields. A plain-text `data: done` frame ends
        the current connection; clients may reconnect with `lastEventId`.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: query
          name: serverId
          required: true
          description: ID of the MCP server to filter events for
          schema:
            type: string
        - in: query
          name: lastEventId
          required: false
          description: >-
            Redis stream ID of the last received request event. Omit to start
            from the available history.
          schema:
            type: string
      responses:
        '200':
          description: >
            SSE event stream with a `:connect` comment followed by request
            frames. The JSON `data` field in each request frame contains the
            tool request.
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
                    description: The tool request data
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '403':
          description: Forbidden. You don't have access to this workspace or MCP server.
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