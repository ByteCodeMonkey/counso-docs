> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# List skills

> Retrieves the custom skills in the workspace. Active skills are returned by default.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/skills
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
  /api/v1/w/{wId}/skills:
    get:
      tags:
        - Skills
      summary: List skills
      description: >-
        Retrieves the custom skills in the workspace. Active skills are returned
        by default.
      parameters:
        - in: path
          name: wId
          required: true
          description: Unique string identifier for the workspace
          schema:
            type: string
        - in: query
          name: status
          required: false
          description: Filter skills by status. Defaults to active.
          schema:
            type: string
            enum:
              - active
              - archived
              - suggested
        - in: query
          name: availability
          required: false
          description: >-
            Filter skills by availability. Repeatable to match several values.
            Unpublished (editors) skills are only returned when
            bypassEditorVisibility is set.
          schema:
            type: array
            items:
              type: string
              enum:
                - editors
                - workspace_users
                - users_and_agents
          style: form
          explode: true
        - in: query
          name: bypassEditorVisibility
          required: false
          description: >-
            When true, also return unpublished (editors) skills. Requires an
            admin API key.
          schema:
            type: boolean
      responses:
        '200':
          description: Skills available in the workspace.
          content:
            application/json:
              schema:
                type: object
                properties:
                  skills:
                    type: array
                    items:
                      $ref: '#/components/schemas/Skill'
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '404':
          description: Workspace not found.
      security:
        - BearerAuth: []
