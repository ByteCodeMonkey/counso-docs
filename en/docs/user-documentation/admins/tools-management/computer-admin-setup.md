# Computer administration

Workspace administrators control Computer's outbound network access and environment values. Network access is restricted until a domain is allowed. Settings apply across new Computer sessions in the workspace, so keep the approved domain list and values limited to what users need.

## Network access

In the **Computer** administration area, add exact hostnames under **Allowed domains**. Wildcard entries such as `*.example.com` allow matching subdomains but do not include the apex domain `example.com`; add both if required. Invalid or duplicate domains are rejected. Removing a domain prevents new requests to it after the configuration propagates.

The **Agent-requested domains** setting controls whether an Agent can ask a user to allow another domain for the current Computer session. Enable it only if users may approve one-off access; otherwise leave domain approval with administrators.

## Environment values and secrets

Use **Config** variables only for non-sensitive values, such as a public endpoint, region, or feature name. Their names use the `DST_` prefix and values are readable by code running in Computer, so do not put credentials there.

Use **HTTPS secret** for API keys and tokens. Give each secret at least one allowed domain and use the `DSEC_` prefix. Inside Computer the value is represented without exposing the raw secret; it is sent only on approved HTTPS requests to configured domains. Saved secrets are write-only; replace or delete them to rotate access.

Changes to environment values apply to newly started Computers. Existing sessions retain their startup values, so start a new session after changing configuration. If a request returns 401 or 403, check provider credentials and permissions; a blocked-domain error instead points to the allowlist.
