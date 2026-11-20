# OpenAI Codex configuration

This guide covers local projects in the Codex desktop app. Paths use macOS and Linux conventions.

## Skills

| Scope | Path | Purpose |
| --- | --- | --- |
| Project | `.agents/skills/<name>/SKILL.md` | Share skills in a repository. Codex scans from the current directory back to the Git root, so subprojects can have their own skills. |
| User | `~/.agents/skills/<name>/SKILL.md` | Load a personal skill across projects. This is also where Skills CLI targets Codex with `-a codex -g`. |
| Legacy user path | `$CODEX_HOME/skills/<name>/SKILL.md` | Load older personal installs. Some built-in tools still use this path. |
| Administrator | `/etc/codex/skills/<name>/SKILL.md` | Deploy shared skills to users on the same machine or container. |
| Bundled | `$CODEX_HOME/skills/.system/` | Codex manages this cache for skills shipped with the app. |

- `CODEX_HOME` defaults to `~/.codex`. Changing it moves the lookup for user configuration and bundled skills. `~/.agents/skills/` still resolves from your home directory.
- Use `.agents/skills/` for new project skills. Codex also supports symlinked skill directories and reads `.codex/skills/` from trusted project configuration layers.
- If two entries have the same name, disable one with a `[[skills.config]]` entry in `config.toml`. Set `path` to the absolute path of its `SKILL.md` and `enabled = false`.

See the [Codex skills guide](https://developers.openai.com/codex/skills), [skill discovery source](https://github.com/openai/codex/blob/main/codex-rs/ext/skills/src/host_roots.rs), and [bundled skill cache source](https://github.com/openai/codex/blob/main/codex-rs/skills/src/lib.rs).

### `SKILL.md`

The YAML frontmatter gives the skill its `name` and `description`. The Markdown body tells the agent what to do. This is the same [shared skill](../../examples/.agents/skills/summarize-diff/SKILL.md) used in the Claude Code example.

```markdown
---
name: summarize-diff
description: Summarize the current repository's pending Git changes when asked for a change summary.
---

Inspect `git status --short`, `git diff`, and `git diff --cached`. Summarize the changes by purpose, mention untracked files by name, and identify any tests whose results are known. Leave the working tree and staging area untouched.
```

In the Codex composer, explicitly select the skill with a prompt such as `Use $summarize-diff to summarize the staged and unstaged changes.`

### `agents/openai.yaml`

Some downloaded skills include an `agents/openai.yaml` file inside the skill directory. This optional file controls how Codex presents the skill and when it can invoke it.

```yaml
interface:
  display_name: "Summarize Git Diff"
  short_description: "Summarize pending Git changes"
  default_prompt: "Use $summarize-diff to summarize the staged and unstaged changes."
policy:
  allow_implicit_invocation: false
```

- `interface` sets the display name, description, and starter prompt shown in the app. It can also reference icons.
- `policy.allow_implicit_invocation` defaults to `true`. Set it to `false` to require explicit selection.
- `dependencies.tools` can declare MCP tools the skill depends on.

See the [metadata reference](https://developers.openai.com/codex/skills#optional-metadata) and [shared example file](../../examples/.agents/skills/summarize-diff/agents/openai.yaml).

## MCP

In the desktop app, open **Settings → MCP servers** to add, manage, or authenticate servers. To share a server with a trusted project, put its configuration in `.codex/config.toml`. For a user-wide server, use `$CODEX_HOME/config.toml`.

Each server has a `[mcp_servers.<name>]` table.

```toml
[mcp_servers.context7]
url = "https://mcp.context7.com/mcp/oauth"

[mcp_servers.chrome-devtools]
command = "npx"
args = ["-y", "chrome-devtools-mcp@latest"]
```

- **Streamable HTTP** uses `url`. For token-based authentication, `bearer_token_env_var` and `env_http_headers` reference environment variables. For OAuth, use **Authenticate** in the app's server settings.
- **Local stdio** uses `command` and `args`. Use `env_vars` to pass named environment variables or `cwd` to set the launch directory.
- **Tool access** can be narrowed with `enabled_tools` and `disabled_tools`. The deny list is applied after the allow list. Use `enabled = false` to disable the entire server.

See the [desktop MCP guide](https://learn.chatgpt.com/docs/extend/mcp?surface=app), [project example](../../examples/.codex/config.toml), and [add-mcp guide](../cli-tools/npx-add-mcp.md).

## Configuration layers

| Scope | Location | What it controls |
| --- | --- | --- |
| Current session | Desktop composer controls | Select the model, reasoning effort, and permissions for the current session. |
| Project | `.codex/config.toml` | Set defaults for a trusted repository or subdirectory. The closest configuration to the working directory takes precedence. |
| User | `$CODEX_HOME/config.toml` (default `~/.codex/config.toml`) | Set personal defaults across projects. |
| System | `/etc/codex/config.toml` | Set machine-wide defaults on Unix. |
| Managed policy | `/etc/codex/requirements.toml` or organization policy | Enforce constraints on settings such as permissions and sandbox modes. |

Codex loads project `.codex/` configuration and command rules after you trust the project. Put repository instructions for the agent in `AGENTS.md`.

See the [configuration precedence guide](https://developers.openai.com/codex/config-basic#configuration-precedence) and [managed settings reference](https://learn.chatgpt.com/docs/enterprise/managed-configuration).

## Model, directories, and sandbox

Use the desktop composer's model and permissions controls for the current session. For persistent defaults, put top-level keys before the first TOML table. Choose a model ID available to your account and replace the example path with a directory you want Codex to edit.

```toml
model = "gpt-6.1-sol"
model_reasoning_effort = "medium"
approval_policy = "on-request"
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
writable_roots = ["/absolute/path/to/shared-workspace"]
network_access = false
```

- **Filesystem access.** `read-only` supports inspection. `workspace-write` allows edits in the workspace and additional `writable_roots`. `danger-full-access` disables the local sandbox.
- **Network access.** `network_access` controls network access for commands in the `workspace-write` sandbox.
- **Approvals.** `on-request` lets Codex ask for permission when needed. `never` disables approval requests while the sandbox still controls access.

To grant or deny access to specific paths, use a named permission profile (beta). If you use a profile, remove `sandbox_mode` and `[sandbox_workspace_write]` from active configuration layers.

```toml
default_permissions = "project-edit"

[permissions.project-edit]
extends = ":workspace"

[permissions.project-edit.filesystem.":workspace_roots"]
"docs" = "read"
".env" = "deny"
```

Use `[permissions.<name>.workspace_roots]` to add roots and `[permissions.<name>.network]` to configure network access for the profile.

See the [desktop settings guide](https://learn.chatgpt.com/docs/developer-settings), [sandbox and approvals guide](https://learn.chatgpt.com/docs/agent-approvals-security#sandbox-and-approvals), and [permission profile reference](https://developers.openai.com/codex/permissions).

## Command rules

Put personal rules in `$CODEX_HOME/rules/default.rules` and project rules in `.codex/rules/*.rules` in a trusted repository. A Starlark `prefix_rule` matches the first arguments of a command.

```python
prefix_rule(pattern = ["git", "status"], decision = "allow")
prefix_rule(pattern = ["git", "fetch"], decision = "prompt")
prefix_rule(pattern = ["git", "push"], decision = "forbidden")
```

- `allow` permits the matching command to run outside the sandbox without prompting.
- `prompt` requires approval.
- `forbidden` blocks the matching command.

The strictest matching rule wins. Filesystem and network boundaries come from the sandbox settings. Restart Codex to load rule changes.

See the [command rules reference](https://developers.openai.com/codex/rules).
