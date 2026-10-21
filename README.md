# Apex Skills Free

67 free AI skill files and packs for the Claude desktop app, claude.ai, Claude Code and Codex. Add a skill, then ask Claude to use it on your next task.

## Use it in the Claude desktop app

### Pro, Max, Team or Enterprise: add the whole set once

1. In the Claude desktop app or on claude.ai, open **Customize**, then **Plugins**.
2. Click **Add**, choose **Add marketplace**, then **Add from a repository**, and paste:
   ```text
   cimbolicproductions/apex-skills-free
   ```
3. Open **Discover**, pick a skill, and click **Add**.

Skills you add here also work in Cowork, and in Claude Code when you sign in with the same account. On Team and Enterprise plans, an Owner can limit which marketplaces members add.

### Any plan, including Free: upload one skill

1. Open **Settings > Capabilities** and turn on **Code execution and file creation**. Skills need it.
2. Download one skill. Each link is a ready-to-upload ZIP:
   - [anti-slop.zip](https://github.com/cimbolicproductions/apex-skills-free/raw/main/desktop/anti-slop.zip): edit a draft that sounds like AI so it sounds like you.
   - [session-handoff.zip](https://github.com/cimbolicproductions/apex-skills-free/raw/main/desktop/session-handoff.zip): save decisions, status and the next step before you end a session.
   - [seo-keyword-fix.zip](https://github.com/cimbolicproductions/apex-skills-free/raw/main/desktop/seo-keyword-fix.zip): audit a website and plan keyword and on-page fixes.
   - All 74 skills: [CATALOG.md](CATALOG.md).
3. Open **Customize > Skills**, click **+**, choose **Create skill**, then **Upload a skill**, and pick the ZIP. Upload the ZIP as it is. Do not unzip it.

### Then use it

Ask for the task in plain words, for example: "Edit this draft so it sounds like me." Claude loads a skill when your request matches it. To pick one yourself, type `/` in the message box and choose the skill.

## Codex

Download a skill ZIP from [CATALOG.md](CATALOG.md), unzip it into the `.agents/skills` folder in your home folder, then restart Codex. Or give Codex the ZIP and ask:

> Install this skill for future sessions. Keep its scripts, references and license together, then tell me how to use it.

## Claude Code in the terminal

Plugins you add in the desktop app already sync to Claude Code. To add the marketplace from a terminal instead:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
/plugin install apex-anti-slop@apex-skills-free
```

Then use `/apex-anti-slop:anti-slop` with a draft. With GitHub SSH access set up, the short form `/plugin marketplace add cimbolicproductions/apex-skills-free` also works. From a local checkout, run `/plugin marketplace add .` in its root.

## What is in this repo

| Folder | What it holds |
|---|---|
| [`desktop/`](desktop/) | One upload-ready ZIP for each of the 74 skills |
| [`plugins/`](plugins/) | The same skills as 67 plugins, one per product, for the marketplace |
| [`products/`](products/) | The 67 original downloads, unchanged |

[START-HERE.md](START-HERE.md) walks through a first skill. [CATALOG.md](CATALOG.md) lists every skill with its download links.

The install copies in `desktop/` and `plugins/` change only the name and description lines that the Claude apps require. Thirteen older skills had no name or description, so they now have one. Nine skill names started with `claude`, a word the apps do not allow in skill names, so those names drop it: `claude-session-handoff` is now `session-handoff`. The instructions themselves are unchanged. [PROVENANCE.json](PROVENANCE.json) records every change.

## Files and licenses

All products permit personal and commercial use. The 54 existing MIT products
keep their MIT permissions. The other 13 use an Apex license that permits paid
client work but prohibits reselling or repackaging the raw skill files. Each
download includes its license. See [LICENSE.md](LICENSE.md) and
[LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the exact scope and retained notices.

if a skill saved you time, a star on this repo is the price.
