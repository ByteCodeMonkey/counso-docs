> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload a tool file

> Download and upload a file from a tool (MCP server) to Dust



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/v1/w/{wId}/search/tools/upload
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
  /api/v1/w/{wId}/search/tools/upload:
    post:
      tags:
        - Search
      summary: Upload a tool file
      description: Download and upload a file from a tool (MCP server) to Dust
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - serverViewId
                - externalId
              properties:
                serverViewId:
                  type: string
                  description: The MCP server view ID
                externalId:
                  type: string
                  description: The external ID of the file in the tool
                conversationId:
                  type: string
                  description: Optional conversation ID for context
                serverName:
                  type: string
                  description: Optional name of the MCP server (e.g., "Notion", "GitHub")
                serverIcon:
                  type: string
                  description: Optional icon identifier for the MCP server
      responses:
        '200':
          description: File uploaded successfully
        '400':
          description: Bad request
        '401':
          description: Unauthorized
        '500':
          description: Internal server error
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````