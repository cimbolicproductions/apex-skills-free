---
name: appliance-repair-triage
description: "Use when triaging washer, dryer, refrigerator, dishwasher, oven, or range symptoms, likely causes, error codes, repair difficulty, parts checklist, and repair-vs-replace decisions."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Appliance Repair Triage

## When to Use This Skill

- The user describes an appliance symptom or error code.
- The user needs likely causes, safe checks, parts, and repair difficulty.
- The user needs to decide whether to repair, part out, sell as-is, or scrap.

## When Not to Use This Skill

- The repair involves gas leaks, live electrical hazards, refrigerant, or unsafe conditions; advise qualified service.
- The user only needs listing copy for a known-working unit.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Appliance type, brand, model, age, symptom, when it happens, noises, leaks, smells, error codes, and recent events.
- Can the user safely power cycle, inspect, or run diagnostic mode?
- What tools and skill level does the user have?

## Operating Workflow

- Start with safety: unplug, shut off water/gas where appropriate, and avoid live testing unless qualified.
- Map symptom to most likely causes and cheapest checks first.
- Ask for model number because part compatibility matters.
- Separate DIY-safe checks from professional-only repairs.
- Estimate repair difficulty, parts cost class, time, and risk.
- Create repair-vs-replace logic based on age, value, parts availability, and resale/rental use.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Likely cause ranking.
- Safe diagnostic steps.
- Parts/tools checklist.
- Repair difficulty.
- Repair, sell as-is, part out, or scrap recommendation.

## Quality Checklist

Before finalizing, verify:

- Never suggest bypassing safety switches or protections.
- Do not guarantee diagnosis from symptoms alone.
- Professional-only hazards are clearly labeled.

## Research-Backed Defaults and Sources

- eBay Seller Center product photo guidance: https://ebaysc.liveplatform.com/tips-for-selling-online/effective-ebay-listings/product-photos
- eBay selling best practices: https://www.selleractive.com/e-commerce-blog/ebays-10-best-selling-practices
- AARP Facebook Marketplace scam guide: https://www.aarp.org/money/scams-fraud/facebook-marketplace/
- Regions Bank online selling safety guide: https://www.regions.com/insights/personal/article/how-to-protect-yourself-when-selling-online
- Repair Clinic troubleshooting library: https://www.repairclinic.com/RepairHelp
- CPSC recalls database: https://www.cpsc.gov/Recalls

