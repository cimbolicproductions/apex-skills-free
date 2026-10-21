---
name: mcp-setup
description: "Use when adding, configuring, auditing, or troubleshooting MCP servers in Claude Code or Claude Desktop, including scope, auth, tool collisions, JSON config, restarts, and context bloat."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# Claude MCP Setup and Troubleshooting

## When to Use This Skill

- The user wants Claude to connect to GitHub, Supabase, Stripe, Notion, Playwright, Context7, Firecrawl, or another tool through MCP.
- An MCP server is not appearing, not authenticating, crashing, or bloating context.
- The user asks whether to use local, user, project, or global MCP scope.

## When Not to Use This Skill

- A native CLI or connector already solves the task more reliably.
- The request is to build a new MCP server from scratch; use mcp-server-builder instead.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- Which MCP server and which client: Claude Code, Claude Desktop, Cursor, or another host?
- Transport type: stdio, SSE, HTTP, or remote OAuth?
- What exact error appears in /mcp, logs, or startup output?

## Operating Workflow

- Audit existing servers first. Keep only 5 to 8 relevant servers enabled for a project.
- Prefer project/local scope for repo-specific tools and user scope for reusable personal tools.
- Verify absolute paths, executable permissions, JSON validity, environment variables, and required restarts.
- Check tool-name collisions and namespace server tools when multiple servers expose generic names.
- Prefer least-privilege credentials and read-only scopes until write access is required.
- Document how to remove or disable the server if it causes token bloat or failures.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- MCP diagnosis.
- Install/config commands or JSON snippet.
- Security checklist.
- Troubleshooting decision tree.

## Quality Checklist

Before finalizing, verify:

- The setup avoids unnecessary always-on MCP servers.
- The user knows how to verify success with /mcp or list commands.
- Auth and secrets are handled through environment variables or official OAuth.

## Research-Backed Defaults and Sources

- Anthropic Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic Claude Code hooks guide: https://code.claude.com/docs/en/hooks-guide
- Anthropic Claude Code MCP guide: https://code.claude.com/docs/en/mcp
- Model Context Protocol server docs: https://modelcontextprotocol.io/docs/develop/build-server
- MCP security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- HumanLayer CLAUDE.md guidance: https://www.humanlayer.dev/blog/writing-a-good-claude-md

