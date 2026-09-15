> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Upsert a document in a data source

> Upsert a document in a data source in the workspace identified by {wId}.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}
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
  /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/documents/{documentId}:
    post:
      tags:
        - Datasources
      summary: Upsert a document in a data source
      description: Upsert a document in a data source in the workspace identified by {wId}.
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
        - in: path
          name: documentId
          required: true
          description: ID of the document
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                title:
                  type: string
                  description: The title of the document to upsert.
                mime_type:
                  type: string
                  description: The MIME type of the document to upsert.
                text:
                  type: string
                  description: The text content of the document to upsert.
                section:
                  $ref: '#/components/schemas/Section'
                source_url:
                  type: string
                  description: The source URL for the document to upsert.
                tags:
                  type: array
                  items:
                    type: string
                  description: Tags to associate with the document.
                timestamp:
                  type: number
                  description: >-
                    Unix timestamp (in milliseconds) for the document (e.g.
                    1736365559000).
                light_document_output:
                  type: boolean
                  description: >-
                    If true, a lightweight version of the document will be
                    returned in the response (excluding the text, chunks and
                    vectors). Defaults to false.
                async:
                  type: boolean
                  description: >-
                    If true, the upsert operation will be performed
                    asynchronously.
                upsert_context:
                  type: object
                  description: Additional context for the upsert operation.
      responses:
        '200':
          description: The document
          content:
            application/json:
              schema:
                type: object
                properties:
                  document:
                    $ref: '#/components/schemas/Document'
                  data_source:
                    $ref: '#/components/schemas/Datasource'
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '403':
          description: Forbidden. The data source is managed.
        '404':
          description: Data source or document not found.
        '429':
          description: Rate limit exceeded.
        '500':
          description: Internal Server Error.
      security:
        - BearerAuth: []
components:
  schemas:
    Section:
      type: object
      description: A section of a document that can contain nested sections
      properties:
        prefix:
          type: string
          nullable: true
          description: Optional prefix text for the section
        content:
          type: string
          nullable: true
          description: Optional content text for the section
        sections:
          type: array
          items:
            $ref: '#/components/schemas/Section'
          description: Array of nested sections
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
    Datasource:
      type: object
      properties:
        id:
          type: integer
          description: Unique identifier for the datasource
          example: 12345
        createdAt:
          type: integer
          description: Timestamp of when the datasource was created
          example: 1625097600
        name:
          type: string
          description: Name of the datasource
          example: Customer Knowledge Base
        description:
          type: string
          description: Description of the datasource
          example: Contains all customer-related information and FAQs
        dustAPIProjectId:
          type: string
          description: ID of the associated Dust API project
          example: 5e9d8c7b6a
        connectorId:
          type: string
          description: ID of the connector used for this datasource
          example: 1f3e5d7c9b
        connectorProvider:
          type: string
          description: Provider of the connector (e.g., 'webcrawler')
          example: webcrawler
        assistantDefaultSelected:
          type: boolean
          description: Whether this datasource is selected by default for agents
          example: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````