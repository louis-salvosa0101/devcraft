# Scenario B: full-stack SaaS

Build a team expense approval product with members, submitters, approvers, an audit trail, and a web UI.

**Profile:** standard. Invoke `setup-devcraft`, `grill-with-docs`, and `product-spec` to settle roles, approval rules, retention, and acceptance outcomes. The developer approves `docs/product.md`. `design-direction` establishes navigation, typography, color/status semantics, loading/error/empty states, responsive layouts, and keyboard behavior in `docs/design.md`; the developer approves it before UI work. `technical-design` defines tenant isolation, role checks, data invariants, API contracts, error responses, audit writes, and tests in `docs/tech-spec.md`; consequential decisions need approval.

`to-tickets` proposes approval-dependent vertical slices with document-section links and obtains breakdown approval:

1. `T-001-team-and-membership`: create team, invite member, enforce team-bound reads.
2. `T-002-submit-expense`: create expense through UI and API with validation and audit event.
3. `T-003-approve-or-reject`: role-bound decision, status UI, audit and denial tests.

Run `implement` separately for each ticket. `api-design`, `frontend-engineering`, `tdd`, `security-review`, `browser-testing`, and `code-review` contribute only where relevant. A product rule found in `docs/design.md` that conflicts with `docs/product.md` is referred to the product owner document and the developer for resolution; implementation does not guess. A failed isolation test blocks `Done`. `ui-review` verifies the built UI against the approved design, then `release` checks build, configuration, smoke flow, known issues, and recovery plan.

**Expected routing:** approved document ownership, secure tenant boundaries, accessible UI, evidence for each ticket and release gate. This trace does not claim a live SaaS was built or deployed.
