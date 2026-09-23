> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a file upload URL



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/v1/w/{wId}/files
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
  - name: Users
    description: User management
  - name: Agents
    description: Agent configurations
  - name: Analytics
    description: Workspace analytics
  - name: Apps
    description: Dust apps
  - name: Conversations
    description: Conversations
  - name: Datasources
    description: Data sources
  - name: DatasourceViews
    description: Data source views
  - name: Feedbacks
    description: Message feedbacks
  - name: MCP
    description: MCP servers
  - name: Mentions
    description: Mentions
  - name: Search
    description: Search
  - name: Skills
    description: Skills
  - name: Spaces
    description: Spaces
  - name: Tools
    description: Tools
  - name: Triggers
    description: Triggers
  - name: Workspace
    description: Workspace
  - name: Private Agents
    description: Private API - Agent configurations
  - name: Private Authentication
    description: Private API - Authentication (WorkOS)
  - name: Private Conversations
    description: Private API - Conversations
  - name: Private Events
    description: Private API - SSE event streams
  - name: Private Extension
    description: Private API - Extension configuration
  - name: Private Files
    description: Private API - File uploads
  - name: Private Mentions
    description: Private API - Mention suggestions
  - name: Private Messages
    description: Private API - Messages
  - name: Private Spaces
    description: Private API - Spaces and data source views
  - name: Private User
    description: Private API - User
  - name: Private Workspace
    description: Private API - Workspace settings
paths:
  /api/v1/w/{wId}/files:
    post:
      tags:
        - Conversations
      summary: Create a file upload URL
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
                - contentType
                - fileName
                - fileSize
                - useCase
                - useCaseMetadata
              properties:
                contentType:
                  type: string
                  description: MIME type of the file
                fileName:
                  type: string
                  description: Name of the file
                fileSize:
                  type: integer
                  description: Size of the file in bytes
                useCase:
                  type: string
                  description: Intended use case for the file, use "conversation"
                useCaseMetadata:
                  type: string
                  description: >-
                    (optional) Metadata for the use case, for conversation
                    useCase should be dictionary with conversationId stringified
      responses:
        '200':
          description: File upload URL created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  file:
                    type: object
                    properties:
                      sId:
                        type: string
                        description: Unique string identifier for the file
                      uploadUrl:
                        type: string
                        description: Upload URL for the file
        '400':
          description: Invalid request or unsupported file type
        '401':
          description: Unauthorized
        '429':
          description: Rate limit exceeded
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````