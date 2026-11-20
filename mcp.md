# MCP catalog

Run the install command from your project root. Add `-a <agent>` to target a specific agent or `-g` for a user-wide install. See the [add-mcp guide](docs/cli-tools/npx-add-mcp.md) for examples.

## Documentation and UI components

| Server | What it does | Project install | Source |
| --- | --- | --- | --- |
| Context7 | Retrieves library and framework documentation and code examples | `npx add-mcp https://mcp.context7.com/mcp/oauth --name context7` | [Context7](https://context7.com/docs/installation) |
| shadcn/ui MCP | Official server for searching registries and installing components | `npx add-mcp "npx -y shadcn@latest mcp" --name shadcn` | [shadcn/ui](https://ui.shadcn.com/docs/mcp) |

- **Context7** uses the OAuth endpoint in this example. For API key authentication, see the [Context7 client guide](https://context7.com/docs/resources/all-clients).
- **shadcn/ui MCP** reads registry settings from the project's `components.json`. See the [official MCP guide](https://ui.shadcn.com/docs/mcp) and the [companion skill](skills.md#development-tooling).

## Browser debugging

| Server | What it does | Project install | Source |
| --- | --- | --- | --- |
| Chrome DevTools | Inspects pages, network requests, console output, and performance | `npx add-mcp "npx -y chrome-devtools-mcp@latest" --name chrome-devtools` | [Chrome DevTools](https://github.com/ChromeDevTools/chrome-devtools-mcp) |

See the [Chrome and Node.js requirements](https://github.com/ChromeDevTools/chrome-devtools-mcp#requirements).

## Databases

| Server | What it does | Project install | Source |
| --- | --- | --- | --- |
| DBHub | Discovers schemas and executes SQL across supported databases. Pairs with the [DBHub skill](skills.md#backend-and-databases). | `npx add-mcp "npx -y @bytebase/dbhub@latest --transport stdio --demo" --name dbhub` | [@bytebase](https://github.com/bytebase/dbhub) |

- **DBHub** starts with its bundled SQLite demo. To connect your own database, replace `--demo` with `--config /absolute/path/to/dbhub.toml` and keep database credentials out of version control. See the [DBHub TOML guide](https://dbhub.ai/config/toml).
