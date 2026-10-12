---
name: diagnosing-bugs
description: Find a root cause from a failing test, build, or user symptom and verify the targeted fix.
---

# Diagnosing Bugs

Input: exact symptom, environment, existing failure output, and relevant code. Output: a reproducible cause or a documented evidence gap, then a verified fix when possible.

First build a tight feedback loop that observes the user's symptom. Redact secrets in captured commands and logs. Reproduce and minimize the failure, then compare falsifiable hypotheses against that signal. Instrument only to distinguish hypotheses. Fix the shared cause and add a regression test at a correct public seam when possible; rerun both the minimized and original scenarios. Remove temporary instrumentation and report the cause and evidence.

If reproduction needs unavailable access or data, state what was attempted and request the specific redacted artifact or environment needed. Do not mask a failed test with fallback behavior or mark a ticket done without green verification. Skip when there is no failure or uncertain symptom to diagnose. Return findings to the calling workflow; do not open a separate lifecycle stage.

Sources: [Matt Pocock's diagnosis loop](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/diagnosing-bugs/SKILL.md) and [Addy Osmani's debugging/recovery](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/debugging-and-error-recovery/SKILL.md).
