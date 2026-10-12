---
name: security-review
description: Review actual trust boundaries when work handles untrusted input, authorization, secrets, personal data, or third-party services.
---

# Security Review

Input: data flows, assets, changed code/config, dependencies, and the current threat context. Output: prioritized findings and verification gaps to the caller.

Trace untrusted input to validation and sensitive operations. Check authentication separately from authorization, ownership rules, secret handling, data exposure, output encoding, dependency changes, and failure behavior. Use a compact threat map only where it reveals a real boundary; verify each finding against the code or running behavior. Recommend a proportionate fix and test. Redact secrets from reports.

Skip a standalone pass for a change with no meaningful security boundary; ordinary code review still applies. Do not add generic approval ceremonies or claim a comprehensive audit from a narrow diff. Return unresolved risk to `technical-design`, `implement`, or `release` as appropriate.

Source: adapted from [Addy Osmani's security and hardening](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/security-and-hardening/SKILL.md).
