---
name: to-tickets
description: Convert approved DevCraft specifications into small vertical-slice Markdown tickets. Run only when the developer requests ticket breakdown.
disable-model-invocation: true
---

# To Tickets

Activation: the developer requests a ticket breakdown. Input is approved `docs/product.md`, `docs/tech-spec.md`, and `docs/design.md` when UI is in scope, relevant code state, and the tracker choice in the DevCraft block of `AGENTS.md` or `CLAUDE.md`. If a required decision is draft or contradictory, resolve it before publishing dependent tickets.

Propose demoable vertical slices, each small enough for one focused session. Include real blockers, acceptance criteria, and a verification method; avoid horizontal architecture-only tickets unless an enabling migration is required. Present the numbered graph and get the developer's approval before writing it. A one-session task needs no ticket unless the developer wants one.

After approval, use the configured tracker. For local Markdown, create `docs/tickets/<feature-slug>/T-001-<ticket-slug>.md`. For GitHub Issues, verify `gh` is authenticated and the configured repository matches the current project, then create one issue per approved ticket with the same `T-001` title, outcome, blockers, spec links, acceptance criteria, status, and verification sections. Use repository web links for GitHub issue references. Mark unblocked tickets `Ready` and dependent tickets `Blocked` until their blockers are Done. Keep GitHub issues open until Done. Do not create issues before approval, or create labels/projects during ticketing.

Done when the first ticket is ready, every dependency is explicit, every slice is independently checkable, and the approved order is written in the configured tracker. Hand back for a separate `implement` invocation.

Sources: [Matt Pocock's `to-tickets`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-tickets/SKILL.md) and [Addy Osmani's planning/task breakdown](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/planning-and-task-breakdown/SKILL.md).
