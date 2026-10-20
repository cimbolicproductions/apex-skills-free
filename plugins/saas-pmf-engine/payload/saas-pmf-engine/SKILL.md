---
name: saas-pmf-engine
description: "Use when measuring product-market fit, running the Superhuman PMF survey, segmenting very-disappointed users, finding high-expectation customers, or building a PMF improvement roadmap."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# SaaS PMF Engine

## When to Use This Skill

- The product has users and the user asks whether they have PMF.
- The user wants to run the Superhuman PMF method.
- The user has survey responses and needs segmentation or roadmap decisions.

## When Not to Use This Skill

- The product has no active users; use validation first.
- The user only wants NPS or satisfaction scoring.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- How many users have used the product at least twice recently?
- What user segments, roles, or use cases exist?
- Do you have survey responses or need the survey drafted?

## Operating Workflow

- Use the four-question PMF survey: disappointment, who benefits most, main benefit, improvement request.
- Calculate the percentage who would be very disappointed without the product.
- Segment very disappointed users by role, use case, acquisition source, and main benefit.
- Identify high-expectation customers and their common language.
- Use somewhat disappointed users to find solvable blockers when they share the core benefit.
- Build a 50/50 roadmap: double down on loved benefits and remove top blockers.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Survey template.
- Scoring sheet structure.
- Segment analysis.
- High-expectation customer profile.
- PMF roadmap.

## Quality Checklist

Before finalizing, verify:

- Do not average all feedback equally.
- Prioritize users who match the loved-benefit segment.
- Roadmap decisions tie to PMF score movement.

## Research-Backed Defaults and Sources

- First Round Superhuman PMF engine: https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
- Lenny activation metric guide: https://www.lennysnewsletter.com/p/how-to-determine-your-activation
- Stripe SaaS integration docs: https://docs.stripe.com/saas
- Userpilot fake door testing: https://userpilot.com/blog/fake-door-testing/
- ProdPad painted door testing: https://www.prodpad.com/blog/painted-door-test/
- Rob Walling Stair Step Method: https://robwalling.com/essays/2015/03/26/the-stair-step-method-of-bootstrapping
- AppTweak ASO best practices: https://www.apptweak.com/en/aso-blog/app-store-optimization-aso

