# JavaScript SDK

Install the [JavaScript client](https://www.npmjs.com/package/@dust-tt/client):

```bash
npm install @dust-tt/client
```

Point the client at Counso and provide the workspace ID and an API key or OAuth access token:

```typescript
import { DustAPI } from "@dust-tt/client";

const client = new DustAPI(
  { baseUrl: "https://app.counso.ai", workspaceId, apiKey }
);
```

Keep credentials in your application’s secret store or a secure server-side configuration. Do not embed a workspace API key in public browser code. Use an OAuth access token when an operation must act as a signed-in user; client-side MCP routes specifically require the user’s OAuth identity.

The SDK follows a Result-based response pattern. Check `isErr()` before reading `value`, and handle API errors before continuing. The [Conversations API reference](../counso-api-documentation/openapi-and-postman.md) lists request fields and available operations.
