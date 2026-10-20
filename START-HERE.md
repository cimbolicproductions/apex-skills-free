# Start with one skill

67 free AI agent skills for Claude Code, Codex, and Gemini CLI. Drop them in, tell your agent to set them up, start with one skill for your next task.

There are 67 product files and packs. Packs can contain several workflows, including copies of standalone skills. Browse [CATALOG.md](CATALOG.md) when you need something beyond the three starters below.

## 1. Pick your next task

| Your task | Pick |
|---|---|
| Edit a draft that sounds like AI. | **Slop Killer**, in [anti-slop.zip](products/anti-slop.zip). |
| Finish a coding session with a clear handoff and resume prompt. | **Claude Code Session Handoff**, in [claude-session-handoff.md](products/claude-session-handoff.md). |
| Audit a site and build a keyword and on-page SEO plan. | **Automated SEO Orchestrator**, in [SEO-Keyword-Fix-Pipeline.md](products/SEO-Keyword-Fix-Pipeline.md). |

## 2. Give the files to your agent

Drop the selected file or ZIP into Codex or Claude Code, or give the agent access to this folder. For a ZIP, keep the extracted skill with all its scripts, references, and templates.

Paste this with your task:

> Install this skill for future sessions using your supported skill location. Preserve its support files and attribution, and tell me how to invoke it. Then apply it to this task: [describe your task].

For Codex, also ask the agent to verify that the installed skill is discovered. Thirteen legacy products have no YAML name or description, which Codex requires for reusable skills. The agent can add metadata to an installed copy or wrapper while keeping the original downloads unchanged. Attached Markdown works as task instructions without a reusable install.

If your agent cannot access attachments, extract the product into a local folder and give it that path. Gemini CLI users can give their agent the same prompt and local files.

You can also use a skill for one task without installing it: attach its Markdown and relevant references, describe your task, and ask the agent to apply the workflow.

## 3. Or install a Claude Code plugin

The marketplace has one plugin per product. Add it in Claude Code:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
```

Install the starter you chose:

```text
/plugin install apex-anti-slop@apex-skills-free
/plugin install apex-session-handoff@apex-skills-free
/plugin install apex-seo-keyword-fix@apex-skills-free
```

You only need to run the install command for your chosen skill. Invoke it with your task:

```text
/apex-anti-slop:anti-slop Edit this draft in my voice: [draft]
/apex-session-handoff:claude-session-handoff Save a handoff for this session and write the next session's resume prompt.
/apex-seo-keyword-fix:seo-keyword-fix Audit [site URL or local project] in plan-only mode.
```

The session handoff plugin keeps the original skill name `claude-session-handoff`, so its invocation includes that name.

HTTPS avoids requiring GitHub SSH keys. With GitHub SSH access already set up,
you can instead use `/plugin marketplace add cimbolicproductions/apex-skills-free`.

If you have a local checkout, you can instead open Claude Code in its root and run:

```text
/plugin marketplace add .
```

## Keep the useful files together

[`products/`](products/) contains all 67 original downloads. [`plugins/`](plugins/) contains their extracted Claude Code payloads and plugin descriptors. Some packs expose multiple skills and include shared scripts or references. Keep the whole selected pack together when moving or installing it.

All products permit personal and commercial use. Existing MIT products retain
their MIT permissions; 13 legacy products use an Apex license that permits
client work but prohibits reselling or repackaging the raw files. Read
[LICENSE.md](LICENSE.md) and [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the exact
scope and retained attribution.

if a skill saved you time, a star on this repo is the price.
