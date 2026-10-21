---
name: seo-keyword-fix
description: "Runs a staged SEO pipeline on a website: site audit, keyword research from free sources, topic clusters with pillar pages, and an exact on-page plan for each URL, with an optional apply mode that edits the code and opens a pull request. Use when the user wants an SEO audit, keyword research, a content cluster plan or on-page SEO fixes. Start in plan-only mode."
license: LicenseRef-Apex-Personal-Commercial-1.0
---

# SKILL: SEO Keyword Research & Implementation Pipeline

**Description:** A multi-agent SEO orchestrator that audits a site, builds a complete keyword universe from real search data (Google Autocomplete, Wikipedia entity graph, competitor SERPs), clusters topics into pillar pages with supporting articles, and ships the on-page changes directly to GitHub as a PR — all using free tools.

**Target Customer:** Technical SEOs, full-stack developers, indie hackers, marketing agencies.
**Price Point Strategy:** $59 (premium tier — most complex workflow in the catalog)

---

## What Makes This Different

Most "SEO prompts" sold online give you a generic keyword brainstorm. This is a real production pipeline:

- **Stage 1 (parallel):** Site audit + keyword universe builder + SERP intent analysis — three agents work simultaneously
- **Stage 2:** Topic clusterer maps keywords to pillar pages plus supporting cluster pages with explicit internal-linking architecture
- **Stage 3:** On-page recipe generator outputs the exact title, meta, H1, H2 outline, schema, and internal links for every URL
- **Stage 4:** Code implementer detects your framework (Next.js, Astro, Hugo, SvelteKit, static HTML) and applies the changes idiomatically, then opens a PR

Uses **only free tools**: Google Autocomplete, PageSpeed Insights, Wikipedia, Google Search Console (if you own the site), Firecrawl free tier. No paid SEO suites required.

---

## Instructions for the AI (The "Brain" you are selling)

`<instructions>`
You are the orchestrator for a complete keyword research and SEO implementation pipeline. The user has invoked you to audit a site, research keywords, build a content/keyword strategy, and apply on-page SEO fixes to the code.

**Step 1 — Intake (ask once, then run).** Confirm:
1. Target URL or local project path (e.g., `https://example.com` or `./apps/marketing-site`)
2. Primary business / niche / topic (1 sentence)
3. Geo target (e.g., `US`, `San Antonio TX`, `global`)
4. Top 2-3 competitor domains (optional — you can discover them)
5. Implementation mode: `plan-only` (write recommendations) or `apply` (modify code + open PR)

**Step 2 — Stage 1: Audit + Research + Intent (run mentally in parallel).**
- **Site audit:** Crawl the site. Extract current title/meta/H1/H2/canonical/schema for every URL. Measure Core Web Vitals via PageSpeed Insights. Check robots.txt and sitemap.xml. Flag technical SEO issues.
- **Keyword universe:** Start from seed keywords. Expand via Google Autocomplete (alphabet-soup expansion). Pull entities from Wikipedia. Mine competitor pages. Score each keyword for opportunity. Label with intent and difficulty estimate.
- **SERP intent:** For the top 30-50 keywords, classify dominant intent (informational/navigational/commercial/transactional), SERP features present (PAA, featured snippet, video, local pack, AI Overview), and dominant content format (listicle, guide, product page, comparison, definition).

**Step 3 — Stage 2: Topic clustering.** Build pillar pages plus supporting cluster pages. Each cluster maps to one dominant intent + content format. Specify explicit internal-linking architecture (which pages link to which, with what anchor text).

**Step 4 — Stage 3: On-page plan.** For each URL in the cluster plan, produce a precise recipe:
- Title tag (with one-line rationale)
- Meta description
- H1
- H2 outline
- Internal links to add (anchor text + destination URL)
- JSON-LD schema block (Article, Product, LocalBusiness, FAQ, etc.)
- Image alt rules
- URL slug

**Step 5 — Stage 4: Implementation (only if mode=apply).** Detect the framework (Next.js, Astro, Hugo, SvelteKit, plain HTML). Apply the changes idiomatically. Update sitemap/robots. Verify the build still passes. Open a PR with a clean changelog of what changed and why.

**Constraints:**
- Use only free data sources. When exact search volume or KD isn't available, say so — never fabricate numbers.
- Plan-then-apply: code changes only happen when the user explicitly says `apply` or `--apply`.
- Code changes are scoped to metadata, schema, sitemap, and internal links. Body content rewrites require explicit sign-off.
- Output intermediate artifacts as separate markdown sections so the user can review each stage before the next runs.
- For sites the user does not own (competitor analysis), do not attempt to access Search Console — fall back to public SERP and autocomplete data.
`</instructions>`

---

## How to use this skill

**Option A — Claude Code skill (recommended, runs the full pipeline):**
1. Save this `.md` file as `SKILL.md` and place it in `~/.claude/skills/keyword-fix/` (or `~/.gemini/skills/keyword-fix/` for Gemini CLI).
2. (Optional) Install the free GSC MCP for real Search Console data: `claude mcp add gsc -- npx -y suganthan-gsc-mcp`.
3. (Optional) Install Firecrawl MCP for better page extraction: `claude mcp add firecrawl -e FIRECRAWL_API_KEY=<key> -- npx -y firecrawl-mcp` (500 free credits/month).
4. Type `/keyword-fix https://yoursite.com` in Claude Code, or naturally ask "run keyword research on my site".

**Option B — Any LLM (Claude.ai, Gemini, ChatGPT):**
1. Open a new chat. Paste the entire `<instructions>` block above as the system prompt.
2. Say: "Audit and run keyword research on `https://yoursite.com` — niche is `[your niche]`, geo is `[your geo]`, mode is plan-only."
3. Let it walk you through each stage. Review the output of each stage before moving to the next.

---

## Suggested first run

For maximum value on your first execution:
- Pick a single, well-defined niche (e.g., "appliance rental in Phoenix, AZ" rather than "general home services")
- Start in `plan-only` mode. You'll get a full audit, keyword universe, cluster plan, and on-page recipes you can implement manually before trusting the apply mode.
- After reviewing the plan, run `--apply` on one pillar page only as a smoke test before letting it touch the whole site.

---

*A production-tested keyword research and on-page SEO pipeline. Built for operators who want real strategy, not regurgitated prompts.*
