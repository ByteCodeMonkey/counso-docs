> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# List consumption analytics facets

> Lists current entities and historical indexed values present in the selected period for each consumption dimension. The workspace route requires a manager; the /me route is restricted server-side to the authenticated member; the agent route is restricted server-side to workspace managers and editors of the selected agent. A facet is disabled when it has no indexed document in that period after applying every active filter except the facet's own dimension.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/w/{wId}/analytics/consumption/facets
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
  /api/w/{wId}/analytics/consumption/facets:
    post:
      tags:
        - Private Analytics
      summary: List consumption analytics facets
      description: >-
        Lists current entities and historical indexed values present in the
        selected period for each consumption dimension. The workspace route
        requires a manager; the /me route is restricted server-side to the
        authenticated member; the agent route is restricted server-side to
        workspace managers and editors of the selected agent. A facet is
        disabled when it has no indexed document in that period after applying
        every active filter except the facet's own dimension.
      parameters:
        - name: wId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                period:
                  type: string
                  enum:
                    - cycle
                    - days
                  default: cycle
                days:
                  type: integer
                  minimum: 1
                  default: 30
                scope:
                  type: string
                  enum:
                    - all
                    - automations
                  default: all
                  description: >-
                    Restricts which documents the facets are computed over.
                    `automations` counts only trigger-originated runs.
                dimensions:
                  type: array
                  description: >-
                    Dimensions to compute facets for. Defaults to every
                    dimension. Omitted dimensions come back as empty arrays. The
                    personal route omits user and group dimensions, and the
                    agent route omits the agent dimension.
                  items:
                    type: string
                    enum:
                      - agent
                      - user
                      - api_key
                      - group
                      - model
                      - tool
                      - skill
                      - source
                filter:
                  type: object
                  description: Map of consumption dimensions to selected values.
                  additionalProperties: false
                  properties:
                    agents:
                      type: array
                      items:
                        type: string
                    users:
                      type: array
                      items:
                        type: string
                    api_keys:
                      type: array
                      items:
                        type: string
                    groups:
                      type: array
                      items:
                        type: string
                    models:
                      type: array
                      items:
                        type: string
                    tools:
                      type: array
                      items:
                        type: string
                    skills:
                      type: array
                      items:
                        type: string
                    sources:
                      type: array
                      items:
                        type: string
      responses:
        '200':
          description: Consumption facets and their contextual availability
          content:
            application/json:
              schema:
                type: object
                required:
                  - period
                  - facets
                properties:
                  period:
                    type: object
                    required:
                      - startDate
                      - endDate
                    properties:
                      startDate:
                        type: string
                        format: date-time
                      endDate:
                        type: string
                        format: date-time
                  facets:
                    type: object
                    required:
                      - agent
                      - user
                      - api_key
                      - group
                      - model
                      - tool
                      - skill
                      - source
                    properties:
                      agent:
                        type: array
                        items:
                          $ref: '#/components/schemas/PrivateConsumptionFacet'
                      user:
                        type: array
                        items:
                          $ref: '#/components/schemas/PrivateConsumptionFacet'
                      api_key:
                        type: array
                        items:
                          $ref: '#/components/schemas/PrivateConsumptionFacet'
                      group:
                        type: array
                        items:
                          $ref: '#/components/schemas/PrivateConsumptionFacet'
                      model:
                        type: array
                        items:
                          $ref: '#/components/schemas/PrivateConsumptionFacet'
                      tool:
                        type: array
                        items:
                          $ref: '#/components/schemas/PrivateConsumptionFacet'
                      skill:
                        type: array
                        items:
                          $ref: '#/components/schemas/PrivateConsumptionFacet'
                      source:
                        type: array
                        items:
                          $ref: '#/components/schemas/PrivateConsumptionFacet'
        '400':
          description: Invalid request body
        '403':
          description: Not authorized for this analytics view
        '500':
          description: Failed to retrieve consumption facets
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateConsumptionFacet:
      type: object
      required:
        - value
        - label
        - pictureUrl
        - documentCount
        - disabled
      properties:
        value:
          type: string
          description: Raw indexed value accepted by the corresponding consumption filter.
        label:
          type: string
          description: >-
            Human-readable label, falling back to the raw value when its
            resource was deleted.
        pictureUrl:
          type: string
          nullable: true
        icon:
          type: string
          nullable: true
          description: Design-system icon name for tool and skill facets when known.
        documentCount:
          type: integer
          minimum: 0
          description: >-
            Number of matching indexed documents after applying the selected
            period and every other facet.
        disabled:
          type: boolean
          description: >-
            Whether selecting this value would produce no matching indexed
            document.
        scope:
          type: string
          enum:
            - global
            - visible
            - hidden
          description: >-
            Current agent scope, when the agent still has accessible
            configuration metadata.
        maker:
          type: string
          description: Model maker, for known model facets.
        tier:
          type: string
          enum:
            - cost_efficient
            - balanced
            - premium
          description: Default reasoning-effort tier, for known model facets.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````