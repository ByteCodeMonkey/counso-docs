> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get mention suggestions

> Returns mention suggestions for the workspace.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/assistant/mentions/suggestions
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
  /api/w/{wId}/assistant/mentions/suggestions:
    get:
      tags:
        - Private Mentions
      summary: Get mention suggestions
      description: Returns mention suggestions for the workspace.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: query
          name: query
          required: false
          description: Search query to filter suggestions
          schema:
            type: string
        - in: query
          name: select
          required: false
          description: Filter by type (agents, users, or both)
          schema:
            type: string
            enum:
              - agents
              - users
        - in: query
          name: current
          required: false
          description: Whether to include only current mentions
          schema:
            type: string
            enum:
              - 'true'
              - 'false'
        - in: query
          name: spaceId
          required: false
          description: Filter suggestions by space
          schema:
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  suggestions:
                    type: array
                    items:
                      $ref: '#/components/schemas/PrivateMentionSuggestion'
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateMentionSuggestion:
      type: object
      description: A rich mention suggestion for agents or users.
      required:
        - id
        - type
        - label
        - pictureUrl
        - description
      properties:
        id:
          type: string
          description: Agent sId or user sId
        type:
          type: string
          enum:
            - agent
            - user
        label:
          type: string
          description: Display name
        pictureUrl:
          type: string
        description:
          type: string
          description: Agent description or user email
        userFavorite:
          type: boolean
          description: Whether the agent is a user favorite (agent mentions only)
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````