> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Gong

At the moment, Dust is only syncing **[Gong Transcripts](https://help.gong.io/docs/see-a-call-transcript)**.

<Danger>
  **Scope and privacy**

  Dust syncs all transcripts in your Gong workspace. Transcripts marked as Private in Gong are excluded from sync.
</Danger>

Setting up the Gong connection involves the following steps that must be completed by an individual with **admin rights on both Dust and Gong** (Technical Administrator).

1. On dust.tt, navigate to **Spaces** > **Connections** and select Gong in the list.

2. Authenticate on Gong, you will then be redirected to a Gong consent screen in order to give Dust access your Gong workspace.

3. That's it! By default, Dust will sync all transcripts in your Gong workspace. Transcripts marked as Private in Gong are not synced. The connection will appear under **Spaces > Connections**. Don't forget that to be able to use this data you need to add it to a [Space](/docs/developer-platform/dust-api-documentation/list-available-spaces).

<Info>
  **How to check if you are an admin on Gong**

  1. Click on your profile picture/icon in the top right corner of your Gong interface.
  2. Select "My Profile".
  3. Navigate to "Workspaces and permissions" (navigation bar on the left).
  4. Check that the "**Technical administrator**" checkbox is ticked.
</Info>

### Data synced in an individual Transcript

We synchronize the following in a transcript:

* The text of the transcript and the email addresses of the speakers.
* The URL to the page in the Gong web application where the call is available.
* The duration of the call.
* The **labels** listed in the "Labels" section.

### How fresh is the Data in Dust?

Upon creating the connection we **immediately** launch an action to sync the data. This operation can take a various amount of time to complete, depending on the amount of transcripts to process.

When a new transcript is added to Gong, **it takes up to 1 hour** to be synced with Dust.

When syncing transcripts, Dust attaches the following **labels** to the synced document and include them in it, making the LLMs aware of them:

* The title of the transcript.
* Date of the transcript.
* The language spoken (in ISO-639-2B format: `eng`, `fre`, `spa`, `ger`, `ita`, ...).
* The media used (audio or video).
* The scope of the call (Internal, External).
* The direction of the call (Inbound, Outbound, Conference).
* The participant's emails if exposed by Gong.
* (Optional) The names of the trackers triggered during a call in the format `tracker:{name}`.

**Labels**  allow for additional filtering on data sources selected on the [semantic search](/docs/user-documentation/agents/knowledge/search-data-sources) tool.
