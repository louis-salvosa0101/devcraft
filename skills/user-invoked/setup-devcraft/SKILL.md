---
name: setup-devcraft
description: Set up DevCraft in a project and clarify its instruction file and issue tracker. Run only when the developer requests setup or repair.
disable-model-invocation: true
---

# Setup DevCraft

Activation: the developer explicitly requests DevCraft setup or repair. The adapter or manual copy must make this skill discoverable first. This stage configures the project; it does not start discovery or implementation.

1. Inspect the project root, installed skill directories, existing `AGENTS.md` and `CLAUDE.md`, repository commands, documents, and tracker evidence. Identify the active agent from evidence rather than guessing.
2. Verify each installed DevCraft skill has its `SKILL.md` and referenced support files. If installation is incomplete and the DevCraft source checkout is available, use its adapter installer. Preserve modified or unrelated skill directories. Otherwise report exact missing files and the installation command.
3. Reuse an explicit existing setup choice. For any missing choice, ask in one short round before editing: which instruction file should own the DevCraft block (`AGENTS.md`, `CLAUDE.md`, or both), and which tracker should tickets use (local Markdown or GitHub Issues)? Recommend portable `AGENTS.md`; if both files are chosen, keep the block in `AGENTS.md` and make `CLAUDE.md` import it with `@AGENTS.md`, avoiding duplicate rules. Recommend local Markdown when no shared GitHub issue workflow is needed.
4. For local Markdown, use `docs/tickets/<feature-slug>/T-001-<ticket-slug>.md`. For GitHub Issues, resolve the repository from its configured `origin`, then verify `gh` is installed, authenticated, and can view that `owner/repo`; record its URL. If there is no GitHub origin or access is unavailable, explain what is missing and ask whether to configure local Markdown instead. Do not create issues, labels, or projects during setup.
5. Preview the exact DevCraft block and files to be changed. Record the chosen instruction file(s), tracker and location, active lightweight/standard/rapid profile, actual verification commands, and explicit-stage guidance. Preserve unrelated text, existing tickets, and approved documents. Create no empty specs or tickets. If existing instructions or tracker conventions conflict, show the evidence and resolve it with the developer before editing.
6. Write only the DevCraft-owned block in the selected file, then verify the installed skills and resulting instructions. For Claude Code, use its adapter guidance if a project `CLAUDE.md` affects `AGENTS.md` loading. Report what changed and any discovery that could not be verified in the active agent.

Done when the collection is discoverable, the chosen instruction file and tracker are documented, and existing project data is intact. If setup already matches, change nothing. Hand back to the developer; suggest `ask-workflow` without invoking it.

Source: adapted from [Matt Pocock's setup skill](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/setup-matt-pocock-skills/SKILL.md); DevCraft clarifies the instruction-file owner and supports local Markdown or GitHub Issues without creating a tracker during setup.
