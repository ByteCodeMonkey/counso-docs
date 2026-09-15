---
title: "Create and use Frames"
---
A Frame is an interactive file saved in a Pod. It can show a dashboard, report, status view, or another interface created by an Agent.

## View and pin a Frame

Open a Frame from the Pod's **Files** tab to preview it. Editors can pin it so it appears at the top of **Conversations** for every Pod member.

The banner is **280px tall** and spans the full width of the Conversations tab. Only one Frame can be pinned at a time; pinning another replaces the current one. To pin, use the Frame's **...** menu in Files and choose **Pin as Pod banner**, or use **Pin** in the preview header. To unpin, use **Unpin Pod banner** in the Files menu, toggle **Pinned** off in the preview, or hover over the banner and select the unpin control. Only Editors see the pin controls.

The banner controls also let you hide it for yourself, show it again, or open it full screen. Hiding is personal; unpinning changes the shared Pod banner.

## Keep a Frame up to date

A Frame is generated from the Pod data available at that point in time. It does not update by itself. For a changing view, configure an Agent to use the wake-up tool on a recurring schedule, read the latest Pod tasks, conversations, or files, and regenerate the Frame by overwriting the same file. The pinned banner stays attached to that file and shows its updated version the next time a member opens the Pod; you do not need to pin it again.

For example, ask an Agent to create and save a weekly status Frame, pin it, then ask it in a new conversation to use the wake-up tool every Monday to read the latest tasks and summary and overwrite that Frame.

Design banner Frames for the fixed 280px height: show a few shared, glanceable facts and avoid content that needs vertical scrolling. Check the pinned banner itself after creating or updating it, since its rendering space differs from the preview.

## Use the underlying record as the source

A Frame displays information from Pod content. When a value matters, check the underlying task, file, or connected system; a displayed value does not itself update that source.
