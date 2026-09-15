> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a single action

> Retrieve a single action by its ID within an agent message, along with the message status.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/actions/{aId}
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
  /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/actions/{aId}:
    get:
      tags:
        - Private Messages
      summary: Get a single action
      description: >-
        Retrieve a single action by its ID within an agent message, along with
        the message status.
      parameters:
        - in: path
          name: wId
          required: true
          description: ID of the workspace
          schema:
            type: string
        - in: path
          name: cId
          required: true
          description: ID of the conversation
          schema:
            type: string
        - in: path
          name: mId
          required: true
          description: ID of the message
          schema:
            type: string
        - in: path
          name: aId
          required: true
          description: ID of the action
          schema:
            type: string
      responses:
        '200':
          description: Successfully retrieved the action
          content:
            application/json:
              schema:
                type: object
                properties:
                  action:
                    $ref: '#/components/schemas/PrivateAgentMCPAction'
                  messageStatus:
                    type: string
                    enum:
                      - created
                      - succeeded
                      - failed
                      - cancelled
                      - gracefully_stopped
        '400':
          description: >-
            Invalid request (missing parameters or message is not an agent
            message)
        '401':
          description: Unauthorized
        '404':
          description: Conversation, message, or action not found
      security:
        - BearerAuth: []
components:
  schemas:
    PrivateAgentMCPAction:
      type: object
      description: An MCP action with its output.
      required:
        - id
        - sId
        - createdAt
        - updatedAt
        - agentMessageId
        - toolName
        - functionCallName
        - functionCallId
        - params
        - citationsAllocated
        - status
        - step
        - generatedFiles
        - output
      properties:
        id:
          type: integer
          description: Numeric model identifier
        sId:
          type: string
          description: Unique string identifier
        createdAt:
          type: integer
          description: Unix timestamp of creation
        updatedAt:
          type: integer
          description: Unix timestamp of last update
        agentMessageId:
          type: integer
          description: ID of the parent agent message
        internalMCPServerName:
          type: string
          nullable: true
          description: Name of the internal MCP server, if any
        toolName:
          type: string
          description: Name of the tool
        mcpServerId:
          type: string
          nullable: true
          description: ID of the MCP server, if external
        functionCallName:
          type: string
          description: Name of the function call
        functionCallId:
          type: string
          description: ID of the function call
        params:
          type: object
          description: Parameters passed to the tool
        citationsAllocated:
          type: integer
          description: Number of citations allocated
        status:
          type: string
          enum:
            - succeeded
            - errored
            - denied
            - blocked_authentication_required
            - blocked_file_authorization_required
            - blocked_validation_required
            - blocked_child_action_input_required
            - blocked_user_answer_required
            - ready_allowed_explicitly
            - ready_allowed_implicitly
            - running
          description: Execution status of the tool
        step:
          type: integer
          description: Step number in the agent execution
        executionDurationMs:
          type: integer
          nullable: true
          description: Duration of execution in milliseconds
        displayLabels:
          type: object
          nullable: true
          properties:
            running:
              type: string
            done:
              type: string
        generatedFiles:
          type: array
          items:
            type: object
            properties:
              fileId:
                type: string
                nullable: true
                description: >-
                  Dust file id for DB-backed files, or null for path-backed
                  files.
              filePath:
                type: string
                description: Canonical scoped path for path-backed files.
              title:
                type: string
              contentType:
                type: string
              snippet:
                type: string
                nullable: true
              createdAt:
                type: integer
              updatedAt:
                type: integer
              isInProjectContext:
                type: boolean
              hidden:
                type: boolean
        output:
          type: array
          nullable: true
          description: Tool call result content
          items:
            type: object
        citations:
          type: object
          nullable: true
          description: Map of citation key to citation object
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````