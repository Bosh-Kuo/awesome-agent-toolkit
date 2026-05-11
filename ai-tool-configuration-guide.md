# AI Coding Tool Configuration Guide

> A comprehensive reference for configuring **Antigravity**, **Claude Code**, **Opencode**, **Windsurf**, and **Codex** — covering rules, skills, agents, workflows, plugins, hooks, and MCP servers.

## 📋 Table of Contents

- [Antigravity](#antigravity)
- [Claude Code](#claude-code)
- [Opencode](#opencode)
- [Windsurf](#windsurf)
- [Codex (OpenAI)](#codex-openai)
- [Cross-Tool Compatibility](#cross-tool-compatibility)
- [Official Documentation Links](#official-documentation-links)

---

## Antigravity

Antigravity is Google's agentic AI IDE powered by Gemini models.

### Rules

Custom instructions that guide agent behavior. Always loaded at session start.

| Scope     | Path                  | Format   |
| --------- | --------------------- | -------- |
| Global    | `~/.gemini/GEMINI.md` | Markdown |
| Workspace | `.agents/rules/*.md`  | Markdown |

### Skills

Specialized instruction sets with progressive discovery — only loaded when relevant.

| Scope     | Path                                           | Format                      |
| --------- | ---------------------------------------------- | --------------------------- |
| Global    | `~/.gemini/antigravity/skills/<name>/SKILL.md` | Markdown + YAML frontmatter |
| Workspace | `.agents/skills/<name>/SKILL.md`               | Markdown + YAML frontmatter |

### Workflows

User-triggered, saved sequences of steps invoked via slash commands.

| Scope     | Path                     | Format   |
| --------- | ------------------------ | -------- |
| Global    | _No specific convention_ | Markdown |
| Workspace | `.agents/workflows/*.md` | Markdown |

### MCP Servers

| Scope     | Path                                    | Format |
| --------- | --------------------------------------- | ------ |
| Global    | `~/.gemini/antigravity/mcp_config.json` | JSON   |
| Workspace | _Relies on global or IDE interface_     | —      |

---

## Claude Code

Claude Code is Anthropic's command-line AI coding assistant.

### Configuration Scopes

Claude Code uses a **scope system** to determine where settings apply and who they're shared with. More specific scopes take precedence over broader ones.

| Scope       | Location                                                                   | Affects                        | Shared with Team?      |
| ----------- | -------------------------------------------------------------------------- | ------------------------------ | ---------------------- |
| **Managed** | Server-managed settings, plist/registry, or system `managed-settings.json` | All users on the machine       | Yes (deployed by IT)   |
| **User**    | `~/.claude/` directory                                                     | You, across all projects       | No                     |
| **Project** | `.claude/` in repository                                                   | All collaborators on this repo | Yes (committed to git) |
| **Local**   | `.claude/settings.local.json`                                              | You, in this repo only         | No (gitignored)        |

**Precedence** (highest → lowest): Managed → CLI args → Local → Project → User

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

### Settings

Persistent behavior configuration via `settings.json`. Controls permissions, hooks, environment variables, and more.

| Scope   | Path                                                      | Format |
| ------- | --------------------------------------------------------- | ------ |
| Managed | System dir `managed-settings.json` or MDM/registry policy | JSON   |
| Global  | `~/.claude/settings.json`                                 | JSON   |
| Project | `.claude/settings.json`                                   | JSON   |
| Local   | `.claude/settings.local.json`                             | JSON   |

### Plugins

Bundles of skills, agents, hooks, and MCP servers that can be distributed and shared via marketplace.

| Scope    | Path                          | Format |
| -------- | ----------------------------- | ------ |
| Global   | `~/.claude/settings.json`     | JSON   |
| Project  | `.claude/settings.json`       | JSON   |
| Local    | `.claude/settings.local.json` | JSON   |
| Manifest | `.claude-plugin/plugin.json`  | JSON   |

### Hooks

Shell commands executed at key lifecycle points (pre/post tool use, notification, etc.).

| Scope     | Path                      | Format |
| --------- | ------------------------- | ------ |
| Workspace | `.claude/settings.json`   | JSON   |
| Global    | `~/.claude/settings.json` | JSON   |

### MCP Servers

| Scope   | Path                                          | Format |
| ------- | --------------------------------------------- | ------ |
| Global  | `~/.claude.json` (with `--scope user`)        | JSON   |
| Project | `.mcp.json`                                   | JSON   |
| Local   | `~/.claude.json` (project-scoped, gitignored) | JSON   |

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

Codex is OpenAI's AI coding agent, available through the Codex CLI, IDE extension, desktop app, and cloud interface.

### Rules

| Scope     | Path                                             | Format   |
| --------- | ------------------------------------------------ | -------- |
| Global    | `~/.codex/AGENTS.md` or `~/.codex/AGENTS.override.md` | Markdown |
| Workspace | `AGENTS.md` or `AGENTS.override.md` from project root down to the current directory | Markdown |

> **Note:** Codex reads one instruction file per level. It checks `AGENTS.override.md` before `AGENTS.md`, then any filenames configured in `project_doc_fallback_filenames`. Instructions are concatenated from global → project root → current directory, so files closer to the current directory take precedence.

### Skills

| Scope     | Path                                  | Format                      |
| --------- | ------------------------------------- | --------------------------- |
| Repository | `.agents/skills/<name>/SKILL.md` in the current directory, parent directories, or repository root | Markdown + YAML frontmatter |
| User      | `~/.agents/skills/<name>/SKILL.md`    | Markdown + YAML frontmatter |
| Admin     | `/etc/codex/skills/<name>/SKILL.md`   | Markdown + YAML frontmatter |
| System    | Bundled with Codex                    | Markdown + YAML frontmatter |

> **Note:** Codex also supports an optional `agents/openai.yaml` file within each skill directory for Codex app UI metadata, invocation policy, and tool dependencies. Per-skill enablement can be controlled with `[[skills.config]]` entries in `~/.codex/config.toml`.

### Agents (Multi-Agent)

Multi-agent orchestration lets Codex spawn sub-agents for parallel tasks. Agent limits and roles are configured in `config.toml` under `agents.*` keys such as `[agents.<name>]`.

| Scope     | Path                                                   | Format |
| --------- | ------------------------------------------------------ | ------ |
| Global    | `~/.codex/config.toml` (under `agents.*` / `[agents.<name>]`) | TOML   |
| Workspace | `.codex/config.toml` (under `agents.*` / `[agents.<name>]`)   | TOML   |

> **Note:** The `features.multi_agent` flag controls the collaboration tools (`spawn_agent`, `send_input`, `resume_agent`, `wait_agent`, and `close_agent`) and is stable/on by default in current Codex docs.

### MCP Servers

| Scope     | Path                                                | Format |
| --------- | --------------------------------------------------- | ------ |
| Global    | `~/.codex/config.toml` (under `[mcp_servers.<id>]`) | TOML   |
| Workspace | `.codex/config.toml` (under `[mcp_servers.<id>]`)   | TOML   |

---

## Cross-Tool Compatibility

One of the biggest challenges when using multiple AI coding tools is maintaining compatible configurations. Here are some key observations:

### Shared Standards

- **SKILL.md format**: The `SKILL.md` + YAML frontmatter format is an emerging open standard adopted by **all five tools**. Skills created in this format have the best cross-tool compatibility.
- **AGENTS.md**: Used by **Codex**, **Opencode**, and **Windsurf** as instruction files in project roots.
- **MCP Protocol**: All five tools support the Model Context Protocol, though the configuration file format differs (`JSON` vs `TOML`).

### Path Compatibility

| Convention          | Tools Using It                                 |
| ------------------- | ---------------------------------------------- |
| `.claude/skills/`   | Claude Code, Opencode (compatible mode)        |
| `.agents/skills/`   | Codex, Antigravity, Opencode (compatible mode) |
| `.windsurf/skills/` | Windsurf                                       |
| `AGENTS.md`         | Codex, Opencode, Windsurf                      |
| `CLAUDE.md`         | Claude Code, Opencode (compatible mode)        |
| `GEMINI.md`         | Antigravity                                    |

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

| Topic             | URL                                                                                      |
| ----------------- | ---------------------------------------------------------------------------------------- |
| Overview          | [docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code) |
| Memory & Rules    | [Memory Docs](https://docs.anthropic.com/en/docs/claude-code/memory)                     |
| Skills            | [Skills Docs](https://docs.anthropic.com/en/docs/claude-code/skills)                     |
| Agents            | [Agents Docs](https://docs.anthropic.com/en/docs/claude-code/sub-agents)                 |
| Settings & Scopes | [Settings Docs](https://code.claude.com/docs/zh-TW/settings#configuration-scopes)        |
| Plugins           | [Plugins Docs](https://docs.anthropic.com/en/docs/claude-code/plugins)                   |
| MCP               | [MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp)                           |

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
| Config Reference  | [Codex Config Reference](https://developers.openai.com/codex/config-reference) |
| MCP               | [Codex MCP Docs](https://developers.openai.com/codex/mcp)                 |
| GitHub (CLI)      | [github.com/openai/codex](https://github.com/openai/codex)                |

---

> **Last verified:** March 2026
>
> **Disclaimer:** AI coding tools evolve rapidly. Configuration paths and features may change between versions. Always refer to the official documentation for the most up-to-date information.
