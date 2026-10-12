---
name: frontend-engineering
description: Implement an approved UI direction with accessible states, responsive behavior, and browser evidence for the current ticket.
---

# Frontend Engineering

Input: one ticket or scoped change, approved `docs/design.md`, relevant product behavior, and the host app's existing components and stack. Output: implemented UI and verification evidence to `implement`.

Reuse the project's design tokens, components and patterns. Implement the requested journey through loading, empty, error, success and disabled states where applicable. Use semantic controls, keyboard/focus behavior, readable contrast and responsive layouts. Preserve approved copy, navigation, forms and analytics behavior unless the ticket changes them. Test rendered behavior with available browser tools and report viewport and interaction coverage.

This skill applies the design direction; it does not choose a new visual system or perform the independent `ui-review` stage. Surface a missing or contradictory direction instead of inventing a permanent design rule. Skip when the task has no frontend surface.

Source: adapted from [Addy Osmani's frontend UI engineering](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/frontend-ui-engineering/SKILL.md).
