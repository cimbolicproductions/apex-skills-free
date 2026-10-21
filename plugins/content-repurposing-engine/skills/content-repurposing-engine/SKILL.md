---
name: content-repurposing-engine
description: "Turn one piece of long-form content (blog post, YouTube video, podcast, transcript, newsletter) into a full week of distribution: LinkedIn post, X thread, newsletter draft, short-form video script, Instagram/Threads post, and email teaser. Use when the user says 'repurpose this', 'turn this into social', 'make this into a thread', 'I have a blog post and need posts for the week', or pastes a transcript/URL and asks for distribution."
license: MIT
metadata:
  author: Apex
  version: '1.0'
  category: content
---

# Content Repurposing Engine

## When to Use This Skill

Trigger when the user says:
- "Repurpose this [blog post / video / transcript / newsletter]"
- "Turn this into [LinkedIn / X / a thread / a newsletter / shorts]"
- "I have a YouTube video, make me social posts"
- "Break this down into a week of content"
- "Make me a content week from this"
- Pastes a URL, transcript, or long-form text and asks for derivatives

## Inputs Required

- **Source content**: blog URL, YouTube URL, transcript, or pasted text (minimum 500 words)
- **Voice samples**: 2-3 prior posts in the user's voice (or load `references/voice-samples.md` if pre-saved)
- **Newsletter URL or CTA destination** (optional but recommended)
- **Platforms to generate** (defaults to all 6 if not specified)

If source content is missing, ask before proceeding. Do not invent content.

## The Output Stack

From one source piece, generate these six artifacts in this exact order:

1. **Atomic Insight List** — extract 5-10 atomic insights (one sentence each, fully self-contained)
2. **LinkedIn Post** (180-250 words, 5-line opening hook, story or framework body, single CTA)
3. **X/Twitter Thread** (5-9 tweets, hook tweet + 1 insight per tweet + close tweet)
4. **Newsletter Draft** (500-800 words, single big idea, 3 supporting points, 1 CTA)
5. **Short-Form Video Script** (45-90 seconds, hook in first 3 seconds, 3 beats, CTA outro)
6. **Instagram/Threads Post** (100-150 words, more conversational, no hashtag spam)
7. **Email Teaser** (75-100 words, drives to newsletter or main piece)

Skip any platform the user explicitly excludes.

## Framework: The Extraction → Reframe → Adapt Loop

For every output, follow this three-step internal process:

1. **EXTRACT** — pull the single best insight from the source that fits this platform's native format
2. **REFRAME** — rewrite the insight in the platform's native rhythm (LinkedIn = line breaks; X = brevity; YouTube Shorts = spoken cadence)
3. **ADAPT** — rewrite in the user's voice using the voice samples

Never copy-paste the source text. Never repurpose by "summarizing." Always extract → reframe → adapt.

## Platform Rules

### LinkedIn Post
- Opening hook: 1 short line that creates an open loop or contrarian claim
- Line breaks every 1-2 sentences for mobile readability
- Body: personal story OR contrarian framework OR specific tactical breakdown
- One CTA at the end, no link in the post body if possible (use comment)
- 180-250 words; never exceed 300
- No emojis unless the user's samples use them
- No "Agree?" or "Thoughts?" sycophantic closers

### X/Twitter Thread
- Tweet 1: hook with specific number, contrarian claim, or open loop
- Tweets 2-N: one atomic insight per tweet, 240 chars max
- Final tweet: CTA (newsletter, follow, or main URL)
- Never split a sentence across tweets
- Never use "1/" "2/" numbering unless the user's samples do
- Never use emoji bullets

### Newsletter Draft
- Subject line: 4-8 words, curiosity gap or specific outcome
- Open: 1-2 sentences that establish the problem
- Body: one big idea with 3 supporting points
- Each support has: claim → proof → example
- Close: 1 sentence that summarizes + 1 CTA
- 500-800 words
- Personal, direct, second-person

### Short-Form Video Script
- HOOK (0-3 seconds): contrarian claim or pattern interrupt
- BEAT 1 (3-15s): the problem / what most people get wrong
- BEAT 2 (15-45s): the insight / framework / contrarian truth
- BEAT 3 (45-75s): the application / what to do Monday morning
- CTA (75-90s): follow / newsletter / next video
- Write for the ear, not the eye. Read it aloud — if it stumbles, rewrite.

