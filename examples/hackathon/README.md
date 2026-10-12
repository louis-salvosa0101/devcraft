# Scenario C: four-hour hackathon

Build a demo that turns a pasted meeting transcript into a short, editable action list.

**Profile:** rapid. Timebox `grill-with-docs` to 15 minutes: agree on demo audience, sample input, acceptable data handling, and one success path. In one compact approval pass, record MVP outcomes in `docs/product.md`, a simple visual direction in `docs/design.md`, and the data/API boundary in `docs/tech-spec.md`. Omit nonessential features and architecture. Do not skip secret handling, basic keyboard access, or critical errors.

Use `prototype` only if transcript extraction is uncertain; discard the experiment after recording its conclusion. `to-tickets` proposes two small slices for approval:

1. `T-001-paste-and-extract`: paste input, extract tasks, display editable list, test the sample transcript.
2. `T-002-save-and-demo`: local save/export, empty/error states, demo smoke flow.

Run `implement` for one slice at a time. Use `frontend-engineering`, `tdd` for critical behavior, `browser-testing` for the demo path, and `code-review` for obvious breakage. Failed critical-path tests stop completion even under time pressure; `diagnosing-bugs` narrows them. `ui-review` checks the visible screen against the compact direction. `release` verifies the actual demo URL only if deployed, records remaining shortcuts, and explains recovery if the demo fails.

**Expected routing:** timeboxed decisions, two vertical slices, critical-path evidence, and honest deployability status. This is a planned trace, not a verified deployment.
