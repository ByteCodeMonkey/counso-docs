> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get current user

> Returns the authenticated user with their workspaces and subscriber hash.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/user
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
  /api/user:
    get:
      tags:
        - Private User
      summary: Get current user
      description: >-
        Returns the authenticated user with their workspaces and subscriber
        hash.
      responses:
        '200':
          description: The authenticated user
          content:
            application/json:
              schema:
                type: object
                properties:
                  user:
                    $ref: '#/components/schemas/PrivateUser'
        '404':
          description: User not found
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateUser:
      type: object
      description: Authenticated user with their workspaces and subscriber hash.
      required:
        - sId
        - id
        - createdAt
        - username
        - email
        - firstName
        - fullName
        - workspaces
      properties:
        sId:
          type: string
          description: Unique string identifier for the user
        id:
          type: integer
          description: Numeric model identifier
        createdAt:
          type: integer
          description: Unix timestamp of user creation
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
          description: Authentication provider
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
          description: URL of the user's profile image
        lastLoginAt:
          type: integer
          nullable: true
        workspaces:
          type: array
          items:
            $ref: '#/components/schemas/PrivateWorkspace'
        selectedWorkspace:
          type: string
          description: sId of the currently selected workspace
        origin:
          type: string
          description: How the user joined (e.g. invitation, provisioned)
        subscriberHash:
          type: string
          nullable: true
          description: Hash used for Intercom identity verification
    PrivateWorkspace:
      type: object
      description: >-
        Workspace as returned by the private API, includes SSO and provider
        settings.
      required:
        - id
        - sId
        - name
        - role
        - regionalModelsOnly
      properties:
        id:
          type: integer
        sId:
          type: string
        name:
          type: string
        role:
          type: string
          enum:
            - admin
            - builder
            - user
            - none
        segmentation:
          type: string
          nullable: true
        whiteListedProviders:
          type: array
          nullable: true
          items:
            type: string
          description: Allowed model provider IDs
        defaultEmbeddingProvider:
          type: string
          nullable: true
        ssoEnforced:
          type: boolean
        regionalModelsOnly:
          type: boolean
          description: >-
            When true, only models whose regionalAvailability includes the
            workspace's region are usable.
        metadata:
          type: object
          nullable: true
          additionalProperties: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````