### Instagram/Threads Post
- More casual than LinkedIn, more developed than X
- 100-150 words
- One image or carousel reference if applicable
- No hashtag spam (3 max, only if user's samples use them)

### Email Teaser
- Subject line + 75-100 word body
- Single CTA to main piece
- Personal salutation if user's samples use one

## Voice & Style Rules

DO:
- Match the user's voice samples literally — same sentence length, same opening patterns, same vocabulary
- Use specific numbers, names, products, examples from the source content
- Maintain the user's level of formality (casual stays casual, professional stays professional)
- Front-load the most valuable insight in every piece (people don't scroll)

DON'T:
- Use any banned slop words (run output through anti-slop skill if available)
- Add em-dashes if user's samples don't use them
- Use "delve", "navigate", "landscape", "ever-evolving", "dynamic", "robust", "leverage", "unleash", "harness"
- Open with "In today's [X] world" or "Let's dive in"
- Close with "I hope this helps" or "What are your thoughts?"
- Use the word "agree" as a question
- Hashtag spam
- Em-dashes as filler punctuation

## Step-by-Step Execution

1. Fetch source content (if URL, extract main text; if YouTube, fetch transcript)
2. Load voice samples from `references/voice-samples.md` or ask user to paste 2-3 examples
3. Generate Atomic Insight List (5-10 one-sentence insights)
4. For each requested platform, run Extract → Reframe → Adapt
5. Score every output on the rubric below
6. If any output scores < 7 on any dimension, rewrite that output
7. Return all outputs in a structured format with platform headers
8. At the bottom, list which atomic insight was used for each platform (so the user can see coverage)

## Scoring Rubric

Score each generated piece on these dimensions, 1-10:

| Dimension | What scores 10 | What scores 1 |
|---|---|---|
| Voice match | Reads exactly like the user's samples | Generic AI prose |
| Platform-native | Format fits how that platform reads | Same prose copy-pasted across platforms |
| Hook strength | First line stops the scroll | Generic opener |
| Specificity | Names, numbers, concrete details | Vague abstractions |
| Slop-free | Zero banned words, zero AI tells | Multiple slop words present |
| CTA clarity | One unambiguous next action | No CTA or vague CTA |

If any output scores below 7 on any dimension, rewrite before returning.

## Examples

### Example 1: Blog Post → LinkedIn

**Source insight (from blog):** "Most founders treat their newsletter like a broadcast. The ones that compound treat it like a 1-on-1 email to one person."

**LinkedIn output:**
```
99% of founders write newsletters wrong.

They treat each issue like a press release.

The 1% who compound treat every issue like a personal email to one customer.

Same content. Different framing.

The "press release" newsletter gets opens but no replies.
The "personal email" newsletter gets opens, replies, and revenue.

I rewrote my own newsletter using this exact shift last quarter.

Reply rate went from 0.2% to 6.4%.

Same list. Same topics. Different voice.

If your newsletter feels like work to write, you're writing it for the wrong reader.

Write it to one specific person. Watch what happens.
```

**Why it works:** Hook is a specific %, body has a contrarian frame, proof is a personal number, close is actionable. No slop words. No emojis. No "agree?".

### Example 2: YouTube Video → X Thread

**Source insight:** "AI tools don't make bad writers good. They make good writers fast."

**X thread output:**
```
Tweet 1: AI doesn't make bad writers good.

It makes good writers fast.

Here's the part nobody says out loud:

Tweet 2: If you can't tell when an AI draft is bad, you can't fix it.

You ship slop. The slop ranks for nothing.

You blame the model.

Tweet 3: The writers winning with AI right now spent 10 years writing without it.

They built taste first. Speed second.

Tweet 4: If you're new to writing, don't start with AI.

Write 50 posts by hand.

Then bring AI in to scale what already works.

Tweet 5: AI compounds skill.

It doesn't create it.

(More on this in my newsletter — link in bio.)
```

**Why it works:** Hook tweet creates open loop, every tweet is atomic, no numbering, final tweet has CTA, voice is direct and contrarian. No slop.

### Example 3: Podcast Transcript → Newsletter

**Source:** 45-minute transcript on pricing strategy

**Newsletter output structure:**
- Subject: "Why your $99 product should be $299"
- Open: 2 sentences on the pricing trap most creators fall into
- Big idea: Anchoring beats positioning
- 3 supports: (a) what most people do, (b) what the top 1% do, (c) the test you can run this week
- Close: "Try one A/B test this week. Report back."

**Why it works:** Specific subject, single big idea, three concrete supports, actionable close. 650 words. Voice matches user's samples.

## Failure Modes (Do Not Ship)

- Output that uses any banned slop words
- LinkedIn post longer than 300 words
- X thread with "1/" numbering when user's samples don't use it
- Newsletter with no clear single big idea
- Short-form script that doesn't have a hook in the first 3 seconds
- Any output that summarizes the source instead of extracting → reframing → adapting
- Two platforms with the same copy-pasted text
- Missing CTA on platforms that should have one (LinkedIn, X, newsletter, video)
- Voice that doesn't match the samples (test: would the user post this verbatim?)

## References

- `references/platform-specs.md` — current character limits and best practices per platform (load if user asks platform-specific questions)
- `references/voice-samples.md` — store user's voice samples here for reuse across runs
