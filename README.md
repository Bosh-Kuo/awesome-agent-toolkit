<div align="center">

<img src="./assets/cover.jpg" alt="Awesome Agent Toolkit cover" width="600"/>

# Awesome Agent Toolkit

</div>

A collection of reusable agent skills and MCP servers from my daily development work with **Codex** and **Claude Code**. Install third-party tools from their upstream sources. My own skills live in [`skills/`](skills/).

| What you need | Where to look |
| --- | --- |
| Find a skill or MCP server | [Skill catalog](skills.md) · [MCP catalog](mcp.md) |
| Install, update, or remove tools | [`npx skills`](docs/cli-tools/npx-skills.md) · [`npx add-mcp`](docs/cli-tools/npx-add-mcp.md) |
| Configure your agent | [OpenAI Codex](docs/config-guidance/openai.md) · [Anthropic Claude Code](docs/config-guidance/antropic.md) |
| See how the files fit together | [Project example](examples/) |

## Install a skill

1. Install Node.js 22.20.0 or later, npm, and Git. Open a terminal at the root of the project where you want to use the skill.
2. Pick a skill from the [catalog](skills.md) and run its install command. For example, this installs Vercel React Best Practices for Codex and Claude Code in the current project.

   ```bash
   npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices -a codex -a claude-code
   ```

Add `-g` to install the skill across your projects. See the [Skills CLI guide](docs/cli-tools/npx-skills.md) for agent selection, updates, and removals.

## Add an MCP server

1. Choose a server from the [MCP catalog](mcp.md) and run its command from your project root.

   ```bash
   npx add-mcp https://mcp.context7.com/mcp/oauth --name context7 -a codex -a claude-code
   ```

2. Review the files written by add-mcp.

   - **Codex** uses `.codex/config.toml`.
   - **Claude Code** uses `.mcp.json` at the project root.

Add `-g` to configure the server across your projects. See the [add-mcp guide](docs/cli-tools/npx-add-mcp.md) for commands and options.

## Share a skill with a symlink

If a skill already lives in `.agents/skills/`, you can expose it to Claude Code with a symlink. Run this from the project root on macOS or Linux, replacing `my-skill` with the skill's directory name.

```bash
mkdir -p .claude/skills
ln -s ../../.agents/skills/my-skill .claude/skills/my-skill
```

See the [shared skill example](examples/).
