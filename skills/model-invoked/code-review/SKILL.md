---
name: code-review
description: Review a scoped diff against requirements and repository standards, including whether each addition is necessary.
---

# Code Review

Input: a fixed Git comparison point or clearly bounded working diff, applicable specs/ticket, repository standards, and verification output. Output: actionable findings for the caller.

Pin the diff before review. Check two separate axes: **Spec** (missing, incorrect, or extra behavior) and **Standards** (correctness, maintainability, conventions, security-sensitive boundaries and performance risks). Also check whether each addition is needed: flag duplicated logic or rules, speculative options, abstractions or dependencies, and unrelated edits only when a smaller complete fix preserves behavior. Preserve required validation, data-loss handling, security, accessibility and requested behavior. Cite the relevant requirement or rule and file location for each finding. Rank by user impact; distinguish verified defects from judgment calls. Do not repeat automated lint/test findings as manual style comments. If no spec exists, say so and review the stated request.

Use one agent by default. Return findings to `implement` for fixes and recheck; this specialist does not commit or mark a ticket done. Skip a review only when there is no code diff to inspect.

Sources: [Matt Pocock's two-axis review](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/code-review/SKILL.md) and [Addy Osmani's quality review](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/code-review-and-quality/SKILL.md).
