# Validation record

**Date:** 2026-10-12. Results below apply to this checkout and the local Windows host. A scenario walkthrough checks the written routing and handoff contracts; it does not prove a model followed them in a new project.

## Automated checks

Command: `python -m unittest discover -s tests -v` (Python 3.12, Windows). **Result: 7 tests run; 6 passed, 1 skipped**. The suite checks all 23 source entrypoints for unique portable frontmatter, local documentation links, installation into Codex/Claude Code/Cursor project paths, workflow-only invocation metadata, clean reruns, missing-file repair, and refusal to overwrite edited or unrelated skills without partial writes. One installation test uses a project path containing a space.

The installer uses only Python's standard library. Its `--check` mode returns nonzero for missing files; installation creates no project specs, tickets, or agent instructions. The directory-symlink escape test is skipped on this Windows account because creating directory symlinks is unavailable. The code still rejects paths whose resolved targets leave the project, but that branch was not dynamically exercised here.

Codex's optional `skill-creator/scripts/quick_validate.py` was attempted on `setup-devcraft` and could not start because PyYAML is absent from this Python environment (`ModuleNotFoundError: yaml`). The repository's own source-format test passed; no dependency was added solely for that optional checker.

`npx --yes skills@latest add . --list` discovered all 23 skills in the nested source layout. `python -u tests/npx_probe.py codex`, `claude-code`, and `cursor` each used the current Skills CLI in a temporary project with `--skill '*' --copy --yes`: all three installed 23 `SKILL.md` files and preserved `setup-devcraft`'s user-only frontmatter and Codex sidecar. This validates the CLI packaging locally, not a GitHub download or host enforcement.

After publishing the public GitHub repository, `npx --yes skills@latest add louis-salvosa0101/devcraft --list` discovered all 23 remote skills. `python -u tests/npx_probe.py codex louis-salvosa0101/devcraft` installed all 23 into a temporary Codex project and preserved `setup-devcraft`'s invocation metadata. This verifies the documented GitHub install source; it does not test live Claude Code or Cursor routing.

## Scenario walkthroughs

| Scenario | Written contract exercised | Observed walkthrough result |
| --- | --- | --- |
| [Small CRUD](../examples/crud-app/README.md) | Lightweight profile; approved compact product/technical decisions; optional design; ready contact ticket; one vertical slice. | `ask-workflow` should recommend `implement` for the ready ticket. `implement` reads its referenced sections, performs form/persistence/test work, records checks, and leaves a failing ticket in progress. No extra planning stage is required. |
| [Full-stack SaaS](../examples/fullstack-saas/README.md) | Standard profile; product, visual and technical document owners; tenant/role boundary; gated ticket graph. | With approved product/technical docs but no visual direction, `ask-workflow` should recommend `design-direction` before frontend tickets. A product/design contradiction is returned for developer resolution. A failed tenant-isolation test blocks ticket completion and release. |
| [Four-hour hackathon](../examples/hackathon/README.md) | Rapid profile; timeboxed discovery; compact approval; two slices; critical-path checks. | With an idea but no approved docs, `ask-workflow` should recommend `grill-with-docs`. The rapid route keeps critical security, accessibility and error handling, and release cannot claim a demo URL before verifying it. |

The scenario rows are deterministic reviews of the skill text and example project states. They are not implementation, UI, or deployment test results.

### Live Codex routing probe

`python -u tests/live_probe.py` creates temporary projects, installs the Codex adapter, and explicitly invokes `$ask-workflow` through `codex exec` in read-only mode. Host: Codex CLI 0.162.1 on Windows. The first command failed in the probe harness after the CRUD result because Python decoded a later UTF-8 response with the Windows legacy code page; the harness was corrected to decode UTF-8. `python -u tests/live_probe.py saas hackathon` then exited 0.

| Fixture | Observed next stage and reason | Stage started or files changed? |
| --- | --- | --- |
| CRUD | `$implement` for Ready T-001; cited Approved product/technical docs and noted a missing platform choice. | No. |
| SaaS | `$design-direction`; approved web UI scope and technical spec existed, but `docs/design.md` did not. | No. |
| Hackathon | `$grill-with-docs`; setup was complete, but demo input, output, and success criteria were unsettled. | No. |

The first SaaS fixture had a one-sentence “Approved” product document; Codex recommended clarification rather than accepting the status label as sufficient. After the fixture recorded the user flow and MVP outcome, it recommended design direction. The first hackathon fixture lacked evidence of completed setup; Codex recommended `setup-devcraft`. After the fixture recorded setup in `AGENTS.md`, it recommended clarification. These are useful prerequisite checks, not failures in the final fixtures. The probes test explicit routing only; they do not test implicit suppression, specialist loading, implementation, or deployment.

## Gate and compatibility limits

- User-invoked skills require a developer request in their descriptions and bodies. Installed workflow copies carry `disable-model-invocation: true`; Codex copies also carry `allow_implicit_invocation: false`. Specialist copies do not carry either flag. The automated tests inspect the installed files, not a host's enforcement.
- `to-tickets` asks for breakdown approval before writing local files. Product, design and technical drafts require approval before their decisions become authoritative. Conflicting approved passages are escalated; no automatic merge rule exists.
- `implement` handles one ready ticket by default. Failing checks keep it in progress or blocked; `diagnosing-bugs` supports investigation. `release` requires build, smoke, configuration, and recovery evidence and distinguishes readiness from verified deployment.
- Codex, Claude Code and Cursor installation layouts were tested with temporary local projects. Live discovery, implicit suppression, named specialist activation, and end-to-end execution in Claude Code and Cursor were not tested. No other agent compatibility is claimed.
