> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a conversation

> Get a conversation in the workspace identified by {wId}. Supports optional pagination of message content via limit and lastValue query parameters.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/assistant/conversations/{cId}
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
  /api/v1/w/{wId}/assistant/conversations/{cId}:
    get:
      tags:
        - Conversations
      summary: Get a conversation
      description: >-
        Get a conversation in the workspace identified by {wId}. Supports
        optional pagination of message content via limit and lastValue query
        parameters.
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
        - in: query
          name: limit
          required: false
          description: >-
            Maximum number of messages to return. When omitted, all messages are
            returned.
          schema:
            type: integer
        - in: query
          name: lastValue
          required: false
          description: >-
            Cursor value (message rank) from a previous response to fetch the
            next page of messages.
          schema:
            type: string
      responses:
        '200':
          description: Conversation retrieved successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Conversation'
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '404':
          description: Conversation not found.
        '500':
          description: Internal Server Error.
      security:
        - BearerAuth: []
components:
  schemas:
    Conversation:
      type: object
      properties:
        conversation:
          type: object
          properties:
            id:
              type: integer
              example: 67890
            created:
              type: integer
              example: 1625097600
            sId:
              type: string
              description: Unique string identifier for the conversation
              example: 3d8f6a2c1b
            owner:
              $ref: '#/components/schemas/Workspace'
            title:
              type: string
              description: Title of the conversation
              example: 'Customer Inquiry #1234'
            visibility:
              type: string
              description: Visibility setting of the conversation
              example: private
            content:
              type: array
              items:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      example: 1
                    sId:
                      type: string
                      description: Unique string identifier for the message
                      example: 9e7d5c3a1f
                    type:
                      type: string
                      description: Type of the message
                      example: human
                    visibility:
                      type: string
                      description: Visibility setting of the message
                      example: visible
                    version:
                      type: integer
                      example: 1
                    created:
                      type: integer
                      example: 1625097700
                    user:
                      $ref: '#/components/schemas/User'
                    mentions:
                      type: array
                      items:
                        $ref: '#/components/schemas/Mention'
                    content:
                      type: string
                      description: Content of the message
                      example: Hello, I need help with my order.
                    context:
                      $ref: '#/components/schemas/Context'
                    agentMessageId:
                      type: integer
                      example: 1
                    parentMessageId:
                      type: string
                      description: ID of the parent message
                      example: 2b8e4f6a0c
                    status:
                      type: string
                      description: Status of the message
                      example: completed
                    actions:
                      type: array
                      items:
                        type: object
                        properties:
                          generatedFiles:
                            type: array
                            description: >
                              Files generated by this action. Path-backed files
                              have `fileId: null`

                              and can be downloaded through the conversation
                              files endpoint using

                              `filePath`.
                            items:
                              type: object
                              properties:
                                fileId:
                                  type: string
                                  nullable: true
                                  description: >-
                                    Dust file id for DB-backed files, or null
                                    for path-backed files.
                                filePath:
                                  type: string
                                  description: >-
                                    Canonical scoped path for path-backed files,
                                    as surfaced by agent file system tools.
                                title:
                                  type: string
                                contentType:
                                  type: string
                                snippet:
                                  type: string
                                  nullable: true
                                hidden:
                                  type: boolean
                                isInProjectContext:
                                  type: boolean
                    chainOfThought:
                      type: string
                      nullable: true
                      description: Chain of thought for the message
                      example: >-
                        The user is asking about their order. I should first
                        greet them and then ask for their order number.
                    rawContents:
                      type: array
                      items:
                        type: object
                        properties:
                          step:
                            type: integer
                            example: 1
                          content:
                            type: string
                            description: Content for each step
                            example: >-
                              Hello! I'd be happy to help you with your order.
                              Could you please provide your order number?
                    error:
                      type: string
                      nullable: true
                      description: Error message, if any
                      example: null
                    configuration:
                      $ref: '#/components/schemas/AgentConfiguration'
    Workspace:
      type: object
      required:
        - regionalModelsOnly
      properties:
        id:
          type: integer
          example: 67890
        sId:
          type: string
          description: Unique string identifier for the workspace
          example: dQFf9l5FQY
        name:
          type: string
          description: Name of the workspace
          example: My Awesome Workspace
        role:
          type: string
          enum:
            - admin
            - manager
            - user
            - none
          description: User's role in the workspace
          example: admin
        segmentation:
          type: string
          nullable: true
          description: Segmentation information for the workspace
          example: enterprise
        flags:
          type: array
          items:
            type: string
            description: Feature flags enabled for the workspace
          example:
            - advanced_analytics
            - beta_features
        ssoEnforced:
          type: boolean
          example: true
        regionalModelsOnly:
          type: boolean
          description: >-
            When true, only models whose regionalAvailability includes the
            workspace's region are usable.
          example: false
        whiteListedProviders:
          type: array
          items:
            type: string
            description: List of allowed authentication providers
          example:
            - google
            - github
        defaultEmbeddingProvider:
          type: string
          nullable: true
          description: Default provider for embeddings in the workspace
          example: openai
    User:
      type: object
      properties:
        sId:
          type: string
          description: Unique string identifier for the user
          example: 0ec9852c2f
        id:
          type: integer
          example: 12345
        createdAt:
          type: integer
          example: 1625097600
        username:
          type: string
          description: User's chosen username
          example: johndoe
        email:
          type: string
          description: User's email address
          example: john.doe@example.com
        firstName:
          type: string
          description: User's first name
          example: John
        lastName:
          type: string
          description: User's last name
          example: Doe
        fullName:
          type: string
          description: User's full name
          example: John Doe
        provider:
          type: string
          description: Authentication provider used by the user
          example: google
        image:
          type: string
          description: URL of the user's profile image
          example: https://example.com/profile/johndoe.jpg
    Mention:
      type: object
      properties:
        configurationId:
          type: string
          description: ID of the mentioned agent configuration
          example: 7f3a9c2b1e
    Context:
      type: object
      required:
        - username
        - timezone
      properties:
        username:
          type: string
          description: Username in the current context
          example: johndoe123
        timezone:
          type: string
          description: User's timezone
          example: America/New_York
        fullName:
          type: string
          description: User's full name in the current context
          example: John Doe
        email:
          type: string
          description: User's email in the current context
          example: john.doe@example.com
        profilePictureUrl:
          type: string
          description: URL of the user's profile picture
          example: https://example.com/profiles/johndoe123.jpg
        selectedSpaceIds:
          type: array
          items:
            type: string
        agenticMessageData:
          type: object
          properties:
            type:
              type: string
              enum:
                - run_agent
                - agent_handover
              description: Type of the agentic message
            originMessageId:
              type: string
              description: ID of the origin message
              example: 2b8e4f6a0c
    AgentConfiguration:
      type: object
      properties:
        id:
          type: integer
          example: 12345
        agentModelId:
          type: integer
          nullable: true
          description: >-
            Stable identifier of the agent across versions; null for global
            agents
          example: 6789
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