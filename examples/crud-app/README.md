# Scenario A: small CRUD application

Build a private contact list with create, edit, search, and delete. Assume one developer, one browser UI, and a local database.

**Profile:** lightweight. Invoke `setup-devcraft` once, then `ask-workflow`. A short `grill-with-docs` round resolves whether delete is permanent and whether contacts are shared. `product-spec` records the minimum outcomes in `docs/product.md`; `technical-design` records the chosen storage and validation boundary in `docs/tech-spec.md`. Use `design-direction` only if the UI lacks an approved direction; keep `docs/design.md` compact. The developer approves consequential choices before coding.

One session may implement a scoped feature directly. For a multi-session project, `to-tickets` proposes and gets approval for:

1. `T-001-create-and-list-contacts`: persistence, form, list, empty state, validation test.
2. `T-002-edit-and-search`: update path, search behavior, keyboard and responsive checks.
3. `T-003-delete-contact`: confirmation, access control if needed, deletion test.

Invoke `implement` once for each ready ticket. `frontend-engineering`, `tdd`, `browser-testing`, and `code-review` are relevant; `security-review` checks any personal-data or authorization boundary. A failed test keeps the ticket in progress and calls for `diagnosing-bugs`. Run `ui-review` for the visible screens and `release` only when shipping. Verification evidence belongs in each ticket; release evidence belongs in the release report.

**Expected routing:** small specs, no repeated interview, one vertical slice at a time, no automatic deploy. This is an example trace, not a claim that an agent built the app.
