> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# List Data Source Views

> Retrieves a list of data source views for the specified space



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/spaces/{spaceId}/data_source_views
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
  /api/v1/w/{wId}/spaces/{spaceId}/data_source_views:
    get:
      tags:
        - DatasourceViews
      summary: List Data Source Views
      description: Retrieves a list of data source views for the specified space
      parameters:
        - in: path
          name: wId
          required: true
          description: Unique string identifier for the workspace
          schema:
            type: string
        - in: path
          name: spaceId
          required: true
          description: ID of the space
          schema:
            type: string
      responses:
        '200':
          description: List of data source views in the space
          content:
            application/json:
              schema:
                type: object
                properties:
                  dataSourceViews:
                    type: array
                    items:
                      $ref: '#/components/schemas/DatasourceView'
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '404':
          description: Workspace not found.
        '500':
          description: Internal Server Error.
      security:
        - BearerAuth: []
components:
  schemas:
    DatasourceView:
      type: object
      properties:
        category:
          type: string
          enum:
            - managed
            - folder
            - website
            - apps
          description: The category of the data source view
        createdAt:
          type: number
          description: Timestamp of when the data source view was created
        dataSource:
          $ref: '#/components/schemas/Datasource'
        editedByUser:
          type: object
          description: The user who last edited the data source view
          properties:
            fullName:
              type: string
              description: Full name of the user
            editedAt:
              type: number
              description: >-
                Timestamp of when the data source view was last edited by the
                user
        id:
          type: number
          description: Unique identifier for the data source view
        kind:
          type: string
          enum:
            - default
            - custom
          description: The kind of the data source view
        parentsIn:
          type: array
          items:
            type: string
          description: >-
            List of IDs included in this view, null if complete data source is
            taken
          nullable: true
        sId:
          type: string
          description: Unique string identifier for the data source view
        updatedAt:
          type: number
          description: Timestamp of when the data source view was last updated
        spaceId:
          type: string
          description: ID of the space containing the data source view
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