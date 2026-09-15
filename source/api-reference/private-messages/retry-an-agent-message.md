> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Retry an agent message

> Retry generating an agent message response, optionally retrying only blocked actions.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/retry
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
  /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/retry:
    post:
      tags:
        - Private Messages
      summary: Retry an agent message
      description: >-
        Retry generating an agent message response, optionally retrying only
        blocked actions.
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
        - in: path
          name: mId
          required: true
          description: ID of the message
          schema:
            type: string
      responses:
        '200':
          description: Successfully retried message
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    $ref: '#/components/schemas/PrivateAgentMessage'
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateAgentMessage:
      type: object
      description: An agent message in a conversation.
      required:
        - type
        - sId
        - version
        - rank
        - status
        - parentMessageId
      properties:
        id:
          type: integer
        agentMessageId:
          type: integer
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
          description: If handover, the agent message that summoned this agent
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
          $ref: '#/components/schemas/PrivateLightAgentConfiguration'
        actions:
          type: array
          items:
            type: object
          description: MCP actions executed by the agent
        contents:
          type: array
          items:
            type: object
            properties:
              step:
                type: integer
              content:
                type: object
        skipToolsValidation:
          type: boolean
        richMentions:
          type: array
          items:
            $ref: '#/components/schemas/PrivateRichMentionWithStatus'
        completionDurationMs:
          type: integer
          nullable: true
        reactions:
          type: array
          items:
            $ref: '#/components/schemas/PrivateReaction'
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
    PrivateLightAgentConfiguration:
      type: object
      description: Agent configuration as returned by the private list endpoint.
      required:
        - id
        - sId
        - version
        - name
        - description
        - pictureUrl
        - status
        - scope
        - model
        - maxStepsPerRun
        - tags
      properties:
        id:
          type: integer
        sId:
          type: string
        version:
          type: integer
        versionCreatedAt:
          type: string
          nullable: true
        versionAuthorId:
          type: integer
          nullable: true
        name:
          type: string
        description:
          type: string
        instructions:
          type: string
          nullable: true
        pictureUrl:
          type: string
        status:
          type: string
          description: Agent status
          enum:
            - active
            - archived
            - draft
            - pending
            - disabled_by_admin
            - disabled_missing_datasource
            - disabled_free_workspace
        scope:
          type: string
          enum:
            - global
            - visible
            - hidden
        userFavorite:
          type: boolean
        model:
          type: object
          properties:
            providerId:
              type: string
            modelId:
              type: string
            temperature:
              type: number
            reasoningEffort:
              type: string
              enum:
                - none
                - light
                - medium
                - high
        maxStepsPerRun:
          type: integer
        tags:
          type: array
          items:
            type: object
            properties:
              sId:
                type: string
              name:
                type: string
        templateId:
          type: string
          nullable: true
        requestedGroupIds:
          type: array
          items:
            type: array
            items:
              type: string
        requestedSpaceIds:
          type: array
          items:
            type: string
        canRead:
          type: boolean
        canEdit:
          type: boolean
        lastAuthors:
          type: array
          description: Optional, returned when withAuthors query param is set
          items:
            type: string
        editors:
          type: array
          description: Optional, returned when withEditors query param is set
          items:
            type: object
            properties:
              sId:
                type: string
              fullName:
                type: string
              image:
                type: string
                nullable: true
        usage:
          type: object
          description: Optional, returned when withUsage query param is set
          properties:
            messageCount:
              type: integer
            conversationCount:
              type: integer
            userCount:
              type: integer
            timePeriodSec:
              type: integer
        feedbacks:
          type: object
          description: Optional, returned when withFeedbacks query param is set
          properties:
            up:
              type: integer
            down:
              type: integer
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````