# Anthropic Claude Code configuration

This guide covers local Claude Code projects. User paths assume the default configuration directory.

## Skills

| Scope | Path | Purpose |
| --- | --- | --- |
| Project | `.claude/skills/<name>/SKILL.md` | Share skills with a repository. |
| Project subdirectory | `<subdir>/.claude/skills/<name>/SKILL.md` | Scope a skill to work in a subdirectory, such as a package in a monorepo. |
| User | `~/.claude/skills/<name>/SKILL.md` | Load a personal skill across projects. With `CLAUDE_CONFIG_DIR` set, use its `skills/` directory. |
| Managed | `.claude/skills/<name>/SKILL.md` under the managed settings directory | Distribute organization-managed skills. |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Load a skill with an enabled plugin. |

Claude Code supports a symlink for an individual skill directory. See the [README symlink example](../../README.md#share-a-skill-with-a-symlink) and [Claude Code skill discovery guide](https://code.claude.com/docs/en/skills#choose-where-skills-load).

### `SKILL.md`

Claude Code reads the skill's name, description, and Claude-specific options from its YAML frontmatter. The Markdown body supplies the instructions. The [shared example](../../examples/.agents/skills/summarize-diff/SKILL.md) uses the same skill file as Codex.

```yaml
---
name: summarize-diff
description: Summarize the current repository's pending Git changes when asked for a change summary.
---
```

- Use `/summarize-diff` to select this skill. Keep the frontmatter `name` aligned with the directory name, which determines a local skill's slash command.
- `argument-hint` displays an argument hint. Set `disable-model-invocation: true` to require user selection or `user-invocable: false` to hide the skill from the slash menu.
- `allowed-tools` can pre-approve specified tools during the skill. `context: fork` can run it in a subagent.

See the [frontmatter reference](https://code.claude.com/docs/en/skills#frontmatter-reference) and [Codex metadata example](openai.md#agentsopenaiyaml).

## MCP

Claude Code stores server definitions under `mcpServers` in JSON. When the same server name is defined in several scopes, the precedence is `local`, `project`, then `user`.

| Scope | Location | Who gets it |
| --- | --- | --- |
| `project` | `.mcp.json` at the repository root | The current project, shareable through Git. |
| `local` | The current project's entry under `projects` in `~/.claude.json` | Only you in this project. This is the default scope of `claude mcp add`. |
| `user` | Top-level `mcpServers` in `~/.claude.json` | Only you across projects. |

```json
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp/oauth"
    },
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

- **HTTP servers** use `type` and `url`. Use `/mcp` in Claude Code to authenticate an OAuth server.
- **Local stdio servers** use `command` and `args`. They can also set `env`.
- **Environment references** in `.mcp.json` can use `${VAR}` or `${VAR:-default}` in supported fields. Consult the authentication reference when using credentials in headers.

To add a server with Claude Code's native CLI, pick one scope.

```bash
claude mcp add --scope project --transport http context7 https://mcp.context7.com/mcp/oauth
claude mcp add --scope local --transport http context7 https://mcp.context7.com/mcp/oauth
claude mcp add --scope user --transport http context7 https://mcp.context7.com/mcp/oauth
```

See the [MCP scope guide](https://code.claude.com/docs/en/mcp#mcp-installation-scopes), [environment variable and authentication reference](https://code.claude.com/docs/en/mcp#environment-variable-expansion-in-mcpjson), and [project example](../../examples/.mcp.json).

## Configuration layers

| Scope | Location | What it controls |
| --- | --- | --- |
| Managed | `managed-settings.json`, MDM, or organization settings | Enforce organization settings. |
| Current session | `--settings <file-or-json>` | Override settings for the current run. |
| Project, personal | `.claude/settings.local.json` | Keep personal project settings on your machine. |
| Project, shared | `.claude/settings.json` | Share team settings such as permissions and hooks. |
| User | `~/.claude/settings.json` | Set personal defaults across projects. |

Higher layers generally take precedence. Permission lists merge across layers. Use `/status` to see which settings sources are active.

Use `CLAUDE.md` for persistent instructions. Define custom subagents in `.claude/agents/<name>.md` or `~/.claude/agents/<name>.md`, with frontmatter such as `model` and `tools`.

See the [settings reference](https://code.claude.com/docs/en/settings), [CLAUDE.md guide](https://code.claude.com/docs/en/memory), and [subagent guide](https://code.claude.com/docs/en/sub-agents).

## Model, directories, and command permissions

Merge this example into `.claude/settings.json`. Machine-specific `additionalDirectories` entries can go in `.claude/settings.local.json`.

```json
{
  "model": "sonnet",
  "permissions": {
    "defaultMode": "default",
    "additionalDirectories": ["/absolute/path/to/shared-workspace"],
    "allow": ["Bash(git status *)"],
    "ask": ["Bash(git fetch *)"],
    "deny": ["Bash(git push *)", "Read(/.env)", "Edit(/secrets/**)"]
  }
}
```

- **Model.** Use a model ID or an alias such as `sonnet` or `opus`. Use `/model` and `/effort` to change the current session.
- **Permission mode.** `default` uses standard prompts, `acceptEdits` accepts common file edits in the working directories, and `plan` supports investigation and planning.
- **Additional directories.** Use `additionalDirectories` for persistent access or `/add-dir` for this session. The same file permission rules apply to added directories.
- **Command and tool rules.** Claude Code evaluates `deny`, then `ask`, then `allow`. In Bash rules, `git status *` also matches plain `git status`.
- **Path rules.** For `Read(...)` and `Edit(...)`, start an absolute path with `//`. `~/` starts at home, `/path` is relative to the settings source, and `./path` is relative to the current directory.

See the [model configuration guide](https://code.claude.com/docs/en/model-config) and [permission rules reference](https://code.claude.com/docs/en/permissions).

## Bash sandbox

Use `/sandbox` to manage the Bash sandbox. This example enables isolation, keeps permission prompts, and disables out-of-sandbox retries.

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": false,
    "allowUnsandboxedCommands": false,
    "filesystem": {
      "denyRead": [".env"],
      "denyWrite": ["./secrets"]
    },
    "network": {
      "allowedDomains": ["registry.npmjs.org"]
    }
  }
}
```

Sandbox filesystem paths use a single leading slash for absolute paths. Use `allowWrite` to add writable paths and `denyRead` or `denyWrite` to restrict subprocesses. Built-in file tools follow the separate `permissions` rules above.

See the [sandbox guide](https://code.claude.com/docs/en/sandboxing) and [settings key reference](https://code.claude.com/docs/en/settings-reference).
