# Start with one skill

67 free AI skill files and packs for the Claude desktop app, claude.ai, Claude Code and Codex. Pick one task, add the skill for it, and try it.

## 1. Pick your next task

| Your task | Skill | Download for the desktop app |
|---|---|---|
| Edit a draft that sounds like AI. | **Slop Killer** | [anti-slop.zip](https://github.com/cimbolicproductions/apex-skills-free/raw/main/desktop/anti-slop.zip) |
| End a work session with a clear handoff and a prompt to resume. | **Session Handoff** | [session-handoff.zip](https://github.com/cimbolicproductions/apex-skills-free/raw/main/desktop/session-handoff.zip) |
| Audit a website and plan keyword and on-page SEO fixes. | **Automated SEO Orchestrator** | [seo-keyword-fix.zip](https://github.com/cimbolicproductions/apex-skills-free/raw/main/desktop/seo-keyword-fix.zip) |

Something else? [CATALOG.md](CATALOG.md) has all 74 skills.

## 2. Add it to Claude

### Claude desktop app or claude.ai, any plan

1. Open **Settings > Capabilities** and turn on **Code execution and file creation**.
2. Download the ZIP from the table above.
3. Open **Customize > Skills**, click **+**, choose **Create skill**, then **Upload a skill**, and pick the ZIP. Upload it as it is. Do not unzip it.
4. Make sure the skill's switch is on in your skills list.

### Pro, Max, Team or Enterprise: get every skill in one place

1. Open **Customize > Plugins**.
2. Click **Add**, choose **Add marketplace**, then **Add from a repository**, and paste `cimbolicproductions/apex-skills-free`.
3. Open **Discover**, pick the skill, and click **Add**.

You only add the marketplace once. After that, every skill in this repo shows up in **Discover**.

## 3. Use it

Ask for the task in plain words. Claude loads the skill when your request matches it.

| Skill | Try saying |
|---|---|
| Slop Killer | "Edit this draft so it sounds like me: [paste draft]" |
| Session Handoff | "Save a handoff for this session and write the prompt to resume it." |
| Automated SEO Orchestrator | "Audit [your website] in plan-only mode." |

To pick a skill yourself, type `/` in the message box and choose it. Start the SEO skill in plan-only mode. It can also change a site's code, and only does that if you choose apply mode.

## Other apps

**Codex.** Unzip the skill into the `.agents/skills` folder in your home folder, then restart Codex. Or give Codex the ZIP and ask it to install the skill and keep its files together.

**Claude Code in the terminal.** Skills you add in the desktop app sync to Claude Code when you sign in with the same account. To use the terminal instead:

```text
/plugin marketplace add https://github.com/cimbolicproductions/apex-skills-free.git
/plugin install apex-anti-slop@apex-skills-free
/plugin install apex-session-handoff@apex-skills-free
/plugin install apex-seo-keyword-fix@apex-skills-free
```

Install only the one you need, then run it with your task:

```text
/apex-anti-slop:anti-slop Edit this draft in my voice: [draft]
/apex-session-handoff:session-handoff Save a handoff for this session and write the next session's resume prompt.
/apex-seo-keyword-fix:seo-keyword-fix Audit [site URL or local project] in plan-only mode.
```

## Keep the files together

Some skills come with scripts, references or templates. Each ZIP in [`desktop/`](desktop/) already holds everything its skill needs plus its license, so upload or unzip the whole ZIP. [`products/`](products/) keeps the 67 original downloads unchanged.

All products permit personal and commercial use. Existing MIT products retain
their MIT permissions; 13 legacy products use an Apex license that permits
client work but prohibits reselling or repackaging the raw files. Read
[LICENSE.md](LICENSE.md) and [LICENSE-NOTICE.md](LICENSE-NOTICE.md) for the exact
scope and retained attribution.

if a skill saved you time, a star on this repo is the price.
