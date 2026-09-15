> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# What data do the agents have access to?

Dust only has access to data admins decided to synchronize with Dust.

The agents can use:

* Notion pages chosen by the admin.
* Content from Slack channels chosen by the admin. Dust agents can't access attachments or links in these channels unless they link to indexed documents. They can’t access “forwarded to channel” and “also sent in channel” messages either. Messages from other bots (eg: Slack workflows) are also not accessible.
* Google Drive folders chosen by the admin. Dust supports GDocs, GSlides, and .txt files with less than 750KB of extracted text. PDF can be indexed if the user toggles it on in the Google Drive connector in Dust. Agents read document titles, but not folder titles. They don’t read images.
* All GitHub discussions & issues. Dust syncs with a repository's Issues, Pull Requests, and Discussions, but not the repository’s code.
* Confluence data selected by the admin.
* Intercom Help Center and Conversations selected by the admin.

Dust doesn’t support pictures and comments within your Google documents or Notion pages.
