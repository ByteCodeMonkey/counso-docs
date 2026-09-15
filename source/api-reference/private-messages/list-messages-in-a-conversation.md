> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# List messages in a conversation

> Retrieve a paginated list of messages for a specific conversation.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/assistant/conversations/{cId}/messages
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
  /api/w/{wId}/assistant/conversations/{cId}/messages:
    get:
      tags:
        - Private Messages
      summary: List messages in a conversation
      description: Retrieve a paginated list of messages for a specific conversation.
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
          description: Successfully retrieved messages
          content:
            application/json:
              schema:
                type: object
                properties:
                  messages:
                    type: array
                    items:
                      oneOf:
                        - $ref: '#/components/schemas/PrivateUserMessage'
                        - $ref: '#/components/schemas/PrivateLightAgentMessage'
                        - $ref: '#/components/schemas/PrivateContentFragment'
                  hasMore:
                    type: boolean
                  lastValue:
                    type: integer
                    nullable: true
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateUserMessage:
      type: object
      description: A user message in a conversation.
      required:
        - type
        - sId
        - content
        - version
        - rank
        - created
      properties:
        id:
          type: integer
        type:
          type: string
          enum:
            - user_message
        sId:
          type: string
        created:
          type: integer
        visibility:
          type: string
          enum:
            - visible
            - deleted
        version:
          type: integer
        rank:
          type: integer
        branchId:
          type: string
          nullable: true
          description: Legacy, always null. Branches were removed.
        user:
          type: object
          nullable: true
          description: The user who sent the message
          properties:
            sId:
              type: string
            username:
              type: string
            fullName:
              type: string
            image:
              type: string
              nullable: true
        mentions:
          type: array
          items:
            $ref: '#/components/schemas/PrivateMention'
        richMentions:
          type: array
          items:
            $ref: '#/components/schemas/PrivateRichMentionWithStatus'
        content:
          type: string
        context:
          $ref: '#/components/schemas/PrivateUserMessageContext'
        reactions:
          type: array
          items:
            $ref: '#/components/schemas/PrivateReaction'
    PrivateLightAgentMessage:
      type: object
      description: A lighter agent message used in paginated message list responses.
      required:
        - type
        - sId
        - version
        - rank
        - status
        - parentMessageId
        - configuration
      properties:
        type:
          type: string
          enum:
            - agent_message
        sId:
          type: string
        created:
          type: integer
        completedTs:
          type: integer
          nullable: true
        visibility:
          type: string
          enum:
            - visible
            - deleted
        version:
          type: integer
        rank:
          type: integer
        branchId:
          type: string
          nullable: true
          description: Legacy, always null. Branches were removed.
        parentMessageId:
          type: string
        parentAgentMessageId:
          type: string
          nullable: true
        status:
          type: string
          enum:
            - created
            - succeeded
            - failed
            - cancelled
        content:
          type: string
          nullable: true
        chainOfThought:
          type: string
          nullable: true
        error:
          type: object
          nullable: true
          properties:
            code:
              type: string
            message:
              type: string
            metadata:
              type: object
              nullable: true
        configuration:
          type: object
          description: Minimal agent configuration info
          properties:
            sId:
              type: string
            name:
              type: string
            pictureUrl:
              type: string
            status:
              type: string
            canRead:
              type: boolean
        citations:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/PrivateCitation'
        generatedFiles:
          type: array
          items:
            type: object
            properties:
              fileId:
                type: string
                nullable: true
                description: >-
                  Dust file id for DB-backed files, or null for path-backed
                  files.
              filePath:
                type: string
                description: Canonical scoped path for path-backed files.
              title:
                type: string
              contentType:
                type: string
              publicUrl:
                type: string
        richMentions:
          type: array
          items:
            $ref: '#/components/schemas/PrivateRichMentionWithStatus'
        completionDurationMs:
          type: integer
          nullable: true
        costCredits:
          type: integer
          nullable: true
          description: >-
            Cost of producing this agent message, in credits (intelligence +
            tool credits). Null when no billable usage is attributed to the
            message.
        subAgentCostCredits:
          type: number
          nullable: true
          description: >-
            Aggregated credit cost of all sub-agents (run_agent /
            agent_handover) spawned recursively by this message. Computed only
            on single-message fetches. Null otherwise.
        resolvedModel:
          type: object
          nullable: true
          description: >-
            Model triplet used to generate the message. Null when the agent ran
            its configured model (legacy).
          properties:
            providerId:
              type: string
            modelId:
              type: string
            reasoningEffort:
              type: string
        modelResolutionMethod:
          type: string
          nullable: true
          enum:
            - agent
            - user
            - auto
            - auto_fast
            - auto_complex
            - fair_use_downgrade
          description: >-
            How resolvedModel was chosen - agent (configured model), user
            (per-message picker), auto/auto_fast/auto_complex (routed through a
            model stream), or fair_use_downgrade (premium allowance spent, ran
            the Standard stream instead). Null (legacy).
        activitySteps:
          type: array
          items:
            type: object
            properties:
              type:
                type: string
                enum:
                  - thinking
                  - action
              content:
                type: string
                description: Chain of thought text (thinking steps only)
              label:
                type: string
                description: Action display label (action steps only)
              id:
                type: string
              actionId:
                type: string
                description: Action string identifier (action steps only)
        reactions:
          type: array
          items:
            $ref: '#/components/schemas/PrivateReaction'
    PrivateContentFragment:
      type: object
      description: A content fragment (file or content node attachment) in a conversation.
      required:
        - type
        - sId
        - title
        - contentType
        - contentFragmentType
      properties:
        type:
          type: string
          enum:
            - content_fragment
        id:
          type: integer
        sId:
          type: string
        created:
          type: integer
        visibility:
          type: string
          enum:
            - visible
            - deleted
        version:
          type: integer
        rank:
          type: integer
        title:
          type: string
        contentType:
          type: string
          description: MIME type of the content
        sourceUrl:
          type: string
          nullable: true
        context:
          type: object
          properties:
            username:
              type: string
              nullable: true
            fullName:
              type: string
              nullable: true
            email:
              type: string
              nullable: true
            profilePictureUrl:
              type: string
              nullable: true
        contentFragmentId:
          type: string
        contentFragmentVersion:
          type: string
          enum:
            - superseded
            - latest
        contentFragmentType:
          type: string
          enum:
            - file
            - content_node
          description: Whether this is a file upload or a content node reference
        expiredReason:
          type: string
          nullable: true
          enum:
            - data_source_deleted
        fileId:
          type: string
          nullable: true
          description: Present for file content fragments
        path:
          type: string
          nullable: true
          description: Path of this file inside the sandbox conversation mount.
        processedPath:
          type: string
          nullable: true
          description: >-
            Path of the plain-text sibling of this file inside the sandbox
            conversation mount (e.g. an audio transcript), when it has one.
        skipFileProcessing:
          type: boolean
          description: Whether upload-time file processing was skipped.
        snippet:
          type: string
          nullable: true
        textUrl:
          type: string
          nullable: true
        textBytes:
          type: integer
          nullable: true
        nodeId:
          type: string
          nullable: true
          description: Present for content node fragments
        nodeDataSourceViewId:
          type: string
          nullable: true
    PrivateMention:
      type: object
      description: A mention in a message (agent or user).
      properties:
        configurationId:
          type: string
          description: Agent configuration sId (for agent mentions)
        type:
          type: string
          enum:
            - user
          description: Present only for user mentions
        userId:
          type: string
          description: User sId (for user mentions)
    PrivateRichMentionWithStatus:
      type: object
      description: A rich mention with approval status, used in message responses.
      required:
        - id
        - type
        - label
        - pictureUrl
        - description
        - dismissed
        - status
      properties:
        id:
          type: string
        type:
          type: string
          enum:
            - agent
            - user
        label:
          type: string
        pictureUrl:
          type: string
        description:
          type: string
        userFavorite:
          type: boolean
        dismissed:
          type: boolean
        status:
          type: string
          enum:
            - pending_conversation_access
            - pending_project_membership
            - approved
            - rejected
            - user_restricted_by_conversation_access
            - agent_restricted_by_space_usage
    PrivateUserMessageContext:
      type: object
      description: Context metadata for a user message.
      required:
        - username
        - timezone
        - origin
      properties:
        username:
          type: string
        fullName:
          type: string
          nullable: true
        email:
          type: string
          nullable: true
        profilePictureUrl:
          type: string
          nullable: true
        timezone:
          type: string
        origin:
          type: string
          enum:
            - web
            - project_kickoff
            - extension
            - agent_sidekick
            - analytics_panel
            - api
            - cli
            - cli_programmatic
            - email
            - excel
            - gsheet
            - make
            - n8n
            - powerpoint
            - raycast
            - slack
            - slack_workflow
            - teams
            - transcript
            - triggered_programmatic
            - triggered
            - wakeup
            - zapier
            - zendesk
            - onboarding_conversation
        selectedSpaceIds:
          type: array
          items:
            type: string
    PrivateReaction:
      type: object
      description: A reaction on a message.
      required:
        - emoji
        - users
      properties:
        emoji:
          type: string
        users:
          type: array
          items:
            type: object
            properties:
              userId:
                type: string
                nullable: true
              username:
                type: string
              fullName:
                type: string
                nullable: true
    PrivateCitation:
      type: object
      properties:
        title:
          type: string
        description:
          type: string
        href:
          type: string
        provider:
          type: string
        contentType:
          type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````