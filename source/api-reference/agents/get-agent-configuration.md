> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get agent configuration

> Retrieve the agent configuration identified by {sId} in the workspace identified by {wId}.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/assistant/agent_configurations/{sId}
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
  /api/v1/w/{wId}/assistant/agent_configurations/{sId}:
    get:
      tags:
        - Agents
      summary: Get agent configuration
      description: >-
        Retrieve the agent configuration identified by {sId} in the workspace
        identified by {wId}.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: path
          name: sId
          required: true
          description: ID of the agent configuration
          schema:
            type: string
        - in: query
          name: variant
          required: false
          description: >-
            Configuration variant to retrieve. 'light' returns basic config
            without actions, 'full' includes complete actions/tools
            configuration
          schema:
            type: string
            enum:
              - light
              - full
            default: light
      responses:
        '200':
          description: Successfully retrieved agent configuration
          content:
            application/json:
              schema:
                type: object
                properties:
                  agentConfiguration:
                    $ref: '#/components/schemas/AgentConfiguration'
        '400':
          description: Bad Request. Invalid or missing parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '404':
          description: Agent configuration not found.
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