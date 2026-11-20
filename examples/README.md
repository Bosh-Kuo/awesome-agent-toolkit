# Project configuration example

This project layout gives Codex and Claude Code the same skill and MCP servers.

```text
.
├── .agents/skills/
│   └── summarize-diff/
│       ├── SKILL.md
│       └── agents/openai.yaml
├── .claude/skills/
│   └── summarize-diff -> ../../.agents/skills/summarize-diff
├── .codex/config.toml
└── .mcp.json
```

- **Skill.** Both agents read the same [`SKILL.md`](.agents/skills/summarize-diff/SKILL.md). Try asking, “Use the summarize-diff skill to summarize my staged and unstaged changes.”
- **MCP.** [Codex's TOML file](.codex/config.toml) and [Claude Code's JSON file](.mcp.json) both configure Context7 over HTTP and Chrome DevTools over stdio.

To try the example in another project, keep the relative paths and copy the symlink as a symlink.
