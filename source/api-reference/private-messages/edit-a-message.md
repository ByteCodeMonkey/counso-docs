> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit a message

> Edit the content and mentions of an existing user message in a conversation.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/edit
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
  /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/edit:
    post:
      tags:
        - Private Messages
      summary: Edit a message
      description: >-
        Edit the content and mentions of an existing user message in a
        conversation.
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - content
                - mentions
              properties:
                content:
                  type: string
                mentions:
                  type: array
                  items:
                    $ref: '#/components/schemas/PrivateMention'
      responses:
        '200':
          description: Successfully edited message
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    $ref: '#/components/schemas/PrivateUserMessage'
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````