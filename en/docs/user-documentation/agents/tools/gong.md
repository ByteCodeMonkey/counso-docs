# Gong

The Gong tool provides live access to call metadata and transcripts. It can list calls within a date range, retrieve details by `callId`, and return a transcript organized by speaker. This is distinct from a synchronized Gong Connection used for search.

An administrator adds Gong from **Spaces → Tools → Add Tools** and completes OAuth, then shares it with the intended Space. Before enabling it broadly, note that the provider tool may return calls across the Gong workspace rather than only the connected user's own calls. Limit use through Space membership and make sure the people in that Space are allowed to see those calls.

Start with a bounded `list_calls` request using `fromDateTime` and `toDateTime`; use the returned `callId` with `get_call` or `get_call_transcript`. Results are paginated, so follow the returned cursor when needed. A transcript may not be available until processing finishes. If only synchronized search is needed, configure a Connection instead of a live Tool.
