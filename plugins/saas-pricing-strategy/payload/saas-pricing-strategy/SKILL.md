---
name: saas-pricing-strategy
description: "Use when pricing SaaS, choosing free trial vs freemium, creating tiers, testing packages, setting Stripe products, evaluating usage-based vs seat-based pricing, or fixing underpricing."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# SaaS Pricing Strategy

## When to Use This Skill

- The user asks how much to charge or which pricing model to use.
- The user needs tiers, packaging, annual plans, trials, coupons, or pricing page copy.
- The product has value that may scale by seats, usage, projects, credits, revenue, or locations.

## When Not to Use This Skill

- The user needs Stripe webhook implementation; use saas-stripe-setup.
- The user only needs general business model brainstorming without a product.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Who pays and what budget does the spend come from?
- What value metric grows with customer value?
- What competitors or substitutes define the price anchor?

## Operating Workflow

- Identify value metric candidates: seat, usage, project, location, revenue, saved time, or transaction.
- Package before pricing: define Good/Better/Best or Starter/Pro/Scale by buyer maturity.
- Anchor with an expensive premium tier and make the recommended tier obvious.
- Choose trial model based on time-to-value and sales motion.
- Test packaging first, then value metric, then price points, then annual discount presentation.
- Map the final structure to Stripe products and prices.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Pricing model recommendation.
- Tier table with inclusions and limits.
- Trial/freemium recommendation.
- Pricing page copy.
- Testing plan.

## Quality Checklist

Before finalizing, verify:

- The value metric is easy to understand and hard to game.
- The recommended tier has a clear reason to choose it.
- Discounts do not train users to wait unless strategic.

## Research-Backed Defaults and Sources

- First Round Superhuman PMF engine: https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
- Lenny activation metric guide: https://www.lennysnewsletter.com/p/how-to-determine-your-activation
- Stripe SaaS integration docs: https://docs.stripe.com/saas
- Userpilot fake door testing: https://userpilot.com/blog/fake-door-testing/
- ProdPad painted door testing: https://www.prodpad.com/blog/painted-door-test/
- Rob Walling Stair Step Method: https://robwalling.com/essays/2015/03/26/the-stair-step-method-of-bootstrapping
- AppTweak ASO best practices: https://www.apptweak.com/en/aso-blog/app-store-optimization-aso