components:
  schemas:
    Skill:
      type: object
      properties:
        sId:
          type: string
          description: Unique string identifier for the skill
          example: skill_abc123
        createdAt:
          type: number
          nullable: true
          description: Timestamp of when the skill was created
        updatedAt:
          type: number
          nullable: true
          description: Timestamp of when the skill was last updated
        editedBy:
          type: integer
          nullable: true
          description: Numeric identifier of the last editor
        status:
          type: string
          enum:
            - active
            - archived
            - suggested
          description: Current status of the skill
          example: active
        name:
          type: string
          maxLength: 256
          description: Name of the skill
          example: Customer Support
        agentFacingDescription:
          type: string
          description: Description shown to agents when selecting or using the skill
          example: Use this skill to answer customer support questions.
        userFacingDescription:
          type: string
          description: Description shown to workspace users
          example: Answers support questions with the right workspace context.
        icon:
          type: string
          nullable: true
          description: Icon identifier for the skill
          example: ActionRobotIcon
        source:
          type: string
          nullable: true
          enum:
            - web_app
            - github
            - api
            - local_file
          description: Source used to create or import the skill
        sourceMetadata:
          type: object
          nullable: true
          allOf:
            - $ref: '#/components/schemas/SkillSourceMetadata'
        reinforcement:
          type: string
          enum:
            - auto
            - 'on'
            - 'off'
          description: Reinforcement setting for the skill
        lastReinforcementAnalysisAt:
          type: string
          nullable: true
          description: Timestamp of the last reinforcement analysis, when available
        requestedSpaceIds:
          type: array
          items:
            type: string
          description: Space identifiers the skill needs access to
        manuallyRequestedSpaceIds:
          type: array
          items:
            type: string
          description: >
            Subset of requestedSpaceIds that was selected by hand rather than
            derived from the skill's tools, knowledge or nested skills
        fileAttachments:
          type: array
          items:
            type: object
            properties:
              fileId:
                type: string
                description: Unique string identifier for the attached file
              fileName:
                type: string
                description: Name of the attached file
        canRead:
          type: boolean
          description: >-
            Whether the authenticated actor can read the skill's instructions,
            tools and files. False when they were redacted for a workspace admin
            who is not a member of every space the skill requires.
        canWrite:
          type: boolean
          description: Whether the authenticated actor can edit the skill
        isDefault:
          type: boolean
          deprecated: true
          description: >-
            Whether this skill is enabled by default. Deprecated, use
            availability instead.
        availability:
          type: string
          enum:
            - editors
            - workspace_users
            - users_and_agents
          description: >-
            Who the skill is available to (users_and_agents makes it
            discoverable by agents)
        instructions:
          type: string
          nullable: true
          description: Instructions used by the agent when running the skill
        instructionsHtml:
          type: string
          nullable: true
          description: HTML representation of the skill instructions
        tools:
          type: array
          items:
            $ref: '#/components/schemas/MCPServerView'
    SkillSourceMetadata:
      type: object
      properties:
        repoUrl:
          type: string
          description: URL of the source repository, when applicable
          example: https://github.com/dust-tt/skills
        filePath:
          type: string
          description: Path to the source skill file
          example: support/SKILL.md
    MCPServerView:
      type: object
      required:
        - isRestrictedToSkills
      properties:
        id:
          type: integer
          description: Unique identifier for the MCP server view
          example: 123
        sId:
          type: string
          description: Unique string identifier for the MCP server view
          example: mcp_sv_abc123
        name:
          type: string
          nullable: true
          description: Custom name for the MCP server view (null if not set)
          example: My Custom MCP Server
        description:
          type: string
          nullable: true
          description: Custom description for the MCP server view (null if not set)
          example: This MCP server handles customer data operations
        createdAt:
          type: number
          description: Unix timestamp of when the MCP server view was created
          example: 1625097600
        updatedAt:
          type: number
          description: Unix timestamp of when the MCP server view was last updated
          example: 1625184000
        spaceId:
          type: string
          description: ID of the space containing the MCP server view
          example: spc_xyz789
        serverType:
          type: string
          enum:
            - remote
            - internal
          description: Type of the MCP server
          example: remote
        server:
          type: object
          properties:
            sId:
              type: string
              description: Unique string identifier for the MCP server
              example: mcp_srv_def456
            name:
              type: string
              description: Name of the MCP server
              example: Customer Data Server
            version:
              type: string
              description: Version of the MCP server
              example: 1.0.0
            description:
              type: string
              description: Description of the MCP server
              example: Handles customer data operations and queries
            icon:
              type: string
              description: Icon identifier for the MCP server
              example: database
            authorization:
              type: object
              nullable: true
              properties:
                provider:
                  type: string
                  description: OAuth provider for authorization
                  example: github
                supported_use_cases:
                  type: array
                  items:
                    type: string
                    enum:
                      - platform_actions
                      - personal_actions
                  description: Supported use cases for the authorization
                  example:
                    - platform_actions
                scope:
                  type: string
                  description: OAuth scope required
                  example: repo:read
            tools:
              type: array
              items:
                type: object
                properties:
                  name:
                    type: string
                    description: Name of the tool
                    example: query_customers
                  description:
                    type: string
                    description: Description of what the tool does
                    example: Query customer database for information
                  inputSchema:
                    type: object
                    description: JSON Schema for the tool's input parameters
                    example:
                      type: object
                      properties:
                        customerId:
                          type: string
            availability:
              type: string
              description: Availability status of the MCP server
              example: production
            allowMultipleInstances:
              type: boolean
              description: Whether multiple instances of this server can be created
              example: false
            documentationUrl:
              type: string
              nullable: true
              description: URL to the server's documentation
              example: https://docs.example.com/mcp-server
        oAuthUseCase:
          type: string
          nullable: true
          enum:
            - platform_actions
            - personal_actions
          description: OAuth use case for the MCP server view
          example: platform_actions
        isRestrictedToSkills:
          type: boolean
          description: Whether the MCP server view can only be used through skills
          example: false
        editedByUser:
          type: object
          nullable: true
          description: Information about the user who last edited the MCP server view
          properties:
            editedAt:
              type: number
              nullable: true
              description: Unix timestamp of when the edit occurred
              example: 1625184000
            fullName:
              type: string
              nullable: true
              description: Full name of the editor
              example: John Doe
            imageUrl:
              type: string
              nullable: true
              description: Profile image URL of the editor
              example: https://example.com/profile/johndoe.jpg
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````