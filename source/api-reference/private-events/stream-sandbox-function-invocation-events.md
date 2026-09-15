> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Stream sandbox function invocation events

> Stream real-time events for a Pod function invocation using Server-Sent Events (SSE). This endpoint is redirected to /api/sse/ for SSE traffic routing.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/sandbox-functions/{functionId}/invocations/{invocationId}/events
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
  /api/w/{wId}/sandbox-functions/{functionId}/invocations/{invocationId}/events:
    get:
      tags:
        - Private Events
      summary: Stream sandbox function invocation events
      description: >-
        Stream real-time events for a Pod function invocation using Server-Sent
        Events (SSE). This endpoint is redirected to /api/sse/ for SSE traffic
        routing.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: path
          name: functionId
          required: true
          description: ID of the Pod function
          schema:
            type: string
        - in: path
          name: invocationId
          required: true
          description: ID of the sandbox function invocation
          schema:
            type: string
      responses:
        '200':
          description: |
            SSE event stream. Each event is sent as `data: {json}\n\n`.
            Events are discriminated by the `type` field.
          content:
            text/event-stream:
              schema:
                $ref: '#/components/schemas/PrivateSandboxFunctionInvocationEvent'
        '401':
          description: Unauthorized
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateSandboxFunctionInvocationEvent:
      type: object
      description: >-
        Server-Sent Event for sandbox function invocation streaming.
        Discriminated on the `type` field.
      discriminator:
        propertyName: type
      oneOf:
        - $ref: '#/components/schemas/PrivateSandboxFunctionInvocationCreatedEvent'
        - $ref: '#/components/schemas/PrivateSandboxFunctionInvocationResultEvent'
        - $ref: '#/components/schemas/PrivateSandboxFunctionInvocationErrorEvent'
    PrivateSandboxFunctionInvocationCreatedEvent:
      type: object
      required:
        - type
        - created
        - invocation
      properties:
        type:
          type: string
          enum:
            - sandbox_function_invocation_created
        created:
          type: integer
        invocation:
          type: object
          required:
            - sId
            - functionId
            - status
            - createdAt
          properties:
            sId:
              type: string
            functionId:
              type: string
            status:
              type: string
              enum:
                - created
            createdAt:
              type: string
              format: date-time
    PrivateSandboxFunctionInvocationResultEvent:
      type: object
      required:
        - type
        - created
        - invocationId
        - functionId
        - result
      properties:
        type:
          type: string
          enum:
            - sandbox_function_invocation_result
        created:
          type: integer
        invocationId:
          type: string
        functionId:
          type: string
        result:
          description: Parsed result validated against the sandbox function output schema.
    PrivateSandboxFunctionInvocationErrorEvent:
      type: object
      required:
        - type
        - created
        - invocationId
        - functionId
        - error
      properties:
        type:
          type: string
          enum:
            - sandbox_function_invocation_error
        created:
          type: integer
        invocationId:
          type: string
        functionId:
          type: string
        error:
          type: object
          required:
            - code
            - message
          properties:
            code:
              type: string
              description: >-
                Whatever classified the failure, forwarded as-is (a runner code
                such as `threw` or `http_error`, or the `type` of the API error
                that failed the call). Open by design, branch on the codes you
                handle and treat the rest as generic failures.
            message:
              type: string
            status:
              type: integer
          description: A structured error describing why the invocation failed.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````