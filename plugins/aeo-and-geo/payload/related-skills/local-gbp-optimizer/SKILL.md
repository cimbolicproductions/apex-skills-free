---
name: local-gbp-optimizer
description: "Use when optimizing a Google Business Profile, local map rankings, GBP categories, services, descriptions, photos, posts, reviews, or local search visibility for a service business. Owns the Optimized GBP Gate that must pass before a GBP is imported into Bing Places (seo-bing-places) and before any downstream listing import."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.1'
  cluster: seo
  public_revision: "2026-10-06"
---

# Local Google Business Profile Optimizer

## When to Use This Skill

- The user asks why their business is not showing up on Google Maps.
- The user needs GBP description, category, services, posts, photos, or review strategy.
- A local service business wants higher map pack visibility.
- Another skill needs the **Optimized GBP Gate** checked (seo-bing-places before import, aeo-and-geo Stage 1.5).

## When Not to Use This Skill

- The business is online-only with no local service area.
- The user needs paid ad setup rather than organic local visibility.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Business name, primary service, city/service area, address or service-area model.
- Top 3 local competitors ranking for the target search.
- Current categories, reviews, photos, website, and NAP consistency if known.

## Operating Workflow

- Prioritize primary category first, matching top competitors when appropriate.
- Add relevant secondary categories without category stuffing.
- Write a natural 750-character description including service, city, value proposition, and trust signals.
- Create service listings with concise descriptions and optional price anchors.
- **Do not seed Q&A.** Google discontinued the My Business Q&A API on 2025-11-03 "as we are in the process of updating the Q&A functionality" ([Google changelog](https://developers.google.com/my-business/content/qanda/change-log)); SEO press reports the public Q&A section was removed and Maps now generates answers from the profile, reviews and website (reported, not confirmed on a Google help page). Put real buyer questions and answers on the website instead, via `aeo-and-geo`, and keep the same facts in the services list and description.
- Build weekly post cadence: offer, proof, education, seasonal reminder.
- Create a photo plan: exterior, team, vehicle, before/after, equipment, jobs, proof, and service area.
- Audit NAP consistency across major directories.
- Run the **Optimized GBP Gate** below. Nothing downstream imports this profile until it passes.


## Canonical Business Facts

Fill this once from owner-confirmed facts before listing work. Reuse the same spelling and values in every listing and on the website. A service-area business should not expose a private address that its owner has chosen to hide.

```text
BUSINESS NAME: <exact real trading name>
ADDRESS OR SERVICE AREA: <owner-approved public address or service area>
PHONE: <real business phone, with tracking-number policy if applicable>
CANONICAL WEBSITE: <working full URL, no fragment>
HOURS: <each day plus special/holiday hours>
PRIMARY CATEGORY: <real primary service>
```

## Optimized GBP Gate

The gate defines the checks to complete before importing a profile into Bing Places. Check each box against the **signed-out public profile** where the field is public, never against what the dashboard says was saved.

```
[ ] Profile verified by the owner; the authorized operator has required access (or the exact missing access is recorded)
[ ] Name, address, phone character-identical to the Canonical Business Facts block above; no keywords added to the name
[ ] Primary category = highest buyer intent that matches the real business; secondaries are real services only
[ ] Website button opens the canonical page: no #anchor, no redirect chain, no dead route
[ ] Appointment / booking link opens a working form on a phone (or the field is empty on purpose)
[ ] Regular hours match owner-confirmed hours for every day; special hours set for the next holiday
[ ] Services list complete, each with a description; prices only where the owner confirmed them
[ ] Description <= 750 characters, service + city stated naturally, no URLs or keyword lists
[ ] At least 6 real photos (exterior, interior, team, work); owner supplied or permission confirmed
[ ] Review link copied from the profile and opened successfully
```

**Why the gate exists:** Bing's import can copy errors from Google, and later synchronization may restore them after a manual Bing fix. Check and correct the source profile before importing.

**On a failing box:** if the fix needs the owner (verification, access, hours, photos), stop downstream imports and use the Blocker Format below, naming the failing box. Work that does not read from GBP (citations, on-site schema, website answers) may continue.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- GBP audit.
- Category recommendation.
- Description draft.
- Service listing copy.
- 10 real buyer questions with answers, routed to the website pages via `aeo-and-geo` (not posted as GBP Q&A).
- 4-week GBP post calendar.
- Photo and citation checklist.
- Optimized GBP Gate, pasted with every box marked.
- Next step line: `Gate passed → import into Bing Places (seo-bing-places)` or the Blocker.

## Quality Checklist

Before finalizing, verify:

- No keyword stuffing.
- Recommendations are service-area specific.
- The first 7 days of actions are clear and ranked by impact.
- The gate was checked against the rendered public profile, not assumed.

## Research-Backed Defaults and Sources

- GBP Rank Tracker local SEO guide: https://gbpranktracker.com/guides/local-seo-complete-guide
- Google My Business Q&A API discontinuation: https://developers.google.com/my-business/content/qanda/change-log
- GetNextPhone missed-call text-back guide: https://www.getnextphone.com/blog/missed-call-text-back
- LeadAngel speed-to-lead statistics: https://www.leadangel.com/blog/operations/speed-to-lead-statistics/
- EstimateRocket quote follow-up templates: https://www.estimaterocket.com/whats_new/how-to-follow-up-on-a-job-quote-and-close-the-sale-with-templates
- Toolsey good-better-best pricing for home services: https://toolsey.com/blog/good-better-best-home-services
- GoHighLevel CRM automation guide: https://www.gohighlevel.com/post/crm-automation-best-practices-for-small-businesses

## Execution and Output Contract

- Read the complete skill before starting. Use the templates and checklist as written.
- Use real source data; never invent prices, access, completed actions, rankings, or results. Mark unavailable data as `unknown` and name the required input.
- Prepare drafts and audits within the user's request. Get the owner's authorization before changing live business listings, publishing site changes, or sending messages. Owner verification and sign-in remain owner actions.
- Verify completed work against the actual export, rendered page, or signed-out listing. Record source URLs and the date checked.
- Optional related skills may help, but do not assume they are installed. Apply this skill's complete workflow directly when they are absent.

```text
DONE: <skill name>
Files or reports created/updated: <paths or none>
Evidence checked: <sources and date>
Checklist: <all required items verified, or explain incomplete items>
Assumptions: <numbered list or none>
Needs owner: <actions or nothing>
```

If a required input or access is missing:

```text
BLOCKED at <skill> / <stage>
What happened: <literal error or missing input>
What I tried: <checks actually performed>
What I need: <one specific question or action>
Work saved at: <paths or none>
```
