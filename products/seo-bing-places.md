---
name: seo-bing-places
description: Set up and optimize Bing Places for Business listings by importing an OPTIMIZED Google Business Profile. Use for 'Bing Places', 'get found on Bing', 'Copilot local results', 'import GBP to Bing', or when auditing a local listing. Requires the Optimized GBP Gate (local-gbp-optimizer) before import. Includes a complete workflow for the task.
license: MIT
metadata:
  author: dominic-operator-pack
  version: "1.1"
  cluster: seo
  public_revision: "2026-10-06"
---

# Bing Places

Why it matters (client pitch line, never strengthen it): Bing Places directly controls the Bing Maps listing and gives Copilot and Windows search correct facts. For ChatGPT it is a likely **indirect** input: OpenAI says ChatGPT search uses outside search providers without naming them, and practitioner testing says ChatGPT reads Bing's web results rather than Bing Places fields. Few local competitors claim their card, so a complete one stands out. Sources: [Microsoft listing guidance](https://support.microsoft.com/en-us/bing/add-and-manage-your-business-listing), [OpenAI ChatGPT search documentation](https://help.openai.com/en/articles/9237897-chatgpt-search), and [Bing AI Performance announcement](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview). The AI-search relationship is indirect; do not promise placement or citations. Recheck current documentation before implementation.

## Gate before import

**Do not import until the Optimized GBP Gate below passes, with every box marked.** If `local-gbp-optimizer` is installed, run its full audit first. Import copies Google's errors into Bing, and sync restores them after you fix Bing by hand. A failing gate box stops this skill with the Blocker Format; fix it in Google first.

No Google Business Profile exists at all → skip the import and build the listing manually from the Canonical Business Facts block below.


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

## Optimized GBP Gate


The gate defines the checks to complete before importing a profile into Bing Places. Check each box against the **signed-out public profile** where the field is public, never against what the dashboard says was saved.

```
[ ] Profile verified by the owner; the authorized operator has required access (or the exact missing access is recorded)
[ ] Name, address, phone character-identical to the Canonical Business Facts block above; no keywords added to the name
[ ] Primary category = highest buyer intent that matches the real business; secondaries are real services only
[ ] Website button opens the canonical page: no #anchor, no redirect chain, no dead route
[ ] Appointment / booking link opens a working form on a phone (or the field is empty on purpose)
[ ] Regular hours match owner-confirmed hours for every day; special hours set for the next holiday
[ ] Services list complete, each with a description; prices only where the owner confirmed them
[ ] Description <= 750 characters, service + city stated naturally, no URLs or keyword lists
[ ] At least 6 real photos (exterior, interior, team, work); owner supplied or permission confirmed
[ ] Review link copied from the profile and opened successfully
```

**Why the gate exists:** Bing's import can copy errors from Google, and later synchronization may restore them after a manual Bing fix. Check and correct the source profile before importing.

**On a failing box:** if the fix needs the owner (verification, access, hours, photos), stop downstream imports and use the Blocker Format below, naming the failing box. Work that does not read from GBP (citations, on-site schema, website answers) may continue.


## Setup Flow

0. **Look first.** Signed out, search `bing.com/maps` for name + city, then for the phone number. Record the card field by field with the date. An existing card gets **claimed**, never duplicated. "Manage business" in the card menu means a record exists.
1. **Import from the gated GBP** — bingplaces.com → Import from Google Business Profile, signed in with the Google account that manages the profile. Leave sync on, so Google stays the source of truth: from now on, fix shared fields in GBP, not in Bing.
2. **Post-import fixes** (import always misses things): NAP matches the canonical block exactly; category mapping (Bing's taxonomy differs, pick the closest high-intent primary); re-upload photos that dropped; service area for service-area businesses.
3. **Verification:** phone, email or postcard, owner action. Hand the client a 3-line instruction. A verified GBP sometimes carries verification over, not always.
4. **Optimize:** description with service + city stated naturally (no keyword stuffing; Bing weights exact business info and citations), every day's hours including holiday hours, website = canonical page with no #anchor, appointment URL.
5. **Website follow-through.** Verify the domain in Bing Webmaster Tools, submit its sitemap, check robots rules permit Bingbot, and record the AI Performance baseline if available. Draft direct, independently understandable website answers with owner-confirmed prices and terms. If installed, `aeo-and-geo` supplies a full page-audit workflow. Listing ownership and Webmaster Tools access are separate permissions.

## Checklist

- [ ] Optimized GBP Gate pasted with every box marked BEFORE import (or: no GBP exists, built from canonical NAP)
- [ ] Existing card checked signed out by name + city AND by phone; claimed, not duplicated
- [ ] GBP import completed, sync on
- [ ] NAP character-identical to canonical block
- [ ] Website field = canonical page, no #anchor
- [ ] Primary category = highest buyer intent available
- [ ] ≥6 photos (exterior, work examples, team)
- [ ] Verified (or client instruction sent)
- [ ] Signed-out card re-read field by field after changes; Copilot query run ("[service] near [city]")
- [ ] Website answer audit run or queued; Bing Webmaster Tools access, sitemap and AI Performance baseline recorded

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
