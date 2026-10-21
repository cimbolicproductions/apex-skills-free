---
name: local-crm-automation
description: "Use when setting up CRM, pipeline stages, GoHighLevel, HubSpot, Twilio, n8n, lead intake, follow-up automation, booking reminders, review triggers, or local service workflow automation."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Local CRM and Automation Setup

## When to Use This Skill

- Leads are scattered across phone, text, Facebook, web forms, email, or spreadsheets.
- The user needs a CRM recommendation or pipeline design.
- The business needs automation from lead intake to review request.

## When Not to Use This Skill

- The user only needs one message template.
- The business has a mature CRM and needs a platform-specific technical integration.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Lead sources, current tools, monthly budget, team size, service type, and booking process.
- Which automations are must-have now?
- What data must be captured for every lead?

## Operating Workflow

- Recommend CRM by stage: spreadsheet/HubSpot for low budget, GHL for all-in-one local automation, field-service tool for dispatch-heavy teams.
- Create minimum viable pipeline: New Lead, Contacted, Quote Sent, Follow-Up, Won, Lost.
- Define automations: missed call text, new lead sequence, quote follow-up, appointment reminder, job complete review request, retention follow-up.
- Create required fields: source, service, location, urgency, quote amount, next action, lead status, lost reason.
- Start with high-revenue leak workflows before advanced marketing.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- CRM recommendation.
- Pipeline stages.
- Automation workflow specs.
- Field schema.
- Implementation priority order.

## Quality Checklist

Before finalizing, verify:

- The system can be run by a busy owner on a phone.
- No automation depends on perfect data entry to work.
- Every workflow has an owner and failure fallback.

## Research-Backed Defaults and Sources

- GBP Rank Tracker local SEO guide: https://gbpranktracker.com/guides/local-seo-complete-guide
- GetNextPhone missed-call text-back guide: https://www.getnextphone.com/blog/missed-call-text-back
- LeadAngel speed-to-lead statistics: https://www.leadangel.com/blog/operations/speed-to-lead-statistics/
- EstimateRocket quote follow-up templates: https://www.estimaterocket.com/whats_new/how-to-follow-up-on-a-job-quote-and-close-the-sale-with-templates
- Toolsey good-better-best pricing for home services: https://toolsey.com/blog/good-better-best-home-services
- GoHighLevel CRM automation guide: https://www.gohighlevel.com/post/crm-automation-best-practices-for-small-businesses

