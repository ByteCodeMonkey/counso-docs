> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Parse mentions in markdown text

> Parses pasted text containing @ mentions and converts them to the proper mention format.
Matches @agentName or @userName patterns against available agents and users.




## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json post /api/v1/w/{wId}/assistant/mentions/parse
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
  /api/v1/w/{wId}/assistant/mentions/parse:
    post:
      tags:
        - Mentions
      summary: Parse mentions in markdown text
      description: >
        Parses pasted text containing @ mentions and converts them to the proper
        mention format.

        Matches @agentName or @userName patterns against available agents and
        users.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - markdown
              properties:
                markdown:
                  type: string
                  description: Markdown text containing @ mentions to parse
                  example: Hello @JohnDoe, can you help with @MyAgent?
      responses:
        '200':
          description: Parsed markdown with mentions converted to proper format
          content:
            application/json:
              schema:
                type: object
                properties:
                  markdown:
                    type: string
                    description: >-
                      Processed markdown text with mentions converted to
                      serialized format
        '400':
          description: Bad Request. Missing or invalid request body.
        '401':
          description: Unauthorized. Invalid or missing authentication token.
        '500':
          description: Internal Server Error.
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````