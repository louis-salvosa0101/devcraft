---
name: api-design
description: Define or review a public API or interface contract when consumers, data validation, errors, or evolution matter.
---

# API Design

Input: consumers, approved product behavior, current API/schema, data and trust boundaries. Output: a contract proposal or targeted findings for the calling workflow.

Specify operations and typed input/output shapes in the host stack's conventions. State validation at untrusted boundaries, authorization checks, error semantics, version/evolution strategy, and observable behavior. Add pagination, retry, idempotency, rate limiting or deprecation plans only where the actual use or side effects warrant them. For state-changing retries, identify how duplicate effects are prevented atomically when that risk exists.

Check existing callers and compatibility before changing a contract. Hand an architectural decision to `technical-design` or a scoped implementation detail to `implement`; do not change approved product semantics. Skip when no external or cross-module contract changes.

Source: adapted from [Addy Osmani's API/interface design](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/api-and-interface-design/SKILL.md).
