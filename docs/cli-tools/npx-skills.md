# `npx skills`

Vercel's Skills CLI installs agent skills from Git repositories, URLs, and local directories. Run it from the root of the project where you want to use the skill.

## Install skills

```bash
npx skills add vercel-labs/agent-skills --list
npx skills add vercel-labs/agent-skills --skill web-design-guidelines -a codex -a claude-code
```

- `--list` previews skills available from the source.
- `--skill <name>` selects a skill using the name declared in its `SKILL.md`.
- `-a <agent>` selects an agent. Repeat the flag to target several.
- `-g` installs for your user account across projects. Omit it for a project install.
- `--copy` installs physical copies. With the default symlink mode, Claude Code can share the copy in `.agents/skills/`.
- `-y` skips the CLI's confirmation prompts.

| Agent | ID | Project path | User path |
| --- | --- | --- | --- |
| Codex | `codex` | `.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `claude-code` | `.claude/skills/` | `~/.claude/skills/` |

See the [supported agents list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) for more agent IDs and paths.

## Install a skill from this repository

Publish the skill under `skills/<name>/SKILL.md` in the source repository. From the target project, run the installer against the GitHub repository or your local checkout.

```bash
npx skills add Bosh-Kuo/awesome-agent-toolkit --list
npx skills add Bosh-Kuo/awesome-agent-toolkit --skill spec-writer
npx skills add /path/to/awesome-agent-toolkit/skills --skill spec-writer
```

For a private repository, use an SSH URL with your existing Git credentials. To pin a release or commit, use `owner/repo@<tag-or-commit>` as the source. See the [source formats reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#source-formats).

## Find, update, and remove skills

| Action | Command |
| --- | --- |
| Search for skills | `npx skills find <query>` |
| List project skills | `npx skills list` |
| List user-wide skills | `npx skills list -g` |
| Check for updates | `npx skills check` |
| Update a project skill | `npx skills update -p web-design-guidelines` |
| Update user-wide skills | `npx skills update -g` |
| Remove a project skill | `npx skills remove web-design-guidelines` |
| Remove a user-wide skill | `npx skills remove web-design-guidelines -g` |

The project's `skills-lock.json` records sources and content hashes. The CLI uses it to compare upstream and local changes.

## References

- [Official command reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
- [Node.js requirements](https://github.com/vercel-labs/skills/blob/main/package.json)
- [Skill catalog](../../skills.md)
