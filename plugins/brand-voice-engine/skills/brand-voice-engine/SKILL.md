---
name: brand-voice-engine
description: "Generate a complete brand voice and content engine for your business in one Claude session. Use when the buyer says 'build my brand voice', 'I need a content engine', 'set up my newsletter and blog voice', 'configure brand for my company', '/brand-voice-engine', or any request for brand identity + content workflow setup. Walks the buyer through a 15-question brand interview, researches their niche with whatever research tools the agent has, applies proven copywriting and writing methods (Halbert, Sugarman, Ogilvy, Parr, Handley, King, Graham, Ravikant and Kennedy) to their brand parameters, then generates a personalized brand voice document plus three companion content skills (newsletter, blog and tweet pipelines)."
license: MIT
metadata:
  author: Apex Skills
  version: '1.0'
  source: https://apexskills.dev
  category: brand + content engine
---

# Brand Voice Engine

> A production-grade content engine for your brand, built in 30-45 minutes of interactive conversation.

## What This Skill Produces

When this skill finishes, you'll have **four files** installed in your Claude skills folder, ready to use forever:

1. **`{your-brand}-voice.md`** — A 13-section canonical brand voice document, personalized to YOUR brand, audience, channels, and goals. Synthesized from 9 legendary copywriting + founder-voice sources.
2. **`{your-brand}-newsletter/SKILL.md`** — Interactive newsletter pipeline. Researches a topic, asks for your take, drafts in your voice, runs Slop Killer + Jobs critique, saves the draft.
3. **`{your-brand}-blog/SKILL.md`** — Interactive blog post pipeline. Same flow, blog-length, blog-tuned voice.
4. **`{your-brand}-tweet/SKILL.md`** — Tweet/thread pipeline. Generates variants in your voice, picks one, refines, saves.

All three content skills read the brand voice document as their single source of truth — when your voice evolves, you edit one file and all three skills auto-update.

## Who This Is For

- **Founders + operators** at any stage who write outbound content (newsletter, blog, social) and want it to sound like them, not like a generic AI marketing voice
- **Solo creators** who don't have time to read 9 copywriting books but want the synthesis baked into their workflow
- **Agencies and consultants** building a content engine for a client (run the skill once per client)

## What This Is NOT

- A landing-page copy generator (use AIDA frameworks directly for that)
- A social media scheduling tool (use Buffer/Hypefury for posting; this is for the writing)
- A SEO-keyword-optimization pipeline (this is brand voice; SEO is a different goal)
- A logo or visual brand kit generator (this is the verbal brand voice only)

## Required Tools / Fallbacks

This skill works with **any AI agent that can read files, write files, and search the web** — Claude Code, Codex (OpenAI), Gemini CLI, Antigravity, Cursor, Windsurf, etc.

| Capability | Preferred | Fallback |
|---|---|---|
| Web research | `mcp__perplexity__*` tools | `WebSearch` + `WebFetch` (Claude Code) / `--web-search` (Codex) / native search (Gemini, Antigravity) |
| File ops | Native | All agents have these |
| Interactive chat | Native | All agents have these |

If the agent has no web research at all, the buyer can paste research findings inline — Stage 2 has a fallback path for that.

## Pipeline — 8 Stages

Run **sequentially**. Pause at every ❓ for the buyer's input before moving on. Do not batch — confirm at each gate.

---

### Stage 1: Identity Intake ❓

Ask the buyer in one message:

1. **Brand name** (the name on the website / business cards)
2. **One-sentence elevator pitch** — what does this brand do, for whom?
3. **Industry / vertical** — be specific (e.g., "B2B SaaS for accountants" beats "software")
4. **Founder or team voice?** — singular "I/me" voice, or plural "we/our" voice?
5. **Slug** — short kebab-case identifier for file naming (e.g., "acme", "stagein", "podcast-authority"). Derive from brand name if buyer doesn't specify.

Wait for response before Stage 2.

---

