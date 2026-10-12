---
name: implement
description: Implement one ready DevCraft ticket or one explicitly scoped small change with verification. Run only when the developer requests implementation.
disable-model-invocation: true
---

# Implement

Activation: the developer requests a specific ticket or a clearly scoped direct change. Choose one ready, unblocked ticket; if the reference is ambiguous, resolve it before editing. A direct small task can bypass ticketing when authorized.

Read the ticket from the configured local Markdown or GitHub Issues tracker, only relevant sections of approved product/design/technical documents, current code and callers, and applicable `AGENTS.md`/`CLAUDE.md` instructions. For GitHub Issues, verify the configured repository and read the issue with `gh`; preserve existing body content when updating its DevCraft status or verification. Mark an existing ticket `In progress`. Implement one complete vertical slice using existing patterns. Load only specialists that the slice requires: `frontend-engineering`, `api-design`, `tdd`, `diagnosing-bugs`, `browser-testing`, or `security-review`. A specialist advises the current task; none opens the next stage.

Run targeted tests/typechecks during the work and the relevant full suite before completion. On failure, use the red output to diagnose; do not mark the ticket done while checks fail. Review the diff against the spec and repo standards using `code-review`. Record commands, results, and any unverified criterion under ticket verification; mark `Done` only when acceptance criteria and checks pass. For GitHub Issues, close the issue only after marking it Done with evidence. Mark dependent tickets `Ready` only if all their blockers are Done. Report changed behavior, evidence, and limitations.

Do not implement another ticket, silently revise approved specs, or commit, push, or deploy without authorization. If the ticket contradicts an approved owner document, stop that branch and request a decision. If there is no ticket, report verification in the response rather than inventing one.

Sources: [Matt Pocock's `implement`](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/implement/SKILL.md) and [Addy Osmani's incremental implementation](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/incremental-implementation/SKILL.md); upstream automatic commit was removed.
