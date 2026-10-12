---
name: ui-review
description: Review and refine an implemented UI against approved docs/design.md. Run only when the developer requests UI review.
disable-model-invocation: true
---

# UI Review

Activation: the developer asks to review built UI. Input is approved `docs/design.md`, relevant product outcomes, and the implemented route or screen. Skip when no UI exists.

Inspect the rendered interface in available viewport sizes and states; use `browser-testing` when browser tools are available. Compare actual hierarchy, typography, spacing, color, component states, responsive layout, interaction, keyboard behavior, and motion against `docs/design.md`. Separate observed technical defects from design judgments, and state the evidence and user impact for each finding. Use `visual-taste` only for context-fit questions; it is not a second design authority.

Prioritize broken tasks, data loss and accessibility before visual refinements. Apply narrow fixes within the approved direction when the developer requested refinement, then recheck the affected path. If the right fix changes the direction itself, propose a `docs/design.md` revision for approval instead of silently rewriting it. Do not claim compliance or browser coverage from screenshots alone.

Done when findings are prioritized, applied fixes are verified, and any remaining disagreement with approved direction is explicit. This stage does not start release.

Sources: Impeccable [`critique`](https://github.com/pbakaus/impeccable/blob/c63b8dd7dd5a5f3c32eaabe1af76d0694f863ed2/plugin/skills/impeccable/reference/critique.md), [`audit`](https://github.com/pbakaus/impeccable/blob/c63b8dd7dd5a5f3c32eaabe1af76d0694f863ed2/plugin/skills/impeccable/reference/audit.md), and [`polish`](https://github.com/pbakaus/impeccable/blob/c63b8dd7dd5a5f3c32eaabe1af76d0694f863ed2/plugin/skills/impeccable/reference/polish.md), adapted without its engine.
