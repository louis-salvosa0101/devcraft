---
name: codebase-design
description: Analyze module boundaries, interfaces, and test seams when an architecture or refactor decision is uncertain.
---

# Codebase Design

Input: affected code and callers, desired behavior, dependencies, and constraints. Output: a recommended seam and module responsibilities with trade-offs for the calling workflow.

Map what callers must know: operations, invariants, ordering, errors and performance. Prefer a small stable interface that contains meaningful behavior and localizes change. Test through that interface. Examine dependency types and existing adapters before introducing a port; avoid an abstraction supported only by a hypothetical second implementation. Compare at least one simpler alternative when a consequential seam is new.

Use the existing codebase's terminology and structure. This skill advises internal module shape; `api-design` handles a consumer-facing API contract. Skip when the existing seam plainly fits the change. Return the recommendation, affected callers and verification implications; do not initiate implementation.

Source: adapted from [Matt Pocock's `codebase-design`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/codebase-design/SKILL.md).
