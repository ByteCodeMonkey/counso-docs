> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Websites

Dust is able to crawl the content of a public website to make its content accessible from your data sources, meaning you can build agents based on this content.

With an admin or builder role, you can set up new website connections on **Spaces** > **Connections**.

To fetch the pages of a website, Dust uses the links present inside the page provided in the URL field. It does not guess any pages but instead it “navigates” from reading the content inside the page provided and the pages linked (that are on the same domain).

And let’s say we have a website formed as is:

`http://myfakewebsite.com`

1. `http://myfakewebsite.com/articles`
   1. `http://myfakewebsite.com/articles/article1`
   2. `http://myfakewebsite.com/articles/article2`
2. `http://myfakewebsite.com/jobs`
   1. `http://myfakewebsite.com/jobs/engineering`
   2. `http://myfakewebsite.com/jobs/design`
3. `http://myfakewebsite.com/product`
4. `http://myfakewebsite.com/about`

**Crawling strategy: All links vs children pages**

If you’d like the whole website crawled, set the URL `http://myfakewebsite.com`  with “Follow all links within the domain”.

If you’d like only the articles crawled, better set the URL [`http://myfakewebsite.com/articles`](http://myfakewebsite.com/articles)  with setting “Only child pages of the provided URL” to ensure the crawler fetches only the pages that contain `http://myfakewebsite.com/articles` in their URL.

**Indexing a single page**

If you want only the Engineering page indexed and no other page, you can set the url [`http://myfakewebsite.com/jobs/engineering`](http://myfakewebsite.com/jobs/engineering) combined with the setting “Page Limit” to 1.

**Advanced setting: “Depth of Search”**

This setting that allows you to say “How many links do I allow the crawler to follow to find a given page?”.

**PDF**

If your PDFs are stored under the URL you are crawling, they will be included.

**Google Docs**

If you enter a Google Docs URL, it will be included. Note that if they're linked from a website, there's a good chance they are on a different domain, so they won't be included.

**URL must be Public**

If a login is required to access the website, Dust will not be able to access its content.

**Blocked websites**

Some websites are blocking crawling, here is a non exhaustive list:

* reddit.com
* linkedin.com
* instagram.com
* x.com
* tiktok.com

**Page Limit**

Each new website connection can be set for a maximum limit of 1024 pages.
