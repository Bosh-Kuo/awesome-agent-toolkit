# AI Coding Tool Configuration Guide

> A comprehensive reference for configuring **Antigravity**, **Claude Code**, **Opencode**, **Windsurf**, and **Codex** — covering rules, skills, agents, workflows, plugins, hooks, and MCP servers.

## 📋 Table of Contents

- [Antigravity](#-antigravity)
- [Claude Code](#-claude-code)
- [Opencode](#-opencode)
- [Windsurf](#-windsurf)
- [Codex (OpenAI)](#-codex-openai)
- [Cross-Tool Compatibility](#-cross-tool-compatibility)
- [Official Documentation Links](#-official-documentation-links)

---

## Antigravity

Antigravity is Google's agentic AI IDE powered by Gemini models.

### Rules

Custom instructions that guide agent behavior. Always loaded at session start.

| Scope     | Path                  | Format   |
| --------- | --------------------- | -------- |
| Global    | `~/.gemini/GEMINI.md` | Markdown |
| Workspace | `.agent/rules/*.md`   | Markdown |

### Skills

Specialized instruction sets with progressive discovery — only loaded when relevant.

| Scope     | Path                                           | Format                      |
| --------- | ---------------------------------------------- | --------------------------- |
| Global    | `~/.gemini/antigravity/skills/<name>/SKILL.md` | Markdown + YAML frontmatter |
| Workspace | `.agent/skills/<name>/SKILL.md`                | Markdown + YAML frontmatter |

### Workflows

User-triggered, saved sequences of steps invoked via slash commands.

| Scope     | Path                     | Format   |
| --------- | ------------------------ | -------- |
| Global    | _No specific convention_ | Markdown |
| Workspace | `.agent/workflows/*.md`  | Markdown |

### MCP Servers

| Scope     | Path                                    | Format |
| --------- | --------------------------------------- | ------ |
| Global    | `~/.gemini/antigravity/mcp_config.json` | JSON   |
| Workspace | _Relies on global or IDE interface_     | —      |

---

## Claude Code

Claude Code is Anthropic's command-line AI coding assistant.

### Rules (Memory)

Persistent instructions loaded at session start. Supports `CLAUDE.md` files and `.claude/rules/` directory for modular rule organization.

| Scope              | Path                                 | Format   |
| ------------------ | ------------------------------------ | -------- |
| Global             | `~/.claude/CLAUDE.md`                | Markdown |
| Workspace          | `./CLAUDE.md` or `.claude/CLAUDE.md` | Markdown |
| Local (gitignored) | `./CLAUDE.local.md`                  | Markdown |
| Modular rules      | `.claude/rules/*.md`                 | Markdown |

### Skills

Reusable instruction sets with YAML frontmatter for metadata.

| Scope           | Path                               | Format                      |
| --------------- | ---------------------------------- | --------------------------- |
| Global          | `~/.claude/skills/<name>/SKILL.md` | Markdown + YAML frontmatter |
| Workspace       | `.claude/skills/<name>/SKILL.md`   | Markdown + YAML frontmatter |
| Plugin-provided | `<plugin>/skills/<name>/SKILL.md`  | Markdown + YAML frontmatter |

### Agents

Subagent definitions for specialized tasks (e.g., code review, documentation).

| Scope     | Path                    | Format   |
| --------- | ----------------------- | -------- |
| Global    | `~/.claude/agents/*.md` | Markdown |
| Workspace | `.claude/agents/*.md`   | Markdown |

### Plugins

Bundles of skills, agents, hooks, and MCP servers that can be distributed and shared via marketplace.

| Scope           | Path                              | Format |
| --------------- | --------------------------------- | ------ |
| Plugin manifest | `.claude-plugin/plugin.json`      | JSON   |
| Installation    | Via `--plugin-dir` or marketplace | —      |

### Hooks

Shell commands executed at key lifecycle points (pre/post tool use, notification, etc.).

| Scope     | Path                      | Format |
| --------- | ------------------------- | ------ |
| Workspace | `.claude/settings.json`   | JSON   |
| Global    | `~/.claude/settings.json` | JSON   |

### MCP Servers

| Scope         | Path                                   | Format |
| ------------- | -------------------------------------- | ------ |
| User (local)  | `~/.claude.json`                       | JSON   |
| User (global) | `~/.claude.json` (with `--scope user`) | JSON   |
| Project       | `.mcp.json`                            | JSON   |

---

## Opencode

Opencode is an open-source terminal-based AI coding agent.

### Rules (Custom Instructions)

| Scope                         | Path                           | Format   |
| ----------------------------- | ------------------------------ | -------- |
| Global                        | `~/.config/opencode/AGENTS.md` | Markdown |
| Global (Claude-compatible)    | `~/.claude/CLAUDE.md`          | Markdown |
| Workspace                     | `AGENTS.md` (project root)     | Markdown |
| Workspace (Claude-compatible) | `CLAUDE.md` (project root)     | Markdown |

> **Note:** The `/init` command can auto-generate an `AGENTS.md` file by analyzing your codebase. Claude Code files (`CLAUDE.md`) are used as fallbacks when no `AGENTS.md` exists. To disable Claude Code compatibility, set `OPENCODE_DISABLE_CLAUDE_CODE=1`.

### Skills

Opencode supports its own paths plus Claude-compatible and agent-compatible paths for cross-tool support.

| Scope                         | Path                                        | Format                      |
| ----------------------------- | ------------------------------------------- | --------------------------- |
| Global (native)               | `~/.config/opencode/skills/<name>/SKILL.md` | Markdown + YAML frontmatter |
| Global (Claude-compatible)    | `~/.claude/skills/<name>/SKILL.md`          | Markdown + YAML frontmatter |
| Global (Agent-compatible)     | `~/.agents/skills/<name>/SKILL.md`          | Markdown + YAML frontmatter |
| Workspace (native)            | `.opencode/skills/<name>/SKILL.md`          | Markdown + YAML frontmatter |
| Workspace (Claude-compatible) | `.claude/skills/<name>/SKILL.md`            | Markdown + YAML frontmatter |
| Workspace (Agent-compatible)  | `.agents/skills/<name>/SKILL.md`            | Markdown + YAML frontmatter |

### Agents

Specialized AI assistants with custom prompts, models, and tool access.

| Scope     | Path                             | Format                                |
| --------- | -------------------------------- | ------------------------------------- |
| Global    | `~/.config/opencode/agents/*.md` | Markdown / JSON (via `opencode.json`) |
| Workspace | `.opencode/agents/*.md`          | Markdown / JSON (via `opencode.json`) |

### MCP Servers

| Scope     | Path                                                 | Format |
| --------- | ---------------------------------------------------- | ------ |
| Global    | `~/.config/opencode/opencode.json` (under `mcp` key) | JSON   |
| Workspace | `opencode.json` (under `mcp` key)                    | JSON   |

---

## Windsurf

Windsurf (formerly Codeium) is an AI-native IDE with its Cascade AI assistant.

### Rules

| Scope     | Path                                           | Format   |
| --------- | ---------------------------------------------- | -------- |
| Global    | `~/.codeium/windsurf/memories/global_rules.md` | Markdown |
| Workspace | `.windsurf/rules/*.md`                         | Markdown |

> **Activation Modes:** Rules support four modes — `Manual` (@mention), `Always On`, `Model Decision`, and `Glob` (file-pattern matching).

### AGENTS.md

Directory-scoped instruction files that automatically apply based on file location. Case-insensitive (`AGENTS.md` or `agents.md`).

| Scope     | Path                             | Format   |
| --------- | -------------------------------- | -------- |
| Root      | `AGENTS.md` (workspace/git root) | Markdown |
| Directory | `<subdirectory>/AGENTS.md`       | Markdown |

### Skills

| Scope     | Path                                         | Format                      |
| --------- | -------------------------------------------- | --------------------------- |
| Global    | `~/.codeium/windsurf/skills/<name>/SKILL.md` | Markdown + YAML frontmatter |
| Workspace | `.windsurf/skills/<name>/SKILL.md`           | Markdown + YAML frontmatter |

### Workflows

Reusable step-by-step task sequences invoked via slash commands.

| Scope     | Path                             | Format   |
| --------- | -------------------------------- | -------- |
| Global    | _System-level only (Enterprise)_ | Markdown |
| Workspace | `.windsurf/workflows/*.md`       | Markdown |

### Hooks

Shell commands executed at lifecycle events (pre/post read, write, command, MCP tool use, etc.).

| Scope        | Path                             | Format |
| ------------ | -------------------------------- | ------ |
| Workspace    | `.windsurf/cascade_hooks.json`   | JSON   |
| System-level | Via cloud dashboard (Enterprise) | JSON   |

### MCP Servers

| Scope     | Path                                  | Format |
| --------- | ------------------------------------- | ------ |
| Global    | `~/.codeium/windsurf/mcp_config.json` | JSON   |
| Workspace | _Unified in global config_            | —      |

---

## Codex (OpenAI)

Codex is OpenAI's CLI-based AI coding agent.

### Rules

| Scope     | Path                       | Format   |
| --------- | -------------------------- | -------- |
| Global    | `~/.codex/AGENTS.md`       | Markdown |
| Workspace | `AGENTS.md` (project root) | Markdown |

> **Note:** Codex also supports `AGENTS.override.md` at any level (global or directory) which takes precedence over `AGENTS.md`. Instructions are discovered from global → project root → current directory, with later files overriding earlier ones.

### Skills

| Scope     | Path                              | Format                      |
| --------- | --------------------------------- | --------------------------- |
| User      | `~/.codex/skills/<name>/SKILL.md` | Markdown + YAML frontmatter |
| Workspace | `.agents/skills/<name>/SKILL.md`  | Markdown + YAML frontmatter |

> **Note:** Codex also supports an optional `agents/openai.yaml` file within each skill directory for UI metadata, invocation policies, and tool dependencies in the Codex app.

### Agents (Multi-Agent)

Experimental multi-agent orchestration — Codex can spawn sub-agents for parallel tasks. Agent roles are defined in `config.toml` under `[agents.<name>]` sections.

| Scope     | Path                                             | Format |
| --------- | ------------------------------------------------ | ------ |
| Global    | `~/.codex/config.toml` (under `[agents.<name>]`) | TOML   |
| Workspace | `.codex/config.toml` (under `[agents.<name>]`)   | TOML   |

> **Note:** Requires enabling via `/experimental` in the CLI or adding `[features] multi_agent = true` to `config.toml`.

### MCP Servers

| Scope     | Path                                   | Format |
| --------- | -------------------------------------- | ------ |
| Global    | `~/.codex/config.toml` (under `[mcp]`) | TOML   |
| Workspace | `.codex/config.toml` (under `[mcp]`)   | TOML   |

---

## Cross-Tool Compatibility

One of the biggest challenges when using multiple AI coding tools is maintaining compatible configurations. Here are some key observations:

### Shared Standards

- **SKILL.md format**: The `SKILL.md` + YAML frontmatter format is an emerging open standard adopted by **all five tools**. Skills created in this format have the best cross-tool compatibility.
- **AGENTS.md**: Used by **Codex**, **Opencode**, and **Windsurf** as instruction files in project roots.
- **MCP Protocol**: All five tools support the Model Context Protocol, though the configuration file format differs (`JSON` vs `TOML`).

### Path Compatibility

| Convention          | Tools Using It                          |
| ------------------- | --------------------------------------- |
| `.claude/skills/`   | Claude Code, Opencode (compatible mode) |
| `.agents/skills/`   | Codex, Opencode (compatible mode)       |
| `.windsurf/skills/` | Windsurf                                |
| `.agent/skills/`    | Antigravity                             |
| `AGENTS.md`         | Codex, Opencode, Windsurf               |
| `CLAUDE.md`         | Claude Code, Opencode (compatible mode) |
| `GEMINI.md`         | Antigravity                             |

### Tips for Multi-Tool Users

1. **Skills**: Store skills in `.claude/skills/` or `.agents/skills/` for best coverage — Opencode reads both locations natively.
2. **Rules**: Maintain separate rule files (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.windsurf/rules/`) as they are tool-specific.
3. **MCP Servers**: JSON-based configs (`~/.claude.json`, `mcp_config.json`, `opencode.json`) share similar schemas; Codex's TOML format requires separate configuration.

---

## 📚 Official Documentation Links

### Antigravity

| Topic     | URL                                                                           |
| --------- | ----------------------------------------------------------------------------- |
| Overview  | [antigravity.google](https://antigravity.google)                              |
| Skills    | [Antigravity Skills Docs](https://antigravity.google/docs/skills)             |
| Rules     | [Antigravity Rules Docs](https://antigravity.google/docs/rules-workflows)     |
| Workflows | [Antigravity Workflows Docs](https://antigravity.google/docs/rules-workflows) |
| MCP       | [Antigravity MCP Docs](https://antigravity.google/docs/mcp)                   |

### Claude Code

| Topic          | URL                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------- |
| Overview       | [docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code) |
| Memory & Rules | [Memory Docs](https://docs.anthropic.com/en/docs/claude-code/memory)                     |
| Skills         | [Skills Docs](https://docs.anthropic.com/en/docs/claude-code/skills)                     |
| Plugins        | [Plugins Docs](https://docs.anthropic.com/en/docs/claude-code/plugins)                   |
| MCP            | [MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp)                           |

### Opencode

| Topic       | URL                                              |
| ----------- | ------------------------------------------------ |
| Overview    | [opencode.ai](https://opencode.ai)               |
| Config      | [Config Docs](https://opencode.ai/docs/config)   |
| Skills      | [Skills Docs](https://opencode.ai/docs/skills)   |
| Agents      | [Agents Docs](https://opencode.ai/docs/agents)   |
| MCP Servers | [MCP Docs](https://opencode.ai/docs/mcp-servers) |

### Windsurf

| Topic            | URL                                                                    |
| ---------------- | ---------------------------------------------------------------------- |
| Overview         | [windsurf.com](https://windsurf.com)                                   |
| Memories & Rules | [Memories Docs](https://docs.windsurf.com/windsurf/cascade/memories)   |
| AGENTS.md        | [AGENTS.md Docs](https://docs.windsurf.com/windsurf/cascade/agents-md) |
| Skills           | [Skills Docs](https://docs.windsurf.com/windsurf/cascade/skills)       |
| Workflows        | [Workflows Docs](https://docs.windsurf.com/windsurf/cascade/workflows) |
| Hooks            | [Hooks Docs](https://docs.windsurf.com/windsurf/cascade/hooks)         |
| MCP              | [MCP Docs](https://docs.windsurf.com/windsurf/cascade/mcp)             |

### Codex (OpenAI)

| Topic             | URL                                                                       |
| ----------------- | ------------------------------------------------------------------------- |
| Overview          | [openai.com/codex](https://openai.com/codex)                              |
| CLI Documentation | [Codex CLI Docs](https://developers.openai.com/codex)                     |
| AGENTS.md Guide   | [AGENTS.md Guide](https://developers.openai.com/codex/guides/agents-md)   |
| Skills            | [Codex Skills Docs](https://developers.openai.com/codex/skills)           |
| Multi-agents      | [Codex Multi-Agent Docs](https://developers.openai.com/codex/multi-agent) |
| MCP               | [Codex MCP Docs](https://developers.openai.com/codex/mcp)                 |
| GitHub (CLI)      | [github.com/openai/codex](https://github.com/openai/codex)                |

---

> **Last verified:** March 2026
>
> **Disclaimer:** AI coding tools evolve rapidly. Configuration paths and features may change between versions. Always refer to the official documentation for the most up-to-date information.
