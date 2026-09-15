> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Resolve a conversation go template draft

> Fetches a Contentful conversation go template by slug and returns a composer-ready draft with optional pre-uploaded attachments.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/assistant/go-template
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
  /api/w/{wId}/assistant/go-template:
    get:
      tags:
        - Private Assistant
      summary: Resolve a conversation go template draft
      description: >-
        Fetches a Contentful conversation go template by slug and returns a
        composer-ready draft with optional pre-uploaded attachments.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: query
          name: slug
          required: true
          description: Contentful template slug
          schema:
            type: string
      responses:
        '200':
          description: Composer draft resolved from the template
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetGoTemplateDraftResponseBody'
        '404':
          description: Template not found or disabled
        '422':
          description: Missing slug query parameter
      security:
        - BearerAuth: []
components:
  schemas:
    GetGoTemplateDraftResponseBody:
      type: object
      description: Composer draft resolved from a Contentful conversation go template.
      required:
        - title
        - prompt
        - attachments
        - attachmentErrors
      properties:
        title:
          type: string
        prompt:
          type: string
        attachments:
          type: array
          items:
            type: object
            required:
              - fileId
              - name
              - contentType
              - size
              - url
            properties:
              fileId:
                type: string
              name:
                type: string
              contentType:
                type: string
              size:
                type: integer
              url:
                type: string
        attachmentErrors:
          type: array
          items:
            type: object
            required:
              - url
              - message
            properties:
              url:
                type: string
              message:
                type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````