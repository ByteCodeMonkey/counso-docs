> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a data source view

> Creates a new data source view in a specific space.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/w/{wId}/spaces/{spaceId}/data_source_views
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
  /api/w/{wId}/spaces/{spaceId}/data_source_views:
    post:
      tags:
        - Private Spaces
      summary: Create a data source view
      description: Creates a new data source view in a specific space.
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - dataSourceId
              properties:
                dataSourceId:
                  type: string
                parentsIn:
                  type: array
                  items:
                    type: string
      responses:
        '201':
          description: Successfully created data source view
          content:
            application/json:
              schema:
                type: object
                properties:
                  dataSourceView:
                    $ref: '#/components/schemas/PrivateDataSourceView'
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateDataSourceView:
      type: object
      description: A view on a data source within a space.
      required:
        - sId
        - id
        - category
        - kind
        - spaceId
        - dataSource
      properties:
        sId:
          type: string
        id:
          type: integer
        category:
          type: string
          enum:
            - managed
            - folder
            - website
            - apps
        kind:
          type: string
          enum:
            - default
            - custom
        spaceId:
          type: string
        createdAt:
          type: integer
        updatedAt:
          type: integer
        parentsIn:
          type: array
          nullable: true
          items:
            type: string
          description: >-
            List of parent IDs included in this view, null if the full data
            source is used
        dataSource:
          $ref: '#/components/schemas/PrivateDataSource'
        editedByUser:
          type: object
          nullable: true
          properties:
            editedAt:
              type: integer
              nullable: true
            fullName:
              type: string
              nullable: true
            imageUrl:
              type: string
              nullable: true
            email:
              type: string
              nullable: true
            userId:
              type: string
              nullable: true
        usage:
          type: object
          description: >-
            Present when the view was fetched with usage details (withDetails
            query param). Counts agents and skills that use this data source
            view.
          properties:
            count:
              type: integer
            agents:
              type: array
              items:
                type: object
                properties:
                  sId:
                    type: string
                  name:
                    type: string
                  pictureUrl:
                    type: string
            skills:
              type: array
              items:
                type: object
                properties:
                  sId:
                    type: string
                  name:
                    type: string
                  icon:
                    type: string
                    nullable: true
    PrivateDataSource:
      type: object
      description: A data source in the workspace.
      required:
        - sId
        - id
        - name
      properties:
        sId:
          type: string
        id:
          type: integer
        createdAt:
          type: integer
        name:
          type: string
        description:
          type: string
          nullable: true
        assistantDefaultSelected:
          type: boolean
        dustAPIProjectId:
          type: string
        dustAPIDataSourceId:
          type: string
        connectorId:
          type: string
          nullable: true
        connectorProvider:
          type: string
          nullable: true
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````