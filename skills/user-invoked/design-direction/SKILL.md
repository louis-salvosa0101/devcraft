---
name: design-direction
description: Establish an approvable visual system at docs/design.md before UI implementation. Run only when the developer requests design direction.
disable-model-invocation: true
---

# Design Direction

Activation: the developer requests visual direction for a UI. Skip this stage for work with no interface. Input is approved product scope, existing UI/brand evidence, constraints, and any validated prototype.

Inspect the actual product and visual context. Ask only unresolved choices that materially change the direction. Use `visual-taste` for context-fit and anti-generic critique. Write `docs/design.md` with `Status: Draft` and concrete decisions: visual concept and rationale; typography roles and scale; palette with semantic roles and values; spacing/grid; density; component shape and states; hierarchy; responsive behavior; interaction and motion purpose, including reduced motion; accessibility targets and known constraints. Distinguish existing tokens from proposed values. Include project-specific anti-patterns, not blanket style bans.

For redesigns, preserve product flows, labels, form fields, brand assets and other approved behavior unless the developer changes their owner documents. Present the draft for approval and stop before frontend implementation. `frontend-engineering` applies the direction; `ui-review` evaluates built UI against it. A conflict with `docs/product.md` must be resolved with the developer, not hidden in styling.

Done when a frontend implementer can make consistent choices without inventing the visual system. The output is a decision document, not code.

Sources: [Taste Skill's design read](https://github.com/Leonxlnx/taste-skill/blob/d237dd399d57524945c0c81327da5da19f7a468d/skills/taste-skill/SKILL.md), and Impeccable's [`shape`](https://github.com/pbakaus/impeccable/blob/c63b8dd7dd5a5f3c32eaabe1af76d0694f863ed2/plugin/skills/impeccable/reference/shape.md) and [`document`](https://github.com/pbakaus/impeccable/blob/c63b8dd7dd5a5f3c32eaabe1af76d0694f863ed2/plugin/skills/impeccable/reference/document.md) references; no Impeccable engine dependency.
