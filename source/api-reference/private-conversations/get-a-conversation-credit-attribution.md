> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a conversation credit attribution

> Returns the latest stable credits billed for completed messages belonging directly to a conversation, plus an additive attribution reconciled exclusively through model input rows. In-progress messages are included after they reach a terminal state.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/assistant/conversations/{cId}/consumption
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
  /api/w/{wId}/assistant/conversations/{cId}/consumption:
    get:
      tags:
        - Private Conversations
      summary: Get a conversation credit attribution
      description: >-
        Returns the latest stable credits billed for completed messages
        belonging directly to a conversation, plus an additive attribution
        reconciled exclusively through model input rows. In-progress messages
        are included after they reach a terminal state.
      parameters:
        - name: wId
          in: path
          required: true
          schema:
            type: string
        - in: path
          name: cId
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Conversation credit attribution
          content:
            application/json:
              schema:
                type: object
                required:
                  - billedCredits
                  - details
                properties:
                  billedCredits:
                    type: number
                    description: >-
                      Latest stable credits billed across completed messages
                      belonging directly to the conversation.
                  details:
                    type: object
                    allOf:
                      - $ref: >-
                          #/components/schemas/PrivateConversationConsumptionDetails
                    nullable: true
        '404':
          description: Conversation not found
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateConversationConsumptionDetails:
      type: object
      description: >-
        Additive attribution reconciled to the authoritative bill exclusively
        through model input rows. Each message uses its newest complete stored
        attribution version. Null when any billed message has no complete stored
        attribution.
      required:
        - agentWorkCredits
        - tools
        - models
        - agents
      properties:
        agentWorkCredits:
          type: number
          description: >-
            Agent work after assigning billing reconciliation exclusively to
            model input rows.
        tools:
          type: array
          items:
            $ref: '#/components/schemas/PrivateConversationConsumptionToolDetails'
        models:
          type: array
          items:
            $ref: '#/components/schemas/PrivateConversationConsumptionModelDetails'
        agents:
          type: array
          items:
            $ref: '#/components/schemas/PrivateConversationConsumptionAgentDetails'
    PrivateConversationConsumptionToolDetails:
      type: object
      required:
        - label
        - internalMCPServerName
        - toolName
        - callCount
        - attributedCredits
        - directCredits
        - pending
      properties:
        label:
          type: string
        internalMCPServerName:
          type: string
          nullable: true
        toolName:
          type: string
        callCount:
          type: integer
        attributedCredits:
          type: number
          description: >-
            Share of billed credits after reconciling exclusively through model
            input rows.
        directCredits:
          type: number
        pending:
          type: boolean
    PrivateConversationConsumptionModelDetails:
      type: object
      required:
        - providerId
        - modelId
        - displayName
        - attributedCredits
      properties:
        providerId:
          type: string
        modelId:
          type: string
        displayName:
          type: string
        attributedCredits:
          type: number
          description: >-
            Model attribution after reconciling exclusively through its input
            rows.
    PrivateConversationConsumptionAgentDetails:
      type: object
      required:
        - agentId
        - name
        - pictureUrl
        - billedCredits
        - agentWorkCredits
        - tools
        - models
      properties:
        agentId:
          type: string
        name:
          type: string
        pictureUrl:
          type: string
          nullable: true
        billedCredits:
          type: number
        agentWorkCredits:
          type: number
          description: >-
            Agent work after assigning billing reconciliation exclusively to
            model input rows.
        tools:
          type: array
          items:
            $ref: '#/components/schemas/PrivateConversationConsumptionToolDetails'
        models:
          type: array
          items:
            $ref: '#/components/schemas/PrivateConversationConsumptionModelDetails'
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````