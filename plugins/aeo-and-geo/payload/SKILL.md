---
name: aeo-and-geo
description: "Aeo and Geo (formerly seo-answer-engine). Audit and improve website answers for extractability by ChatGPT, Gemini, Perplexity, Copilot and AI Overviews. Use for 'get cited by ChatGPT', 'AI search', 'answer engine optimization', 'AEO', 'GEO', 'LLM SEO', 'why does ChatGPT recommend my competitor', 'show up in AI results', 'get a local business recommended by ChatGPT or Copilot', 'Bing Places for ChatGPT', or when a page ranks but earns no clicks and no mentions. Audits a page for extractability, finds what incumbents hide, rewrites so a model can lift the answer whole, and for local businesses enforces the local entity layer in order: Optimized GBP Gate (local-gbp-optimizer), then that GBP imported into Bing Places (seo-bing-places), then Bing Webmaster Tools. Includes companion listing and research workflows for local businesses. Includes a complete workflow for the task."
license: MIT
metadata:
  display_name: "Aeo and Geo"
  author: dominic-operator-pack
  version: "1.3"
  cluster: seo
  public_revision: "2026-10-06"
---

# Aeo and Geo

This workflow helps make factual website answers easier for search assistants to extract and cite. It combines page structure, transparent pricing, listing consistency and measurement. A completed audit does not guarantee citation, ranking or customer acquisition.

## Package contents and setup

Keep `scripts/`, `reference/`, `_shared/` and `related-skills/` beside this file. Run Python commands from this package directory or substitute the installed directory path. Python 3 is required; the audit script uses only its standard library.

Read `_shared/execution-standard.md` before starting. For local listing work, read `related-skills/local-gbp-optimizer/SKILL.md` and `related-skills/seo-bing-places/SKILL.md` first. Question research and performance-analysis companions are also included under `related-skills/`. These are packaged workflows, so no unpublished skill library or private account is required. Access to the target site's tools still needs the owner's authorization.

## The one principle

Publish the number a buyer can verify, explain its inclusions and exceptions, and write direct answers that stand on their own. Treat this as an extractability hypothesis to test with cold queries and real lead attribution. Evidence sources and limits are in `reference/evidence.md`.

## When NOT to run this

Stop and say so if any of these is true. Running anyway wastes the client's time.

- **There is no evidence anyone asks the target question.** Validate demand through actual customer questions, search suggestions or performance data. A zero-volume estimate alone does not rule out a useful buying question.
- **The page targets a category, not a problem.** "AI consulting San Antonio" is a category. "How much does an AI receptionist cost" is a problem. For buyers unfamiliar with the service category, research the problem they actually describe. Use `related-skills/seo-longtail-keywords/SKILL.md` first.
- **The business cannot publish a real number.** If pricing is genuinely bespoke, this skill's core lever is unavailable. Use ranges plus the disqualifier section, and set expectations lower.

---

## Stage 0: Scope

Fill this. Do not proceed with blanks.

```
TARGET PAGE:      <full URL>
TARGET QUESTION:  <the exact sentence a buyer types at 9pm, not a keyword>
MONEY QUESTION:   <the cost/price question inside it>
COMPETITORS:      <3 URLs that currently answer it>
BASELINE:         <clicks + impressions, last 90d, from GSC>
LOCAL BUSINESS:   <yes / no. yes = has a street address or service area; runs Stage 1.5>
```

**Decision rule for TARGET QUESTION:** it must be answerable in one paragraph and contain either a number, a comparison, or a yes/no. "Tell me about AI" fails. "Do I need a monthly subscription for missed call text back" passes.

---

## Stage 1: Extractability audit (mechanical)

Run the audit script. Do not eyeball this.

```bash
python scripts/audit.py <URL>
```

It reports the seven checks below. **Verify by doing:** paste the real output, never a summary of what you expect it to say.

