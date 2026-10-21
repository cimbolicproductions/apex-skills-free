# Evidence and limits

This public reference retains research sources from the original workflow. It omits private customer records, owner-reported revenue and lead counts, named client audits, account details and local working files. Source research dates were August 30 through September 16, 2026; this package does not claim those pages were reverified at publication. Recheck current official documentation before making platform-specific changes.

## What the workflow tests

The practical hypothesis is that direct, accurate, self-contained answers with clear pricing and consistent business facts are easier for search assistants and people to extract. The audit rubric checks structure; it does not measure rankings, citation probability or conversion.

The original observations were limited to a local transactional vertical and one metro. They were not a randomized experiment, did not isolate individual page changes, and included possible session personalization. No causal or general ranking claim follows. Cold queries and first-party attribution are required to assess a new deployment.

## Local entity layer

| Claim | Source and limit |
|---|---|
| A business can claim and update a Bing business listing | [Microsoft Support](https://support.microsoft.com/en-us/bing/add-and-manage-your-business-listing), official listing guidance |
| Bing Webmaster Tools introduced AI Performance reporting for citations across Copilot and Bing AI summaries | [Bing Webmaster Blog, February 2026](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview), official public-preview announcement; availability can change |
| ChatGPT search uses outside search providers and local-information providers | [OpenAI Help: ChatGPT search](https://help.openai.com/en/articles/9237897-chatgpt-search), official; provider relationships and behavior can change |
| The My Business Q&A API was discontinued | [Google developer changelog](https://developers.google.com/my-business/content/qanda/change-log), official; an API discontinuation does not by itself prove every public-interface change |
| ChatGPT local search can use web results rather than Bing Places profile fields | [Search Engine Land, May 2025](https://searchengineland.com/how-does-chatgpt-conduct-local-searches-454894), practitioner reporting, partly based on model self-description; treat as a hypothesis |
| Public GBP Q&A was reported replaced by generated answers | [Accrisoft, January 2026](https://www.accrisoft.com/blog/2026/01/28/main/google-removes-business-profile-q-a-what-it-means-and-what-to-do-now/), secondary reporting; confirm the current public interface before acting |

Bing Places is a direct control for Bing listing facts. Its relationship to ChatGPT recommendations is indirect and incompletely documented. Do not promise that claiming a listing produces a ChatGPT recommendation, or quote unsourced percentages for Bing's share of AI searches.

## Measurement requirements

- Record a dated baseline before edits.
- Use logged-out or temporary chats with the same questions and record the cited URLs and extracted facts. Results vary with time, location and personalization.
- Separate citations and impressions from visitors and customers. Referrer data can miss people who read an answer and later search for the business directly.
- Pair analytics with a first-party “how did you find us” question; report owner recollection separately from instrumented evidence.
- Keep prices, hours, inclusions and policies current across the website and listings.

## Audit-script limits

The script uses lightweight HTML pattern matching. It may miss client-rendered text, unusual markup, international price formats or structured-data variants. Checks 5 and 7 are heuristics. Check 6 detects parseable FAQ structure but does not compare its answer text with the visible page. Human review must confirm self-contained answers, every price's inclusions and visible/schema parity. A score below five flags work to investigate; it does not establish that a page is uncitable.
