---
name: saas-stripe-setup
description: "Use when adding subscriptions, Stripe Checkout, pricing tables, trials, customer portal, webhooks, failed payment handling, Stripe plus Supabase access control, or SaaS billing lifecycle logic."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# SaaS Stripe Setup

## When to Use This Skill

- The user wants to set up SaaS payments or subscriptions.
- The task includes Stripe products, prices, Checkout, Billing Portal, trials, webhooks, or dunning.
- Subscription status must control app access.

## When Not to Use This Skill

- The user only needs pricing strategy without implementation.
- The user is processing one-off marketplace transactions with no subscription lifecycle.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- What plans, intervals, trials, and usage limits exist?
- What stack controls auth and authorization: Supabase, Firebase, Clerk, custom DB?
- What should happen on payment failure, cancellation, upgrade, downgrade, and refund?

## Operating Workflow

- Model products and prices before writing code.
- Use Stripe Checkout or Pricing Table for MVP speed unless custom UX is required.
- Listen for subscription lifecycle events: created, updated, deleted, invoice paid, invoice failed.
- Make webhook handlers idempotent and verify Stripe signatures.
- Store Stripe customer id, subscription id, plan, status, current period, and entitlement flags.
- Gate access from server-side subscription state, not only client state.
- Configure customer portal, Smart Retries, cancellation flow, and tax needs.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Stripe product/price map.
- Webhook event matrix.
- Database fields and entitlement model.
- Implementation checklist.
- Failure and dunning behavior.

## Quality Checklist

Before finalizing, verify:

- Webhooks are idempotent and signature-verified.
- Subscription access is controlled server-side.
- Payment failure does not silently grant or revoke incorrectly.

## Research-Backed Defaults and Sources

- First Round Superhuman PMF engine: https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
- Lenny activation metric guide: https://www.lennysnewsletter.com/p/how-to-determine-your-activation
- Stripe SaaS integration docs: https://docs.stripe.com/saas
- Userpilot fake door testing: https://userpilot.com/blog/fake-door-testing/
- ProdPad painted door testing: https://www.prodpad.com/blog/painted-door-test/
- Rob Walling Stair Step Method: https://robwalling.com/essays/2015/03/26/the-stair-step-method-of-bootstrapping
- AppTweak ASO best practices: https://www.apptweak.com/en/aso-blog/app-store-optimization-aso

