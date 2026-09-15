> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Import agent configuration

> Create a new agent configuration from a JSON body matching the agent config schema.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/v1/w/{wId}/assistant/agent_configurations/import
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
  /api/v1/w/{wId}/assistant/agent_configurations/import:
    post:
      tags:
        - Agents
      summary: Import agent configuration
      description: >-
        Create a new agent configuration from a JSON body matching the agent
        config schema.
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
                - agent
                - instructions
                - generation_settings
                - tags
                - editors
                - toolset
              properties:
                agent:
                  type: object
                  required:
                    - handle
                    - description
                    - scope
                    - avatar_url
                    - max_steps_per_run
                    - visualization_enabled
                  properties:
                    handle:
                      type: string
                    description:
                      type: string
                    scope:
                      type: string
                      enum:
                        - visible
                        - hidden
                    avatar_url:
                      type: string
                    max_steps_per_run:
                      type: number
                    visualization_enabled:
                      type: boolean
                instructions:
                  type: string
                generation_settings:
                  type: object
                  properties:
                    model_id:
                      type: string
                    provider_id:
                      type: string
                    temperature:
                      type: number
                    reasoning_effort:
                      type: string
                tags:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                      kind:
                        type: string
                        enum:
                          - standard
                          - protected
                editors:
                  type: array
                  description: >-
                    Emails of the workspace members to set as editors of the
                    agent.
                  items:
                    type: string
                    format: email
                  example:
                    - alice@example.com
                toolset:
                  type: array
                  items:
                    type: object
                    properties:
                      name:
                        type: string
                      description:
                        type: string
                      type:
                        type: string
                        enum:
                          - MCP
                      configuration:
                        type: object
      responses:
        '200':
          description: Successfully created agent configuration
          content:
            application/json:
              schema:
                type: object
                properties:
                  agentConfiguration:
                    $ref: '#/components/schemas/AgentConfiguration'
                  skippedActions:
                    type: array
                    items:
                      type: object
                      properties:
                        name:
                          type: string
                        reason:
                          type: string
        '400':
          description: Bad Request. Invalid request body.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '500':
          description: Internal Server Error.
      security:
        - BearerAuth: []
components:
  schemas:
    AgentConfiguration:
      type: object
      properties:
        id:
          type: integer
          example: 12345
        sId:
          type: string
          description: Unique string identifier for the agent configuration
          example: 7f3a9c2b1e
        version:
          type: integer
          example: 2
        versionCreatedAt:
          type: string
          nullable: true
          description: Timestamp of when the version was created
          example: '2023-06-15T14:30:00Z'
        versionAuthorId:
          type: string
          nullable: true
          description: ID of the user who created this version
          example: 0ec9852c2f
        name:
          type: string
          description: Name of the agent configuration
          example: Customer Support Agent
        description:
          type: string
          description: Description of the agent configuration
          example: An AI agent designed to handle customer support inquiries
        instructions:
          type: string
          nullable: true
          description: Instructions for the agent
          example: >-
            Always greet the customer politely and try to resolve their issue
            efficiently.
        pictureUrl:
          type: string
          description: URL of the agent's picture
          example: https://example.com/agent-images/support-agent.png
        status:
          type: string
          description: Current status of the agent configuration
          example: active
        scope:
          type: string
          description: Scope of the agent configuration
          example: workspace
        userFavorite:
          type: boolean
          description: Status of the user favorite for this configuration
          example: true
        model:
          type: object
          properties:
            providerId:
              type: string
              description: ID of the model provider
              example: openai
            modelId:
              type: string
              description: ID of the specific model
              example: gpt-4
            temperature:
              type: number
              example: 0.7
        actions:
          type: array
          example: []
        skills:
          type: array
          description: >-
            Skills attached to the agent. Returned by the agent GET endpoints
            (list and single-agent) whatever the requested variant. Empty both
            for an agent with no skill and for an agent whose details were
            redacted for the caller (canRead false).
          items:
            $ref: '#/components/schemas/AgentSkill'
        tags:
          type: array
          description: Tags attached to the agent
          items:
            type: object
            properties:
              sId:
                type: string
                example: 3f9d1c7a5b
              name:
                type: string
                example: Support
              kind:
                type: string
                enum:
                  - standard
                  - protected
        requestedSpaceIds:
          type: array
          description: Identifiers of the spaces the agent needs access to
          items:
            type: string
          example:
            - vlt_a1b2c3d4e5
        maxStepsPerRun:
          type: integer
          example: 10
        templateId:
          type: string
          nullable: true
          description: ID of the template used for this configuration
          example: b4e2f1a9c7
    AgentSkill:
      type: object
      description: A skill attached to an agent configuration.
      properties:
        sId:
          type: string
          description: Unique string identifier for the skill
          example: skill_abc123
        name:
          type: string
          description: Name of the skill
          example: Customer Support
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````