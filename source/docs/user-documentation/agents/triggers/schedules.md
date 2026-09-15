> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Schedules

## Add triggers to your agents in the Agent Builder

We introduced a dedicated **Triggers** section in the **Agent Builder**. From there, you can create **schedules** for your agent to follow.

When setting up a **schedule**, you can specify a name, describe the frequency you'd like the agent to run at, and add an optional custom message that will be sent to the **agent**.
You can also specify a timezone you'd like the schedule to effect in. The timezone defaults to the user's location.

A **Large Language Model** is responsible to generate the actual schedule behind the hood. To make sure it generated the right thing, we added an entry that confirms the schedule the **agent** will effectively run at.
Here, it's confirming that the agent will run *at 8:00 AM, every week from monday to friday, in Los Angeles time*.

You just have to Save the **agent** for the **schedule** to be registered.

<Info>
  For now, triggers are personal, and only the editor can observe the runs.
  More to come on that topic !
</Info>
