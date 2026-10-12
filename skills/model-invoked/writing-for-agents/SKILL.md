---
name: writing-for-agents
description: Improve skill, AGENTS.md, and pointed-to documentation so agents load the right instructions and know when work is complete.
---

# Writing for Agents

Input: an agent-facing document and the tasks it must guide. Output: a shorter, actionable document or review findings for its caller.

Put each rule in one authoritative place. Make discovery pointers name the situations that should load a document; keep the always-visible description narrow. Place ordered actions and concrete completion criteria in the main file. Move branch-specific details to a reference only when they are not needed in every run. Keep a concept's definition and caveats together. Prefer positive, checkable instructions over repeated warnings or prose a model already knows.

Inspect actual callers before moving or deleting a document. Preserve authorization gates, validation, error handling and user-owned decisions. Do not create a separate reference or skill without an independent reason to load it. Skip when no agent-facing instruction is being changed or reviewed. Return the changed document and any unresolved ambiguity to the calling workflow.

Source: adapted from [Matt Pocock's `writing-for-agents`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/productivity/writing-for-agents/SKILL.md).
