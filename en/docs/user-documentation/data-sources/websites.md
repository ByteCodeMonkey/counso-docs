# Website sources

A website source makes public pages available for search. Add it from the target Space's **Connections** area and enter a public starting URL. The crawler follows links it finds on that page; it does not guess or discover pages that are not linked.

Choose the crawl boundary to fit the site:

- **Follow all links within the domain** to traverse the linked site.
- **Only child pages of the provided URL** to stay within a section, such as `/articles`.
- Set **Page limit** to `1` to index only the starting page.
- Set **Depth of search** to limit how many links away from the start the crawler may go.

PDFs reachable under the crawled URL can be included. A Google Docs file is included when its URL is entered directly; links to another domain are generally outside the crawl. Pages behind a sign-in cannot be read. Some sites block automated access. The current interface enforces its own maximum page limit; choose a smaller limit for a focused source.

After the first crawl, search for a known page and inspect its URL. If it is absent, check that the page is public, linked from the starting page, within the chosen path/depth and page limit, and not blocked by the site.
