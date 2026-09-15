# API rate limits

Counso limits API request volume over rolling time windows. A rolling window means that capacity becomes available as earlier requests leave the window, rather than resetting for every client at the same clock time. Different operations may have limits at different scopes, such as a workspace or an application. For example, document-upsert limits can be measured per workspace, while application-run quotas can be measured per app.

The published reference limits are 120 document upserts per minute per workspace for data sources, and 10,000 app requests per day per app. Treat these as configured defaults: workspace or deployment settings may define a different limit. Check the current Counso environment before setting a throughput target. A request that exceeds a limit may receive an HTTP `429` response.

When a request is throttled, reduce concurrency and queue remaining work instead of retrying immediately in a tight loop. Follow any retry guidance returned with the response, and monitor both successful requests and throttling errors. For document imports, stable document IDs make it easier to safely retry an upsert after checking the result. See the [API reference](../counso-api-documentation/openapi-and-postman.md) for limits published for your Counso environment.
