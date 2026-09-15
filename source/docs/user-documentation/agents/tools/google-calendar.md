> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Calendar

## Overview

<Info>
  This tool uses personal credentials. It interacts with Google Calendar using
  the user accounts; it adapts to each user.
</Info>

## Admin: Setup in Dust

Go to Spaces > Tools in your Dust workspace, click `Add Tools`, and select Google Calendar.

You will then be redirected to an oAuth flow to connect an admin Google Calendar Account. This account only be used during the set up and users won't be able to query Google Calendar from this account.

By default this tool is added to the Company data Space, so accessible in all the workspace.

## Usage

Once the tool has been configured by the admin as described before, it can be selected on any agent: in the Agent Builder, simply click on `Add Tool` and select Google Calendar.

When users use an agent with the Google Calendar tool for the first time, they will get this error:

They will have to click on the `Connect` button to connect their own Google Calendar credentials. After it will look like this:

And they can click on the `Retry` button to replay the agent answer if not done automatically.
