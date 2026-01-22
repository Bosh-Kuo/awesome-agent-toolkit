<div align="center">

<img src="./assets/cover.jpg" alt="Awesome Agent Toolkit Cover" width="600"/>

# Awesome Agent Toolkit

> A curated collection of essential configurations, skills, prompts, and workflows for AI-powered development tools

[![Last Updated](https://img.shields.io/badge/Last%20Updated-January%202026-blue.svg)](https://github.com/Bosh-Kuo/awesome-agent-toolkit)
[![Awesome](https://awesome.re/badge.svg)](https://github.com/Bosh-Kuo/awesome-agent-toolkit)

</div>


## 📖 About

**Awesome Agent Toolkit** is a tool-agnostic repository accumulated through my own daily development work. This collection is a blend of resources gathered from the open-source community and insights gained from my personal experience, curated to form the most effective development toolkit for my daily needs.

Whether you're using Claude Code, Codex, Antigravity, Windsurf, Cursor, or any other AI coding assistant, this collection provides reusable configurations and resources that can be easily adapted to your preferred tool. The focus is on **content quality** and **portability** rather than tool-specific implementations.

### Why Tool-Agnostic?

Modern AI development tools share similar underlying concepts:
- **MCP (Model Context Protocol)** servers for extending capabilities
- **Custom rules** for guiding AI behavior
- **Agent skills** for specialized tasks
- **Prompts** for consistent interactions
- **Workflows** for repeatable processes

By focusing on these universal concepts, this repository remains valuable regardless of which AI tool you choose.

---

## 📂 Repository Structure

```
awesome-agent-devtools/
├── mcp-configs/      # Model Context Protocol server configurations
├── rules/            # Custom rules for AI behavior
├── skills/           # Agent skills for specialized tasks
├── prompts/          # Reusable prompt templates
└── workflows/        # Automated workflow definitions
```

---

## 🔌 MCP Configurations

Model Context Protocol (MCP) servers extend your AI assistant's capabilities by connecting to external tools and data sources.

### Available MCP Servers

| Name                      | Description                                                                                | Link                                               | Source                                                               | Added to Repo |
| ------------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------------------- | -------------------------------------------------------------------- | ------------- |
| **Context7**              | Access up-to-date documentation and code examples for any programming library or framework | [Config](./mcp-configs/context7.json)              | [Official Site](https://context7.com/)                               | 2026-01-21    |
| **Chrome DevTools**       | Interact with Chrome browser for testing, debugging, and automation                        | [Config](./mcp-configs/chrome-devtools-mcp.json)   | [Chrome Blog](https://developer.chrome.com/blog/chrome-devtools-mcp) | 2026-01-21    |
| **MCP Feedback Enhanced** | Enhanced feedback and debugging capabilities with web interface                            | [Config](./mcp-configs/mcp-feedback-enhanced.json) | [GitHub](https://github.com/hexonal/mcp-feedback-enhanced)           | 2026-01-21    |

### MCP Resources

Discover more MCP servers from these curated collections:
- [Cursor MCP Directory](https://cursor.directory/mcp) - Community-curated MCP servers
- [MCP.so](https://mcp.so/) - Official MCP server registry

---

## 📏 Rules

> Coming soon

Custom rules help guide AI behavior and enforce coding standards across your projects.

---

## 🎯 Skills

Agent skills are specialized instruction sets that enable AI assistants to perform complex, domain-specific tasks. Each skill contains detailed guidelines, best practices, and workflows for specific domains.

### Available Skills

| Name                            | Description                                                                                                                       | Link                                          | Source                                                                                       | Added to Repo |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------- |
| **UI/UX Pro Max**               | Comprehensive design intelligence with 50+ styles, 97 color palettes, 57 font pairings, and 99 UX guidelines across 9 tech stacks | [Skill](./skills/ui-ux-pro-max)               | [Official Site](https://ui-ux-pro-max-skill.nextlevelbuilder.io/)                            | 2026-01-21    |
| **Vercel React Best Practices** | React and Next.js performance optimization, patterns, and best practices from Vercel                                              | [Skill](./skills/vercel-react-best-practices) | [GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)  | 2026-01-21    |
| **Skill Creator**               | Meta-skill for creating new agent skills with proper structure and documentation                                                  | [Skill](./skills/skill-creator)               | [GitHub](https://github.com/anthropics/skills/tree/main/skills/skill-creator)                | 2026-01-21    |
| **Web Design Guidelines**       | Modern web design principles, patterns, and accessibility guidelines                                                              | [Skill](./skills/web-design-guidelines)       | [GitHub](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | 2026-01-21    |

### Skills Resources

Discover more agent skills:
- [SkillsMP](https://skillsmp.com/) - Community marketplace for agent skills

### Skill Creation Tools

Tools to help you create your own skills:
- [Skill Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) - Interactive skill creation and management tool

---

## 💬 Prompts

> Coming soon

Reusable prompt templates for common development tasks and interactions.

---

## 🔄 Workflows

> Coming soon

Automated workflow definitions for repeatable development processes.

---

## 🚀 Getting Started

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/awesome-agent-devtools.git
   cd awesome-agent-devtools
   ```

2. **Browse the directories** to find resources relevant to your needs

3. **Copy and adapt** configurations to your AI tool of choice

4. **Customize** as needed for your specific workflow

---

## 🌟 Acknowledgments

Special thanks to the open-source community and the developers of:
- Model Context Protocol (MCP)
- All the MCP server maintainers
- AI tool developers who make these integrations possible


## ⭐️ AI Coding Tools I've Explored

<div align="center">

![Cursor](https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=cursor&logoColor=white)
![Windsurf](https://img.shields.io/badge/Windsurf-f9f3e9?style=for-the-badge&logo=windsurf&logoColor=black)
![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-000000?style=for-the-badge&logo=githubcopilot&logoColor=white)
![Augment Code](https://img.shields.io/badge/Augment_Code-10A37F?style=for-the-badge&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-D97706?style=for-the-badge&logo=claude&logoColor=white)
![Gemini CLI](https://img.shields.io/badge/Gemini_CLI-4285F4?style=for-the-badge&logo=googlegemini&logoColor=white)
![Codex](https://img.shields.io/badge/Codex-white?style=for-the-badge&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPgo8c3ZnIGZpbGw9IiMwMDAwMDAiIHdpZHRoPSI4MDBweCIgaGVpZ2h0PSI4MDBweCIgdmlld0JveD0iMCAwIDI0IDI0IiByb2xlPSJpbWciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHRpdGxlPk9wZW5BSSBpY29uPC90aXRsZT48cGF0aCBkPSJNMjIuMjgxOSA5LjgyMTFhNS45ODQ3IDUuOTg0NyAwIDAgMC0uNTE1Ny00LjkxMDggNi4wNDYyIDYuMDQ2MiAwIDAgMC02LjUwOTgtMi45QTYuMDY1MSA2LjA2NTEgMCAwIDAgNC45ODA3IDQuMTgxOGE1Ljk4NDcgNS45ODQ3IDAgMCAwLTMuOTk3NyAyLjkgNi4wNDYyIDYuMDQ2MiAwIDAgMCAuNzQyNyA3LjA5NjYgNS45OCA1Ljk4IDAgMCAwIC41MTEgNC45MTA3IDYuMDUxIDYuMDUxIDAgMCAwIDYuNTE0NiAyLjkwMDFBNS45ODQ3IDUuOTg0NyAwIDAgMCAxMy4yNTk5IDI0YTYuMDU1NyA2LjA1NTcgMCAwIDAgNS43NzE4LTQuMjA1OCA1Ljk4OTQgNS45ODk0IDAgMCAwIDMuOTk3Ny0yLjkwMDEgNi4wNTU3IDYuMDU1NyAwIDAgMC0uNzQ3NS03LjA3Mjl6bS05LjAyMiAxMi42MDgxYTQuNDc1NSA0LjQ3NTUgMCAwIDEtMi44NzY0LTEuMDQwOGwuMTQxOS0uMDgwNCA0Ljc3ODMtMi43NTgyYS43OTQ4Ljc5NDggMCAwIDAgLjM5MjctLjY4MTN2LTYuNzM2OWwyLjAyIDEuMTY4NmEuMDcxLjA3MSAwIDAgMSAuMDM4LjA1MnY1LjU4MjZhNC41MDQgNC41MDQgMCAwIDEtNC40OTQ1IDQuNDk0NHptLTkuNjYwNy00LjEyNTRhNC40NzA4IDQuNDcwOCAwIDAgMS0uNTM0Ni0zLjAxMzdsLjE0Mi4wODUyIDQuNzgzIDIuNzU4MmEuNzcxMi43NzEyIDAgMCAwIC43ODA2IDBsNS44NDI4LTMuMzY4NXYyLjMzMjRhLjA4MDQuMDgwNCAwIDAgMS0uMDMzMi4wNjE1TDkuNzQgMTkuOTUwMmE0LjQ5OTIgNC40OTkyIDAgMCAxLTYuMTQwOC0xLjY0NjR6TTIuMzQwOCA3Ljg5NTZhNC40ODUgNC40ODUgMCAwIDEgMi4zNjU1LTEuOTcyOFYxMS42YS43NjY0Ljc2NjQgMCAwIDAgLjM4NzkuNjc2NWw1LjgxNDQgMy4zNTQzLTIuMDIwMSAxLjE2ODVhLjA3NTcuMDc1NyAwIDAgMS0uMDcxIDBsLTQuODMwMy0yLjc4NjVBNC41MDQgNC41MDQgMCAwIDEgMi4zNDA4IDcuODcyem0xNi41OTYzIDMuODU1OEwxMy4xMDM4IDguMzY0IDE1LjExOTIgNy4yYS4wNzU3LjA3NTcgMCAwIDEgLjA3MSAwbDQuODMwMyAyLjc5MTNhNC40OTQ0IDQuNDk0NCAwIDAgMS0uNjc2NSA4LjEwNDJ2LTUuNjc3MmEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxMDctMy4wMjMxbC0uMTQyLS4wODUyLTQuNzczNS0yLjc4MThhLjc3NTkuNzc1OSAwIDAgMC0uNzg1NCAwTDkuNDA5IDkuMjI5N1Y2Ljg5NzRhLjA2NjIuMDY2MiAwIDAgMSAuMDI4NC0uMDYxNWw0LjgzMDMtMi43ODY2YTQuNDk5MiA0LjQ5OTIgMCAwIDEgNi42ODAyIDQuNjZ6TTguMzA2NSAxMi44NjNsLTIuMDItMS4xNjM4YS4wODA0LjA4MDQgMCAwIDEtLjAzOC0uMDU2N1Y2LjA3NDJhNC40OTkyIDQuNDk5MiAwIDAgMSA3LjM3NTctMy40NTM3bC0uMTQyLjA4MDVMOC43MDQgNS40NTlhLjc5NDguNzk0OCAwIDAgMC0uMzkyNy42ODEzem0xLjA5NzYtMi4zNjU0bDIuNjAyLTEuNDk5OCAyLjYwNjkgMS40OTk4djIuOTk5NGwtMi41OTc0IDEuNDk5Ny0yLjYwNjctMS40OTk3WiIvPjwvc3ZnPg==&logoColor=white)
![Antigravity](https://img.shields.io/badge/Antigravity-667EEA?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiBmaWxsPSIjMDAwMDAwIiBzdHlsZT0ib3BhY2l0eToxOyI+PHBhdGggIGQ9Ik0xMi4wMjUgMnEyLjAyNSAwIDMuMTYzIDEuNTI1VDE3LjEyNSA3cS42NSAxLjU3NSAxLjI1IDMuNXQxLjI3NSAzLjg3NXEuNjUgMS44NzUgMS40MjUgMy41MjV0MS44IDIuODI1cS4yLjIyNS4xNzUuNTI1dC0uMjI1LjUyNXQtLjQ3NS4yNXQtLjU1LS4xNzVxLTEuOTc1LTEuNTUtMy4yNS0zLjQ2M3QtMi41NzUtMy4zMzdxLS44NS0uOTUtMS44MTItMS41VDEyLjAyNSAxM3QtMi4xMzcuNTV0LTEuODEzIDEuNXEtMS4zIDEuNDI1LTIuNTc1IDMuMzM4VDIuMjUgMjEuODVxLS4yNzUuMi0uNTUuMTc1dC0uNDc1LS4yNVQxIDIxLjI1dC4xNzUtLjUyNVEyLjIgMTkuNTUgMi45NzUgMTcuOVQ0LjQgMTQuMzc1cS42NzUtMS45NSAxLjI3NS0zLjg3NVQ2LjkyNSA3cS44LTEuOTUgMS45MzgtMy40NzVUMTIuMDI1IDJtMCAycS0xLjEyNSAwLTEuNzc1Ljk3NVQ5LjEgN3EtLjY1IDEuNC0xLjE2MiAzLjAxM1Q2LjggMTMuNXEuNS0uNTI1Ljk2My0uOTI1dC45NjItLjcyNXEuOC0uNDc1IDEuNTg4LS42NjNUMTIuMDI1IDExdDEuNzEzLjE4OHQxLjU4Ny42NjJxLjUuMzI1Ljk2My43MjV0Ljk2Mi45MjVxLS42MjUtMS44NzUtMS4xMzctMy40ODdUMTQuOTUgN3EtLjUtMS4wNS0xLjE1LTIuMDI1VDEyLjAyNSA0bTAgNyIvPjwvc3ZnPg==&logoColor=white)

*Currently powered by **Antigravity** ⚡*

</div>


---

<div align="center">

**[⬆ Back to Top](#awesome-agent-toolkit)**

Made with ❤️ for the AI development community

</div>
