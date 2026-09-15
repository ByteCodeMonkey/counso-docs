> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# I try to create an agent using the Table Query tool, but it doesn't work

The Table Query tool can't automatically create a relation between tables. You need to explicitly set the relationships in your instructions. Clearly explain the structure of your data to the agent. Describe how tables are related and where to find specific information.

Table Format:

**If you are using a CSV or a GSheet:** Verify that the first line of your CSV or Google Spreadsheet is a header row made of columns and isn't made of raw text (i.e., guidance for reading the document) or isn't empty.

The Dust CSV parsing logic focuses on identifying the header row and the subsequent data rows. It doesn't have built-in functionality to recognize and handle introductory text or guidance information that precedes the actual CSV structure.

**You are using a Notion Database:** Table view in Notion doesn't mean Dust has access to all the databases your view is using. Ensure all related Notion databases are within Dust's indexed data scope. To identify related databases, look at the "Relations & rollups" properties in your Notion Database, like in the `Item Purchased` column in the picture below.
