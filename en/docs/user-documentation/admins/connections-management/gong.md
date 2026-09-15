# Connect Gong

The Gong connection indexes call transcripts. It synchronizes transcripts across the connected Gong workspace, excluding calls marked **Private**. Review this workspace-wide scope before authorizing it.

## Connect the workspace

1. Use an account with Counso admin access and Gong's **Technical administrator** permission. In Gong, check **My Profile > Workspaces and permissions** to confirm the role.
2. Open **Spaces > Connections**, select Gong, and sign in.
3. Review the Gong consent screen and complete authorization.
4. After synchronization, make the data available in the relevant [Space](../spaces-management.md) so agents can use it.

The initial import starts when the connection is created; its duration depends on transcript volume. Later transcripts can take up to an hour to appear.

## Transcript content

Each indexed transcript includes the transcript text, available speaker email addresses, the original Gong call link, and call duration. Audio and video recordings are not the synchronized knowledge source.

Labels describe the title, date, language, media type, call scope, direction, participants, and any triggered trackers. Language codes use ISO-639-2B values such as `eng` or `fre`. Tracker labels use `tracker:{name}`.

Use these labels to filter the [knowledge search tool](../../agents/knowledge/search-data-sources.md), for example to focus on external calls in a particular language. Participant details are included only when Gong exposes them.
