---
name: saas-activation-analytics
description: "Use when defining activation metrics, aha moments, PostHog or Mixpanel events, onboarding funnels, retention cohorts, or analytics schemas for SaaS products."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# SaaS Activation Analytics

## When to Use This Skill

- The user asks what events to track or how to find the aha moment.
- A product has signups but weak activation, retention, or unclear funnels.
- The user is setting up PostHog, Mixpanel, Amplitude, or internal analytics.

## When Not to Use This Skill

- The product has no users and needs validation first.
- The task is general financial reporting.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- What is the product's promised first value?
- What actions can users take in the first session, first day, and first week?
- What retention definition matters: day 7, day 30, weekly active, paid renewal, or repeat usage?

## Operating Workflow

- List all candidate first-value events.
- Create an event taxonomy: acquisition, signup, onboarding, activation, engagement, billing, retention.
- Define properties consistently: user role, plan, source, workspace id, feature, error state.
- Use cohort analysis to compare retained users who did vs did not complete each candidate event.
- Pick the event with the strongest retention delta as the activation metric.
- Redesign onboarding to route directly to that event.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Event schema table.
- Activation metric candidates.
- Funnel design.
- PostHog/Mixpanel setup notes.
- Dashboard and experiment recommendations.

## Quality Checklist

Before finalizing, verify:

- Events are named consistently in past tense or action-object format.
- Activation is tied to retained behavior, not vanity signups.
- The schema includes user and account-level properties for B2B SaaS.

## Research-Backed Defaults and Sources

- First Round Superhuman PMF engine: https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
- Lenny activation metric guide: https://www.lennysnewsletter.com/p/how-to-determine-your-activation
- Stripe SaaS integration docs: https://docs.stripe.com/saas
- Userpilot fake door testing: https://userpilot.com/blog/fake-door-testing/
- ProdPad painted door testing: https://www.prodpad.com/blog/painted-door-test/
- Rob Walling Stair Step Method: https://robwalling.com/essays/2015/03/26/the-stair-step-method-of-bootstrapping
- AppTweak ASO best practices: https://www.apptweak.com/en/aso-blog/app-store-optimization-aso

