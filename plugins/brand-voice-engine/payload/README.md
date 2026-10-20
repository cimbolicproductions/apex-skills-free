# Brand Voice Engine

A complete brand voice + content engine for your business, built interactively in one Claude session.

## What you bought

When you run this skill, your AI walks you through a 15-question brand interview, researches your niche, applies the synthesized methodology of 9 legendary copywriting + founder-voice sources (Halbert, Sugarman, Ogilvy, Sam Parr, Ann Handley, Stephen King, Paul Graham, Naval, Dan Kennedy) to YOUR brand parameters, then generates:

1. **`{your-brand}-voice.md`** — A 13-section canonical brand voice document personalized to your brand, audience, channels, and goals.
2. **`{your-brand}-newsletter/SKILL.md`** — Interactive newsletter pipeline.
3. **`{your-brand}-blog/SKILL.md`** — Interactive blog pipeline.
4. **`{your-brand}-tweet/SKILL.md`** — Tweet/thread pipeline (optionally posts via Claude in Chrome).

All three channel skills read the brand voice document as their single source of truth. When your voice evolves, you edit one file and all three skills auto-update.

## How to install

### Option A: One-prompt install (Claude Code, recommended)

1. Save `SKILL.md` from this zip anywhere on your computer.
2. Open Claude Code in your terminal: `claude --dangerously-skip-permissions`
3. Paste this prompt:

> *Please install the skill from `~/Downloads/SKILL.md` (or wherever you saved it) into my Claude Code skills folder at `~/.claude/skills/brand-voice-engine/SKILL.md`. After installing, briefly tell me how to start.*

4. Restart Claude Code. Type `/brand-voice-engine` to begin.

### Option B: Manual install (any AI agent)

Drop `SKILL.md` into `~/.claude/skills/brand-voice-engine/SKILL.md` (or the equivalent skills folder for your AI agent — Codex, Gemini CLI, Cursor, Windsurf, Antigravity, etc.). Restart your agent and invoke.

### Option C: Project-local install

If you only want this skill in one project, drop the folder into `<your-project>/.claude/skills/brand-voice-engine/SKILL.md` instead of the global path.

## What's required

- **Any modern AI agent**: Claude Code, Codex (OpenAI), Gemini CLI, Antigravity, Cursor, Windsurf — all supported.
- **Web research capability**: Preferred is Perplexity MCP; falls back to WebSearch / WebFetch / `--web-search` flag depending on agent. If none available, you'll paste competitor samples instead.
- **30-45 minutes**: Interactive session, you'll answer ~15 questions in 3 batches.

## What you'll get out of it

A content engine that produces newsletters, blog posts, and tweets in your voice — not in generic AI marketing voice. Your audience will be able to tell the difference within 2-3 sends.

## Support

Email **support@apexskills.dev** with questions, edge cases, or feature requests. We read every one.

## License

MIT. Use for your own brands or your clients' brands. Don't resell the skill itself.

---

Built by [Apex Skills](https://apexskills.dev) — production-grade AI agent skills for operators.
