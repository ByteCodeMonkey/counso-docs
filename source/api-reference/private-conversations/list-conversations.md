> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# List conversations

> Retrieve a paginated list of conversations for the authenticated user in the workspace.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/assistant/conversations
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
  /api/w/{wId}/assistant/conversations:
    get:
      tags:
        - Private Conversations
      summary: List conversations
      description: >-
        Retrieve a paginated list of conversations for the authenticated user in
        the workspace.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
      responses:
        '200':
          description: Successfully retrieved conversations
          content:
            application/json:
              schema:
                type: object
                properties:
                  conversations:
                    type: array
                    items:
                      $ref: '#/components/schemas/PrivateConversation'
                  hasMore:
                    type: boolean
                  lastValue:
                    type: string
                    nullable: true
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateConversation:
      type: object
      description: Conversation without content, used in list responses.
      required:
        - id
        - created
        - updated
        - sId
        - depth
      properties:
        id:
          type: integer
        created:
          type: integer
          description: Unix timestamp of creation
        updated:
          type: integer
          description: Unix timestamp of last update
        unread:
          type: boolean
        lastReadMs:
          type: integer
          nullable: true
        actionRequired:
          type: boolean
          description: Whether the conversation requires user action
        hasError:
          type: boolean
        sId:
          type: string
        title:
          type: string
          nullable: true
        spaceId:
          type: string
          nullable: true
          description: >-
            ID of the space the conversation belongs to (for project
            conversations)
        triggerId:
          type: string
          nullable: true
        depth:
          type: integer
          description: Conversation depth (for agent handover chains)
        metadata:
          type: object
          additionalProperties: true
        requestedSpaceIds:
          type: array
          items:
            type: string
        forkingData:
          $ref: '#/components/schemas/PrivateConversationForkingData'
    PrivateConversationForkingData:
      type: object
      properties:
        forkedFrom:
          $ref: '#/components/schemas/PrivateConversationForkedFrom'
        forkedChildren:
          type: array
          items:
            $ref: '#/components/schemas/PrivateConversationForkedChild'
    PrivateConversationForkedFrom:
      type: object
      required:
        - parentConversationId
        - parentConversationTitle
        - sourceMessageId
        - branchedAt
        - user
        - fileCopyStatus
      properties:
        parentConversationId:
          type: string
        parentConversationTitle:
          type: string
          nullable: true
        sourceMessageId:
          type: string
        branchedAt:
          type: integer
        user:
          $ref: '#/components/schemas/PrivateConversationForkUser'
        fileCopyStatus:
          type: string
          enum:
            - pending
            - done
    PrivateConversationForkedChild:
      type: object
      properties:
        childConversationId:
          type: string
        childConversationTitle:
          type: string
          nullable: true
        sourceMessageId:
          type: string
        branchedAt:
          type: integer
        user:
          $ref: '#/components/schemas/PrivateConversationForkUser'
    PrivateConversationForkUser:
      type: object
      properties:
        sId:
          type: string
        id:
          type: integer
        createdAt:
          type: integer
        provider:
          type: string
          nullable: true
          enum:
            - auth0
            - github
            - google
            - okta
            - samlp
            - waad
        username:
          type: string
        email:
          type: string
        firstName:
          type: string
        lastName:
          type: string
          nullable: true
        fullName:
          type: string
        image:
          type: string
          nullable: true
        lastLoginAt:
          type: integer
          nullable: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````