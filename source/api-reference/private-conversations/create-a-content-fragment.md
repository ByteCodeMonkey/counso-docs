> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a content fragment

> Post a new content fragment to an existing conversation.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/w/{wId}/assistant/conversations/{cId}/content_fragment
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
  /api/w/{wId}/assistant/conversations/{cId}/content_fragment:
    post:
      tags:
        - Private Conversations
      summary: Create a content fragment
      description: Post a new content fragment to an existing conversation.
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
                - title
                - content
                - contentType
                - context
              properties:
                title:
                  type: string
                content:
                  type: string
                contentType:
                  type: string
                  description: MIME type of the content
                url:
                  type: string
                  nullable: true
                context:
                  type: object
                  properties:
                    profilePictureUrl:
                      type: string
                      nullable: true
                fileId:
                  type: string
                  nullable: true
      responses:
        '200':
          description: Successfully created content fragment
          content:
            application/json:
              schema:
                type: object
                properties:
                  contentFragment:
                    $ref: '#/components/schemas/PrivateContentFragment'
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateContentFragment:
      type: object
      description: A content fragment (file or content node attachment) in a conversation.
      required:
        - type
        - sId
        - title
        - contentType
        - contentFragmentType
      properties:
        type:
          type: string
          enum:
            - content_fragment
        id:
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
        title:
          type: string
        contentType:
          type: string
          description: MIME type of the content
        sourceUrl:
          type: string
          nullable: true
        context:
          type: object
          properties:
            username:
              type: string
              nullable: true
            fullName:
              type: string
              nullable: true
            email:
              type: string
              nullable: true
            profilePictureUrl:
              type: string
              nullable: true
        contentFragmentId:
          type: string
        contentFragmentVersion:
          type: string
          enum:
            - superseded
            - latest
        contentFragmentType:
          type: string
          enum:
            - file
            - content_node
          description: Whether this is a file upload or a content node reference
        expiredReason:
          type: string
          nullable: true
          enum:
            - data_source_deleted
        fileId:
          type: string
          nullable: true
          description: Present for file content fragments
        path:
          type: string
          nullable: true
          description: Path of this file inside the sandbox conversation mount.
        processedPath:
          type: string
          nullable: true
          description: >-
            Path of the plain-text sibling of this file inside the sandbox
            conversation mount (e.g. an audio transcript), when it has one.
        skipFileProcessing:
          type: boolean
          description: Whether upload-time file processing was skipped.
        snippet:
          type: string
          nullable: true
        textUrl:
          type: string
          nullable: true
        textBytes:
          type: integer
          nullable: true
        nodeId:
          type: string
          nullable: true
          description: Present for content node fragments
        nodeDataSourceViewId:
          type: string
          nullable: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````