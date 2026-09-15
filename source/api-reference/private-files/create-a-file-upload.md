> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a file upload

> Creates a file record and returns a pre-signed upload URL. The file content should then be uploaded to the returned URL.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/w/{wId}/files
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
  /api/w/{wId}/files:
    post:
      tags:
        - Private Files
      summary: Create a file upload
      description: >-
        Creates a file record and returns a pre-signed upload URL. The file
        content should then be uploaded to the returned URL.
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
              properties:
                contentType:
                  type: string
                fileName:
                  type: string
                fileSize:
                  type: number
                useCase:
                  type: string
                  enum:
                    - conversation
                    - folders_document
                    - avatar
                    - upsert_document
                    - upsert_table
                    - project_context
                    - skill_attachment
                    - workspace_branding
                useCaseMetadata:
                  type: object
      responses:
        '200':
          description: File record created with upload URL
          content:
            application/json:
              schema:
                type: object
                properties:
                  file:
                    $ref: '#/components/schemas/PrivateFileWithUploadUrl'
        '400':
          description: Invalid request
        '429':
          description: Rate limit exceeded
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateFileWithUploadUrl:
      type: object
      description: File record with a pre-signed upload URL.
      required:
        - sId
        - id
        - fileName
        - fileSize
        - contentType
        - status
        - useCase
        - uploadUrl
      properties:
        sId:
          type: string
        id:
          type: string
        contentType:
          type: string
        fileName:
          type: string
        fileSize:
          type: integer
        version:
          type: integer
        status:
          type: string
          enum:
            - created
            - failed
            - ready
        useCase:
          type: string
          enum:
            - conversation
            - avatar
            - tool_output
            - upsert_document
            - folders_document
            - upsert_table
            - project_context
            - skill_attachment
        uploadUrl:
          type: string
          description: Pre-signed URL for uploading the file content
        downloadUrl:
          type: string
        publicUrl:
          type: string
        path:
          type: string
          nullable: true
          description: >-
            path when the file is ready on a mount (e.g. `project/report.pdf` or
            `conversation/chart.png`). Same shape as mount file listing entries.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````