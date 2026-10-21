---
name: marketplace-pricing-comps
description: "Use when pricing items for eBay, Facebook Marketplace, Craigslist, OfferUp, appliances, furniture, electronics, or resale inventory using sold comps, local comps, condition, urgency, and negotiation room."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Marketplace Pricing Comps

## When to Use This Skill

- The user asks what to list an item for.
- The item has comps across sold listings, local listings, retail price, or repair cost.
- The user wants fast sale, max profit, wholesale, or rental-ready pricing.

## When Not to Use This Skill

- The item is unique art, collectible, or vehicle requiring specialist appraisal.
- There are safety or recall concerns not yet checked.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Exact item identifiers: brand, model, condition, age, defects, accessories, and location.
- Goal: sell fast, maximize profit, clear inventory, bundle, or test demand.
- Known retail price, repair cost, delivery cost, and platform fees.

## Operating Workflow

- Use sold listings for shipped marketplaces and active local comps for pickup marketplaces.
- Normalize comps by condition, age, completeness, warranty, delivery, and seasonality.
- Set list price with negotiation room for local platforms.
- Calculate floor price from acquisition cost, parts/labor, platform fees, delivery, and target margin.
- Create price-drop schedule tied to days listed and inquiry volume.
- For appliances, price differently for as-is, tested, refurbished, delivered, and warrantied units.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Comp table structure.
- Recommended list price, target price, and floor price.
- Negotiation margin.
- Price-drop schedule.
- Bundle or delivery fee guidance.

## Quality Checklist

Before finalizing, verify:

- Sold comps are weighted above asking prices when available.
- Condition adjustments are explicit.
- The floor price protects margin.

## Research-Backed Defaults and Sources

- eBay Seller Center product photo guidance: https://ebaysc.liveplatform.com/tips-for-selling-online/effective-ebay-listings/product-photos
- eBay selling best practices: https://www.selleractive.com/e-commerce-blog/ebays-10-best-selling-practices
- AARP Facebook Marketplace scam guide: https://www.aarp.org/money/scams-fraud/facebook-marketplace/
- Regions Bank online selling safety guide: https://www.regions.com/insights/personal/article/how-to-protect-yourself-when-selling-online
- Repair Clinic troubleshooting library: https://www.repairclinic.com/RepairHelp
- CPSC recalls database: https://www.cpsc.gov/Recalls

