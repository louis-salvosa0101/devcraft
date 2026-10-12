---
name: visual-taste
description: Assess whether visual composition, typography, density, and motion suit a specific product and avoid generic UI patterns.
---

# Visual Taste

Input: product audience/purpose, approved brand and `docs/design.md` when present, and a proposed or rendered interface. Output: a few specific observations or options for the calling design, frontend, or review workflow.

Judge hierarchy, type, spacing, color, density, imagery and motion against the actual brief. Name what is generic or incoherent and why it harms comprehension or identity; recommend the smallest concrete correction. Preserve useful existing brand and product behavior during redesign. Motion should serve feedback or meaning and respect reduced-motion preferences. Do not impose dark mode, an image, a framework, a fixed page structure, or universal aesthetic bans.

This specialist does not write `docs/design.md`, implement UI, or replace an approved direction. Skip when there is no visual decision or interface to assess. If a recommendation contradicts that direction, return it as a proposed revision for developer approval.

Source: adapted from [Taste Skill's `design-taste-frontend`](https://github.com/Leonxlnx/taste-skill/blob/d237dd399d57524945c0c81327da5da19f7a468d/skills/taste-skill/SKILL.md), limited to portable visual judgment.
