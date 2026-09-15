> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Credit management

Credits are the unit of AI work on Dust. See [Credits](/docs/user-documentation/admins/usage-seats-and-credits/credits) for how they're calculated and what each seat type includes.

When using Dust, members can draw credits from different sources depending on their plan and seat type. This page explains how those sources work, in what order they are consumed, how admins can set limits, and how to monitor your workspace's usage.

When a user or automated workflow consumes credits, they are drawn in this order:

1. **Individual credits**: from the user's seat credit pool (see [Credits](/docs/user-documentation/admins/usage-seats-and-credits/credits))
2. **Workspace credit pool**: a shared pool managed by your admin
3. **Overage / Pay As You Go**: Enterprise plans only

A user is only blocked when all available sources are exhausted or when a personal spend limit is reached.

<Info>
  **Free seat users only have individual credits. They cannot draw from the workspace pool and are blocked once their 500 lifetime credits are exhausted.**

  **Individual credits (seat credit pool)**
</Info>

Each member's individual credit allocation comes from their seat type:

* **Free seat**: 500 credits (lifetime)
* **Pro seat**: 8,000 credits/month
* **Max seat**: 40,000 credits/month

These credits belong to the individual user. They are not shared across users and reset monthly (except Free seat credits).

## Workspace credit pool

The workspace credit pool is a shared credit reserve that Pro and Max seat members can draw from once their individual credits are exhausted. On the Enterprise Pooled plan, members have no individual credit allocation and draw directly from this shared pool as their only credit source.

The pool is managed by workspace admins:

* **Business plan**: admins can purchase top-up credit packages as needed. Credits purchased through workspace pool top-ups are valid for one year from the date of purchase.
* **Enterprise plans**: the pool is funded by the committed credits defined in your contract.

Free seat users do not have access to the workspace pool.

## Overage / Pay As You Go (Enterprise only)

Enterprise customers can continue using Dust after the workspace pool is exhausted through **Pay As You Go (PAYG)** billing. A spending cap is configured for your workspace to prevent unexpected charges.

PAYG is not available on the Business plan. Business customers must purchase workspace pool top-up packages in advance.

**Business plan**

| Seat type | Individual credits     | Workspace pool                     | Overage       |
| --------- | ---------------------- | ---------------------------------- | ------------- |
| Free      | 500 credits (lifetime) | No access                          | Not available |
| Pro       | 8,000/month            | After individual credits exhausted | Not available |
| Max       | 40,000/month           | After individual credits exhausted | Not available |

**Enterprise Seat-based plan**

| Seat type | Individual credits     | Workspace pool                     | Overage                        |
| --------- | ---------------------- | ---------------------------------- | ------------------------------ |
| Free      | 500 credits (lifetime) | No access                          | Not available                  |
| Pro       | 8,000/month            | After individual credits exhausted | After workspace pool exhausted |
| Max       | 40,000/month           | After individual credits exhausted | After workspace pool exhausted |

**Enterprise Pooled plan**

| Seat type | Individual credits | Workspace pool           | Overage                        |
| --------- | ------------------ | ------------------------ | ------------------------------ |
| Workspace | None               | Draws directly from pool | After workspace pool exhausted |

By default, all members with workspace pool access can draw from it without individual limit. Admins can configure a **personal spend limit** for each member to cap how much of the shared pool they can consume.

The personal spend limit applies **on top of** a member's individual seat credits: it restricts access to the workspace pool, not the seat credits themselves.

* If no personal spend limit is set, the member has unlimited pool access.
* When a member reaches their cap, they are blocked from further pool usage and receive an in-app notification.
* Admins can set a workspace-wide default limit. When the default is updated, only members currently on the previous default are affected.

Members can view their personal spend limit in the Usage page (**Admin > Usage**).

Programmatic usage covers all interactions that are not manually sent by a user, including API calls, Zapier automations, n8n workflows, Google Sheets integrations, Slack bots, and automated triggers.

**How programmatic usage draws credits:**

Programmatic usage is not tied to any individual user. It draws exclusively from the **workspace credit pool**, then from PAYG (Enterprise only) once the pool is exhausted. If neither is available, programmatic usage is blocked.

There is no free credit baseline for programmatic usage.

**Monthly programmatic cap:**

Admins can configure a monthly cap on programmatic credit consumption from **Admin > Usage**. An email notification is sent when 80% of the cap is reached.

## Tracking usage

Workspace admins can view and manage everything credit-related from **Admin > Usage**.

## Workspace credit pool

At the top of the page, the current workspace credit pool balance is displayed (credits consumed vs. total available). Admins on Business plans can purchase top-up packages directly from this page using the **Top up** button.

## Settings

### Spending policies

* **Default workspace credit pool limit**: sets the default amount of workspace pool credits each member can consume. This is added on top of each seat's built-in allowance and can be overridden per member in the Members table. Set to 0 to remove pool access for all members by default.
* **Upgrade request**: when enabled, members who reach their credit limit can request an upgrade instead of being immediately blocked. Workspace admins and managers can review and act on those requests from the Requests tab in the Members section.
* **Auto-upgrade seats**: when enabled, members who reach their credit limit are automatically moved to the next seat tier (Free  Pro, Pro  Max) instead of being blocked. This may increase subscription costs.

### Programmatic usage

* **Programmatic monthly limit**: sets the maximum credits allowed for programmatic usage per month. Set to 0 to block all programmatic access.

### Notifications

* **Workspace credit pool threshold**: admins receive an email when the remaining workspace credit pool balance drops below the configured amount. Set to 0 to disable.
* **Upgrade request emails**: when enabled, all workspace admins receive an email whenever a member requests a spend-limit upgrade.

## Members table

The Members section lists all workspace members with their usage details. Admins can:

* See each member's **seat type** (Free, Pro, Max, or Platform), **credits consumed**, and **credits remaining** for the current period.
* Search members by name and filter by seat type.
* Use the **···** menu on each member row to adjust their personal spend limit or seat type individually.
* Review pending upgrade requests in the **Requests** tab.

For a broader view of workspace credit consumption, trends, and contributing agents or members, see [Analytics](/analytics).
