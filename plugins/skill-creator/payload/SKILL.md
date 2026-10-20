---
name: skill-creator
description: "Generate production-grade Claude Code skill files from a voice dump, rough idea, or existing workflow. Use when the user says 'create a skill', 'make this into a skill', 'turn this prompt into a skill', 'package this workflow', 'I keep doing X manually', or describes a repeatable task they want Claude to handle automatically. Outputs a complete SKILL.md with frontmatter, scoring criteria, examples, and guardrails — not just a prompt."
license: MIT
metadata:
  author: Apex
  version: '1.0'
  category: meta
---

# Skill Creator

## When to Use This Skill

Trigger this skill whenever the user:

- Says "create a skill", "make a skill", "build a skill", or "turn this into a skill"
- Describes a workflow they repeat (writing X type of content, doing Y type of review, generating Z type of output)
- Pastes a long prompt and wants it productionized
- Says "I keep telling Claude to do the same thing over and over"
- Wants to capture a personal SOP, voice, brand style, or proprietary framework as a reusable skill file

A skill is not a prompt. A skill is an instruction manual with context, examples, scoring rubrics, and guardrails that lives in `.claude/skills/` and loads automatically when triggered.

## What Separates a Real Skill From a Prompt

| Prompt | Skill |
|---|---|
| One-shot instruction | Reusable framework |
| No examples | 2-5 worked examples |
| No quality bar | Explicit scoring rubric |
| No guardrails | Failure modes + anti-patterns listed |
| Forgets your voice | Voice samples embedded |
| Lives in chat history | Lives in `.claude/skills/` and auto-loads |

If the output doesn't have all six right-column items, you have not built a skill. You've written a long prompt.

## The 7-Phase Skill Build Process

Execute these phases in order. Do not skip phases even if the user is impatient — skipping phases is what produces fragile skills that fail on the second use.

### Phase 1: Interview (5-10 questions, batched)

Ask the user in ONE message:

1. **What is the trigger?** When should Claude reach for this skill? (Give 3-5 example phrases.)
2. **What is the input?** What does the user paste/upload/say to kick it off?
3. **What is the output?** What artifact does Claude produce? (Format, length, structure.)
4. **What does "good" look like?** Paste 1-3 examples of past outputs you were happy with. If none exist, describe the qualities.
5. **What does "bad" look like?** What failure modes have you seen? What should this skill refuse to produce?
6. **What's your voice/style?** Paste 2-3 samples of your writing, or name the writers/brands you sound like.
7. **What context does Claude need?** Brand docs, audience description, product details, past work to reference?

Do not proceed to Phase 2 until you have answers to at least 1, 2, 3, and 4.

### Phase 2: Extract the Framework

Read the user's example outputs and reverse-engineer the structure:

- What sections appear every time?
- What's the typical length?
- What's the opening pattern? Closing pattern?
- What rhetorical moves repeat? (Hook → problem → proof → CTA, etc.)
- What words/phrases recur in their voice?
- What does the user explicitly NOT do? (No emojis, no exclamation points, no hedging language, etc.)

Output this as a "Framework" section the skill will reference.

### Phase 3: Build the Scoring Rubric

Every skill must score its own output before returning it. Define 4-7 dimensions, each scored 1-10:

