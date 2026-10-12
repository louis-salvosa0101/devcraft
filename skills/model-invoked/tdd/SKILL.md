---
name: tdd
description: Use a behavior-first red/green loop for new logic or bug fixes when a meaningful public test seam exists.
---

# Test-Driven Development

Input: expected observable behavior, approved testing seam or public interface, and the project's test command. Output: a regression or behavior test plus passing implementation evidence for the caller.

Use the seam approved in `docs/tech-spec.md` when present. For a new consequential seam, explain what it catches and misses and resolve it with the developer. Write one test whose expected result comes from requirements or a known example, observe it fail for the target behavior, then write only enough production code to pass. Repeat by vertical slice, refactor safely, and run relevant broader checks. Prefer real collaborators; mock external boundaries only when needed. Do not test private call counts or recompute the expected value using the production algorithm.

Skip when the change is documentation, static data, or another trivial edit without meaningful behavior. If no correct seam exists, report that limitation instead of writing a tautological test. Return the red/green commands and outcomes to the calling workflow.

Sources: [Matt Pocock's `tdd`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/tdd/SKILL.md) and [Addy Osmani's test-driven development](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/test-driven-development/SKILL.md).
