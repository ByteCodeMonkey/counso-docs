> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Initiate WorkOS login

> Redirects to WorkOS AuthKit for authentication. Supports PKCE flow for extensions.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/workos/login
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
  /api/workos/login:
    get:
      tags:
        - Private Authentication
      summary: Initiate WorkOS login
      description: >-
        Redirects to WorkOS AuthKit for authentication. Supports PKCE flow for
        extensions.
      parameters:
        - in: query
          name: redirect_uri
          required: false
          description: Custom redirect URI (used by extensions for PKCE flow)
          schema:
            type: string
        - in: query
          name: code_challenge
          required: false
          description: PKCE code challenge
          schema:
            type: string
        - in: query
          name: code_challenge_method
          required: false
          description: PKCE code challenge method (S256)
          schema:
            type: string
      responses:
        '200':
          description: Login page HTML
        '302':
          description: Redirect to WorkOS authorization URL
        '400':
          description: Bad request
      security: []

````