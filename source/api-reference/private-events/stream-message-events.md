> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Stream message events

> Stream real-time events for a specific agent message using Server-Sent Events (SSE). Only available for agent messages. This endpoint is redirected to /api/sse/ for SSE traffic routing.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/events
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
  /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/events:
    get:
      tags:
        - Private Events
      summary: Stream message events
      description: >-
        Stream real-time events for a specific agent message using Server-Sent
        Events (SSE). Only available for agent messages. This endpoint is
        redirected to /api/sse/ for SSE traffic routing.
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
          description: >
            SSE event stream. Each event is sent as `data: {json}\n\n`.

            Events are discriminated by the `type` field. Each event payload
            also includes a `step` integer.
          content:
            text/event-stream:
              schema:
                $ref: '#/components/schemas/PrivateAgentMessageEvent'
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateAgentMessageEvent:
      type: object
      description: >-
        Server-Sent Event for agent message streaming. Discriminated on the
        `type` field. Each event also includes a `step` integer.
      discriminator:
        propertyName: type
      oneOf:
        - $ref: '#/components/schemas/PrivateGenerationTokensEvent'
        - $ref: '#/components/schemas/PrivateToolCallStartedEvent'
        - $ref: '#/components/schemas/PrivateAgentActionSuccessEvent'
        - $ref: '#/components/schemas/PrivateAgentMessageSuccessEvent'
        - $ref: '#/components/schemas/PrivateAgentErrorEvent'
        - $ref: '#/components/schemas/PrivateAgentGenerationCancelledEvent'
        - $ref: '#/components/schemas/PrivateToolErrorEvent'
        - $ref: '#/components/schemas/PrivateToolParamsEvent'
        - $ref: '#/components/schemas/PrivateToolApproveExecutionEvent'
        - $ref: '#/components/schemas/PrivateToolNotificationEvent'
        - $ref: '#/components/schemas/PrivateToolPersonalAuthRequiredEvent'
        - $ref: '#/components/schemas/PrivateToolFileAuthRequiredEvent'
        - $ref: '#/components/schemas/PrivateAgentContextPrunedEvent'
    PrivateGenerationTokensEvent:
      type: object
      required:
        - type
        - created
        - configurationId
        - messageId
        - text
        - classification
      properties:
        type:
          type: string
          enum:
            - generation_tokens
        created:
          type: integer
        configurationId:
          type: string
        messageId:
          type: string
        text:
          type: string
          description: The token(s) generated in this chunk
        classification:
          type: string
          enum:
            - tokens
            - chain_of_thought
            - opening_delimiter
            - closing_delimiter
        delimiterClassification:
          type: string
          description: >-
            Present when classification is opening_delimiter or
            closing_delimiter
        step:
          type: integer
    PrivateToolCallStartedEvent:
      type: object
      required:
        - type
        - created
        - configurationId
        - messageId
        - toolName
      properties:
        type:
          type: string
          enum:
            - tool_call_started
        created:
          type: integer
        configurationId:
          type: string
        messageId:
          type: string
        toolCallId:
          type: string
        toolCallIndex:
          type: integer
        toolName:
          type: string
        step:
          type: integer
    PrivateAgentActionSuccessEvent:
      type: object
      required:
        - type
        - created
        - configurationId
        - messageId
        - action
      properties:
        type:
          type: string
          enum:
            - agent_action_success
        created:
          type: integer
        configurationId:
          type: string
        messageId:
          type: string
        action:
          $ref: '#/components/schemas/PrivateAgentMCPAction'
        step:
          type: integer
    PrivateAgentMessageSuccessEvent:
      type: object
      required:
        - type
        - created
        - configurationId
        - messageId
        - message
        - runIds
      properties:
        type:
          type: string
          enum:
            - agent_message_success
        created:
          type: integer
        configurationId:
          type: string
        messageId:
          type: string
        message:
          $ref: '#/components/schemas/PrivateAgentMessage'
        runIds:
          type: array
          items:
            type: string
        step:
          type: integer
    PrivateAgentErrorEvent:
      type: object
      required:
        - type
        - created
        - configurationId
        - messageId
        - error
      properties:
        type:
          type: string
          enum:
            - agent_error
        created:
          type: integer
        configurationId:
          type: string
        messageId:
          type: string
        error:
          type: object
          properties:
            code:
              type: string
            message:
              type: string
        runIds:
          type: array
          items:
            type: string
        step:
          type: integer
    PrivateAgentGenerationCancelledEvent:
      type: object
      required:
        - type
        - created
        - configurationId
        - messageId
      properties:
        type:
          type: string
          enum:
            - agent_generation_cancelled
        created:
          type: integer
        configurationId:
          type: string
        messageId:
          type: string
        step:
          type: integer
    PrivateToolErrorEvent:
      type: object
      required:
        - type
        - created
        - configurationId
        - messageId
        - conversationId
        - error
        - isLastBlockingEventForStep
      properties:
        type:
          type: string
          enum:
            - tool_error
        created:
          type: integer
        configurationId:
          type: string
        messageId:
          type: string
        conversationId:
          type: string
        error:
          type: object
          properties:
            code:
              type: string
            message:
              type: string
        isLastBlockingEventForStep:
          type: boolean
        step:
          type: integer
    PrivateToolParamsEvent:
      type: object
      required:
        - type
        - created
        - configurationId
        - messageId
        - action
      properties:
        type:
          type: string
          enum:
            - tool_params
        created:
          type: integer
        configurationId:
          type: string
        messageId:
          type: string
        action:
          type: object
          description: The MCP action with its parameters
        runIds:
          type: array
          items:
            type: string
        step:
          type: integer
    PrivateToolApproveExecutionEvent:
      type: object
      description: Sent when a tool requires user approval before execution.
      required:
        - type
        - created
        - conversationId
        - messageId
        - actionId
        - configurationId
        - inputs
      properties:
        type:
          type: string
          enum:
            - tool_approve_execution
        created:
          type: integer
        conversationId:
          type: string
        messageId:
          type: string
        actionId:
          type: string
        configurationId:
          type: string
        inputs:
          type: object
          additionalProperties: true
        stake:
          type: string
          description: Risk level of the tool execution
        isLastBlockingEventForStep:
          type: boolean
        metadata:
          type: object
        step:
          type: integer
    PrivateToolNotificationEvent:
      type: object
      description: Progress notification from a running tool.
      required:
        - type
        - created
        - configurationId
        - conversationId
        - messageId
        - action
        - notification
      properties:
        type:
          type: string
          enum:
            - tool_notification
        created:
          type: integer
        configurationId:
          type: string
        conversationId:
          type: string
        messageId:
          type: string
        action:
          type: object
          description: The MCP action producing the notification
        notification:
          type: object
          description: Progress notification content
        step:
          type: integer
    PrivateToolPersonalAuthRequiredEvent:
      type: object
      description: Sent when a tool requires personal OAuth authentication.
      required:
        - type
        - created
        - conversationId
        - messageId
        - actionId
        - configurationId
        - authError
      properties:
        type:
          type: string
          enum:
            - tool_personal_auth_required
        created:
          type: integer
        conversationId:
          type: string
        messageId:
          type: string
        actionId:
          type: string
        configurationId:
          type: string
        authError:
          type: object
          properties:
            mcpServerId:
              type: string
            provider:
              type: string
            scope:
              type: string
            toolName:
              type: string
            message:
              type: string
        step:
          type: integer
    PrivateToolFileAuthRequiredEvent:
      type: object
      description: >-
        Sent when a tool requires file access authorization (e.g., Google
        Drive).
      required:
        - type
        - created
        - conversationId
        - messageId
        - actionId
        - configurationId
        - fileAuthError
      properties:
        type:
          type: string
          enum:
            - tool_file_auth_required
        created:
          type: integer
        conversationId:
          type: string
        messageId:
          type: string
        actionId:
          type: string
        configurationId:
          type: string
        fileAuthError:
          type: object
          properties:
            fileId:
              type: string
            fileName:
              type: string
            connectionId:
              type: string
            mimeType:
              type: string
            toolName:
              type: string
            message:
              type: string
        step:
          type: integer
    PrivateAgentContextPrunedEvent:
      type: object
      required:
        - type
        - created
        - configurationId
        - messageId
      properties:
        type:
          type: string
          enum:
            - agent_context_pruned
        created:
          type: integer
        configurationId:
          type: string
        messageId:
          type: string
        step:
          type: integer
    PrivateAgentMCPAction:
      type: object
      description: An MCP action with its output.
      required:
        - id
        - sId
        - createdAt
        - updatedAt
        - agentMessageId
        - toolName
        - functionCallName
        - functionCallId
        - params
        - citationsAllocated
        - status
        - step
        - generatedFiles
        - output
      properties:
        id:
          type: integer
          description: Numeric model identifier
        sId:
          type: string
          description: Unique string identifier
        createdAt:
          type: integer
          description: Unix timestamp of creation
        updatedAt:
          type: integer
          description: Unix timestamp of last update
        agentMessageId:
          type: integer
          description: ID of the parent agent message
        internalMCPServerName:
          type: string
          nullable: true
          description: Name of the internal MCP server, if any
        toolName:
          type: string
          description: Name of the tool
        mcpServerId:
          type: string
          nullable: true
          description: ID of the MCP server, if external
        functionCallName:
          type: string
          description: Name of the function call
        functionCallId:
          type: string
          description: ID of the function call
        params:
          type: object
          description: Parameters passed to the tool
        citationsAllocated:
          type: integer
          description: Number of citations allocated
        status:
          type: string
          enum:
            - succeeded
            - errored
            - denied
            - blocked_authentication_required
            - blocked_file_authorization_required
            - blocked_validation_required
            - blocked_child_action_input_required
            - blocked_user_answer_required
            - ready_allowed_explicitly
            - ready_allowed_implicitly
            - running
          description: Execution status of the tool
        step:
          type: integer
          description: Step number in the agent execution
        executionDurationMs:
          type: integer
          nullable: true
          description: Duration of execution in milliseconds
        displayLabels:
          type: object
          nullable: true
          properties:
            running:
              type: string
            done:
              type: string
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
              snippet:
                type: string
                nullable: true
              createdAt:
                type: integer
              updatedAt:
                type: integer
              isInProjectContext:
                type: boolean
              hidden:
                type: boolean
        output:
          type: array
          nullable: true
          description: Tool call result content
          items:
            type: object
        citations:
          type: object
          nullable: true
          description: Map of citation key to citation object
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