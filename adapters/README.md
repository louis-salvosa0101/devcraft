# Agent adapters

The source skills live under `skills/user-invoked/` and `skills/model-invoked/`. `install.py` copies both tiers into one project discovery directory. Workflow skills carry optional invocation frontmatter and a Codex sidecar beside portable `name` and `description` fields so `npx skills` can preserve the controls too. Core procedures remain provider-neutral.

| `--agent` | Project discovery directory | Workflow-only metadata |
| --- | --- | --- |
| `codex` | `.agents/skills/` | `agents/openai.yaml` with `policy.allow_implicit_invocation: false`; `disable-model-invocation: true` in installed frontmatter |
| `claude-code` | `.claude/skills/` | `disable-model-invocation: true` |
| `cursor` | `.agents/skills/` | `disable-model-invocation: true` |

Run from the DevCraft checkout, using an absolute project path:

```sh
python adapters/install.py --agent claude-code --project /path/to/project
python adapters/install.py --agent claude-code --project /path/to/project --check
```

The adapter marks its own directories with `.devcraft-installed`. Reruns add missing files but refuse a same-name unrelated skill or a modified installed file without making partial changes. Review differences yourself before replacing an edited skill. Codex and Cursor share `.agents/skills/`; install only once for a project using either host. The installer does not create `AGENTS.md`, specs, tickets, or `CLAUDE.md`; invoke `setup-devcraft` after discovery. The `npx skills` path uses its own installation and update behavior; do not run both installers in the same project without checking for conflicts.

For manual installation, copy every named skill directory from both source tiers into the target directory above, without nesting the tier names. The workflow metadata is already present; Codex needs its `agents/openai.yaml` sidecar. Verify each host sees the skills before relying on its invocation rules. If Claude Code in your environment does not load project `AGENTS.md`, add an `@AGENTS.md` import to `CLAUDE.md` after checking existing instructions.

These paths and flags follow each host's published conventions. `npx skills` copies whole skill directories, so Claude Code and Cursor also receive the inert Codex sidecar; the Python adapter omits it for those hosts. The local installer tests verify copied files and metadata, not the host's live routing or its enforcement of explicit-only invocation. Other compatible agents can load the core `SKILL.md` files, but may lack a strict user-only control. The skill bodies require an explicit developer request as an additional convention.
