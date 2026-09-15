> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# List agent configurations

> Returns all agent configurations in the workspace.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/assistant/agent_configurations
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
  /api/w/{wId}/assistant/agent_configurations:
    get:
      tags:
        - Private Agents
      summary: List agent configurations
      description: Returns all agent configurations in the workspace.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: query
          name: view
          required: false
          description: Filter agents by view
          schema:
            type: string
            enum:
              - all
              - analytics
              - list
              - favorites
              - published
              - admin_internal
              - manage_unrestricted
              - global
              - workspace
        - in: query
          name: limit
          required: false
          description: Maximum number of results to return
          schema:
            type: integer
        - in: query
          name: withUsage
          required: false
          description: Include usage statistics
          schema:
            type: string
            enum:
              - 'true'
        - in: query
          name: withAuthors
          required: false
          description: Include recent authors
          schema:
            type: string
            enum:
              - 'true'
        - in: query
          name: withFeedbacks
          required: false
          description: Include feedback counts
          schema:
            type: string
            enum:
              - 'true'
        - in: query
          name: withEditors
          required: false
          description: Include editors list
          schema:
            type: string
            enum:
              - 'true'
        - in: query
          name: sort
          required: false
          description: Sort order
          schema:
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  agentConfigurations:
                    type: array
                    items:
                      $ref: '#/components/schemas/PrivateLightAgentConfiguration'
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````