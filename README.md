# Apex Skills Free

67 free AI agent skills for Claude Code, Codex, and Gemini CLI. Drop them in, tell your agent to set them up, start with one skill for your next task.

The download contains **67 product files and packs**, not 67 unique workflows. Some packs contain several workflows and copies of standalone skills.

## Drop it into your agent

Download this repository with **Code > Download ZIP**, extract it, or clone it:

```sh
git clone https://github.com/cimbolicproductions/apex-skills-free.git
```

Give Codex or Claude Code the skill file, its ZIP, or this folder. Ask:

> Install the skill I selected for future sessions using your supported skill location. Keep its scripts, references, templates, and attribution together. Tell me how to invoke it, then help me use it for my next task.

Thirteen legacy files have no YAML metadata. Codex needs a skill name and description for reusable installation, so ask your agent to add that metadata to an installed copy or wrapper and verify that Codex discovers it. Keep this package's originals unchanged. You can also attach the original Markdown as instructions for a single task.

Start with one skill. Your agent can inspect the files and choose the right installation steps for its environment. The original downloads are in [`products/`](products/). See [START-HERE.md](START-HERE.md) for a walkthrough and [CATALOG.md](CATALOG.md) for the full inventory.

## Three places to start

| Skill | Use it when | Original download |
|---|---|---|
| **Slop Killer** | A draft sounds generic and you want an edit in your voice. | [anti-slop.zip](products/anti-slop.zip) |
| **Claude Code Session Handoff** | You need to save decisions, work status, and the next action before ending a session. | [claude-session-handoff.md](products/claude-session-handoff.md) |
| **Automated SEO Orchestrator** | You want a site audit, keyword research, and a plan for on-page changes. Start in `plan-only` mode. | [SEO-Keyword-Fix-Pipeline.md](products/SEO-Keyword-Fix-Pipeline.md) |

## Claude Code marketplace

In Claude Code, run:

```text
/plugin marketplace add cimbolicproductions/apex-skills-free
/plugin install apex-anti-slop@apex-skills-free
```

Then use `/apex-anti-slop:anti-slop` with a draft.

To use a local checkout instead, open Claude Code in its root and add it with:

```text
/plugin marketplace add .
```

Each product has its own plugin, so you can install the one you need. Codex and Gemini CLI users should use the file installation prompt above; these marketplace commands are for Claude Code.

## Files and licenses

Original product files are preserved in [`products/`](products/). The [`plugins/`](plugins/) folder exposes their workflows and support files to Claude Code. Existing attribution stays with the files.

All products permit personal and commercial use. The 54 existing MIT products
keep their MIT permissions. The other 13 use an Apex license that permits paid
client work but prohibits reselling or repackaging the raw skill files. See
[LICENSE.md](LICENSE.md) and [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the exact
scope and retained notices.

if a skill saved you time, a star on this repo is the price.
