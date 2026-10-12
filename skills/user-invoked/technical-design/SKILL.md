---
name: technical-design
description: Define the smallest viable architecture and technical contracts at docs/tech-spec.md. Run only when the developer requests technical design.
disable-model-invocation: true
---

# Technical Design

Activation: the developer requests technical design. Input is approved product scope, applicable approved design direction, existing code and stack, and consequential constraints.

Explore current modules and operational limits before selecting technology. Use `codebase-design` when a module seam is uncertain and `api-design` when consumers or trust boundaries need an explicit contract. Write `docs/tech-spec.md` with `Status: Draft`: architecture and module responsibilities; data model/invariants; APIs or interfaces; authentication/authorization boundaries; validation and error behavior; external dependencies; testing seams and commands; migration/rollout concerns where relevant; consequential choices and rejected alternatives. Prefer the simplest design satisfying the approved outcomes. Do not introduce speculative services, abstractions, or dependencies.

Point to product and design requirements instead of repeating them. Surface conflicts with those owners and request a decision. Present consequential technical choices for approval and stop; this stage does not create tickets or code. For a small change, a compact document or approved amendment is enough.

Done when a fresh implementer can identify boundaries, contracts, risks, and how to verify the change.

Sources: [Matt Pocock's `codebase-design`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/codebase-design/SKILL.md) and [Addy Osmani's API/interface design](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/api-and-interface-design/SKILL.md).
