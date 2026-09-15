> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a space

> Creates a new space in the workspace.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/w/{wId}/spaces
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
    post:
      tags:
        - Private Spaces
      summary: Create a space
      description: Creates a new space in the workspace.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - isRestricted
                - name
                - spaceKind
              properties:
                isRestricted:
                  type: boolean
                name:
                  type: string
                spaceKind:
                  type: string
                  enum:
                    - regular
                    - project
                memberIds:
                  type: array
                  items:
                    type: string
                  description: >-
                    The space's manual member list. Omitted or empty means the
                    space starts with no manual member.
                groupIds:
                  type: array
                  items:
                    type: string
                  description: >-
                    The groups given access to the space. Omitted or empty means
                    no group has access to it.
      responses:
        '201':
          description: Successfully created space
          content:
            application/json:
              schema:
                type: object
                properties:
                  space:
                    $ref: '#/components/schemas/PrivateSpace'
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