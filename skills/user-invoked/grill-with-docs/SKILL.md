---
name: grill-with-docs
description: Clarify an idea, scope, constraints, and terms before specification. Run only when the developer explicitly requests this discovery stage.
disable-model-invocation: true
---

# Grill with Docs

Activation: the developer explicitly starts clarification. Input is the idea, existing code and documents, and prior decisions. Output is a compact record of settled decisions and remaining questions, not an implementation.

1. Inspect relevant project facts yourself. Use `grilling` for dependency-ordered, focused question rounds; ask the developer for decisions, not facts available in the project.
2. Use `domain-modeling` when project terms or invariants are unclear. Keep `GLOSSARY.md` strictly for vocabulary and create an ADR only for a consequential, surprising, hard-to-reverse trade-off.
3. Record product decisions in a draft owning document when one exists; otherwise leave a concise discovery handoff for `product-spec`. Preserve any approved document and label proposed revisions. Record constraints, exclusions, contradictions, and unanswered questions without inventing answers.
4. Summarize the settled scope and ask the developer to confirm it. A confirmation closes this stage only; it does not authorize `product-spec`, tickets, or code.

Skip questions already settled in approved documents. If a runnable experiment is needed, use `prototype` to answer that question, then return its finding here. If a specialist is unavailable, perform the bounded step directly and report the fallback. Done when the decision frontier is empty or explicitly deferred and the handoff is usable in a fresh session.

Source: adapted from [Matt Pocock's `grill-with-docs`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/grill-with-docs/SKILL.md), [`grilling`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/grilling/SKILL.md), and [`domain-modeling`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md).
