---
name: seo-keyword-research
description: General keyword research — seed generation, competitor keyword extraction, intent mapping, and a keyword→page map for any site or niche. Use for 'keyword research', 'what keywords should this site target', 'keyword map', or as the pre-build research pass for any new site. Includes a complete workflow for the task.
license: MIT
metadata:
  author: dominic-operator-pack
  version: "1.1"
  cluster: seo
  public_revision: "2026-10-06"
---

# Keyword Research

No paid tools assumed. Web search + SERP reading + free sources (Google autocomplete, People Also Ask, Keyword Planner if available, competitor pages).

## Process

1. **Seeds:** services/products × locations × modifiers (repair, cost, near me, emergency, best, [brand]). For local: every service the business actually offers (from an owner-confirmed service inventory) × city + 2–3 suburb names.
2. **Competitor extraction:** pull the top 3 ranking competitors' page titles, H1s, and service page slugs — their page set IS their keyword map. Note what they rank for that the client can't credibly claim, and gaps they've missed.
3. **Intent mapping:** tag each keyword — `emergency` (call now), `transactional` (quote/buy), `comparison` (best/vs/cost), `informational` (how/why). Emergency + transactional get pages; informational gets FAQ entries or blog posts, never a service page.
4. **Difficulty proxy without tools:** scan page 1. Older or incomplete competing pages can indicate an opportunity; national brands and strong content may require a narrower question. Neither is a ranking guarantee. Expand long-tail variants using service × problem × location; `seo-longtail-keywords` provides a companion workflow if installed.
5. **Autocomplete intent gate (GO/NO-GO — run before writing the map):** for each head term, pull the raw suggestion list and read the MODIFIER DISTRIBUTION, not just the phrases:

   ```bash
   curl -s "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=<seed>" \
     | python -c "import sys,json;[print(' -',s) for s in json.load(sys.stdin)[1]]"
   ```

   Autocomplete supplies observed phrasing, not a complete or unbiased demand estimate. Use its modifier distribution as a practical intent signal and compare it with real customer language and available performance data. Classify every suggestion:
   - **Commercial** — cost, price, buy, best, near me, hire, service, quote, `[brand]`
   - **Free-seeking** — github, repo, free, open source, download, template, examples
   - **Educational** — how to, what is, guide, documentation, tutorial, specification, vs

   **The gate:** if a head term returns ZERO commercial modifiers across its suggestions, do not assume purchase intent from volume alone. Verify buying demand with customer or conversion evidence before choosing commercial pages. Ranking there delivers people who came for a free repo or the docs. Either find a different corpus where the buyer actually searches, or accept the term as top-of-funnel only (guide/FAQ, never a money page). Record the classification counts in the map so the decision is auditable later.

6. **The map (deliverable):**

| Keyword | Intent | Target page | H1? | Priority |
|---|---|---|---|---|

One primary keyword per page. A page per keyword CLUSTER, not per keyword variant. The map decides site structure — pages, H1s, titles — before any copy is written.

## Handoffs

Expand natural-language questions into clusters and map them to existing pages or a proposed page set. If installed, `seo-longtail-keywords` supplies expansion and `seo-search-console` supplies performance analysis. Apply an approved map through the site's normal editing and verification workflow.

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
