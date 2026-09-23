> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a trigger

> Get one agent trigger (scheduled run or webhook) by id. Requires a workspace admin API
key.




## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/triggers/{tId}
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
  /api/v1/w/{wId}/triggers/{tId}:
    get:
      tags:
        - Triggers
      summary: Get a trigger
      description: >
        Get one agent trigger (scheduled run or webhook) by id. Requires a
        workspace admin API

        key.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: path
          name: tId
          required: true
          description: ID of the trigger
          schema:
            type: string
      responses:
        '200':
          description: The trigger
          content:
            application/json:
              schema:
                type: object
                properties:
                  trigger:
                    $ref: '#/components/schemas/Trigger'
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '403':
          description: Forbidden. Requires a workspace admin API key.
        '404':
          description: Workspace or trigger not found.
      security:
        - BearerAuth: []
components:
  schemas:
    Trigger:
      type: object
      required:
        - id
        - sId
        - name
        - agentConfigurationId
        - kind
        - status
        - createdAt
        - executionMode
        - configuration
      properties:
        id:
          type: integer
          example: 12345
        sId:
          type: string
          description: Unique string identifier for the trigger
          example: 0ec9852c2f
        name:
          type: string
          example: Daily summary
        agentConfigurationId:
          type: string
          description: sId of the agent this trigger runs
          example: 8f3a1c2d9e
        kind:
          type: string
          enum:
            - schedule
            - webhook
        status:
          type: string
          enum:
            - enabled
            - disabled
            - disabled_by_manager
            - relocating
            - downgraded
        createdAt:
          type: integer
          example: 1625097600
        customPrompt:
          type: string
          nullable: true
        naturalLanguageDescription:
          type: string
          nullable: true
        executionMode:
          type: string
          enum:
            - user_pool
            - workspace_pool
        configuration:
          type: object
          description: >
            For `kind: schedule`, either a cron config (`cron`, `timezone`) or
            an interval

            config (`intervalDays`, `dayOfWeek`, `hour`, `minute`, `timezone`).
            For

            `kind: webhook`, `{ includePayload, event?, filter? }`.
        webhookSource:
          type: object
          nullable: true
          description: 'Present only for `kind: webhook` triggers'
          properties:
            name:
              type: string
            provider:
              type: string
              example: github
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````