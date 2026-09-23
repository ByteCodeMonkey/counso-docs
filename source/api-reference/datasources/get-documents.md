> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get documents

> Get documents in the data source identified by {dsId} in the workspace identified by {wId}.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents
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
  /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents:
    get:
      tags:
        - Datasources
      summary: Get documents
      description: >-
        Get documents in the data source identified by {dsId} in the workspace
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
          name: dsId
          required: true
          description: ID of the data source
          schema:
            type: string
        - in: query
          name: document_ids
          description: The IDs of the documents to fetch (optional)
          schema:
            type: array
            items:
              type: string
        - in: query
          name: limit
          description: Limit the number of documents returned
          schema:
            type: integer
        - in: query
          name: offset
          description: Offset the returned documents
          schema:
            type: integer
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
                      $ref: '#/components/schemas/Document'
                  total:
                    type: integer
        '404':
          description: The data source was not found
      security:
        - BearerAuth: []
components:
  schemas:
    Document:
      type: object
      properties:
        data_source_id:
          type: string
          example: 3b7d9f1e5a
        created:
          type: number
          example: 1625097600
        document_id:
          type: string
          example: 2c4a6e8d0f
        title:
          type: string
          description: Title of the document
          example: Customer Support FAQ
        mime_type:
          type: string
          description: MIME type of the table
          example: text/md
        timestamp:
          type: number
          example: 1625097600
        tags:
          type: array
          items:
            type: string
          example:
            - customer_support
            - faq
        parent_id:
          type: string
          description: ID of the document parent
          items:
            type: string
          example: 1234f4567c
        parents:
          type: array
          items:
            type: string
          example:
            - 7b9d1f3e5a
            - 2c4a6e8d0f
        source_url:
          type: string
          nullable: true
          example: https://example.com/support/article1
        hash:
          type: string
          example: a1b2c3d4e5
        text_size:
          type: number
          example: 1024
        chunk_count:
          type: number
          example: 5
        chunks:
          type: array
          items:
            type: object
          example:
            - chunk_id: 9f1d3b5a7c
              text: This is the first chunk of the document.
              embedding:
                - 0.1
                - 0.2
                - 0.3
                - 0.4
            - chunk_id: 4a2c6e8b0d
              text: This is the second chunk of the document.
              embedding:
                - 0.5
                - 0.6
                - 0.7
                - 0.8
        text:
          type: string
          example: >-
            This is the full text content of the document. It contains multiple
            paragraphs and covers various topics related to customer support.
        token_count:
          type: number
          nullable: true
          example: 150
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````