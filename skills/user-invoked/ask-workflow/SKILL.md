---
name: ask-workflow
description: Recommend DevCraft's next development stage from the project's actual state. Run only when the developer asks what workflow or skill to use.
disable-model-invocation: true
---

# Ask Workflow

Activation: the developer requests a workflow recommendation. Return advice; never start the recommended stage.

Inspect `AGENTS.md`, applicable approved documents, ticket statuses and blockers, code state, and the current request. Read a candidate skill's `SKILL.md` before claiming what it does. Recommend one next user-invoked skill with its needed input and approval gate; mention a short alternative only if the situation genuinely branches.

Routing cues: absent setup → `setup-devcraft`; unresolved product decisions → `grill-with-docs`; settled requirements without a product spec → `product-spec`; UI needing a direction → `design-direction`; architecture/API decisions → `technical-design`; approved multi-session work → `to-tickets`; ready ticket or small direct change → `implement`; built UI needing evaluation → `ui-review`; candidate release → `release`. A hard bug may instead start with `diagnosing-bugs`. Existing approved work is reused, not repeated for ceremony.

State the evidence for the route and what is still missing. If authoritative documents conflict, identify the passages and their owners; ask for resolution rather than selecting one. Done when the developer has an actionable next choice. Do not invoke it.

Source: adapted from [Matt Pocock's `ask-matt`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/ask-matt/SKILL.md), narrowed to DevCraft stages.
