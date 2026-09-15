> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Why is Dust slow or my agent taking too long to respond?

If you're experiencing slow response times, here's how to diagnose:

## Check your connection

* Test your internet speed
* Try a different browser (Chrome/Arc recommended)
* Clear browser cache and cookies

## Agent configuration issues

**Too many data sources:**

* Agents with access to 10+ large data sources will be slower
* Solution: Limit to only essential data sources per agent

**Complex tool chains:**

* Agents using multiple tools (Search + Table Query + Browse) take longer
* Solution: Create specialized agents for different tasks

**Large documents:**

* Agents retrieving very large documents (>1MB) process slower
* Solution: Break large documents into smaller, focused pages

## System status

Check [https://dust.statuspage.io/](https://dust.statuspage.io/) for:

* Current incidents
* Scheduled maintenance
* Historical uptime

If issues persist and status page shows no problems, contact [support@dust.tt](mailto:support@dust.tt) with:

* Agent name or ID
* Example query that's slow
* Approximate response time
