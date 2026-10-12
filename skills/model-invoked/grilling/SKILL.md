---
name: grilling
description: Interrogate unsettled requirements in dependency-ordered rounds when a workflow needs the developer's decisions.
---

# Grilling

Input: a concrete idea, known facts, prior answers, and open decisions. Output: settled decisions and the remaining frontier for the calling workflow. Do not start specification or implementation.

Map which decisions depend on others. Ask a short round of currently answerable questions, each with a recommendation and its trade-off; defer downstream questions until prerequisites are settled. Find repository or external facts yourself instead of interviewing the developer for them. After each answer, update the frontier, identify contradictions, and ask only what remains material. Stop when questions are settled or explicitly deferred, then return a concise decision record to the caller.

Use only when clarification can change the work. If an approved owner document already resolves a question, cite it rather than repeat it. If it conflicts with the developer's answer, surface both. Approval of an answer closes that decision, not the next lifecycle stage.

Source: adapted from [Matt Pocock's `grilling`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/grilling/SKILL.md).
