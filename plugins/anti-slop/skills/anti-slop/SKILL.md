---
name: anti-slop
description: "Scan any AI-generated text for tell-tale slop words, hedge phrases, em-dash overuse, sycophancy, rule-of-three structure, staccato fragment crutch, and generic AI cadence — then run a holistic vibe check and rewrite cleanly in the user's voice. Use when the user says 'remove the slop', 'make this sound human', 'this sounds like AI', 'kill the fluff', 'clean this up', 'detect AI slop', or pastes a draft and asks for a human pass. Outputs a flagged report + a clean rewrite."
license: MIT
metadata:
  author: Apex
  version: '1.1'
  category: editing
---

# Anti-Slop

> From [Apex Skills](https://apexskills.dev) — operator-grade Claude workflows. This one's free; 15 more at [apexskills.dev](https://apexskills.dev). Share the file, keep this line.

## When to Use This Skill

Trigger when the user says:
- "Remove the slop"
- "Make this sound human"
- "This sounds like AI"
- "Kill the fluff"
- "De-slop this"
- "Clean this up"
- "Strip the AI tells"
- "Run this through anti-slop"
- Pastes any text and asks for a "human pass" or "voice pass"

Also chain this skill automatically after any content-generation skill (LinkedIn writer, blog writer, email writer) to QC the output before returning.

## Inputs Required

- **Text to scan** (any length)
- **Optional**: voice samples to calibrate the rewrite against the user's natural style

If no voice samples are provided, default to a direct, declarative, sentence-varied style and skip personalization in the rewrite.

## The Slop Detection Framework

Run the input through these 8 detection passes in order:

### Pass 1: Banned Word Scan

Flag every instance of words in the **Tier 1 banned list** (load `references/slop-dictionary.md` for the full list). Tier 1 = always slop, no exceptions:

- delve, delving
- landscape (when used metaphorically: "the marketing landscape")
- navigate (when used metaphorically: "navigate this challenge")
- elevate, elevating
- unleash, unleashing
- harness (as verb: "harness the power of")
- leverage (as verb: "leverage AI to")
- robust
- seamless, seamlessly
- dynamic (as filler adjective)
- ever-evolving, ever-changing
- in today's [X] world / in today's fast-paced world
- game-changer, game-changing
- tapestry, mosaic (metaphorical)
- testament to
- in the realm of
- it's worth noting that
- it's important to note
- it's crucial to
- moreover, furthermore (when used as transition crutch)
- delineate, delineating
- multifaceted
- holistic (when used vaguely)
- paradigm shift
- synergy, synergize
- best-in-class
- cutting-edge (without specifics)
- thought leader, thought leadership
- circle back, touch base (in written content)
- low-hanging fruit
- move the needle (without a specific metric)

### Pass 2: Sycophancy Scan

Flag every instance of:
- "I hope this helps"
- "Let me know if you have any questions"
- "Feel free to reach out"
- "I'd be happy to"
- "Great question"
- "Absolutely!"
- "Certainly!"
- "What are your thoughts?"
- "Agree?" (as standalone question)
- "Thoughts?" (as standalone close)
- Any opener starting with "I'm excited to..."

### Pass 3: Hedge Scan

Flag overhedged phrases that drain authority:
- "It seems that"
- "It may be the case that"
- "Some would argue"
- "In many cases"
- "Generally speaking"
- "More often than not"
- "It could be said that"
- "Arguably" (when used as crutch)
- "Essentially" (filler)
- "Basically" (filler)

A single hedge per piece is fine. More than two is slop.

### Pass 4: Em-Dash Audit

Count em-dashes (—) in the text. AI overuses them dramatically. Rules:
- 0-1 em-dashes per 500 words: fine
- 2-3 per 500 words: flag for review
- 4+ per 500 words: rewrite, replace most with periods or commas

Exception: if user's voice samples use em-dashes heavily, calibrate up.

### Pass 5: Cadence Scan

Flag these AI cadence tells:
- **List-of-three crutch**: "X, Y, and Z" repeated more than twice in close proximity ("clarity, focus, and results... speed, scale, and quality... vision, mission, and values")
- **Rule-of-three structure**: a numbered list of exactly three items, or a "here are three things / three habits / three rules" frame. Three is the AI default count. Real arguments rarely have exactly three of anything — vary the number (2, 4, 5) or dissolve the list into prose.
- **Parallel sentence structure** repeated 3+ times in a row ("It's not X. It's Y. It's Z.") — once is rhetorical; three times is formula
- **Staccato fragment crutch**: clusters of ultra-short fragments deployed for manufactured drama ("That's it." "Every time." "Period." "The cut is the work."), or every section/paragraph landing on a 2-5 word punch line. One or two per piece can land. A steady drumbeat of them is the single most common "operator voice" AI tell. This is distinct from a genuinely terse writer — flag the *pattern of manufactured punch lines*, and calibrate against the user's real voice samples before cutting.
- **Em-dash sandwich**: "Word — phrase — word" structure repeated
- **Question-answer pattern**: rhetorical question followed immediately by its answer, repeated more than once per piece
- **Bolded-phrase summary** at end of every paragraph

### Pass 6: Vagueness Scan

Flag every claim that has no concrete number, name, or example:
- "Many companies struggle with X" → which companies? how many?
- "Studies show" → which studies?
- "Most marketers" → what %? what segment?
- "Significant improvement" → how much?
- "Customers love it" → how many? what NPS?

Slop runs on adjectives. Good writing runs on nouns and numbers.

### Pass 7: Opening / Closing Pattern Scan

Flag these openers (rewrite required):
- "In today's [X] world"
- "Let's dive into"
- "Picture this:"
- "Imagine if"
- "Have you ever wondered"
- "We've all been there"
- "In the world of [X]"
- "When it comes to [X]"

Flag these closers (rewrite required):
- "I hope this helps"
- "The choice is yours"
- "Only time will tell"
- "The possibilities are endless"
- "The future is bright"
- "Stay tuned"
- "Let's see what the future holds"
- Any close that doesn't include a specific next action or a concrete final thought

### Pass 8: Holistic AI Gut-Check

A piece can pass all seven scans above and still read as AI to an experienced reader. People who have spent millions of tokens reading Claude output pattern-match the *aggregate vibe*, not individual words. Word-level cleanliness is necessary but not sufficient. After the word passes, step back and read the whole piece the way a skeptic who has read a billion tokens of AI prose would:

- Does the rhythm feel manufactured — short punch, short punch, longer reflective beat, repeat?
- Does every section resolve neatly into a tidy aphorism or one-line landing?
- Is the structure suspiciously clean: hook, three points, callback, sign-off?
- Would someone clock this as AI in the first paragraph, before any banned word appears?

If the answer is yes, the fix is not another word swap. It is structural:
- Break the rhythm. Let one section run long and slightly messy.
- Vary the shape of sections — not all setup-then-payoff.
- Cut at least one manufactured punch line; let a paragraph end flat.
- Add a specific lived detail only the actual author could know (a name, a number, a small concrete moment). Specificity is the hardest thing for AI to fake and the fastest way to read human.

Flag the verdict explicitly: **passes word scan, fails vibe check** — then rewrite for texture, not vocabulary.

> Field note: this pass exists because of real reader feedback. An experienced Claude user reviewed a blog with a clean word profile and still called it "almost entirely AI," naming em-dashes, the rule-of-three, and bursty staccato sentences as the giveaways. The lesson: the tells that survive a word scan are structural and rhythmic. Hunt those.

## Output Format

Return the scan as a structured report:

```
SLOP SCAN: [N] issues flagged

TIER 1 BANNED WORDS (X instances)
  ✗ "delve" — line 3
  ✗ "landscape" — line 7
  ✗ "leverage" — line 12

SYCOPHANCY (X instances)
  ✗ "I hope this helps" — final line

HEDGES (X instances)
  ✗ "It seems that" — line 4
  ✗ "Generally speaking" — line 9

EM-DASH OVERUSE: X em-dashes in Y words (target: ≤1 per 500)

CADENCE ISSUES
  ✗ Parallel "It's not X. It's Y. It's Z." appears 4 times
  ✗ List-of-three crutch repeated 3x
  ✗ Rule-of-three structure: numbered list of exactly 3
  ✗ Staccato fragment crutch: 6 manufactured punch lines ("That's it." "Every time." ...)

VAGUENESS
  ✗ "Many companies struggle" — no number
  ✗ "Significant improvement" — no metric

OPENER/CLOSER
  ✗ Opens with "In today's fast-paced world"
  ✗ Closes with "The possibilities are endless"

VIBE CHECK: passes word scan / fails vibe check
  ✗ Rhythm manufactured (punch-punch-reflect repeated)
  ✗ Every section lands on an aphorism
  → Needs structural rewrite, not word swaps

---

CLEAN REWRITE:
[The rewritten text with all issues fixed]

---

CHANGE LOG:
- Replaced "leverage AI to" with "use AI to" (line 12)
- Replaced opener "In today's fast-paced world" with [user's actual claim]
- Removed em-dashes in lines 4, 7, 14 (replaced with periods)
- Replaced "Many companies struggle" with "47% of Fortune 500 marketers..." [if data available, otherwise flag as needing source]
- Cut "I hope this helps" closer entirely
```

## Voice & Style Rules for the Rewrite

DO:
- Replace adjectives with nouns and verbs
- Replace vague claims with specific numbers (or flag for the user to supply)
- Vary sentence length (short, medium, longer — not all medium)
- Use direct declarative sentences
- Match user's voice samples if provided

DON'T:
- Replace one slop word with another slop word ("delve" → "explore" is still slop in marketing copy)
- Add new slop while removing old slop
- Rewrite content the user got right — surgical edits only
- Lose the user's actual argument while cleaning the prose

## Scoring Rubric

After rewrite, self-score on these dimensions, 1-10:

| Dimension | What scores 10 | What scores 1 |
|---|---|---|
| Slop elimination | Zero Tier 1 banned words remain | Multiple slop words still present |
| Voice preservation | Sounds like the user (if samples given) | Sounds like a different writer |
| Specificity gain | More concrete nouns/numbers than original | Same vague claims, just reworded |
| Cadence variety | Sentence length and structure vary | Same rhythm throughout |
| Length discipline | Same or shorter than original | Bloated longer |
| Argument intact | User's actual point preserved | Original argument lost or softened |

If any dimension scores below 8, run a second rewrite pass on that dimension only.

## Replacement Patterns

When rewriting, use these direct swaps:

| Slop | Replacement |
|---|---|
| "leverage X to" | "use X to" |
| "harness the power of" | "use" |
| "unleash" | "release" / "start" |
| "delve into" | "look at" / "examine" / cut entirely |
| "navigate the landscape" | name the specific thing |
| "robust solution" | name the specific solution + its specs |
| "seamless experience" | name the specific UX win + metric |
| "in today's fast-paced world" | cut entirely; start with the claim |
| "it's important to note" | cut entirely |
| "moreover" / "furthermore" | "also" or start a new sentence |
| "best-in-class" | name the actual benchmark |
| "thought leader" | name the actual expertise |
| "elevate your X" | "improve your X by [specific amount]" |
| "ever-evolving" | "the [specific industry] in [year]" |

## Examples

### Example 1: Generic AI Blog Intro

**Input:**
> In today's fast-paced digital landscape, leveraging AI to elevate your marketing has become a game-changer. It's important to note that businesses must navigate this ever-evolving terrain with robust strategies. Studies show that many companies are delving into AI to harness its power and unleash unprecedented growth.

**Slop scan:**
- Banned words: 9 (today's fast-paced, landscape, leverage, elevate, game-changer, navigate, ever-evolving, robust, delve, harness, unleash)
- Vagueness: "businesses", "many companies", "studies show", "unprecedented growth" — zero specifics

**Clean rewrite:**
> 73% of marketing teams added an AI tool in the last 12 months. Most got nothing for it. The ones seeing real revenue lift share three habits: they pick one workflow, they pick one tool, and they measure one metric. That's it.

**Why it works:** Replaced 9 slop words with 0. Replaced vague claims with one specific number. Replaced "imagine the future" cadence with a falsifiable thesis. Now ~50% shorter and 10x more credible.

### Example 2: LinkedIn Post Closer

**Input:**
> ...and that's why every marketer should be using AI. I hope this helps! What are your thoughts? Let's dive into the conversation in the comments. Agree?

**Slop scan:**
- Sycophancy: 4 instances
- Banned phrases: "let's dive in"
- Question-bait close: "Agree?"

**Clean rewrite:**
> ...and that's why every marketer should be using AI.
>
> If you've tested this and it didn't work, you tested the wrong workflow. Reply with the workflow and I'll tell you why.

**Why it works:** Cut all four sycophantic closers. Replaced with a specific, useful offer that creates real replies (which actually feed the algorithm — unlike "agree?").

### Example 3: Email Newsletter Open

**Input:**
> Hi friends! I'm excited to share that I've been delving deep into the world of AI marketing automation. The possibilities are truly endless, and I can't wait to navigate this journey with you. Let's unlock the potential together!

**Slop scan:**
- Sycophancy: "I'm excited to", "Hi friends!"
- Banned words: "delving", "world of", "navigate", "journey", "unlock"
- Vagueness: "possibilities are endless"

**Clean rewrite:**
> Last month I rebuilt my entire newsletter workflow on Claude Code. It cut my Tuesday writing time from 6 hours to 90 minutes. Here's the exact stack.

**Why it works:** Replaced 5 slop words with a specific outcome and a falsifiable claim. Opens with proof, not enthusiasm.

## Failure Modes (Do Not Ship)

- Rewrite that contains ANY Tier 1 banned word
- Rewrite that's longer than the original (slop edits should compress, not expand)
- Rewrite that introduces new slop while removing old slop
- Rewrite that loses the user's argument or softens their stance
- Rewrite that ignores user's voice samples
- Report without a clear count of issues found
- Report without a change log explaining each edit

## References

- `references/slop-dictionary.md` — full banned word list with categories and replacement options (load when scanning)
- `references/voice-calibration.md` — how to adjust rewrite intensity based on user's voice samples