Examples for a blog post skill:
- Readability (8th-grade or below = 10)
- Keyword density (target met without stuffing = 10)
- Structural integrity (H2/H3/TL;DR/CTA present = 10)
- Voice match (sounds like the user's samples = 10)
- Hook strength (first 50 words hook the reader = 10)

If any dimension scores below 7, the skill must rewrite before returning.

### Phase 4: Write the SKILL.md

Use this template:

```markdown
---
name: [kebab-case-name]
description: "[1-2 sentences. Include trigger phrases the agent will pattern-match on.]"
license: MIT
metadata:
  author: [user name or brand]
  version: '1.0'
---

# [Skill Title]

## When to Use This Skill

Trigger this skill when the user says:
- "[trigger phrase 1]"
- "[trigger phrase 2]"
- "[trigger phrase 3]"

## Inputs Required

- [Input 1]: [what it is, format expected]
- [Input 2]: [optional/required]

If any required input is missing, ask for it before proceeding. Do not invent it.

## Framework

[The reverse-engineered structure from Phase 2. Use checklists, not paragraphs.]

## Voice & Style Rules

DO:
- [Voice rule 1]
- [Voice rule 2]

DON'T:
- [Anti-pattern 1]
- [Anti-pattern 2 — usually "delve", "landscape", "elevate", "navigate", emojis, etc.]

## Step-by-Step Execution

1. [Step 1 with concrete action]
2. [Step 2]
3. [Step 3]
4. Score the output using the rubric below.
5. If any score < 7, rewrite and re-score.
6. Return the final output with scores at the bottom (collapsed).

## Scoring Rubric

| Dimension | What scores 10 | What scores 1 |
|---|---|---|
| [Dim 1] | [...] | [...] |
| [Dim 2] | [...] | [...] |

## Examples

### Example 1: [Title]
**Input:** [...]
**Output:** [...]
**Why it works:** [...]

### Example 2: [Title]
[...]

## Failure Modes (Do Not Ship)

- [Anti-pattern 1]
- [Anti-pattern 2]
```

### Phase 5: Embed 2-5 Worked Examples

Take the examples the user gave in Phase 1 and format them as input → output pairs. Annotate WHY each one works. Examples are the highest-leverage part of a skill — they teach by demonstration what 500 lines of prose cannot.

If the user only gave one example, generate two more in the same style and ask the user to approve before saving.

### Phase 6: Add Guardrails

Every skill must include a "Failure Modes" section. Common entries:

- "Do not produce output if [required input] is missing — ask for it instead."
- "Do not use the following words: delve, landscape, navigate, elevate, unleash, harness, leverage (as verb), ever-evolving, dynamic, robust, seamless, journey, in today's [X] world."
- "Do not use em-dashes if the user's samples don't."
- "Do not add 'I hope this helps' or any sycophantic close."
- "Do not generate more than [N] words unless asked."

### Phase 7: Validate & Save

1. Save to `.claude/skills/[skill-name]/SKILL.md`
2. Test the skill by running it once on a sample input from Phase 1
3. Compare the output against the user's example outputs. If voice match < 8/10, return to Phase 2.
4. Report to the user: "Skill saved. Tested with [input]. Voice match: X/10. Trigger phrases: [...]"

## Voice & Style Rules

DO:
- Treat skills as products. Name them well. Write descriptions buyers/users would pay for.
- Embed examples liberally. Examples > prose.
- Make the scoring rubric specific. "Sounds good" is not a rubric. "Reads at 8th-grade level per Hemingway score" is.
- Use checklists, tables, and headers. Skills are scanned, not read.

DON'T:
- Write skills longer than 500 lines without splitting into `references/`
- Skip the scoring rubric. A skill without a rubric is a prompt.
- Forget the `description` field's trigger phrases — that's how Claude Code decides to load it.
- Use vague language like "be professional" or "match the brand voice" without showing what that means.

## Scoring Rubric for the Skill Itself

Before returning a completed skill, self-score on these dimensions. Any below 7 means rewrite.

| Dimension | What scores 10 | What scores 1 |
|---|---|---|
| Trigger clarity | Description has 3+ exact phrases Claude can pattern-match | Vague description like "helps with writing" |
| Framework specificity | Every step is concrete and actionable | Steps say "think about" or "consider" |
| Example quality | 3+ real input/output pairs with annotations | Zero examples, or fake examples |
| Rubric specificity | Each dimension has measurable criteria | Rubric says "good" / "bad" |
| Voice capture | Reading the skill, you can hear the user's voice | Generic prose anyone could have written |
| Guardrails | Explicit failure modes and forbidden words listed | No anti-patterns, no refusal conditions |
| File hygiene | Frontmatter valid, name kebab-case, under 500 lines | Frontmatter broken, name has spaces |

## Example: Skill Build From a Voice Dump

**User says:** "I keep writing LinkedIn posts the same way — hook, then a personal story, then 3 bullets of lessons, then a CTA to my newsletter. Can you make this a skill?"

**Phase 1 questions you ask:**
1. Trigger: "Write a LinkedIn post about X" — confirm
2. Input: A topic or rough idea
3. Output: ~200-word post, 4 sections
4. Examples: Please paste 3 of your best-performing posts
5. Failure modes: What do you hate seeing in LinkedIn AI posts?
6. Voice: Paste those 3 posts; I'll extract patterns
7. Context: Do you have a newsletter URL to embed as CTA?

**Phase 2-7:** Build the SKILL.md, embed the 3 posts as examples, define rubric (hook strength, story specificity, lesson concreteness, CTA clarity), add guardrails ("no emojis, no 'agree?' questions, no '1/' thread formatting").

**Output:** A `.claude/skills/linkedin-post-writer/SKILL.md` file the user can drop in and trigger with "Write a LinkedIn post about [topic]".

## Failure Modes (Do Not Ship)

- Skill with no examples
- Skill with no scoring rubric
- Skill with description shorter than 100 characters or missing trigger phrases
- Skill that just restates a long prompt without framework extraction
- Skill that doesn't capture the user's voice (test: does it sound like anyone could have written this?)
- Skill saved without testing on at least one sample input
- Skill files over 500 lines with no `references/` split
