> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# List wake-ups for a conversation

> Retrieve all wake-ups scheduled in a conversation (any status).



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/assistant/conversations/{cId}/wakeups
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
  /api/w/{wId}/assistant/conversations/{cId}/wakeups:
    get:
      tags:
        - Private Conversations
      summary: List wake-ups for a conversation
      description: Retrieve all wake-ups scheduled in a conversation (any status).
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
      responses:
        '200':
          description: Successfully retrieved wake-ups
          content:
            application/json:
              schema:
                type: object
                properties:
                  wakeUps:
                    type: array
                    items:
                      $ref: '#/components/schemas/PrivateWakeUp'
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateWakeUp:
      type: object
      description: >-
        A wake-up scheduled in a conversation to re-invoke the agent at a later
        time.
      required:
        - id
        - sId
        - createdAt
        - agentConfigurationId
        - scheduleConfig
        - reason
        - status
        - fireCount
        - maxFires
      properties:
        id:
          type: integer
        sId:
          type: string
        createdAt:
          type: integer
          description: Unix timestamp (milliseconds).
        agentConfigurationId:
          type: string
        scheduleConfig:
          oneOf:
            - type: object
              required:
                - type
                - fireAt
              properties:
                type:
                  type: string
                  enum:
                    - one_shot
                fireAt:
                  type: integer
                  description: Unix timestamp (milliseconds) when the wake-up should fire.
            - type: object
              required:
                - type
                - cron
                - timezone
              properties:
                type:
                  type: string
                  enum:
                    - cron
                cron:
                  type: string
                  description: 5-field cron expression.
                timezone:
                  type: string
                  description: IANA timezone name.
        reason:
          type: string
        status:
          type: string
          enum:
            - scheduled
            - fired
            - cancelled
            - expired
        fireCount:
          type: integer
        maxFires:
          type: integer
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````