> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Browser Extension (Chrome, Firefox & Chromium-based browsers)

<iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/yARlEaMEDJQ" title="Video" allowFullScreen />

Choose your browser and install the extension:

* **Chrome, Arc, Microsoft Edge, and other Chromium-based browsers:** [Install from the Chrome Web Store](https://chromewebstore.google.com/detail/dust/fnkfcndbgingjcbdhaofkcnhcjpljhdn)
* **Firefox:** [Install from Firefox Add-ons](https://addons.mozilla.org/firefox/addon/dust/)

**Optional: Set a shortcut to open the Dust side panel.**

* **Chrome and Chromium-based browsers:** Go to `chrome://extensions/shortcuts`, then set your shortcut by clicking the pen icon.
* **Firefox:** Go to `about:addons`, click the settings gear in the top-right corner, then click **Manage Extension Shortcuts**.

**Optional: Pin the extension to get immediate access to the icon.**

Broad permissions are required by browsers to enable core features like capturing tab content and screenshots.

No data is ever collected automatically. The extension only reads webpage content when you explicitly request it or when it asks for your permission before doing so.

Source code available for review: [background.ts](https://github.com/dust-tt/dust/blob/main/extension/platforms/chrome/background.ts)

## Dust, right in your browser

Just like in the web app, you can start a conversation with any of your Dust agents directly from the extension: ask questions, get summaries, draft content, and more, without leaving your current tab.

Find the features you're used to in the web app, such as:

### Input & Composition

The extension's composer is now fully on par with the web app: everything you can do on dust.tt, you can do directly from your browser.

* **@Mentions**: Mention members of your workspace directly in a conversation.
* **Rich text formatting**: Bold, italic, lists, and emoji support.
* **Attach to conversations**: Add agents, tools, skills, or knowledge sources to any conversation.
* **Draft auto-save**: Your unsent message is preserved when you close the extension and restored when you reopen it.

### Sidebar

The sidebar mirrors the web app navigation. Click the sidebar icon to access:

* Your **conversation history**, sorted by most recent activity.
* Your **inbox**, with unread indicators so you never miss a reply.

### MCP Tools

The extension now shares the same tool architecture as the web app. Any MCP tool your workspace has configured (Notion, Gmail, Google Drive, etc.) is automatically available to agents in the extension, with no extra setup needed.

***

## Browser-Aware Agents

The extension gives agents direct awareness of what's happening in your browser. Agents can access browser content **only with your explicit permission**.

### Workspace admin control

Workspace admins can disable browser tab access for the entire workspace with the **Browser Extension Tools** setting in the workspace governance settings. When disabled, the extension does not register its browser tools, so agents cannot list or read browser tabs or use multi-tab support.

### Page content & screenshots

You can manually attach the current tab's text or a full-page screenshot using the icons in the composer. You can also use keyboard shortcuts:

* `⌘ + Shift + Y` (Mac) / `Ctrl + Shift + Y` (Windows): attach page content
* `⌘ + Shift + S` (Mac) / `Ctrl + Shift + S` (Windows): attach screenshot

**Agents can also request access to the page content on their own** when it is relevant to your question. A permission prompt will appear before any content is accessed.

### Multi-tab support

Agents can work across multiple open tabs at once. When you ask a question that spans several pages, the agent will identify which tabs it needs and request permission to access their content.

### PDF & file auto-attachment

If you are on a page displaying a file (e.g. a PDF or an image), the agent will detect it and offer to attach the file to the conversation automatically, with no manual download or upload needed.

### Page interaction

Agents can interact with the current page using mouse clicks and keystrokes. This enables use cases like filling out forms, clicking buttons, or navigating a board, all without leaving the page.

**Note:** Page interaction is intentionally disabled on pages where a dedicated MCP tool is available (e.g. Notion, Gmail). In those cases, the agent will use the MCP tool instead, which is faster and more reliable.

***

The Dust extension is available on **Chrome**, **Firefox**, **Arc**, **Microsoft Edge**, and other Chromium-based browsers.

## Known Limitations

* **Include page content is not working well on Google Drive, Gdoc included** (since it’s not really text on the page but a canvas). The workaround is to use the “include tab screenshot” feature or to download the Gdoc as a PDF.

## Use case examples

* **Sales teams** are speeding up their follow-ups, pulling insights directly from meeting transcripts, Slack channels and CRM data while working in their email client.
* **Support teams** are becoming more data-fluent, getting instant assistance in interpreting dashboards and metrics.
* **Engineering teams** are accelerating code reviews with on-point comments co-written with their Dust coding agents.

## Troubleshooting

### Can't open past conversations

If you can't open past conversations in the extension, update the Dust extension:

1. Open `chrome://extensions` in your browser.
2. Click **Update**.
3. Create a new conversation, then try opening a past conversation again.
