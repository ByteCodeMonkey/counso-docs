> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get feedbacks for a conversation

> Retrieves all feedback entries for a specific conversation.
Requires authentication and read:conversation scope.




## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/assistant/conversations/{cId}/feedbacks
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
  /api/v1/w/{wId}/assistant/conversations/{cId}/feedbacks:
    get:
      tags:
        - Feedbacks
      summary: Get feedbacks for a conversation
      description: |
        Retrieves all feedback entries for a specific conversation.
        Requires authentication and read:conversation scope.
      parameters:
        - name: wId
          in: path
          required: true
          schema:
            type: string
          description: Workspace ID
        - name: cId
          in: path
          required: true
          schema:
            type: string
          description: Conversation ID
      responses:
        '200':
          description: List of feedback entries for the conversation
          content:
            application/json:
              schema:
                type: object
                properties:
                  feedbacks:
                    type: array
                    items:
                      type: object
                      properties:
                        messageId:
                          type: string
                          description: ID of the message that received feedback
                        agentMessageId:
                          type: number
                          description: ID of the agent message
                        userId:
                          type: number
                          description: ID of the user who gave feedback
                        thumbDirection:
                          type: string
                          enum:
                            - up
                            - down
                          description: Direction of the thumb feedback
                        content:
                          type: string
                          nullable: true
                          description: Optional feedback content/comment
                        createdAt:
                          type: number
                          description: Timestamp when feedback was created
                        agentConfigurationId:
                          type: string
                          description: ID of the agent configuration
                        agentConfigurationVersion:
                          type: number
                          description: Version of the agent configuration
                        isConversationShared:
                          type: boolean
                          description: Whether the conversation was shared
        '400':
          description: Invalid request parameters
        '401':
          description: Unauthorized
        '403':
          description: Forbidden
        '404':
          description: Conversation not found
        '500':
          description: Internal server error
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````