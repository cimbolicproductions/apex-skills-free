---
name: seo-longtail-keywords
description: Long-tail keyword research — question mining, 'near me' variants, voice/AI-answer phrasing, zero-volume-but-buying keywords. Use for 'long tail keywords', 'what questions do customers ask', 'easy keywords to win', or when seo-keyword-research finds page 1 too competitive. Includes a complete workflow for the task.
license: MIT
metadata:
  author: dominic-operator-pack
  version: "1.1"
  cluster: seo
  public_revision: "2026-10-06"
---

# Long-Tail Keyword Research

Long tails are where small sites win: lower competition, higher intent, and they're what people actually say to Siri/ChatGPT/Copilot.

## Mining Sources

1. **Question mining:** Google People Also Ask (recurse 2 levels deep), autocomplete A–Z suffixing ("stump grinding a…", "…b"), Reddit/Facebook group threads in the niche ("how much does X cost in [city]" posts are gold).
2. **Modifier matrix:** service × {cost, price, near me, same day, emergency, cheap, best, licensed, [brand name], [problem symptom]} × {city, suburb, zip, "in my area"}.
3. **Symptom keywords** (highest intent, least competition): customers search the PROBLEM not the service — "washer won't spin" beats "washer repair". List every symptom the business solves.
4. **Zero-volume ≠ zero-value:** tools show 0 volume for hyper-specific buying queries; if a real customer would say it, it counts. Page-1 for 30 zero-volume queries beats page-3 for one head term.

   **But zero volume PLUS zero commercial modifiers = a space that doesn't buy.** The rule above holds when a real buyer would plausibly type the phrase ("who fixes a Maytag that won't drain in Alamo Heights") — it does NOT license building against a term just because it's specific. Discriminate with an autocomplete modifier scan: collect the parent head term's real suggestions, then classify each as commercial (cost, price, buy, hire, near me), free-seeking (free, download, template, repo), or educational (how to, guide, documentation). If installed, `seo-keyword-research` step 5 supplies the full scan. In that scan, if the parent head term's suggestions contain no cost/price/buy/hire/near-me modifiers at all, the searchers are after a free repo, a template, or the docs, and every long-tail under it inherits that intent. Treat those as FAQ/top-of-funnel only. Getting this backwards is how a "high-intent zero-volume" argument becomes a rationalization for chasing traffic that never converts.
5. **AI-answer phrasing:** full natural-language questions ("who does same-day washer repair in San Antonio") — these feed FAQ schema and get quoted by AI assistants.

## Deliverable

Clustered long-tail map: cluster theme → representative long-tails → target (service page section / FAQ entry with FAQPage schema / dedicated page only if the cluster is fat). Never one thin page per long-tail — that's the 2015 doorway-page mistake.

## Handoffs

Use the clustered map to update existing page sections, plan new service pages, or draft FAQ blocks. If available, `seo-keyword-research` can incorporate it into a full keyword-to-page map. Verify visible FAQ answers and any structured data describe the same facts.

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
