---
name: to-tickets
description: Convert approved DevCraft specifications into small vertical-slice Markdown tickets. Run only when the developer requests ticket breakdown.
disable-model-invocation: true
---

# To Tickets

Activation: the developer requests a ticket breakdown. Input is approved `docs/product.md`, `docs/tech-spec.md`, and `docs/design.md` when UI is in scope, plus relevant code state. If a required decision is draft or contradictory, resolve it before publishing dependent tickets.

Propose demoable vertical slices, each small enough for one focused session. Include real blockers, acceptance criteria, and a verification method; avoid horizontal architecture-only tickets unless an enabling migration is required. Present the numbered graph and get the developer's approval before writing it. A one-session task needs no ticket unless the developer wants one.

After approval, create `docs/tickets/<feature-slug>/T-001-<ticket-slug>.md` and increment in blocker-first order. Each file records one outcome, `Blocked by`, links to relevant spec headings, acceptance criteria, and a blank verification-evidence section. Mark unblocked tickets `Ready` and dependent tickets `Blocked` until their blockers are Done. Reference approved documents without copying them. Do not publish to an external tracker or create labels.

Done when the first ticket is ready, every dependency is explicit, every slice is independently checkable, and the approved order is written. Hand back for a separate `implement` invocation.

Sources: [Matt Pocock's `to-tickets`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-tickets/SKILL.md) and [Addy Osmani's planning/task breakdown](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/planning-and-task-breakdown/SKILL.md).