| # | Check | Pass condition |
|---|---|---|
| 1 | Number in `<title>` | Title contains a digit that is a price, quantity or timeframe |
| 2 | Number in meta description | Same |
| 3 | Money question answered | A dollar figure or explicit range appears in the body |
| 4 | Question shaped headings | At least 3 headings phrased as a question a human would type |
| 5 | Standalone answers | Each question heading is followed by a complete answer in ≤3 sentences, with no pronoun that depends on an earlier section |
| 6 | FAQPage JSON-LD | Present, parses, and its answers match the visible ones |
| 7 | All in pricing | Every price states what is included, or names what else the buyer pays |

**Score 0 to 7.** This is an internal diagnostic rubric, not a search-engine score or a prediction of citations. Checks 5 and 7 are heuristics; check 6 detects parseable FAQ structure and still requires manually matching it to visible answers. Report the score and unresolved manual checks before touching anything.

### The extraction test (the check that actually matters)

Read the page as if you were the model. Ask:

> Can I answer the TARGET QUESTION by copying ONE sentence from this page, with no synthesis and no stitching?

If no, the page fails regardless of its score. A self-contained answer reduces the synthesis needed to understand the page. Test the hypothesis with real queries; page structure alone cannot establish visibility.

---

## Stage 1.5: Local entity layer, optimized GBP → Bing (local businesses only)

Skip when `LOCAL BUSINESS: no`. A perfect page does nothing for "which shop near me" if the engine cannot resolve the business itself. For local queries, the page is half the input; the listings are the other half.

**This stage owns the order, not the listing work.** The work lives in the included `related-skills/local-gbp-optimizer/SKILL.md` (the Optimized GBP Gate) and `related-skills/seo-bing-places/SKILL.md` (the import). Complete them in that order. If those checks were already performed during this same engagement, reference their evidence and run step 5 plus Verify; otherwise run all five steps.

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


### What is actually established (say it this way, never stronger)

| Surface | How the listing reaches it | Strength |
|---|---|---|
| Google Maps AI answers | Google discontinued the Business Profile Q&A API on 2025-11-03 while "updating the Q&A functionality". SEO press reports Maps now generates answers from the profile, reviews and website | API change official; answer sources **reported** |
| Bing Maps | Bing Places is the owner's control over the listing | Direct, official |
| Copilot | Grounded in Bing; Bing Webmaster Tools reports citations across Copilot and Bing AI summaries | Direct, official |
| ChatGPT | OpenAI says ChatGPT search sends rewritten queries to unnamed third-party search providers and uses third-party providers for nearby business listings. Practitioner testing says it reads Bing **web results**, not Bing Places fields | **Indirect, reported** |

**Pitch line:** "Bing Places fixes what Bing and Copilot say about you, and is a likely indirect input to ChatGPT. It is free, so it goes in week one." Never say "ChatGPT pulls from your Bing listing." Never quote third-party percentages about ChatGPT's Bing usage; none trace to OpenAI or Microsoft. Sources and limits: `reference/evidence.md` → *Local entity layer*.

### Steps