### Stage 2: Audience + Tone Calibration ❓

Ask in one message:

1. **Single-archetype audience** — describe ONE imagined reader. Job title, stage of company, what they struggle with, what they read. (Example: "solo SaaS founder at $5-50k MRR, uses ChatGPT daily, follows Sahil Bloom and Jason Cohen on X.")
2. **Three brands whose voice you admire** — name them. (Example: "Stripe, Linear, Sam Parr's Hustle newsletter.")
3. **Three brands whose voice you hate** — name them. (Example: "every Salesforce email, LinkedIn thought-leader posts, anything with 'unleash potential'.")
4. **Tone axis** — pick a side for each:
   - Formal ↔ Casual (default: casual)
   - Direct ↔ Diplomatic (default: direct)
   - Irreverent ↔ Respectful (default: middle)
   - Playful ↔ Serious (default: middle)
   - Plain ↔ Poetic (default: plain)
5. **One sentence that captures the brand's vibe** (optional but useful) — what's the one-liner you'd want a customer to remember?

Wait for response.

---

### Stage 3: Channel + Content Strategy ❓

Ask in one message:

1. **Which channels?** — Newsletter, blog, X/Twitter, LinkedIn, all? (We'll build skills for the ones picked.)
2. **Cadence** — for each picked channel: weekly / monthly / ad-hoc / experimental?
3. **Goals per channel** — pick ONE primary goal per channel:
   - Pure broadcast (brand presence)
   - Drive replies / community
   - Drive clicks to sales pages
   - Build authority for fundraising / hiring / partnerships
   - Educate to convert
4. **Three topics you'll cover** — and three you'll **never** cover.
5. **One specific CTA** — what's the action you most want readers to take? (Examples: "book a demo", "reply with their stack", "buy the $99 starter pack".)

Wait for response.

---

### Stage 4: Niche Research

Now research the buyer's niche to understand what's working and what's slop. Use **whichever tool the agent has available**, in this order of preference:

#### Preferred: Perplexity MCP

If `mcp__perplexity__*` tools are available, run **3 parallel queries**:

1. *"Best newsletters / blogs / X accounts in [their industry] in 2025-2026 — by founder voice, not corporate marketing."*
2. *"Common writing slop patterns / AI-generated tone in [their industry] content — what are operators complaining about?"*
3. *"Recent trends and tools in [their industry] last 60-90 days — what's everyone talking about that signals they're paying attention?"*

#### Fallback A: WebSearch + WebFetch

If Perplexity isn't connected, use the agent's built-in web tools:
- `WebSearch` for "best [industry] newsletters", "[industry] founders to follow on X", "[industry] AI tools 2026"
- `WebFetch` 2-3 of the top results for actual content samples

Same goal: identify 3-5 voices the buyer's brand is in dialogue with.

#### Fallback B: Codex / Gemini / Antigravity native research

If running in OpenAI Codex (`codex --web-search`), Google Gemini CLI, or Antigravity — those have native web search. Use it the same way.

#### Fallback C: Buyer provides

If no research tool is available at all, **ask the buyer**:

> *"I don't have web research available. Paste 1-2 sample paragraphs from a brand you admire in your space, plus 1 sample paragraph of slop you want to avoid. I'll calibrate from those."*

#### Synthesize

Return a 5-7 bullet brief to the buyer:

- 3 voices in their space that match the tone they want
- 2-3 specific tactics those voices use (hooks, sentence rhythm, CTA patterns)
- 2-3 anti-patterns common in their niche to avoid

Wait for buyer's reaction. Ask: **"Anything here surprise you? Anything you'd push back on?"**

---

### Stage 5: Apply the 9-Source Synthesis

You now have:
- The buyer's brand identity (Stage 1)
- Their audience + tone (Stage 2)
- Their channels + goals (Stage 3)
- Niche research (Stage 4)

Apply the synthesized methodology from these 9 sources to the buyer's brand:

| Source | What they bring |
|---|---|
| **Gary Halbert** — *The Boron Letters* | AIDA structure (Attention/Interest/Desire/Action), market-first thinking, copywork discipline |
| **Joseph Sugarman** — *Adweek Copywriting Handbook* | The slippery slide ("first sentence's job is to make you read the second"), sell concept not product, sell on emotion + justify with logic |
| **David Ogilvy** — *Confessions of an Advertising Man* | Brand image as long-term investment, headline obsession, must-sell-not-entertain |
| **Sam Parr** — *The Hustle / My First Million* | Write like you talk, think in headlines, 6th-grade reading level, AIDA as structure, copywork practice |
| **Ann Handley** — *Everybody Writes / Total Annarchy* | Quality > quantity, reader-centric content, Logo-Off Test (strip the brand — is it still recognizably yours?) |
| **Stephen King** — *On Writing* | "2nd Draft = 1st Draft − 10%" puffiness rule |
| **Paul Graham** — *Good Writing* essay | Reread 50-100 times, the writer is the first reader |
| **Naval Ravikant** — *Almanack* | Terse declarative philosophy, mechanism over jargon |
| **Dan Kennedy** — *No B.S. Direct Marketing* | One ask per email, measurable response, no fluff |

The synthesis is **NOT** a quote-collection. It's an operating system. Apply it as below.

---

### Stage 6: Generate the Brand Voice Document

Create `{slug}-voice.md` in the buyer's project root (or wherever they prefer — ask if unclear). Structure: **13 sections**, every one populated with the BUYER's specifics (not generic placeholders).

```markdown
# {Brand Name} — Brand Voice Reference

> Single source of truth for {Brand Name}'s written voice across all channels.
> Synthesized for {Brand Name} from Halbert, Sugarman, Ogilvy, Parr, Handley, King, Graham, Naval, Kennedy.

## 1. Voice DNA (one-paragraph definition)
[Write a paragraph that captures THIS brand's voice based on Stages 1-3. Include the tone axis decisions, the founder-or-team voice, and a 3-word mantra in Sam Parr style.]

## 2. The North Star — Handley's Logo-Off Test
[Customize: tell THIS brand what "their" Logo-Off Test sounds like. Compare to the 3 admired brands they named.]

## 3. Subject Lines / Headlines / Hook First Lines — The N-Character War
[Whatever the brand's primary channel is, the headline/hook is the highest-leverage line. Give 5 archetype patterns specific to the brand's audience + topic mix:
- The Specific Claim
- The Contrarian Take
- The Curiosity Gap
- The Mistake
- The Cut
For each, give an EXAMPLE specific to the buyer's vertical.]

## 4. The Opening — Sugarman's Slippery Slide
[Adapt Sugarman's rule to THIS brand's content. Show 5 opener patterns with brand-specific examples.]

## 5. The Body — Halbert's AIDA, Brand-Tuned
[Map AIDA to the brand's primary content format. Include mechanism-over-summary rule and specifics calibration (named tools, named amounts, etc. — tailored to the brand's domain).]

## 6. The Cut-to-the-Chase Word List
[Standard filler/marketing-slop/hedging/engagement-bait list + ADD industry-specific slop the brand should avoid based on the Stage 4 research.]

## 7. Hooks — Working Taxonomy
[6 mid-body hook patterns with brand-specific examples.]

## 8. The CTA — One. Soft. Specific.
[Tie to the buyer's CTA from Stage 3. Give 3 working CTA templates and 3 that die for this brand.]

## 9. The Close — Sign-Off
[Default closing based on tone axis. If casual+direct, "— {Name}" works. If formal, something else.]

## 10. Practice — Halbert's Copywork
[Recommend specific brands the buyer should swipe-file based on Stage 4 research. Name 3.]

## 11. The Audience (re-state every time)
[Restate the single-archetype audience from Stage 2 in 2-3 sentences. This goes in every draft session.]

## 12. The Final Checks
[10-point checklist tailored to brand. Same structure as Apex's brand voice doc.]

## 12.5 Channel-Specific Tactics
[Only include sections for the channels the buyer picked in Stage 3:
- If Newsletter → email/subject-line section
- If Blog → long-form structure section
- If Twitter/X → 280-char game section
- If LinkedIn → LinkedIn-specific section]

## 13. Sources
[Same 9 sources, with one-line "what they brought to this voice".]
```

After writing the file, show the buyer the path + a preview of Section 1 + Section 3. Ask: **"Read it through. Anything off?"** Wait for response. Apply edits.

---

### Stage 7: Generate the Channel Skills

For each channel the buyer picked in Stage 3, generate a `SKILL.md` file in the appropriate folder. Default install location:

```
~/.claude/skills/{slug}-newsletter/SKILL.md
~/.claude/skills/{slug}-blog/SKILL.md
~/.claude/skills/{slug}-tweet/SKILL.md
```

If the buyer is on Windows, use `C:\Users\<user>\.claude\skills\...` paths. On Mac/Linux, `~/.claude/skills/...`.

Each generated SKILL.md should:

1. Have a frontmatter `name`, `description`, `metadata.brand_voice_reference` (pointing to the brand voice doc from Stage 6)
2. Have an 8-stage pipeline (topic intake → optional research → variant generation → user picks → refine → slop pass → save draft → optional publish)
3. **Read the brand voice doc end-to-end before drafting** — same single-source-of-truth pattern Apex uses
4. Use the Halbert AIDA structure adapted to the channel
5. Save drafts to a sensible location (default: `~/Documents/{Brand}/content/{newsletter|blog|tweets}/`)

#### Template for newsletter SKILL.md

```markdown
---
name: {slug}-newsletter
description: "Interactive newsletter pipeline for {Brand Name}. Triggers: /{slug}-newsletter, 'write a {brand} newsletter', 'compose the next newsletter'. Reads {slug}-voice.md as canonical source. Drafts in {brand} voice, runs Slop Killer + Jobs critique, saves draft."
metadata:
  brand: {Brand Name}
  brand_voice_reference: {path-to-brand-voice-doc}
  audience: {restate from Stage 2}
---

# {Brand Name} Newsletter Pipeline

## ⚠️ Read Before Drafting
Read the brand voice doc end-to-end: {path}

## Stages
1. Topic + take intake
2. Optional research (Perplexity/WebSearch)
3. Surface candidates → buyer picks
4. Deeper research on chosen angle
5. Buyer's take ❓
6. Draft per brand voice doc Section 5
7. Slop Killer pass
8. Save draft to {drafts_path}/{YYYY-MM-DD-slug}.md
```

(Repeat the template adapted for blog and tweet, modifying lengths + structure per brand voice doc Section 12.5.)

After generating, **list the file paths** for the buyer. Tell them: **"Restart your AI agent to pick up the new skills."**

---

### Stage 8: Install Verification + Handoff

Walk the buyer through:

1. **Restart their AI agent** (Claude Code, Codex, Gemini CLI, etc.). New skills load on startup.
2. **Test invocation**: tell them to type `/{slug}-newsletter` (or the channel they care most about). The skill should be in the available list. If not, troubleshoot the skill folder path.
3. **First content session**: optionally walk them through their first newsletter / blog post / tweet draft using the new skill. (Or tell them to call you back if they want guided first-use.)
4. **Iterating on voice**: when the buyer notices something off, the fix is always to edit `{slug}-voice.md`. All 3 channel skills will pick up the change automatically next time they run.

Final summary:

```
✅ Brand Voice Engine complete.
   Brand voice doc:    {path}
   Newsletter skill:   ~/.claude/skills/{slug}-newsletter/SKILL.md
   Blog skill:         ~/.claude/skills/{slug}-blog/SKILL.md
   Tweet skill:        ~/.claude/skills/{slug}-tweet/SKILL.md

   First run:          Restart your AI agent, then type /{slug}-newsletter
   Edit voice:         Always edit the brand voice doc, never the skill files
   Support:            support@apexskills.dev
```

## Embedded Methodology Reference (for the agent running this skill)

Below is the synthesized methodology — refer to it when generating Stage 6's brand voice doc. This is included in-file so the skill works without external lookups.

### Subject Line / Hook Archetypes (Halbert + Sugarman + Ogilvy)

| Archetype | Pattern | Why it works |
|---|---|---|
| Specific Claim | `[Named thing] just [verb] [outcome]` | Halbert's specificity rule — buyers trust numbers and names |
| Contrarian Take | `Why [common belief] is wrong` / `Stop [behavior]` | Sugarman's first-sentence curiosity gap |
| Curiosity Gap | `The [N]-word [thing] that [outcome]` | Ogilvy's headline + Sugarman's slippery slide |
| Mistake | `I [costly mistake] — here's the fix` | Sam Parr's confession pattern, Handley's reader-centric |
| Cut | `[Tool/Thing] is dead. Use [X] instead.` | Naval-style declarative |

### Opener Patterns (Sugarman's Slippery Slide)

1. **The Blunt Claim** — state the take, no setup
2. **The Lived Anecdote** — specific story, 1-2 sentences
3. **The Question You Already Want Answered** — match the reader's existing thought
4. **The Contrarian Snap** — short declarative against a common belief
5. **The Numbered Reveal** — "Three skills shipped. One of them changed how I priced."

### Body Structure (Halbert's AIDA, Brand-Tuned)

| AIDA | Section | Job |
|---|---|---|
| Attention | Subject + opening line | Earn the open + the next sentence |
| Interest | Why-now paragraph | Cite the specific recent thing |
| Desire | What-I-would-do | Concrete, opinionated, actionable |
| Action | Single CTA | One verb, one link, one ask |

### Universal Cut List (Stephen King + Halbert + Handley)

**Filler:** However, In conclusion, To be honest, Essentially, Ultimately, Basically, Actually, Just, Really, Very, Quite, Honestly, Frankly.

**Marketing slop:** Leverage (verb), Robust, Seamless, Unlock, Unleash, Game-changing, Next-level, Revolutionary, Cutting-edge, Industry-leading, Thought leader, Synergy, Empower, Curated.

**Hedging:** Some say, It could be argued, Typically, Often, Tends to, Might, Perhaps, Sort of, Kind of, A bit, Somewhat.

**Engagement bait:** Let me know what you think!, Smash that reply button, What are YOUR thoughts?, Drop a 🔥, Don't miss out.

**Clichés:** Hope this email finds you well, In this edition, Welcome back, Stay tuned, Until next time, Cheers, Best regards.

### Handley's Logo-Off Test (apply at end of every draft)

Strip every brand-specific reference. Does the content still sound recognizably like the buyer's brand — or could it be any company in their space? If "any company," rewrite.

### Stephen King's Rule (apply before save)

Second draft = first draft minus 10%. Cut puffiness ruthlessly.

### Paul Graham's Rule (apply before publish)

Reread the piece end-to-end. If you stumble at any sentence, rewrite it.

---

## Anti-Patterns (do not produce)

- A brand voice doc that reads as generic ("clear, concise, professional") — every section must be brand-specific
- A SKILL.md that doesn't reference the brand voice doc (drift will start day 1)
- Newsletter / blog / tweet skills that don't share the same source-of-truth doc
- A single-skill output that doesn't cover the buyer's actual chosen channels
- Drafts that don't pause for the buyer's take at key stages — content engines run with the buyer in the loop, not autonomous

## Support

Issues? Email **support@apexskills.dev** with the slug of the brand you were building. Include the AI agent you're running (Claude Code, Codex, Gemini, etc.).

Built by [Apex Skills](https://apexskills.dev) — production-grade AI agent skills for operators.
