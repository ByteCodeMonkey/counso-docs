> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# List spaces

> Returns all spaces in the workspace.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/spaces
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
  /api/w/{wId}/spaces:
    get:
      tags:
        - Private Spaces
      summary: List spaces
      description: Returns all spaces in the workspace.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: query
          name: role
          required: false
          description: Filter by role (e.g. admin to list all workspace spaces)
          schema:
            type: string
        - in: query
          name: kind
          required: false
          description: >-
            Filter by one or more space kinds. Repeat the parameter to include
            several kinds.
          style: form
          explode: true
          schema:
            type: array
            items:
              type: string
              enum:
                - global
                - system
                - conversations
                - regular
                - project
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  spaces:
                    type: array
                    items:
                      oneOf:
                        - $ref: '#/components/schemas/PrivateSpace'
                        - $ref: '#/components/schemas/PrivateProject'
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateSpace:
      type: object
      description: A space in the workspace.
      required:
        - sId
        - name
        - kind
      properties:
        sId:
          type: string
        name:
          type: string
        kind:
          type: string
          enum:
            - global
            - system
            - conversations
            - regular
            - project
        createdAt:
          type: integer
        updatedAt:
          type: integer
    PrivateProject:
      type: object
      description: A project space with additional metadata.
      allOf:
        - $ref: '#/components/schemas/PrivateSpace'
        - type: object
          properties:
            groupIds:
              type: array
              items:
                type: string
            isRestricted:
              type: boolean
            description:
              type: string
              nullable: true
            isMember:
              type: boolean
            archivedAt:
              type: integer
              nullable: true
            todoGenerationEnabled:
              type: boolean
              description: >-
                Whether automatic todo suggestions from project activity are
                enabled.
            lastTodoAnalysisAt:
              type: integer
              nullable: true
              description: >-
                Unix timestamp (ms) of the last automatic todo suggestion scan,
                if any.
            pinnedFramePath:
              type: string
              nullable: true
              description: >-
                Scoped path to the frame file pinned as the Pod banner (e.g.
                project/banner.html).
            frameTabs:
              type: array
              description: Frames promoted as custom Pod tabs (shared for all members).
              items:
                type: object
                required:
                  - path
                  - title
                  - icon
                properties:
                  path:
                    type: string
                    description: >-
                      Canonical scoped path to the frame file in the Pod
                      filesystem.
                  title:
                    type: string
                    description: Display title for the tab.
                  icon:
                    type: string
                    description: Action icon name (e.g. ActionDashboardIcon).
            tabsOrder:
              type: array
              description: Interleaved system tab ids and frame paths before Settings.
              items:
                type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````