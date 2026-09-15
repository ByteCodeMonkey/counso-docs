> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Compact a conversation

> Trigger compaction of a conversation, summarizing older messages into a compaction message. Requires a model to use for summary generation.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/w/{wId}/assistant/conversations/{cId}/compactions
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
  /api/w/{wId}/assistant/conversations/{cId}/compactions:
    post:
      tags:
        - Private Conversations
      summary: Compact a conversation
      description: >-
        Trigger compaction of a conversation, summarizing older messages into a
        compaction message. Requires a model to use for summary generation.
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - model
              properties:
                model:
                  type: object
                  required:
                    - providerId
                    - modelId
                  properties:
                    providerId:
                      type: string
                    modelId:
                      type: string
      responses:
        '200':
          description: Compaction started
          content:
            application/json:
              schema:
                type: object
                properties:
                  compactionMessage:
                    $ref: '#/components/schemas/PrivateCompactionMessage'
        '400':
          description: Invalid request body
        '404':
          description: Conversation not found
        '409':
          description: Conflict — compaction or agent message is already running
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateCompactionMessage:
      type: object
      description: A compaction message summarizing earlier conversation content.
      required:
        - type
        - sId
        - status
        - version
        - rank
        - created
      properties:
        type:
          type: string
          enum:
            - compaction_message
        id:
          type: integer
        compactionMessageId:
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
        branchId:
          type: string
          nullable: true
          description: Legacy, always null. Branches were removed.
        sourceConversationId:
          type: string
          nullable: true
        status:
          type: string
          enum:
            - created
            - succeeded
            - failed
        content:
          type: string
          nullable: true
          description: Compacted summary. Null while status is "created".
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````