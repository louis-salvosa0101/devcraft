---
name: domain-modeling
description: Clarify domain terms, invariants, and consequential decisions when project language is ambiguous.
---

# Domain Modeling

Input: the relevant conversation, code, and any existing glossary/ADRs. Output: precise domain vocabulary, edge-case findings, and only justified document updates. Return control to the caller.

Challenge overloaded terms against real scenarios and code. Write a resolved project-specific term to `GLOSSARY.md` in one or two sentences; keep implementation, requirements and design rules out. Create an ADR under `docs/adr/` only when a decision is hard to reverse, surprising without context, and made among real alternatives. Create these files lazily. Read relevant existing ADRs first and surface contradictions for a developer decision.

Skip when the task uses established terms without changing the model. A domain invariant that belongs in product or technical specification should be handed to that owner rather than duplicated in the glossary.

Source: adapted from [Matt Pocock's `domain-modeling`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/domain-modeling/SKILL.md).
