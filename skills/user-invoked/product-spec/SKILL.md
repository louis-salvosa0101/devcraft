---
name: product-spec
description: Turn clarified decisions into an approvable product specification at docs/product.md. Run only when the developer requests product specification.
disable-model-invocation: true
---

# Product Spec

Activation: the developer requests a product specification or revision. Read the clarified decisions, existing product document, relevant code, and only the project context needed to check claims.

Write `docs/product.md` with `Status: Draft`: target users, problem, proposed outcome, MVP scope, primary journeys, functional and nonfunctional requirements, observable acceptance criteria, and real exclusions. Use the project's domain terms. Mark unresolved material decisions explicitly instead of filling gaps with plausible guesses. Keep architecture, API shape, tokens, and component styling with their technical/design owners; point to open questions there when needed.

For an existing approved product document, preserve it unless a revision was requested; show material changes for approval and return its status to Draft. Ask for approval of the finished spec and stop. `technical-design`, `design-direction`, and `to-tickets` are separate developer-invoked stages.

Done when every included feature has an observable outcome, scope is bounded, and the draft is reviewable. A lightweight or rapid profile may make the document short, but not ambiguous. If relevant approved documents conflict, show the passages and ask for resolution.

Sources: [Matt Pocock's `to-spec`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/to-spec/SKILL.md) and [Addy Osmani's spec-driven development](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/spec-driven-development/SKILL.md), separated into DevCraft's document owners.
