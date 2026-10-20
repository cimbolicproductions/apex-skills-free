---
name: claude-mcp-server-builder
description: "Use when creating a custom MCP server, exposing an API or script as Claude tools, designing MCP tool schemas, or building with FastMCP or the MCP SDK. Do not use for merely installing existing servers."
license: MIT
metadata:
  author: dominic-operator-pack
  version: '1.0'
---

# MCP Server Builder

## When to Use This Skill

- The user wants to build a custom tool for Claude.
- An internal API, script, database, or workflow should become MCP-accessible.
- The user needs a tool schema, auth plan, and implementation scaffold.

## When Not to Use This Skill

- The user only needs to install a public MCP server.
- A normal CLI command is enough and does not need LLM tool exposure.

## Intake Questions

Ask only for missing information that changes the output. If enough context exists, proceed and state assumptions.

- What real-world action or data source should the tool expose?
- Who is allowed to call it and what permissions are required?
- What are the inputs, outputs, failure modes, and rate limits?

## Operating Workflow

- Design the smallest set of tools possible. Avoid dumping an entire API surface into MCP.
- For each tool, define name, description, JSON schema, examples, success output, and errors.
- Add input validation, timeouts, pagination, and safe defaults.
- Use environment variables or OAuth for secrets. Never hardcode tokens.
- Block private IP access and risky write operations unless explicitly needed.
- Build a smoke test that calls each tool with a valid and invalid input.
- Document registration steps for Claude Desktop or Claude Code.

## Output Contract

Always produce practical artifacts the user can copy, paste, configure, or hand to a contractor.

- Tool inventory table.
- Security and permission model.
- FastMCP or TypeScript MCP scaffold.
- Registration snippet and test commands.

## Quality Checklist

Before finalizing, verify:

- Every tool has a narrow, verb-based purpose.
- Descriptions tell Claude when to call the tool and when not to.
- Dangerous actions require confirmation or are split into draft/execute steps.

## Research-Backed Defaults and Sources

- Anthropic Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Anthropic Claude Code hooks guide: https://code.claude.com/docs/en/hooks-guide
- Anthropic Claude Code MCP guide: https://code.claude.com/docs/en/mcp
- Model Context Protocol server docs: https://modelcontextprotocol.io/docs/develop/build-server
- MCP security best practices: https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices
- HumanLayer CLAUDE.md guidance: https://www.humanlayer.dev/blog/writing-a-good-claude-md

