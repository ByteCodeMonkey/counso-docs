> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get mention suggestions

> Get suggestions for mentions (agents and users) based on a query string.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/assistant/mentions/suggestions
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
  /api/v1/w/{wId}/assistant/mentions/suggestions:
    get:
      tags:
        - Mentions
      summary: Get mention suggestions
      description: Get suggestions for mentions (agents and users) based on a query string.
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
          description: Search query string to filter suggestions
          schema:
            type: string
        - in: query
          name: select
          required: false
          description: >-
            Array of mention types to include. Can be "agents", "users", or
            both. If not provided, defaults to agents and users.
          schema:
            type: array
            items:
              type: string
              enum:
                - agents
                - users
        - in: query
          name: current
          required: false
          description: Whether to include the current user in the suggestions.
          schema:
            type: boolean
      responses:
        '200':
          description: List of mention suggestions
          content:
            application/json:
              schema:
                type: object
                properties:
                  suggestions:
                    type: array
                    items:
                      $ref: '#/components/schemas/RichMention'
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '500':
          description: Internal Server Error.
      security:
        - BearerAuth: []
components:
  schemas:
    RichMention:
      type: object
      description: >-
        A rich mention suggestion containing detailed information about an agent
        or user
      required:
        - id
        - type
        - label
        - pictureUrl
        - description
      properties:
        id:
          type: string
          description: Unique identifier for the mention (agent sId or user sId)
          example: 7f3a9c2b1e
        type:
          type: string
          enum:
            - agent
            - user
          description: Type of the mention
          example: agent
        label:
          type: string
          description: Display label for the mention
          example: My Assistant
        pictureUrl:
          type: string
          description: URL of the profile picture
          example: https://example.com/avatar.png
        description:
          type: string
          description: Description of the mention (agent description or user email)
          example: A helpful AI assistant
        userFavorite:
          type: boolean
          nullable: true
          description: >-
            Whether the agent is marked as a favorite by the user (only for
            agent mentions)
          example: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````