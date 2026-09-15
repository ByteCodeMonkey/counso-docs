> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# [Beta] Import Hubspot Data

## Hubspot Data Importer for Dust

This script imports company summaries from Hubspot into a Dust datasource.

This open-source script, **available on GitHub at[dust-tt/dust-labs/hubspot](https://github.com/dust-tt/dust-labs/tree/main/hubspot)**, automates the process of exporting accounts updated in the last 24 hours from Hubspot and importing them into a Dust datasource. It fetches detailed account summaries, like so:

```
Company Summary for Evil Corp

Basic Company Details:
Company Name: Evil Corp

Key Contacts:
- Email: dr.evil@evilcorp.com
- Dr Maboul, Title: Head of AI, Email: dr.maboul@evilcorp.com
- Dr Zeuss, Email: dr.zeuss@evilcorp.com, Phone: +33 7 66 66 66 66

Deals:
- Evil Corp, Stage: decisionmakerboughtin, Amount: 42000, Close Date: 2024-07-31T10:21:55.017Z

Notes:
- 2024-09-04: Adding some notes to be more Evil.
```

The script then formats and uploads this data to Dust.

Because the script picks up accounts updated in the last 24 hours, running it daily keeps your Dust knowledge base current with Hubspot. Agents can then draw on this data to analyze support trends, response times, and customer service quality. Rate limiting and error handling keep the script reliable with large volumes of CRM data.
