# The Slop Dictionary

Reference for the anti-slop skill. Load when running the banned-word scan.

## Tier 1: Always Slop (Zero Tolerance)

These words/phrases are flagged as slop in 100% of contexts. Replace or cut every instance.

### Verbs
- delve / delving / delved
- navigate (metaphorical)
- leverage (as verb)
- harness (as verb)
- unleash / unleashing
- elevate / elevating
- unlock (metaphorical, e.g., "unlock potential")
- empower / empowering (without specific action)
- delineate

### Nouns
- landscape (metaphorical)
- tapestry (metaphorical)
- mosaic (metaphorical)
- realm (e.g., "in the realm of")
- journey (metaphorical, e.g., "this journey")
- testament (e.g., "a testament to")
- paradigm (e.g., "paradigm shift")
- synergy / synergize
- ecosystem (when used vaguely)

### Adjectives
- robust
- seamless / seamlessly
- dynamic (when filler)
- ever-evolving / ever-changing
- multifaceted
- holistic (when vague)
- best-in-class
- cutting-edge (without specifics)
- game-changing / game-changer
- bespoke (overused)
- curated (when generic)

### Phrases
- "in today's [X] world"
- "in today's fast-paced [X]"
- "in the world of [X]"
- "when it comes to [X]"
- "it's worth noting that"
- "it's important to note"
- "it's crucial to"
- "it goes without saying"
- "needless to say"
- "at the end of the day"
- "thought leader / thought leadership"
- "move the needle" (without metric)
- "low-hanging fruit"
- "circle back" (in writing)
- "touch base" (in writing)
- "thinking outside the box"
- "the sky's the limit"
- "the possibilities are endless"
- "only time will tell"
- "stay tuned"

### Transition Crutches
- "moreover" (use "also" or split sentence)
- "furthermore" (same)
- "additionally" (often deletable)
- "in conclusion" (just conclude)
- "to sum up" (just sum up)

## Tier 2: Context-Dependent

These are sometimes fine, sometimes slop. Flag for human review.

- "explore" (cut if abstract; keep if literal)
- "discover" (cut if hype; keep if literal)
- "transform" (cut if vague; keep with specific before/after)
- "optimize" (cut if no metric; keep with specific number)
- "scale" (cut if vague; keep with growth number)
- "innovative" (cut unless followed by what's actually new)
- "solutions" (cut if generic; keep if specific)
- "engage" / "engagement" (cut if vague; keep with metric)
- "actionable" (often filler — does the next word need this modifier?)
- "insights" (often filler — say what insight)
- "value" (cut if vague; keep with $ or specific benefit)

## Tier 3: AI Cadence Patterns (Not Words, Patterns)

These structural tics signal AI authorship even when individual words are clean:

### The List-of-Three Crutch
Three parallel items, comma-separated, repeated multiple times in one piece.
> "clarity, focus, and results"
> "vision, mission, and values"
> "speed, scale, and impact"

Fine once. Twice is a tell. Three times is slop.

### The Rule-of-Three Structure
Bigger than the comma-list version: the whole piece organizes around exactly three points, or a numbered list of exactly three items, or a "here are three things / three habits / three rules" frame.

> "Three things, in order of..."
> "The ones seeing real lift share three habits: ..."
> "1. ... 2. ... 3. ..." (and it's always three)

Three is the count AI reaches for by default. Real arguments rarely have exactly three of anything. Vary the number (2, 4, 5, 7) or dissolve the list into prose. If it must be a list, make the count honest, not aesthetic.

### The Staccato Fragment Crutch
Clusters of ultra-short fragments deployed for manufactured drama, or every paragraph/section landing on a 2-5 word punch line.
> "That's it."
> "Every time."
> "Period."
> "The cut is the work."
> "Same fear, two outfits."

One or two across a whole piece can land. A steady drumbeat — a punchy fragment closing nearly every section — is the most common "operator voice" AI tell. Distinct from a genuinely terse writer (Hemingway, Halbert): the tell is the *manufactured punch line stapled onto every beat*, not short sentences as a consistent natural voice. Calibrate against the user's real voice samples before cutting.

### The Negation Triplet
> "It's not just X. It's Y. It's Z."
> "This isn't a feature. It's a philosophy. It's a movement."

Once = rhetorical. Twice = formula. Three+ = rewrite.

### The Em-Dash Sandwich
> "Marketing — at its core — is storytelling."
> "AI — when used correctly — changes everything."

Acceptable in 0-1 instances per 500 words. More = flag.

### The Rhetorical Question Sandwich
> "What does this mean for you? It means [X]. What should you do? [Y]."

Once is fine. Repeated = AI tell.

### The Bold Summary Tic
Every paragraph ends with a **bolded one-line summary** of the paragraph above.

This is a strong AI tell. Strip all but the most essential.

## Tier 4: Sycophancy

Always cut:

- "I hope this helps"
- "I hope this makes sense"
- "Let me know if you have any questions"
- "Feel free to reach out"
- "I'd be happy to"
- "Happy to discuss further"
- "Great question!"
- "Absolutely!"
- "Certainly!"
- "What are your thoughts?"
- "Agree?" / "Thoughts?" (as standalone close)
- Any opening starting with "I'm excited to..."
- Any opening starting with "Hi friends!" (unless user's voice samples do this)
- Any closing that praises the reader's question

## Tier 5: Hedge Words

One hedge per piece = fine. Two = flag. Three+ = rewrite.

- "It seems that"
- "It may be the case that"
- "Some would argue"
- "In many cases"
- "Generally speaking"
- "More often than not"
- "It could be said that"
- "Arguably"
- "Essentially"
- "Basically"
- "Perhaps"
- "Possibly"
- "Somewhat"
- "Relatively"

## Replacement Map

When you find slop, use these direct swaps where possible:

| Slop | Direct replacement |
|---|---|
| "leverage X to do Y" | "use X to do Y" |
| "harness the power of X" | "use X" |
| "unleash X" | "release X" / "start X" / cut |
| "delve into X" | "look at X" / "examine X" / cut |
| "navigate the X landscape" | "[the specific market/topic]" |
| "robust X" | "[X with specific specs/proof]" |
| "seamless X" | "[X that does Y without Z friction]" |
| "in today's [X] world" | cut entirely, lead with claim |
| "elevate your X" | "improve X by [specific amount]" |
| "ever-evolving" | "the [industry] in [year]" |
| "best-in-class" | "[specific benchmark beaten]" |
| "thought leader" | "[specific expertise + proof]" |
| "moreover" / "furthermore" | "also" or new sentence |
| "the possibilities are endless" | name one specific possibility |
| "stay tuned" | give the specific next step |
| "let's dive in" | start with the claim |
| "I hope this helps" | cut |
| "agree?" | cut or replace with specific question |

## Final Rule

When in doubt, cut. Slop is almost always additive. Removing words rarely hurts an argument. Adding them almost always does.
