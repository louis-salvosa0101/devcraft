---
name: prototype
description: Build a disposable experiment to answer one uncertain logic, state, or UI design question.
---

# Prototype

Input: one decision that cannot be settled confidently from discussion or static code. Output: a runnable experiment, observed answer, and a pointer for the calling workflow.

State the question and what result would settle it. Build the smallest runnable experiment in the host project's tools, with in-memory or scratch data. For logic, expose relevant state transitions; for UI, compare genuinely different structures in the real visual context where possible. Keep it clearly marked as a prototype and easy to run. Test the question, capture the observation and decision, then remove throwaway code from the production path or preserve it outside the release branch when useful.

Do not promote prototype code directly to production without the normal validation, error handling and tests. Skip when the answer is already known from requirements or a cheap code inspection. Return control to the calling clarification, design, or technical workflow.

Source: adapted from [Matt Pocock's `prototype`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/prototype/SKILL.md).
