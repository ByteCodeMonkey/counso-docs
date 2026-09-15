# Workspace analytics

Open **Admin > Analytics** to understand how your workspace uses credits. Start with the overall pace, inspect unusual days, and then look at the agents or members behind the change.

## Set the reporting period

Choose **This cycle**, **Last 7 days**, **Last 30 days**, or **Last 90 days**. The selection applies to the summary, chart, attribution, comparisons, and data export. The page shows the period boundaries, active members, and the last data refresh. A member is active after consuming credits during that period. Recent activity may not yet be included; daily boundaries use UTC.

## Read the overview

For **This cycle**, the pace indicator compares the share of the credit cap consumed with the share of the cycle elapsed. **On target** suggests the remaining allowance can cover the cycle at the present pace. **Off target** calls for a closer look; **Critical** indicates that credits are likely to run out before the cycle ends. Use **Manage in Usage** to review [credit controls](docs/user-documentation/admins/usage-seats-and-credits/credit-management.md).

**Used this period** shows consumption, while **Top agent** identifies the largest contributor and its share. Rolling periods do not show cap status or cap values. Filters in **Explore** affect the chart, attribution, and exports, but do not change the overview cards or pace indicator.

## Compare daily and cumulative usage

**Daily** shows a stacked bar for each day. The selected attribution dimension determines the breakdown: for example, **Models** splits daily credits by model. The five leading contributors appear separately; **Others** combines the rest. Hover over a bar for individual and total values. The faded **Today (partial)** bar is still growing, so compare completed days when investigating a trend.

**Cumulative** shows how usage builds over the period. In an unfiltered **This cycle** view, a target line distributes the cap evenly across the cycle. This line is absent for rolling periods and when Explore filters are active.

## Narrow the analysis

Use **Filters** to select agents, members, groups, models, tools, skills, or request sources, then select **Apply**. Multiple selections in one category use an OR condition; different categories combine with AND. For example, two selected agents and one selected model show either agent's usage of that model.

Applied filters remain when you switch periods or attribution tabs. Remove them individually or clear the set; leaving or reloading the page resets them.

## Find the main contributors

Attribution can group usage by agent, member, group, model, tool, skill, or source. A member's usage follows the person who triggered it. The same usage can appear in several groups when that person belongs to more than one group; do not add group totals as if they were mutually exclusive.

Search within the selected tab or sort the table. Its measures are:

| Measure | How to read it |
| --- | --- |
| Consumption share | A contributor's credits as a share of all credits in the selected scope, not just the visible rows. |
| Total credits | Credits attributed to that contributor. |
| Credits / message | Average credits per originating user message, including the model and tool work it starts. |
| Credits / invocation | Average credits per tool or skill invocation. |
| Vs Prev | Change against the previous cycle or the immediately preceding rolling period. `--` means there is insufficient comparison data. |

Expand a row to see leading models, tools, or members. **View all** applies that contributor as a filter and opens the relevant attribution tab. The row's funnel icon also adds or removes it from the filters.

Admin and manager analytics include unpublished agents. For an unpublished agent you cannot edit, the creator's email can appear instead of its description; the analytics view does not grant access to the agent configuration.

## Export the selected data

Select **Download raw data** above Attribution. If a matching export is unavailable, the panel starts one; **New export** requests a fresh file. The CSV covers the selected period and Explore filters. The current attribution tab, text search, and sort order do not limit it.

Records include usage amounts and metadata such as time, conversation and message identifiers, agent, member, model, tool, skill, status, and execution time. They do not include message content. Generated exports are retained for up to 15 days, so download a file you need to keep.
