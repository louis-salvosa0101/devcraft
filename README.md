# DevCraft

*From idea to production. One skill at a time.*

DevCraft is a modular, agent-agnostic collection of reusable skills for structured, design-driven software development. Developers invoke major stages; agents use bounded specialist skills inside them. Project decisions live in local Markdown documents and tickets, not in chat history or an external service.

## Install in a project

From your project directory, start the [Skills CLI](https://github.com/vercel-labs/skills) installer:

```sh
npx skills@latest add louis-salvosa0101/devcraft
```

Choose your agent and the skills to install when prompted; select all 23 for the complete DevCraft workflow. To inspect the collection first, run `npx skills@latest add louis-salvosa0101/devcraft --list`. Run `setup-devcraft` explicitly after installation to configure the project.

### Python adapter alternative

Python 3.9 or newer is required for the installer. From this source checkout:

```sh
python adapters/install.py --agent codex --project /path/to/project
python adapters/install.py --agent codex --project /path/to/project --check
```

Use `--agent claude-code` or `--agent cursor` for those hosts. On Windows, pass a quoted absolute path to `--project`. The installer copies 23 skills into that agent's project discovery directory, asks the host to keep the ten workflow skills explicit-only, refuses unrelated or edited skill files, and can repair missing DevCraft files. It does not change project specifications, tickets, or `AGENTS.md`. See [adapter details](adapters/README.md) for paths, metadata, manual installation, and compatibility limits.

After either installation method, invoke `setup-devcraft` explicitly in your agent. It asks which project instruction file(s) to configure and whether tickets should use local Markdown under `docs/tickets/` or GitHub Issues. It preserves existing project instructions and tickets.

Then invoke `ask-workflow` for a recommendation or name a stage directly. An example standard route is:

```text
grill-with-docs → product-spec → design-direction → technical-design
→ to-tickets → implement → ui-review → release
```

These are separate invocations. Backend-only work can skip visual stages; a small bug fix can go directly to diagnosis and implementation. The **lightweight**, **standard**, and **rapid** profiles change planning depth, not correctness, accessibility, security, or approval gates.

## Documents and boundaries

| Artifact | Decision owner |
| --- | --- |
| `docs/product.md` | Users, scope, requirements, acceptance outcomes |
| `docs/design.md` | Visual system, interaction, responsive and accessibility direction |
| `docs/tech-spec.md` | Architecture, data/API contracts, security boundaries, test strategy |
| Local ticket or GitHub Issue | One vertical slice, blockers, criteria, status and verification |
| `AGENTS.md` and/or `CLAUDE.md` | Project conventions, document paths, commands and stage guidance |

Start from [the four templates](templates/) when useful. `setup-devcraft` asks which instruction file(s) to configure and whether to use local Markdown or GitHub Issues. GitHub mode requires authenticated `gh` access. Specs and ticket breakdowns need developer approval. An `implement` invocation works on one ready ticket by default and never silently commits, pushes, or deploys. Specialists cannot advance a major stage or rewrite an approved specification. See [architecture](docs/architecture.md) for contracts and conflict handling.

## Source and validation

The [source audit](docs/research/source-audit.md) and [provenance record](docs/research/provenance.md) inspect and pin Matt Pocock's Skills, Addy Osmani's Agent Skills, Taste Skill, and Impeccable. DevCraft uses original skill prose and does not bundle their engines, assets, or scripts. [Licenses and attribution](LICENSES.md) records the source terms.

Run the local checks with:

```sh
python -m unittest discover -s tests -v
```

[Validation results](docs/validation.md) distinguish packaging checks and scenario walkthroughs from live agent behavior. The [CRUD](examples/crud-app/README.md), [SaaS](examples/fullstack-saas/README.md), and [hackathon](examples/hackathon/README.md) traces show how to use the three profiles.

DevCraft's source is under [MIT](LICENSE).
