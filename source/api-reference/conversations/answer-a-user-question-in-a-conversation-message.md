> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Answer a user question in a conversation message

> Submits an answer to a question asked by an agent in a specific message



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/answer-question
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
  /api/v1/w/{wId}/assistant/conversations/{cId}/messages/{mId}/answer-question:
    post:
      tags:
        - Conversations
      summary: Answer a user question in a conversation message
      description: Submits an answer to a question asked by an agent in a specific message
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
        - in: path
          name: mId
          required: true
          schema:
            type: string
          description: Message ID
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - actionId
                - answer
              properties:
                actionId:
                  type: string
                  description: ID of the action to answer
                answer:
                  type: object
                  required:
                    - selectedOptions
                  properties:
                    selectedOptions:
                      type: array
                      items:
                        type: integer
                      description: Indices of selected options
                    customResponse:
                      type: string
                      description: Optional free-text response
      responses:
        '200':
          description: Answer submitted successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
        '400':
          description: Invalid request body or action not blocked
        '403':
          description: User not authorized to answer this question
        '404':
          description: Conversation, message, or action not found
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