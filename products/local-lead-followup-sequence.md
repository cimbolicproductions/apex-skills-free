---
name: local-lead-followup-sequence
description: "Use when writing new lead SMS/email follow-up for local service inquiries, speed-to-lead automation, no-response nurturing, booking prompts, or inbound lead conversion workflows."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Local Lead Follow-Up Sequence

## When to Use This Skill

- A new inbound lead has not booked yet.
- The user needs SMS/email sequence for form leads, Facebook leads, calls, or web chat.
- The business responds too slowly or inconsistently.

## When Not to Use This Skill

- The lead has already received an estimate; use local-quote-followup.
- The user needs cold B2B outreach; use local-b2b-property-manager-outreach.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Lead source, service type, business hours, booking link, and offer if any.
- Preferred channel: SMS, email, phone, or all.
- What information is needed before quoting or booking?

## Operating Workflow

- Respond immediately with acknowledgment and next-step expectation.
- Use binary-choice CTAs such as morning or afternoon, today or tomorrow.
- Send follow-ups at immediate, 1 hour, 24 hours, and 72 hours if no response.
- Add value or urgency at each touch. Do not send empty just checking in messages.
- Branch based on replies: booked, needs quote, price objection, not ready, wrong fit.
- Log the lead status and next follow-up in CRM.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- 4-message SMS sequence.
- 3-email companion sequence.
- Branching logic.
- Booking CTA variations.
- CRM stage mapping.

## Quality Checklist

Before finalizing, verify:

- The first message can send within two minutes.
- Each message has one clear ask.
- Opt-out and consent considerations are included.

## Research-Backed Defaults and Sources

- GBP Rank Tracker local SEO guide: https://gbpranktracker.com/guides/local-seo-complete-guide
- GetNextPhone missed-call text-back guide: https://www.getnextphone.com/blog/missed-call-text-back
- LeadAngel speed-to-lead statistics: https://www.leadangel.com/blog/operations/speed-to-lead-statistics/
- EstimateRocket quote follow-up templates: https://www.estimaterocket.com/whats_new/how-to-follow-up-on-a-job-quote-and-close-the-sale-with-templates
- Toolsey good-better-best pricing for home services: https://toolsey.com/blog/good-better-best-home-services
- GoHighLevel CRM automation guide: https://www.gohighlevel.com/post/crm-automation-best-practices-for-small-businesses

