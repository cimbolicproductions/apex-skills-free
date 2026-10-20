---
name: seo-search-console
description: Google Search Console analysis — quick wins, CTR gaps, cannibalization, indexing issues from real performance data. Use for 'check Search Console', 'why did traffic drop', 'what's almost ranking', 'GSC report', or any research on a site that already has traffic data. Includes a complete workflow for the task.
license: MIT
metadata:
  author: dominic-operator-pack
  version: "1.0"
  cluster: seo
  public_revision: "2026-10-06"
---

# Search Console Analysis

Requires access (or an export). No access? Output the 3-line instruction for the owner: search.google.com/search-console → verify via DNS or HTML file → add the authorized analyst as a user, OR export Performance → last 3 months → queries + pages CSVs.

## The Four Reports

1. **Quick wins (run first, highest ROI):** queries at position 4–15 with real impressions. These pages already half-rank — propose a title/H1 tune, add the query's exact phrasing to the page, internal-link to it. Deliver as a table: query, page, position, impressions, prescribed fix.
2. **CTR gaps:** queries ranking top 5 with CTR below comparable queries on this site. Generic position-based CTR benchmarks are rough heuristics; device, brand, SERP features and query intent materially change them. The title/meta is losing the click — rewrite against the SERP's actual competition.
3. **Cannibalization:** one query, multiple pages splitting impressions. Pick the winner, merge or de-optimize the loser, 301 if merging.
4. **Health:** Coverage errors on money pages, sitemap submitted/processed, Core Web Vitals failing on mobile, manual actions (rare but check).

## Cadence

New sites: check indexing weekly for the first month and confirm the sitemap is submitted. Established sites: monthly quick-wins pass. Always baseline before changes and save the Performance graph with the project report so later comparisons use the same date range and filters.

Archive each export and analysis in the user's chosen project report folder with the site, date range, filters, and date of collection. State exactly what changed on the site and when. This pairing supports before/after analysis; it does not establish causation by itself.

## Handoffs

Turn findings into proposed page edits with a priority, expected mechanism, and verification step. New content gaps can use `seo-keyword-research` if installed. For local queries, compare the website facts with the public Google Business Profile and correct inconsistencies through the owner-approved workflow.

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
