> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# List rows

> List rows in the table identified by {tId} in the data source identified by {dsId} in the workspace identified by {wId}.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables/{tId}/rows
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
  /api/v1/w/{wId}/spaces/{spaceId}/data_sources/{dsId}/tables/{tId}/rows:
    get:
      tags:
        - Datasources
      summary: List rows
      description: >-
        List rows in the table identified by {tId} in the data source identified
        by {dsId} in the workspace identified by {wId}.
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
        - in: query
          name: limit
          description: Limit the number of rows returned
          schema:
            type: integer
        - in: query
          name: offset
          description: Offset the returned rows
          schema:
            type: integer
      responses:
        '200':
          description: The rows
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Datasource'
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '404':
          description: Table, data source or workspace not found.
        '500':
          description: Internal Server Error.
      security:
        - BearerAuth: []
components:
  schemas:
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