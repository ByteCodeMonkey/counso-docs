> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dust.tt/llms.txt
> Use this file to discover all available pages before exploring further.

# Subscriptions & Payments

You can manage your subscription by going to **Admin > Billing**.

## Plans

Dust offers two plans:

* **Business**: available with a free option (no credit card required, up to 5 users, 3 connector, 5 Spaces) or with paid Pro and Max seats for more capacity (up to 100 seats, up to 3 connectors, 5 Spaces).
* **Enterprise**: unlimited users and connectors, unlimited Spaces, SSO, SCIM, audit logs, and advanced credit controls. Contact sales to get started.

Each seat type (Free, Pro, Max) comes with a monthly credit allocation. Learn more in [Credits](/docs/user-documentation/admins/usage-seats-and-credits/credits) and [Seat management](/docs/user-documentation/admins/usage-seats-and-credits/seat-management).

## Subscribing to the Business plan

### How do I subscribe to the Business plan?

You can subscribe in two ways:

* **At sign-up**: when creating your workspace, select a Pro or Max seat to go directly to checkout.
* **From the free option**: start with a free workspace and upgrade any member's seat to Pro or Max from **Admin > Usage**. This triggers the checkout flow.

At checkout, you are billed for one full billing period (monthly or annual) for the paid seat.

### How do I pay as a business?

To pay as a company on Dust with Stripe:

1. At checkout, choose "I'm purchasing as a business".
2. Enter your company name and VAT number correctly.
3. Click 'Save' to save your payment method, then confirm the payment to complete the purchase.

A Stripe invoice is generated and the new seat is available immediately.

## How Business plan billing works

Your billing period is anchored to your subscription start date and renews on that same date each month or year. Billing is per seat: seats can be billed **monthly** or **annually**, and both billing cycles can coexist in the same workspace.

* **Monthly seats**: billed upfront each month based on seats active at the start of the period.
* **Annual seats**: billed at a lower monthly rate, for the full year.

### Adding seats mid-period

Mid-period seat additions are prorated from the date the seat is added through the end of the current subscription term, and invoiced in the next billing month.

Here is an example:

Let's assume you have 2 Pro seats at the start of your pay period (September 3rd – October 2nd) and add a third seat on September 18th.

* On September 3rd, you are charged upfront for 2 seats for the September period.
* On October 3rd, you are charged upfront for 3 seats for October, **plus** a prorated charge for the 15 days of the added September seat.

### Removing seats

* **Monthly seats** removed mid-period are credited on a prorated basis to the next invoice.
* **Annual seats** are returned to your seat stock when unassigned. They can be reassigned to another member at the end of the current credit period. Seats vacated when someone leaves are not refunded.

## Managing your subscription

You can manage your subscription from **Admin > Billing**. From there, you can upgrade your plan, update your payment details, and access invoices.

## What happens when you cancel your subscription?

When you cancel your paid subscription, your subscription remains active until the end of the current billing period. Once that period ends:

* Your workspace will revert to the free version of the Business plan.
* All users except one will be removed from your workspace.
* Your connections will be deleted.
* The rest of your data (conversations, custom agents, custom data sources) will still be accessible but with multiple limitations.

Below are answers to the most common questions.

### Will we continue to be able to use agents, connections, and data sources?

Your workspace will revert to the free version of the Business plan and be subject to its limitations. In particular:

* All users except one will be removed from your workspace.
* Your connections will be deleted.
* The rest of your data (conversations, custom agents, custom data sources) will still be accessible but with multiple limitations.

### Which user will remain after the downgrade?

The user who was given an `admin` role the earliest. This will typically be the person who initially subscribed, unless they were removed or their role was changed later.

If you'd like a different user to remain, remove all other admins (by revoking them or downgrading their role) before your subscription ends.

### What will happen to our connections (Notion, Slack, Google Drive, etc.)?

They will be deleted, along with all the related data that was synced to our servers. Your original data remains available via the data providers themselves. Dust cannot and will not alter the original data.

### What will happen to the Dust Slackbot?

It will be removed.

### What will happen to our users' conversations?

The remaining user's conversations, as well as former users' conversation links, will remain accessible. However, the ability to interact with those conversations will be limited due to the free Business plan restrictions.

### What will happen to our data sources and uploaded documents?

Your data sources and documents will not be automatically deleted, except for data sources with combined data over 50 MB, which will be deleted after 7 days (you will be warned by email).

If the total number of data sources and documents exceeds the free Business plan limit, you will need to delete some data to stay within the limit. If you resubscribe, your data sources and documents will become fully accessible again.

### What will happen to our custom agents?

Your custom agents will be deactivated upon downgrading. If you resubscribe, they will be reactivated and function as they did before.

### What if we want to reactivate our subscription?

Go to **Admin > Subscription** and resubscribe. Upon reactivating, all previously limited or inaccessible features and data will be restored, including access to multiple users, connections, data sources, and custom agents.

### What if we want to delete everything?

Send us an email at [support@dust.tt](mailto:support@dust.tt). We will delete your account and all associated data, except for data we are legally required to keep (such as invoicing data). Note that this action is irreversible: all custom agents, data sources, documents, and conversations will be permanently deleted.

*If you have any further questions about your Dust subscription, don't hesitate to contact us at [support@dust.tt](mailto:support@dust.tt).*
