> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Search the data source view

> Search the data source view identified by {dsvId} in the workspace identified by {wId}.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}/search
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
  /api/v1/w/{wId}/spaces/{spaceId}/data_source_views/{dsvId}/search:
    get:
      tags:
        - DatasourceViews
      summary: Search the data source view
      description: >-
        Search the data source view identified by {dsvId} in the workspace
        identified by {wId}.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: path
          name: spaceId
          required: true
          description: ID of the space
          schema:
            type: string
        - in: path
          name: dsvId
          required: true
          description: ID of the data source view
          schema:
            type: string
        - in: query
          name: query
          required: true
          description: The search query
          schema:
            type: string
        - in: query
          name: top_k
          required: true
          description: The number of results to return
          schema:
            type: number
        - in: query
          name: full_text
          required: true
          description: Whether to return the full document content
          schema:
            type: boolean
        - in: query
          name: target_document_tokens
          required: false
          description: The number of tokens in the target document
          schema:
            type: number
        - in: query
          name: timestamp_gt
          required: false
          description: The timestamp to filter by
          schema:
            type: number
        - in: query
          name: timestamp_lt
          required: false
          description: The timestamp to filter by
          schema:
            type: number
        - in: query
          name: tags_in
          required: false
          description: The tags to filter by
          schema:
            type: string
        - in: query
          name: tags_not
          required: false
          description: The tags to filter by
          schema:
            type: string
        - in: query
          name: parents_in
          required: false
          description: The parents to filter by
          schema:
            type: string
        - in: query
          name: parents_not
          required: false
          description: The parents to filter by
          schema:
            type: string
      responses:
        '200':
          description: The documents
          content:
            application/json:
              schema:
                type: object
                properties:
                  documents:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: ID of the document
                        title:
                          type: string
                          description: Title of the document
                        content:
                          type: string
                          description: Content of the document
                        tags:
                          type: array
                          items:
                            type: string
                          description: Tags of the document
                        parents:
                          type: array
                          items:
                            type: string
                          description: Parents of the document
                        timestamp:
                          type: number
                          description: Timestamp of the document
                        data:
                          type: object
                          description: Data of the document
                        score:
                          type: number
                          description: Score of the document
        '400':
          description: Invalid request error
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````