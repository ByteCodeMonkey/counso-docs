> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a content fragment

> Create a new content fragment in the workspace identified by {wId}.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/v1/w/{wId}/assistant/conversations/{cId}/content_fragments
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
  /api/v1/w/{wId}/assistant/conversations/{cId}/content_fragments:
    post:
      tags:
        - Conversations
      summary: Create a content fragment
      description: Create a new content fragment in the workspace identified by {wId}.
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
              $ref: '#/components/schemas/ContentFragment'
      responses:
        '200':
          description: Content fragment created successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ContentFragment'
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '500':
          description: Internal Server Error.
      security:
        - BearerAuth: []
components:
  schemas:
    ContentFragment:
      type: object
      required:
        - title
      properties:
        title:
          type: string
          description: The title of the content fragment
          example: My content fragment
        content:
          type: string
          description: The content of the content fragment (optional if `fileId` is set)
          example: This is my content fragment extracted text
        contentType:
          type: string
          description: >-
            The content type of the content fragment (optional if `fileId` is
            set)
          example: text/plain
        url:
          type: string
          description: The URL of the content fragment
          example: https://example.com/content
        fileId:
          type: string
          description: >-
            The id of the previously uploaded file (optional if `content` and
            `contentType` are set)
          example: fil_123456
        path:
          type: string
          nullable: true
          description: Path of this file inside the sandbox conversation mount.
          example: conversation/report.csv
        processedPath:
          type: string
          nullable: true
          description: >-
            Path of the plain-text sibling of this file inside the sandbox
            conversation mount (e.g. an audio transcript), when it has one.
          example: conversation/voice.processed.txt
        skipFileProcessing:
          type: boolean
          description: Whether upload-time file processing was skipped.
        nodeId:
          type: string
          description: >-
            The id of the content node (optional if `content` and `contentType`
            are set)
          example: node_123456
        nodeDataSourceViewId:
          type: string
          description: >-
            The id of the data source view (optional if `content` and
            `contentType` are set)
          example: dsv_123456
        context:
          $ref: '#/components/schemas/Context'
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
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````