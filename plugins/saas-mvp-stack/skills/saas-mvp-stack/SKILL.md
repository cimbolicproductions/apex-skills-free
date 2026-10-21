---
name: saas-mvp-stack
description: "Use when choosing a SaaS MVP tech stack, boilerplate, Supabase vs Firebase, Next.js setup, Vercel, Resend, PostHog, Sentry, auth, or pre-launch technical checklist."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# SaaS MVP Stack

## When to Use This Skill

- The user asks what stack to use for a SaaS MVP.
- The user wants to ship quickly without reinventing auth, billing, analytics, or email.
- The user is comparing Supabase, Firebase, Clerk, Next.js, Vercel, or boilerplates.

## When Not to Use This Skill

- The user already has a mature stack and needs a specific bug fix.
- The user is building a native-only app where web stack guidance is irrelevant.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Is this web, mobile, browser extension, API, or internal tool?
- Do you need teams/workspaces, file uploads, real-time updates, or role-based access?
- What matters most: speed, cost, control, mobile SDKs, SQL, or enterprise readiness?

## Operating Workflow

- Default indie web SaaS stack: Next.js, Supabase, Stripe, Vercel, Resend, PostHog, Sentry.
- Prefer Supabase when SQL, relational data, RLS, and predictable database behavior matter.
- Prefer Firebase when mobile-first, Google ecosystem, realtime sync, and offline SDKs dominate.
- Recommend boilerplates only when they reduce non-differentiated work and match the founder's stack.
- Include production basics before launch: auth, rate limits, logs, error tracking, backups, analytics, legal pages, SSL.
- Avoid premature microservices, custom auth, and custom billing for MVPs.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Stack recommendation with tradeoffs.
- 48-hour setup sequence.
- Pre-launch technical checklist.
- Boilerplate decision criteria.

## Quality Checklist

Before finalizing, verify:

- The recommendation fits the founder's skill level and distribution plan.
- The stack covers auth, billing, email, analytics, errors, and deployment.
- Avoids trendy tools that do not reduce launch risk.

## Research-Backed Defaults and Sources

- First Round Superhuman PMF engine: https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
- Lenny activation metric guide: https://www.lennysnewsletter.com/p/how-to-determine-your-activation
- Stripe SaaS integration docs: https://docs.stripe.com/saas
- Userpilot fake door testing: https://userpilot.com/blog/fake-door-testing/
- ProdPad painted door testing: https://www.prodpad.com/blog/painted-door-test/
- Rob Walling Stair Step Method: https://robwalling.com/essays/2015/03/26/the-stair-step-method-of-bootstrapping
- AppTweak ASO best practices: https://www.apptweak.com/en/aso-blog/app-store-optimization-aso

