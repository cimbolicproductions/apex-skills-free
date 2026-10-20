---
name: local-missed-call-textback
description: "Use when a local business misses calls, needs missed-call auto-SMS, after-hours triage, urgent/routine branching, Twilio, GoHighLevel, Grasshopper, or n8n missed-call workflows."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Missed-Call Text-Back Builder

## When to Use This Skill

- The user loses leads when unable to answer the phone.
- The business needs auto-SMS recovery for missed calls.
- The user wants urgent vs routine triage and after-hours handling.

## When Not to Use This Skill

- The business never receives phone leads.
- The user is asking for full CRM setup; use local-crm-automation.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Business type, phone system, hours, emergency availability, and desired callback SLA.
- What counts as urgent?
- What platform is available: GHL, Twilio, Grasshopper, n8n, Zapier, or none?

## Operating Workflow

- Trigger within 30 to 60 seconds of missed call.
- Send business-hours SMS with apology, quick reply prompt, and callback expectation.
- Send after-hours SMS with next-open promise and urgent keyword option.
- If no reply after 20 to 30 minutes, send one polite follow-up.
- Route urgent replies to owner notification.
- Create or update CRM record with source, call time, message status, and next action.
- Include STOP opt-out language when appropriate.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Business-hours template.
- After-hours template.
- Urgent triage logic.
- Platform setup steps.
- TCPA-aware compliance checklist.

## Quality Checklist

Before finalizing, verify:

- Messages sound human and local, not spammy.
- There is a clear owner alert for urgent replies.
- Automation never promises an impossible response time.

## Research-Backed Defaults and Sources

- GBP Rank Tracker local SEO guide: https://gbpranktracker.com/guides/local-seo-complete-guide
- GetNextPhone missed-call text-back guide: https://www.getnextphone.com/blog/missed-call-text-back
- LeadAngel speed-to-lead statistics: https://www.leadangel.com/blog/operations/speed-to-lead-statistics/
- EstimateRocket quote follow-up templates: https://www.estimaterocket.com/whats_new/how-to-follow-up-on-a-job-quote-and-close-the-sale-with-templates
- Toolsey good-better-best pricing for home services: https://toolsey.com/blog/good-better-best-home-services
- GoHighLevel CRM automation guide: https://www.gohighlevel.com/post/crm-automation-best-practices-for-small-businesses

