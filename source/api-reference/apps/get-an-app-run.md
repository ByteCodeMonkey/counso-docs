> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an app run

> Retrieve a run for an app in the space identified by {spaceId}.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/v1/w/{wId}/spaces/{spaceId}/apps/{aId}/runs/{runId}
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
  /api/v1/w/{wId}/spaces/{spaceId}/apps/{aId}/runs/{runId}:
    get:
      tags:
        - Apps
      summary: Get an app run
      description: Retrieve a run for an app in the space identified by {spaceId}.
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
          name: aId
          required: true
          description: ID of the app
          schema:
            type: string
        - in: path
          name: runId
          required: true
          description: ID of the run
          schema:
            type: string
      responses:
        '200':
          description: The run
          content:
            application/json:
              schema:
                type: object
                properties:
                  run:
                    $ref: '#/components/schemas/Run'
        '400':
          description: Bad Request. Missing or invalid parameters.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
      security:
        - BearerAuth: []
components:
  schemas:
    Run:
      type: object
      properties:
        run_id:
          type: string
          description: The ID of the run
          example: 4a2c6e8b0d
        app_id:
          type: string
          description: The ID of the app
          example: 9f1d3b5a7c
        status:
          type: object
          properties:
            run:
              type: string
              description: The status of the run
              example: succeeded
            build:
              type: string
              description: The status of the build
              example: succeeded
        results:
          type: object
          description: The results of the run
          example: {}
        specification_hash:
          type: string
          description: The hash of the app specification
          example: 8c0a4e6d2f
        traces:
          type: array
          items:
            type: array
            items:
              type: object
              properties:
                timestamp:
                  type: number
                  description: The timestamp of the trace
                  example: 1234567890
                trace:
                  type: object
                  description: The trace
                  example: {}
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````