# Skill catalog

Run an install command from the target project's root. Installation is project-scoped by default. Use `-a <agent>` to select an agent, repeat it to select several, or add `-g` for a user-wide install.

```bash
npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices -a codex -a claude-code
```

Each example starts by explicitly invoking the skill. Use `/skill-name` in Claude Code or `$skill-name` in Codex. See the [Skills CLI guide](docs/cli-tools/npx-skills.md) for more agent IDs and commands.

## React development

| Skill | What it does | Project install | Example prompt | Author |
| --- | --- | --- | --- | --- |
| Vercel React Best Practices | Reviews React components and data fetching for performance issues | `npx skills add vercel-labs/agent-skills --skill vercel-react-best-practices` | `/vercel-react-best-practices` Review this dashboard for request waterfalls and unnecessary re-renders. | [Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) |
| Vercel React View Transitions | Implements route, list, and shared-element transitions with React's View Transition API | `npx skills add vercel-labs/agent-skills --skill vercel-react-view-transitions` | `/vercel-react-view-transitions` Animate a product card into its detail page and respect reduced-motion preferences. | [Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-view-transitions) |

## Next.js

| Skill | What it does | Project install | Example prompt | Author |
| --- | --- | --- | --- | --- |
| Cache Components Adoption | Enables Cache Components and resolves blocking routes | `npx skills add vercel/next.js --skill next-cache-components-adoption` | `/next-cache-components-adoption` Enable Cache Components and resolve the blocking prerender errors on the product routes. | [Vercel](https://github.com/vercel/next.js/tree/canary/skills/next-cache-components-adoption) |
| Cache Components Optimizer | Improves the UI available immediately and adds regression coverage | `npx skills add vercel/next.js --skill next-cache-components-optimizer` | `/next-cache-components-optimizer` Make the product title and price visible on first load and cover them with an instant navigation test. | [Vercel](https://github.com/vercel/next.js/tree/canary/skills/next-cache-components-optimizer) |
| Next.js Dev Loop | Checks runtime behavior with the Next.js dev server and a browser | `npx skills add vercel/next.js --skill next-dev-loop` | `/next-dev-loop` Verify that my checkout change works in the running app and look for runtime errors. | [Vercel](https://github.com/vercel/next.js/tree/canary/skills/next-dev-loop) |
| Partial Prefetching Adoption | Enables Partial Prefetching and audits existing link behavior | `npx skills add vercel/next.js --skill next-partial-prefetching-adoption` | `/next-partial-prefetching-adoption` Enable Partial Prefetching and check which existing catalog links need migration. | [Vercel](https://github.com/vercel/next.js/tree/canary/skills/next-partial-prefetching-adoption) |
| Partial Prefetching Optimizer | Tunes the UI available before a selected link is clicked | `npx skills add vercel/next.js --skill next-partial-prefetching-optimizer` | `/next-partial-prefetching-optimizer` Make the product title appear immediately after a catalog link is clicked and leave reviews to load on navigation. | [Vercel](https://github.com/vercel/next.js/tree/canary/skills/next-partial-prefetching-optimizer) |

General Next.js guidance previously shipped as `next-best-practices`. Next.js 16.3 and later ship version-matched docs and generate agent instructions during `next dev`. See the [upstream migration notice](https://github.com/vercel-labs/next-skills) and [Next.js agent guide](https://nextjs.org/docs/app/guides/ai-agents).

## Web design

| Skill | What it does | Project install | Example prompt | Author |
| --- | --- | --- | --- | --- |
| Impeccable | Evaluates and refines layout, typography, and interaction | `npx skills add pbakaus/impeccable --skill impeccable` | `/impeccable` Refine the homepage color palette and interaction design. | [@pbakaus](https://github.com/pbakaus/impeccable) |
| UI/UX Pro Max | Suggests design styles, palettes, and typography for a product | `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max` | `/ui-ux-pro-max` Propose a color palette and type system for a calm, readable personal finance dashboard. | [@nextlevelbuilder](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |
| Frontend Design | Creates distinctive visual directions and implements web interfaces | `npx skills add anthropics/skills --skill frontend-design` | `/frontend-design` Build a portfolio landing page with an editorial look and a responsive project grid. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| Web Design Guidelines | Audits accessibility, interactions, and interface implementation | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` | `/web-design-guidelines` Audit this sign-up form for keyboard navigation, focus states, and error messages. | [Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) |

## Development tooling

| Skill | What it does | Project install | Example prompt | Author |
| --- | --- | --- | --- | --- |
| shadcn/ui | Official skill for composing, styling, and installing components in a shadcn/ui project | `npx skills add shadcn-ui/ui --skill shadcn` | `/shadcn` Add a dialog for editing a team member and use the project's existing form components. | [shadcn/ui](https://ui.shadcn.com/docs/skills#install) |
| Turborepo | Configures monorepo tasks, caching, package boundaries, and CI | `npx skills add vercel/turborepo --skill turborepo` | `/turborepo` Review our Turbo task graph and fix the cache settings for the shared UI package. | [Vercel](https://github.com/vercel/turborepo/tree/main/skills/turborepo) |

For registry access through MCP, see the [shadcn/ui MCP server](mcp.md#documentation-and-ui-components).

## Backend and databases

| Skill | What it does | Project install | Example prompt | Author |
| --- | --- | --- | --- | --- |
| NestJS Best Practices | Reviews NestJS modules, dependency injection, security, and performance | `npx skills add Kadajett/agent-nestjs-skills --skill nestjs-best-practices` | `/nestjs-best-practices` Review the billing module's provider boundaries and flag dependencies that should be injected. | [@Kadajett](https://github.com/Kadajett/agent-nestjs-skills/tree/main/skills/nestjs-best-practices) |
| DBHub | Discovers database schemas and runs SQL through the [DBHub MCP server](mcp.md#databases) | `npx skills add bytebase/dbhub --skill dbhub` | `/dbhub` In the demo database, find the employee and department tables, then count employees by department. | [@bytebase](https://github.com/bytebase/dbhub/tree/main/skills/dbhub) |

## Product and technical specifications

| Skill | What it does | Project install | Example prompt | Author |
| --- | --- | --- | --- | --- |
| Product PRD | Turns product discussions into a project-level requirements document | `npx skills add Bosh-Kuo/awesome-agent-toolkit --skill product-prd` | `/product-prd` Turn our discussion about the team dashboard into a PRD with target users, MVP scope, and milestones. | [@Bosh-Kuo](skills/product-prd/) |
| Spec Writer | Documents feature behavior from code and product requirements | `npx skills add Bosh-Kuo/awesome-agent-toolkit --skill spec-writer` | `/spec-writer` Read the current login flow and write a feature spec that covers validation, errors, and redirects. | [@Bosh-Kuo](skills/spec-writer/) |
| Spec-Driven Development | Breaks complex work into a spec, an implementation plan, and tracked tasks | `npx skills add Bosh-Kuo/awesome-agent-toolkit --skill spec-driven-development` | `/spec-driven-development` Plan the notification service and record the tasks needed to ship it. | [@Bosh-Kuo](skills/spec-driven-development/) |

## Documents and diagrams

| Skill | What it does | Project install | Example prompt | Author |
| --- | --- | --- | --- | --- |
| PDF | Extracts content, fills forms, and manipulates PDF pages | `npx skills add anthropics/skills --skill pdf` | `/pdf` Extract the invoice line items from this PDF into a CSV. | [Anthropic](https://github.com/anthropics/skills/tree/main/skills/pdf) |
| Excalidraw Diagram | Produces editable architecture, workflow, and concept diagrams | `npx skills add coleam00/excalidraw-diagram-skill --skill excalidraw-diagram` | `/excalidraw-diagram` Draw an editable diagram showing how a browser request reaches our API, cache, and database. | [@coleam00](https://github.com/coleam00/excalidraw-diagram-skill) |

## IELTS

| Skill | What it does | Project install | Example prompt | Author |
| --- | --- | --- | --- | --- |
| IELTS Writing Task 1 Examiner | Scores and corrects Academic or General Training Task 1 responses | `npx skills add Bosh-Kuo/awesome-agent-toolkit --skill ielts-writing-task1-examiner` | `/ielts-writing-task1-examiner` Score my Task 1 chart summary, mark errors inline, and show me a stronger overview. | [@Bosh-Kuo](skills/ielts-writing-task1-examiner/) |
| IELTS Writing Task 2 Examiner | Scores and corrects Task 2 essays and provides a model answer | `npx skills add Bosh-Kuo/awesome-agent-toolkit --skill ielts-writing-task2-examiner` | `/ielts-writing-task2-examiner` Score my Task 2 essay for each criterion and show me how to develop the second argument. | [@Bosh-Kuo](skills/ielts-writing-task2-examiner/) |
