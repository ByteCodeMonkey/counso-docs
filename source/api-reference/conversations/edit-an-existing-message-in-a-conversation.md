> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit an existing message in a conversation



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/edit
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
  /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/edit:
    post:
      tags:
        - Conversations
      summary: Edit an existing message in a conversation
      parameters:
        - name: wId
          in: path
          required: true
          schema:
            type: string
          description: Workspace ID
        - name: cId
          in: path
          required: true
          schema:
            type: string
          description: Conversation ID
        - name: mId
          in: path
          required: true
          schema:
            type: string
          description: Message ID to edit
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - content
                - mentions
              properties:
                content:
                  type: string
                  description: New content for the message
                mentions:
                  type: array
                  description: List of agent mentions in the message
                  items:
                    type: object
                    required:
                      - configurationId
                    properties:
                      configurationId:
                        type: string
                        description: ID of the mentioned agent configuration
      responses:
        '200':
          description: Message successfully edited
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: object
                    description: The edited user message
                  agentMessages:
                    type: array
                    description: Optional array of agent messages generated in response
        '400':
          description: Invalid request (message not found or not a user message)
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````