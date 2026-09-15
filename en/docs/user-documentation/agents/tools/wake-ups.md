# Wake-ups

A wake-up schedules an Agent to continue work at a later time. It can run a one-time check, repeat on a schedule, or follow up after someone is expected to respond. An Agent can create a wake-up when asked; administrators do not need to add a separate provider connection.

For example, ask an Agent to check a named public status page each weekday and alert you only if a component changes, or to return to a conversation on a specified date to check for a reply. State the reason, time zone, source, recurrence, and what the Agent should do when it resumes. The pending wake-up is visible above the composer and on its conversation.

## Available operations

- `schedule_wakeup` creates a future run with a reason and schedule. This is a high-confirmation action.
- `list_wakeups` shows a wake-up's status, schedule, and reason.
- `cancel_wakeup` cancels a pending wake-up.

A future run uses the identity of the user whose request created it. While it is pending, other users cannot post into that conversation, preventing them from steering a run that will use the original user's credentials. A conversation can have one active wake-up at a time; after it triggers, another can be scheduled. Repeating schedules have a finite execution limit, shown by the current interface. Scheduled runs use the wake-up user's normal Agent quota. Review the schedule and cancel it when it is no longer needed.
