> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Stream MCP tool requests for a workspace

> [Documentation](https://docs.dust.tt/docs/client-side-mcp-server)
Server-Sent Events (SSE) endpoint that streams MCP tool requests for a workspace.
This endpoint is used by client-side MCP servers to listen for tool requests in real-time.
The connection will remain open and events will be sent as new tool requests are made.




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

        The connection will remain open and events will be sent as new tool
        requests are made.
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
          description: ID of the last event to filter events for
          schema:
            type: string
      responses:
        '200':
          description: >
            Connection established successfully. Events will be streamed in
            Server-Sent Events format.

            Each event will contain a tool request that needs to be processed by
            the MCP server.
          content:
            text/event-stream:
              schema:
                type: object
                properties:
                  type:
                    type: string
                    description: Type of the event (e.g. "tool_request")
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