# Work with meeting transcripts

Use Counso to summarize a meeting, collect decisions, or turn a discussion into a draft action list. Start from the actual transcript and ask the Agent to distinguish what was agreed from what is still open.

## Bring the transcript into the conversation

Attach a transcript file, select material from a connected knowledge source, or use a meeting tool that your administrator has added to the workspace. For example, a connected Google Drive source can provide a Meet transcript, while a meeting service can provide its own recordings or notes. The Agent needs access to the chosen material.

Ask for a focused result: “Summarize the decisions, list each action with its owner, and flag any deadline that was not agreed.” Review names, dates, and commitments against the transcript before sharing the result.

## Set up automatic Google Meet processing

For automatic processing, the deployment administrator first enables Meeting Transcripts and its background processing service. A workspace administrator then configures the transcript source and the Agent that should handle new meetings.

1. Enable transcription for the Google Meet meeting.
2. Connect the organizer's Google Drive account. Google normally saves the transcript in that account, often in **Meet Recordings**.
3. Select the Agent in the Meeting Transcripts settings.
4. After a meeting, check that the file exists and that the expected conversation was created.

Transcript detection can depend on the generated filename. When troubleshooting, check the transcription settings, organizer account, Drive connection, selected Agent, and processing status. Ask the administrator to check the background service if files are present but no processing begins.

Automatic capture and a manually attached transcript are separate ways to supply the source. Neither makes a meeting summary an approved decision or sends it to other participants without a separate sharing action.
