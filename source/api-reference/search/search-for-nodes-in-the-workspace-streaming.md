> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Search for nodes in the workspace (streaming)

> Search for nodes in the workspace with SSE streaming



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/search
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
  /api/v1/w/{wId}/search:
    get:
      tags:
        - Search
      summary: Search for nodes in the workspace (streaming)
      description: Search for nodes in the workspace with SSE streaming
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: query
          name: query
          required: true
          description: The search query (minimum 3 characters)
          schema:
            type: string
        - in: query
          name: limit
          required: false
          description: Number of results per page (1-100, default 25)
          schema:
            type: integer
        - in: query
          name: cursor
          required: false
          description: Cursor for pagination
          schema:
            type: string
        - in: query
          name: viewType
          required: false
          description: Type of view to filter results
          schema:
            type: string
            enum:
              - all
              - document
              - table
        - in: query
          name: spaceIds
          required: false
          description: Comma-separated list of space IDs to search in
          schema:
            type: string
        - in: query
          name: includeDataSources
          required: false
          description: Whether to include data sources
          schema:
            type: boolean
        - in: query
          name: searchSourceUrls
          required: false
          description: Whether to search source URLs
          schema:
            type: boolean
        - in: query
          name: includeTools
          required: false
          description: Whether to include tool results
          schema:
            type: boolean
      responses:
        '200':
          description: Search results streamed successfully
          content:
            text/event-stream:
              schema:
                type: string
        '400':
          description: Bad request
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````