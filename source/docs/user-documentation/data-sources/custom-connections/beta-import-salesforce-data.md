> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# [Beta] Import Salesforce Data

## Salesforce Accounts Data Importer for Dust

This script imports your Salesforce account summaries into a Dust datasource.

This open-source script, **available on GitHub at[dust-tt/dust-labs/salesforce](https://github.com/dust-tt/dust-labs/tree/main/salesforce)**, automates the process of exporting accounts updated in the last 24 hours from Salesforce and importing them into a Dust datasource. It fetches detailed account summaries, like so:

```
Account Summary for Grand Hotels & Resorts Ltd dd
Basic Account Details:
Company Name: Grand Hotels & Resorts Ltd dd
Industry: Hospitality
Annual Revenue: $500,000,000
Number of Employees: 5600
Phone: (312) 596-1000
Website: www.grandhotels.com
Locations:
Billing Address: 2334 N. Michigan Avenue, Suite 1500
Chicago, IL 60601, USA, Chicago, IL
Shipping Address: 2334 N. Michigan Avenue, Suite 1500
Chicago, IL 60601, USA
Key Contacts:
- John Bond, VP, Facilities
    Email: bond_john@grandhotels.com, Phone: (312) 596-1000
    Last Modified: 2022-10-17T08:54:06.000+0000
- Tim Barr, SVP, Administration and Finance
    Email: barr_tim@grandhotels.com, Phone: (312) 596-1000
    Last Modified: 2022-10-17T08:54:06.000+0000
Account Status:
Type: Customer - Direct
Rating: Warm
Account Source: N/A
Created Date: 2022-10-17T08:54:06.000+0000
Last Modified Date: 2023-11-30T08:45:06.000+0000
Last Activity Date: N/A
Sales Information:
Open Opportunities:
- Grand Hotels SLA
    Stage: Closed Won, Amount: $90,000, Close Date: 2022-07-06
    Last Modified: 2023-12-18T15:28:14.000+0000
- Grand Hotels Generator Installations
    Stage: Closed Won, Amount: $350,000, Close Date: 2022-09-25
    Last Modified: 2022-10-17T08:54:06.000+0000
- GRAND Hotels Guest Portable Generators TEAMS UPDATED
    Stage: Proposal/Price Quote, Amount: $2,500, Close Date: 2023-03-16
    Last Modified: 2024-02-29T22:31:41.000+0000
- Grand Hotels Emergency Generators
    Stage: Closed Won, Amount: $210,000, Close Date: 2022-09-23
    Last Modified: 2022-10-17T08:54:06.000+0000
- Grand Hotels Kitchen Generator
    Stage: Value Proposition, Amount: $1,200, Close Date: 2023-01-18
    Last Modified: 2024-08-20T07:14:36.000+0000
Account Health:
Recent Support Cases:
- Case Number: 00001013
    Subject: Starting up generator consumes excessive power, Status: Closed, Created Date: 2022-10-17T08:54:06.000+0000
    Last Modified: 2022-10-17T08:54:06.000+0000
- Case Number: 00001008
    Subject: Customer service for portable generators needs beefing up, Status: Closed, Created Date: 2022-10-17T08:54:06.000+0000
    Last Modified: 2022-10-17T08:54:06.000+0000
- Case Number: 00001014
    Subject: Delay in installation; spare parts unavailable, Status: Closed, Created Date: 2022-10-17T08:54:06.000+0000
    Last Modified: 2022-10-17T08:54:06.000+0000
- Case Number: 00001007
    Subject: Structural breakdown of rotor assembly, Status: Closed, Created Date: 2022-10-17T08:54:06.000+0000
    Last Modified: 2022-10-17T08:54:06.000+0000
Additional Information:
Chain of hotels and resorts across the US, UK, Eastern Europe, Japan, and SE Asia.
```

The script then formats and uploads this data to Dust.

Run the script daily to keep your Dust knowledge base up to date with the latest account information from Salesforce. Agents can then work from this data to analyze support trends, response times, and customer service quality. The script includes rate limiting and error handling, so it stays reliable with large volumes of account data.