1. **Optimized GBP Gate first.** Run `local-gbp-optimizer` and paste its gate with every box marked. A failing box → Blocker Format naming it, and **no Bing import happens**. Stages 2 to 4 of this skill (the website) may continue meanwhile.
2. **Look at Bing before creating anything.** Search `bing.com/maps?q=<name> <city>` signed out, then the phone number. Record every field (name, address, phone, website, category, each day's hours, about text, photos, ratings shown, menu options) in a dated table beside the approved NAP block. An existing card gets **claimed**, never duplicated. "Manage business" in the card menu means a record exists; claim status is not visible from outside.
3. **Trace each Bing error to its origin.** Correct a shared error in Google first, then verify what the import carries into Bing. Correct Bing-only errors in Bing when the field does not synchronize. Record what actually happened rather than assuming imports overwrite every field.
4. **Import the gated GBP into Bing** by running `seo-bing-places`: the owner claims or imports with sync on (three-line instruction; the agent never creates the account, signs in, or verifies for them), then post-import fixes. From here, shared fields are edited in GBP, not Bing.
5. **Site side.** Verify the domain in Bing Webmaster Tools (it imports a verified Search Console property), submit the sitemap, confirm Bingbot is not blocked in robots, and open **AI Performance** for the Copilot citation baseline. Webmaster Tools access and listing ownership are separate permissions.

**One set of facts.** The Stage 3 answers, the GBP services list and description, and the Bing description must state the same prices, hours and policies. A mismatch between them is exactly the number a model has to correct.

### Verify (by doing)

Re-open the signed-out Google profile and Bing Maps card and assert each field from the rendered text, not from either dashboard. Search the phone number and the street address separately on Bing: exactly one card must come back. Then run the Stage 5 cold query in **ChatGPT, Copilot and Google AI Mode** and record all three.

---

## Stage 2: The incumbent gap

Look for useful facts competitors omit or leave unclear. Transparent answers can differentiate a smaller business; domain authority and other retrieval signals still matter.

For each competitor, record:

```
COMPETITOR:        <name / URL>
HEADLINE NUMBER:   <what they advertise, or "none published">
REAL TOTAL:        <what a buyer actually pays, incl. fees, minimums, setup>
THE GAP:           <the difference, and where it is disclosed, if anywhere>
WHAT THEY HIDE:    <the specific fact they will not put on the page>
```

**Never invent a competitor's fee.** If the real total is not published, write `not disclosed` and say so. `not disclosed` is itself the finding, and it is usually the strongest one.

Two useful gap types:

- **Hidden fees:** compare the advertised number with the documented total, including required fees and minimums. Publish the owner's verified all-in figure and terms.
- **Missing answers:** record an important buyer question a competitor does not answer. Do not infer motive or invent the absent figure; label it `not disclosed`.

---

## Stage 3: The rewrite

Apply the five checks below, using owner-confirmed facts.

### 3.1 Title tag: carry the number

Suggested format:

```
<What it is> <Where> | <Number>, <Objection killer>
```

Fill the format with the actual service, location and verified price. An objection-killer claim must be true for the stated offer.

The objection killer is the one thing that stops the sale. "No Credit Check" and "No Monthly Fee" occupy the same slot. Mirror the number into `og:title` and `twitter:title`.

**Working limit:** aim for 60 characters or fewer; search engines can still rewrite or truncate titles based on display width.

### 3.2 The answer block

For the money question, verbatim shape:

```markdown
### <The question, phrased exactly as a human types it>

<Direct answer with the number, in ONE sentence.> <What is included, enumerated.>
<What else the buyer pays, if anything.>
```

Verify that the direct answer and its inclusions are complete without relying on earlier paragraphs.

### 3.3 The comparison table

One row per real option, including the ones cheaper than the client. Columns: **Option / Typical price / What you are actually paying for.**

The third column is where the gap gets stated plainly. This gives a reader enough context to compare the offers without mistaking a headline price for the total.

Every researched number needs a source and a date. Write the actual verification date and source URL, and recheck current pricing before publishing. Undated pricing can go stale silently.

### 3.4 The disqualifier

A section naming who should NOT buy. Three reasons, specific, with thresholds.

Use owner-confirmed limitations: an existing alternative already solves the need, the service does not include required support, or a measured usage threshold makes the offer poor value. Do not invent a numeric threshold. Honest exclusions help buyers assess fit; citation effects must be measured.

### 3.5 Mirror into JSON-LD

Every question block goes into `FAQPage` JSON-LD with the answer text **matching the visible copy**. Mismatched schema and visible copy is a trust signal problem, not a shortcut.

---

## Stage 4: Verify (by doing)

```bash
# Build and preview the production output using this site's actual commands.
# Substitute its preview URL, or pass a rendered HTML file directly.
python scripts/audit.py http://127.0.0.1:<port>/<path>/
```

Then, after deploy, **probe the live domain, never the build state**:

```bash
curl -s -L https://<domain>/<path>/ | grep -oE '<title>[^<]*</title>'
curl -s -L https://<domain>/<path>/ | grep -c '"@type": "Question"'
```

Assert rendered state, not properties. `el.hidden` reads true on an element that any author `display:` rule has made visible. Use `getComputedStyle(el).display` and `offsetParent !== null`.

Confirm no horizontal page overflow at 390px, with wide tables scrolling inside their own `overflow-x:auto` container.

---

## Stage 5: Instrument and measure

Measure whether this work earns correct citations and qualified inquiries for the target business. Establish an auditable baseline and keep citations, referrer visits and customers as separate measures. Sources and limitations are in `reference/evidence.md`.

Set all three up at handoff:

1. **A "how did you find us" field on the lead form.** Free text beats a dropdown, because "ChatGPT told me about you" is the answer you want captured in the customer's own words. Treat it as first-party self-reported attribution and compare it with other evidence.
2. **Referrers and citations.** Track `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com` in analytics. For local businesses, also read Bing Webmaster Tools AI Performance monthly (citations, not customers). Undercounts badly, since many people read the answer and then type the business name directly, so treat it as a floor and never as the total.
3. **Cold query test, monthly.** Run the target question in a **logged out or temporary chat** in both engines. Record which cited, at what position, and whether the number was extracted correctly. Logged out matters: a session that knows the user owns the site may be personalizing the answer.

**Watch for the drift failure.** A published price that no longer matches the real charge can mislead customers and search assistants. **Any price change means the page changes the same day.** Put that in the handoff in writing.

Use a paid citation-tracking tool only when the owner already has access and wants it. The workflow also works with dated manual query samples, analytics and first-party lead attribution.

---

## Completion checklist

Check each box by performing it. Paste this filled into the final output.

```
[ ] Stage 0 scope block filled, no blanks
[ ] Baseline clicks/impressions recorded from GSC
[ ] audit.py run on the BEFORE state, real output pasted, score recorded
[ ] Extraction test answered explicitly (yes/no + which sentence)
[ ] LOCAL ONLY (else mark n/a): Optimized GBP Gate (local-gbp-optimizer) pasted, every box marked, BEFORE any Bing import
[ ] LOCAL ONLY: signed-out Bing Maps card recorded field by field with date
[ ] LOCAL ONLY: each wrong Bing field traced to Google or Bing-only; Bing imported from the gated GBP, sync on
[ ] LOCAL ONLY: existing card claimed, not duplicated (phone and address searches each return one card)
[ ] LOCAL ONLY: site verified in Bing Webmaster Tools, sitemap submitted, AI Performance baseline saved
[ ] Gap table filled for 3 competitors, unpublished values marked "not disclosed"
[ ] Title carries a verified number, aims for <= 60 chars, mirrored to og: and twitter:
[ ] Money question answered in one sentence with inclusions enumerated
[ ] Comparison table includes cheaper options when verified options exist; otherwise absence is stated
[ ] Disqualifier section names 3 specific reasons with thresholds
[ ] Every published number carries a source and a date
[ ] FAQPage JSON-LD parses and matches visible copy
[ ] audit.py re-run on the AFTER state, score and manual checks recorded, output pasted
[ ] Live domain probed after deploy (not build state)
[ ] No horizontal overflow at 390px
[ ] "How did you find us" field live on the lead form
[ ] AI referrers tracked in analytics
[ ] Cold logged-out query test run and recorded (Copilot included for local businesses)
[ ] Price-drift rule handed over in writing (price changes = same-day page update)
```

One unchecked box means NOT DONE. Say so instead of shipping.

## Output format

```
DONE: aeo-and-geo
Page: <URL>
Score: <before>/7 -> <after>/7
Files written/updated: <full paths>
Checklist: <pasted, all boxes marked>
Assumptions made: <numbered>
Needs owner: <list, or "nothing">
```

Blocked instead? Use the Blocker Format from `_shared/execution-standard.md`.
