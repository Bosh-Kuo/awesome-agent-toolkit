# `npx add-mcp`

Neon's add-mcp writes an MCP server's URL or launch command to your agent's configuration. Run it from the root of the target project.

## Add a server

```bash
# Remote Streamable HTTP server
npx add-mcp https://mcp.context7.com/mcp/oauth --name context7 -a codex -a claude-code

# Local stdio server
npx add-mcp "npx -y chrome-devtools-mcp@latest" --name chrome-devtools -a codex -a claude-code
```

- `--name <name>` sets the server's name in the generated configuration.
- `-a <agent>` selects an agent. Repeat the flag to target several.
- `-g` writes user-wide configuration. Omit it for a project install.
- `-y` outside the quoted launch command skips add-mcp's confirmation prompts.

Pass the entire local launch command as one quoted argument, including the server's flags. Remote URLs use HTTP by default.

## Configuration paths

| Agent | Project install | User-wide install with `-g` |
| --- | --- | --- |
| Codex | `.codex/config.toml` | `$CODEX_HOME/config.toml` (default `~/.codex/config.toml`) |
| Claude Code | `.mcp.json` | `~/.claude.json` |

See the [supported agents list](https://github.com/neon-solutions/add-mcp#supported-agents) for the other configuration paths.

## Find, list, and remove servers

| Action | Command |
| --- | --- |
| Search and select a server interactively | `npx add-mcp find context7` |
| List supported agents | `npx add-mcp list-agents` |
| List project servers | `npx add-mcp list` |
| List user-wide servers | `npx add-mcp list -g` |
| Remove a project server from Codex | `npx add-mcp remove context7 -a codex` |
| Remove a user-wide server from Codex | `npx add-mcp remove context7 -a codex -g` |
| Sync settings across detected project agents | `npx add-mcp sync` |

Use `sync` when the same server is configured in multiple agents and you want consistent settings. It groups entries by URL or package name and skips groups with conflicting arguments, headers, or environment variables. See the [sync reference](https://github.com/neon-solutions/add-mcp#sync-command).

## References

- [Official add-mcp documentation](https://github.com/neon-solutions/add-mcp)
- [MCP catalog](../../mcp.md)
