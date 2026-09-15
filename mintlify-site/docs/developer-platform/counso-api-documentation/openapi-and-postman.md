---
title: "API specifications and Postman"
---
Use the Counso API definitions to inspect request and response schemas, or import the collection into Postman to work with individual requests.

- [Postman collection](/docs/developer-platform/counso-api-documentation/postman.collection.json)
- [Postman environment](/docs/developer-platform/counso-api-documentation/postman.environment.json)
- [OpenAPI 3.0 specification](/docs/developer-platform/counso-api-documentation/openapi.json)
- [OpenAPI specification in swagger.json](/docs/developer-platform/counso-api-documentation/swagger.json)

## Use the collection

1. Open [Postman](https://web.postman.co), select **Import**, and import the collection and environment files.
2. Select the **Counso** environment. Its `baseUrl` is `https://app.counso.ai`; change it only when connecting to another Counso deployment. Enter the target `workspaceId`.
3. Add your credential as a local secret value: `apiKey` for workspace API requests, or `userAccessToken` for requests that act as a signed-in user. The shared environment contains no credentials.
4. Choose a request, fill in its path parameters and body, then send it. Start with a read request, such as listing Agents, to check the workspace and connection.

The collection groups requests by authentication:

| Request group | Credential |
| --- | --- |
| Workspace API | A workspace API key; operations also apply their documented role and scope checks. Where supported, a user OAuth token can be used instead. |
| User session API | A user OAuth access token. A same-origin browser may use its signed-in session cookie. |
| Client-side MCP | A user OAuth access token; workspace API keys are not accepted. |
| Sign-in flow | The authorization code, refresh token, PKCE parameters or session ID required by that step; no existing Bearer token is required. |
| Webhook receiver | The full URL generated for the source, including its URL secret, plus the configured signature when required. |

Postman also accepts a URL during import. To use that option, copy the raw download URL of the collection or environment file above. Before sending a request, check its workspace, credentials and body; write operations change the selected workspace.
