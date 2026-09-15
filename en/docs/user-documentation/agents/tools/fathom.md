# Fathom

The Fathom tool provides read-only access to meetings and transcripts. It can list meetings using time, team, recorder, or invitee-domain filters; include available summaries, action items, or CRM matches; and retrieve a transcript by recording ID.

An administrator adds Fathom from **Spaces → Tools → Add Tools**, completes OAuth, and chooses personal or shared credentials if offered. Share it with the relevant Space and add it to the Agent. Personal credentials make the user's provider access the boundary; shared credentials use the connected account's access for everyone allowed to invoke the tool.

For an initial check, list meetings for a bounded date range and confirm the recording ID and participants. Then retrieve one transcript using `recording_id`. A transcript may not be ready immediately after a meeting. Large transcripts can be returned as files; open or read them in chunks. Meeting, transcript, summary, and CRM visibility can differ, so check the recording identity before sharing findings.

## Tool parameters

`list_meetings` supports pagination with `cursor`; an ISO 8601 `start_date` and `end_date`; a numeric `recording_id`; exact-match `calendar_invitees_domains` and the `calendar_invitees_domains_type` filter (`all`, `only_internal`, or `one_or_more_external`); recorder email addresses in `recorded_by`; team names in `teams`; and flags for `include_action_items`, `include_crm_matches`, and `include_summary`. CRM matches are limited to the connected CRM. `get_transcript` requires the numeric `recording_id`. Long transcripts may be saved as conversation files and should be read progressively.
