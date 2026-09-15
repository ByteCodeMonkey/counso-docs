> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload file content

> Process and store the uploaded file content.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/w/{wId}/files/{fileId}
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
  /api/w/{wId}/files/{fileId}:
    post:
      tags:
        - Private Files
      summary: Upload file content
      description: Process and store the uploaded file content.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: path
          name: fileId
          required: true
          description: ID of the file
          schema:
            type: string
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
      responses:
        '200':
          description: File processed successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  file:
                    $ref: '#/components/schemas/PrivateFileWithUploadUrl'
        '400':
          description: Invalid file content (e.g. a CSV with an unsupported encoding)
        '403':
          description: Permission denied
        '404':
          description: File not found
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