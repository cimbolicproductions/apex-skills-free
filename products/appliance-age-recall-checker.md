---
name: appliance-age-recall-checker
description: "Use when checking appliance age from model/serial, recall risk, safety warnings, resale eligibility, listing disclosure, or whether an appliance should not be sold or rented."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Appliance Age and Recall Checker

## When to Use This Skill

- The user provides appliance model or serial and asks age or recall status.
- An appliance is being listed, rented, refurbished, bought, or delivered.
- The user wants to avoid selling unsafe recalled equipment.

## When Not to Use This Skill

- No model/serial/manufacturer information is available and cannot be obtained.
- The user asks for a definitive safety certification without official verification.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Manufacturer, model number, serial number, appliance type, and country.
- Photos of data plate if available.
- Whether the appliance will be sold, rented, repaired, or scrapped.

## Operating Workflow

- Locate model and serial on the appliance data plate.
- Use manufacturer resources or serial decoding references to estimate age when possible.
- Search official recall databases such as CPSC in the US before resale or rental.
- If recall status is unclear, advise contacting manufacturer support with model and serial.
- Flag do-not-sell conditions: active safety recall without remedy, unsafe electrical/gas condition, missing safety components.
- Prepare disclosure language for age, condition, repairs, and warranty if listing.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Age lookup plan.
- Recall check steps.
- Safety/resale recommendation.
- Listing disclosure language.
- Manufacturer contact template.

## Quality Checklist

Before finalizing, verify:

- Official recall sources are preferred over forum claims.
- Uncertain age is labeled estimated.
- The skill errs on safety for rental or resale inventory.

## Research-Backed Defaults and Sources

- eBay Seller Center product photo guidance: https://ebaysc.liveplatform.com/tips-for-selling-online/effective-ebay-listings/product-photos
- eBay selling best practices: https://www.selleractive.com/e-commerce-blog/ebays-10-best-selling-practices
- AARP Facebook Marketplace scam guide: https://www.aarp.org/money/scams-fraud/facebook-marketplace/
- Regions Bank online selling safety guide: https://www.regions.com/insights/personal/article/how-to-protect-yourself-when-selling-online
- Repair Clinic troubleshooting library: https://www.repairclinic.com/RepairHelp
- CPSC recalls database: https://www.cpsc.gov/Recalls

