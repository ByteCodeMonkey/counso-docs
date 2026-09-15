> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get events for a message

> Get events for a message in the workspace identified by {wId}.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/events
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
  /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/events:
    get:
      tags:
        - Conversations
      summary: Get events for a message
      description: Get events for a message in the workspace identified by {wId}.
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
        - in: query
          name: lastEventId
          description: ID of the last event received
          schema:
            type: string
      responses:
        '200':
          description: The events
          content:
            application/json:
              schema:
                type: object
                properties:
                  events:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: ID of the event
                        type:
                          type: string
                          description: Type of the event
                        data:
                          $ref: '#/components/schemas/Message'
        '400':
          description: Bad Request
        '401':
          description: Unauthorized
        '404':
          description: Not Found
        '500':
          description: Internal Server Error
      security:
        - BearerAuth: []
components:
  schemas:
    Message:
      type: object
      required:
        - content
        - mentions
      properties:
        content:
          type: string
          description: The content of the message. Should not be empty.
          example: This is my message
        mentions:
          type: array
          description: Empty array is accepted but won't trigger any agent.
          items:
            $ref: '#/components/schemas/Mention'
        context:
          $ref: '#/components/schemas/Context'
        modelSelection:
          $ref: '#/components/schemas/ModelSelection'
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
    ModelSelection:
      type: object
      description: |
        Optional per-message model and reasoning-effort override applied to the
        mentioned agent(s). When omitted, each agent runs its configured model.
        A provider/model pair that is not authorized for the workspace is
        rejected with a 400 (`model_disabled`), it does not fall back to the
        agent's configured model. A malformed object, or an unknown reasoning
        effort, also results in a 400.
      required:
        - providerId
        - modelId
      properties:
        providerId:
          type: string
          description: >-
            The model provider id (e.g. "anthropic", "openai",
            "google_ai_studio").
          example: anthropic
        modelId:
          type: string
          description: The model id to run (e.g. "claude-sonnet-4-20250514").
          example: claude-sonnet-4-20250514
        reasoningEffort:
          type: string
          enum:
            - none
            - light
            - medium
            - high
          description: >-
            Optional reasoning effort. Honored only if the resolved model
            supports it.
          example: medium
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````