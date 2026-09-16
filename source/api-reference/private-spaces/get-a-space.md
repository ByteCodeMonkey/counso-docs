> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a space

> Returns the details of a specific space including categories, members, and permissions.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/spaces/{spaceId}
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
  /api/w/{wId}/spaces/{spaceId}:
    get:
      tags:
        - Private Spaces
      summary: Get a space
      description: >-
        Returns the details of a specific space including categories, members,
        and permissions.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: path
          name: spaceId
          required: true
          description: ID of the space
          schema:
            type: string
        - in: query
          name: includeAllMembers
          required: false
          description: Include all members (including inactive)
          schema:
            type: string
            enum:
              - 'true'
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  space:
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
                          categories:
                            type: object
                            additionalProperties:
                              type: object
                              properties:
                                count:
                                  type: integer
                                usage:
                                  type: object
                                  properties:
                                    count:
                                      type: integer
                                    agents:
                                      type: array
                                      items:
                                        type: object
                          canWrite:
                            type: boolean
                          canRead:
                            type: boolean
                          isMember:
                            type: boolean
                          isEditor:
                            type: boolean
                          members:
                            type: array
                            items:
                              type: object
                          groups:
                            type: array
                            description: >-
                              The groups given access to the space, with the
                              role their grant confers.
                            items:
                              type: object
                              properties:
                                sId:
                                  type: string
                                name:
                                  type: string
                                kind:
                                  type: string
                                role:
                                  type: string
                                  enum:
                                    - member
                                    - editor
                          description:
                            type: string
                            nullable: true
                          archivedAt:
                            type: integer
                            nullable: true
                          todoGenerationEnabled:
                            type: boolean
                            description: >-
                              Whether automatic todo suggestions from project
                              activity are enabled.
                          lastTodoAnalysisAt:
                            type: integer
                            nullable: true
                            description: >-
                              Unix timestamp (ms) of the last automatic todo
                              suggestion scan, if any.
                          pinnedFramePath:
                            type: string
                            nullable: true
                            description: >-
                              Scoped path to the MiniApp file pinned as the Pod
                              banner.
                          frameTabs:
                            type: array
                            description: MiniApps promoted as custom Pod tabs.
                            items:
                              type: object
                              properties:
                                path:
                                  type: string
                                title:
                                  type: string
                                icon:
                                  type: string
                          tabsOrder:
                            type: array
                            description: >-
                              Interleaved system tab ids and MiniApp paths before
                              Settings.
                            items:
                              type: string
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````