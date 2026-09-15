> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Seat management

Seats control each workspace member's AI usage capacity. Every member has two independent attributes: a **role** (what they can configure and access; see [Memberships & Roles](/docs/user-documentation/getting-started/dust-rollout-guide/admin-guide-set-up-your-dust-workspace)) and a **seat type** (their credit allocation).

Roles and seat types are independent: an Admin can hold a Free seat, and a Viewer can hold a Pro seat.

## Seat types

Seat types define the monthly credit allocation available to each member. Available seat types depend on your plan.

### Business and Enterprise (seat-based) plans

| Seat type | Monthly credits                            |
| --------- | ------------------------------------------ |
| **Free**  | 500 credits (one-time lifetime allocation) |
| **Pro**   | 8,000 credits/month                        |
| **Max**   | 40,000 credits/month                       |

* **Free seat:** A limited-access tier included on all plans. Free seat credits are a one-time lifetime allocation: they don't renew monthly and cannot be replenished once consumed.
* **Pro seat:** Standard access with a solid monthly credit allocation, well-suited for regular usage.
* **Max seat:** High-capacity access designed for power users with significantly more monthly credits.

For details on how credits work, see [Credits](/docs/user-documentation/admins/usage-seats-and-credits/credits).

### Enterprise (pooled) plan

On the Enterprise Pooled plan, there is a single seat type, the **Workspace seat**, with no individual credit allocation. All members draw from a shared workspace credit pool instead of having personal credits.

## Assigning and managing seats

Admins can assign and change seats from **Admin > Members**.

### Inviting a new member

When inviting someone to your workspace, you specify both their **role** and **seat type**. Available seat types at invitation time depend on your plan:

* **Business (free option):** Free seats only (up to 5 members total). You can offer a Pro or Max seat during invitation, but this will trigger checkout to add a paid subscription first.
* **Business (paid):** Free, Pro, or Max, subject to available seats and plan limits.
* **Enterprise Seat-based:** Pro or Max (annual only).
* **Enterprise Pooled:** Workspace seats only.

### Changing an existing member's seat

Admins can change a member's seat type at any time from **Admin > Usage**, in the Members list, using the **Change seat type** action. Timing depends on the direction of the change:

| Transition       | Timing                                                                                                    |
| ---------------- | --------------------------------------------------------------------------------------------------------- |
| Free  Pro or Max | Immediate. Full credit allocation granted right away.                                                     |
| Pro  Max         | Immediate.                                                                                                |
| Max  Pro         | Deferred to the next billing period. The member retains Max access through the end of the current period. |

### Member-initiated upgrade requests

When members reach their credit limit, they are blocked from sending messages. Admins can allow members to request a seat upgrade instead of being silently blocked.

To enable this, go to **Admin > Usage > Settings** and turn on the **Upgrade request** toggle. Once enabled, blocked members see a prompt to request an upgrade. Workspace admins and managers can then review and act on pending requests from the **Requests** tab in the Members section.

The video below shows how to review and process an upgrade request as a workspace admin or manager:

### Unassigned members

A member can exist in the workspace without a seat ("Unassigned"). Unassigned members can access the workspace but cannot post messages or interact with agents until a seat is assigned.

## Monthly vs. annual seats

On the **Business plan**, seats can be billed monthly or annually, and both billing cycles can coexist within the same workspace. Annual seats are billed at a lower monthly rate.

On **Enterprise plans**, all seats are annual only. Mid-year seat additions are billed on a prorated basis from the date the seat is added through the end of the current subscription term. The new member receives their full credit allocation immediately, not prorated.

When a seat is unassigned:

* **Monthly seats** are removed immediately (with a prorated credit applied to the next invoice).
* **Annual seats** are returned to your seat stock and can be reassigned to another member at the end of the current credit period. Seats vacated when someone leaves are not refunded.
