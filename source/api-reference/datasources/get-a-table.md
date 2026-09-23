> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a table

> Get a table in the data source identified by {dsId} in the workspace identified by {wId}.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables/{tId}
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
  /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables/{tId}:
    get:
      tags:
        - Datasources
      summary: Get a table
      description: >-
        Get a table in the data source identified by {dsId} in the workspace
        identified by {wId}.
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
        - in: path
          name: dsId
          required: true
          description: ID of the data source
          schema:
            type: string
        - in: path
          name: tId
          required: true
          description: ID of the table
          schema:
            type: string
      responses:
        '200':
          description: The table
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Table'
        '404':
          description: The table was not found
      security:
        - BearerAuth: []
components:
  schemas:
    Table:
      type: object
      properties:
        name:
          type: string
          description: Name of the table
          example: Roi data
          deprecated: true
        title:
          type: string
          description: Title of the table
          example: ROI Data
        table_id:
          type: string
          description: Unique identifier for the table
          example: 1234f4567c
        description:
          type: string
          description: Description of the table
          example: roi data for Q1
        mime_type:
          type: string
          description: MIME type of the table
          example: text/csv
        schema:
          type: array
          description: Array of column definitions
          items:
            type: object
            properties:
              name:
                type: string
                description: Name of the column
                example: roi
              value_type:
                type: string
                description: Data type of the column
                enum:
                  - text
                  - int
                  - float
                  - bool
                  - date
                example: int
              possible_values:
                type: array
                description: Array of possible values for the column (null if unrestricted)
                items:
                  type: string
                nullable: true
                example:
                  - '1'
                  - '2'
                  - '3'
        timestamp:
          type: number
          description: Unix timestamp of table creation/modification
          example: 1732810375150
        tags:
          type: array
          description: Array of tags associated with the table
          items:
            type: string
        parent_id:
          type: string
          description: ID of the table parent
          items:
            type: string
          example: 1234f4567c
        parents:
          type: array
          description: Array of parent table IDs
          items:
            type: string
          example:
            - 1234f4567c
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````