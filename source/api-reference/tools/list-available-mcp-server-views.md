> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# List available MCP server views.

> Retrieves a list of enabled MCP server views (aka tools) for a specific space of the authenticated workspace.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/spaces/{spaceId}/mcp_server_views
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
  /api/v1/w/{wId}/spaces/{spaceId}/mcp_server_views:
    get:
      tags:
        - Tools
      summary: List available MCP server views.
      description: >-
        Retrieves a list of enabled MCP server views (aka tools) for a specific
        space of the authenticated workspace.
      parameters:
        - in: path
          name: wId
          required: true
          description: Unique string identifier for the workspace
          schema:
            type: string
        - in: path
          name: spaceId
          required: true
          description: ID of the space
          schema:
            type: string
      responses:
        '200':
          description: MCP server views of the space
          content:
            application/json:
              schema:
                type: object
                properties:
                  spaces:
                    type: array
                    items:
                      $ref: '#/components/schemas/MCPServerView'
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '404':
          description: Workspace not found.
        '500':
          description: Internal Server Error.
      security:
        - BearerAuth: []
components:
  schemas:
    MCPServerView:
      type: object
      required:
        - isRestrictedToSkills
      properties:
        id:
          type: integer
          description: Unique identifier for the MCP server view
          example: 123
        sId:
          type: string
          description: Unique string identifier for the MCP server view
          example: mcp_sv_abc123
        name:
          type: string
          nullable: true
          description: Custom name for the MCP server view (null if not set)
          example: My Custom MCP Server
        description:
          type: string
          nullable: true
          description: Custom description for the MCP server view (null if not set)
          example: This MCP server handles customer data operations
        createdAt:
          type: number
          description: Unix timestamp of when the MCP server view was created
          example: 1625097600
        updatedAt:
          type: number
          description: Unix timestamp of when the MCP server view was last updated
          example: 1625184000
        spaceId:
          type: string
          description: ID of the space containing the MCP server view
          example: spc_xyz789
        serverType:
          type: string
          enum:
            - remote
            - internal
          description: Type of the MCP server
          example: remote
        server:
          type: object
          properties:
            sId:
              type: string
              description: Unique string identifier for the MCP server
              example: mcp_srv_def456
            name:
              type: string
              description: Name of the MCP server
              example: Customer Data Server
            version:
              type: string
              description: Version of the MCP server
              example: 1.0.0
            description:
              type: string
              description: Description of the MCP server
              example: Handles customer data operations and queries
            icon:
              type: string
              description: Icon identifier for the MCP server
              example: database
            authorization:
              type: object
              nullable: true
              properties:
                provider:
                  type: string
                  description: OAuth provider for authorization
                  example: github
                supported_use_cases:
                  type: array
                  items:
                    type: string
                    enum:
                      - platform_actions
                      - personal_actions
                  description: Supported use cases for the authorization
                  example:
                    - platform_actions
                scope:
                  type: string
                  description: OAuth scope required
                  example: repo:read
            tools:
              type: array
              items:
                type: object
                properties:
                  name:
                    type: string
                    description: Name of the tool
                    example: query_customers
                  description:
                    type: string
                    description: Description of what the tool does
                    example: Query customer database for information
                  inputSchema:
                    type: object
                    description: JSON Schema for the tool's input parameters
                    example:
                      type: object
                      properties:
                        customerId:
                          type: string
            availability:
              type: string
              description: Availability status of the MCP server
              example: production
            allowMultipleInstances:
              type: boolean
              description: Whether multiple instances of this server can be created
              example: false
            documentationUrl:
              type: string
              nullable: true
              description: URL to the server's documentation
              example: https://docs.example.com/mcp-server
        oAuthUseCase:
          type: string
          nullable: true
          enum:
            - platform_actions
            - personal_actions
          description: OAuth use case for the MCP server view
          example: platform_actions
        isRestrictedToSkills:
          type: boolean
          description: Whether the MCP server view can only be used through skills
          example: false
        editedByUser:
          type: object
          nullable: true
          description: Information about the user who last edited the MCP server view
          properties:
            editedAt:
              type: number
              nullable: true
              description: Unix timestamp of when the edit occurred
              example: 1625184000
            fullName:
              type: string
              nullable: true
              description: Full name of the editor
              example: John Doe
            imageUrl:
              type: string
              nullable: true
              description: Profile image URL of the editor
              example: https://example.com/profile/johndoe.jpg
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````