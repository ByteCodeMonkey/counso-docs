> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Download a conversation-scoped file by path

> Download a file from a conversation's file system by its scoped path. Pass the
canonical `filePath` surfaced in a message action's `generatedFiles` (the legacy
`conversation/foo.pdf` form is also accepted). The file content is streamed
directly from the conversation mount.




## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/assistant/conversations/{cId}/files/{rel}
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
  /api/v1/w/{wId}/assistant/conversations/{cId}/files/{rel}:
    get:
      tags:
        - Conversations
      summary: Download a conversation-scoped file by path
      description: >
        Download a file from a conversation's file system by its scoped path.
        Pass the

        canonical `filePath` surfaced in a message action's `generatedFiles`
        (the legacy

        `conversation/foo.pdf` form is also accepted). The file content is
        streamed

        directly from the conversation mount.
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
        - name: rel
          in: path
          required: true
          description: >
            Conversation-scoped file path: the canonical `filePath` returned in
            a message

            action's `generatedFiles`, or the legacy `conversation/foo.pdf`
            form. Paths

            scoped to another conversation or to a different scope are rejected.
            Path

            traversal segments (`..`) are rejected.
          schema:
            type: string
      responses:
        '200':
          description: File content streamed directly.
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
        '400':
          description: >-
            Missing or invalid path parameters (e.g. missing or wrong scope
            prefix).
        '403':
          description: Resolved path is outside the conversation scope.
        '404':
          description: Conversation or file not found.
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````