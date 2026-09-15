> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a file

> Delete a file from the workspace. Files referenced by a skill or its version history cannot be deleted.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json delete /api/w/{wId}/files/{fileId}
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
    delete:
      tags:
        - Private Files
      summary: Delete a file
      description: >-
        Delete a file from the workspace. Files referenced by a skill or its
        version history cannot be deleted.
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
      responses:
        '204':
          description: File deleted
        '400':
          description: File is referenced by a skill or its version history
        '403':
          description: Permission denied
        '404':
          description: File not found
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````