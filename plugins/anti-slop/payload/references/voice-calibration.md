# Voice Calibration

Use this reference to adjust the anti-slop rewrite intensity based on the user's voice samples.

## Step 1: Detect Voice Profile

Read the voice samples and classify on these axes:

### Sentence Length
- **Short**: avg 8-12 words. Punchy. Direct. (Hemingway, Halbert)
- **Medium**: avg 14-18 words. Conversational. (most modern operators)
- **Long**: avg 20+ words. Considered, journalistic. (longform essayists)

### Tone Register
- **Casual**: contractions, lowercase, fragments OK
- **Direct**: declarative, no hedges, contractions OK
- **Formal**: full sentences, no contractions, hedges measured
- **Persuasive/sales**: direct-response cadence, urgency, specific numbers

### Em-Dash Usage
- **None**: never use em-dashes in rewrite
- **Sparse**: 0-1 per 500 words
- **Frequent**: matches user's actual usage rate

### First-Person Style
- **I-driven**: writes from personal experience
- **You-driven**: writes to the reader
- **We-driven**: writes inclusively
- **None**: third-person observational

### Closer Pattern
- **CTA close**: ends with specific next action
- **One-liner close**: short punchy final line
- **Question close**: ends with rhetorical or genuine question (rare in good copy)
- **PS close**: uses P.S. for secondary CTA (email-style)

## Step 2: Calibrate Rewrite

After detecting the voice profile, apply these calibrations to the rewrite:

### If voice is "short + direct + no em-dashes"
- Aggressive cuts. Break compound sentences into two.
- Replace every comma-clause with a period when possible.
- Zero em-dashes regardless of original.
- One CTA per piece, no preamble.

### If voice is "medium + conversational + sparse em-dashes"
- Preserve sentence variety.
- 1 em-dash per 500 words max.
- Keep contractions.
- Maintain rhythm; don't over-shorten.

### If voice is "long + considered + frequent em-dashes"
- Lighter cuts. Preserve complex sentences if they serve the argument.
- Allow user's natural em-dash rate.
- Focus rewrite on slop words and vagueness, not sentence structure.

### If no voice samples provided
- Default to "medium + direct + sparse em-dashes"
- Lead every paragraph with a claim
- One CTA at the end
- No sycophancy at all

## Step 3: Voice-Specific Vocabulary

Build a vocabulary list from the samples:

- **Words the user uses repeatedly**: keep these in the rewrite even if they could be replaced
- **Words the user never uses**: avoid these in the rewrite
- **Sentence openers the user prefers**: match their pattern
- **Sign-off patterns**: match exactly

## Step 4: Voice Match Test

After rewrite, run this check before returning:

1. Read 3 sentences from the rewrite aloud.
2. Read 3 sentences from the user's voice sample aloud.
3. Do they sound like the same person? Yes/No.
4. If no, identify the specific mismatch (sentence length? vocabulary? rhythm?) and redo that aspect only.

Voice match should score 8+ on the rubric before shipping.
