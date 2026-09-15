> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an agent message credit attribution

> Returns direct and total billed credits. Run-agent tool rows combine invocation cost with the bill of their sub-agent subtree.



## OpenAPI

````yaml https://raw.githubusercontent.com/dust-tt/dust/refs/heads/main/front-api/public/swagger.json get /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/consumption
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
  /api/w/{wId}/assistant/conversations/{cId}/messages/{mId}/consumption:
    get:
      tags:
        - Private Messages
      summary: Get an agent message credit attribution
      description: >-
        Returns direct and total billed credits. Run-agent tool rows combine
        invocation cost with the bill of their sub-agent subtree.
      parameters:
        - name: wId
          in: path
          required: true
          schema:
            type: string
        - in: path
          name: cId
          required: true
          schema:
            type: string
        - in: path
          name: mId
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Credit attribution for the agent message
          content:
            application/json:
              schema:
                type: object
                required:
                  - billedCredits
                  - details
                properties:
                  billedCredits:
                    type: number
                    nullable: true
                    description: >-
                      Authoritative credits billed directly for this agent
                      message, excluding sub-agents.
                  totalBilledCredits:
                    type: number
                    description: >-
                      Total credits billed by this message and its recursively
                      spawned sub-agents.
                  details:
                    type: object
                    nullable: true
                    description: >-
                      Additive attribution reconciled to totalBilledCredits
                      through model input rows. Each run-agent tool row includes
                      its sub-agent subtree's bill. Null when no stored version
                      is complete.
                    required:
                      - attributionVersion
                      - agentWorkCredits
                      - tools
                    properties:
                      attributionVersion:
                        type: integer
                        description: Attribution version used for this breakdown.
                      agentWorkCredits:
                        type: number
                        description: >-
                          Non-tool work for the originating message after
                          assigning billing reconciliation exclusively to model
                          input rows.
                      tools:
                        type: array
                        items:
                          type: object
                          required:
                            - label
                            - internalMCPServerName
                            - toolName
                            - callCount
                            - attributedCredits
                            - directCredits
                            - pending
                          properties:
                            label:
                              type: string
                            internalMCPServerName:
                              type: string
                              nullable: true
                            toolName:
                              type: string
                            callCount:
                              type: integer
                            attributedCredits:
                              type: number
                              description: >-
                                Share of total billed credits after input-only
                                reconciliation. Run-agent tools include their
                                sub-agent subtree's bill.
                            directCredits:
                              type: number
                            pending:
                              type: boolean
        '403':
          description: The workspace does not have access to consumption details
        '404':
          description: Conversation or agent message not found
      security:
        - BearerAuth: []
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Your DUST API key is a Bearer token.

````