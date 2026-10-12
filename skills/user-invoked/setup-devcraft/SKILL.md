---
name: setup-devcraft
description: Configure an installed DevCraft collection and its local Markdown ticket tracker in a project. Run only when the developer requests setup or repair.
disable-model-invocation: true
---

# Setup DevCraft

Activation: the developer explicitly requests DevCraft setup or repair. The adapter or manual copy must make this skill discoverable first. This stage configures the project; it does not start discovery or implementation.

1. Inspect the project root, installed skill directories, existing `AGENTS.md` and `CLAUDE.md`, repository commands, documents, and tickets. Identify the active agent from evidence rather than guessing.
2. Verify each installed DevCraft skill has its `SKILL.md` and referenced support files. If installation is incomplete and the DevCraft source checkout is available, use its adapter installer. Preserve modified or unrelated skill directories. Otherwise report exact missing files and the installation command.
3. Configure the developer-selected local tracker: `docs/tickets/<feature-slug>/T-001-<ticket-slug>.md`. Record this convention, document paths, a chosen lightweight/standard/rapid profile, actual verification commands, and explicit-stage guidance in a short `## DevCraft` block of `AGENTS.md`. Update that block in place; preserve all other instructions. Create no empty ticket or specification files.
4. If an existing tracker or project instruction conflicts, show the conflicting lines and resolve the choice with the developer before editing them. For Claude Code, follow the adapter's guidance if a project `CLAUDE.md` prevents `AGENTS.md` from loading.
5. Check the installed files and final `AGENTS.md` block. Report what changed and any discovery that could not be verified in the active agent.

Done when the collection is discoverable, local ticket ownership is documented, and existing project data is intact. If setup already matches, change nothing. Hand back to the developer; suggest `ask-workflow` without invoking it.

Source: adapted from [Matt Pocock's setup skill](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/setup-matt-pocock-skills/SKILL.md); DevCraft's local tracker and installation checks replace its tracker bootstrap.
