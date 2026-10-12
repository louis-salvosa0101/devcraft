# DevCraft architecture

**Status:** Approved by the developer on 2026-10-12; implemented for the first release.
**Tagline:** From idea to production. One skill at a time.

DevCraft is a source collection of portable Agent Skills, not an agent runtime. A developer starts each major stage. Specialist skills contribute bounded expertise inside that stage. The active project's documents carry decisions between sessions. The [source audit](research/source-audit.md) and [provenance record](research/provenance.md) pin the upstream material behind this architecture.

## Skill boundary

| Tier | First-release skills | Activation and result |
| --- | --- | --- |
| User-invoked | `setup-devcraft`, `ask-workflow`, `grill-with-docs`, `product-spec`, `design-direction`, `technical-design`, `to-tickets`, `implement`, `ui-review`, `release` | Developer names the stage. The stage produces or reviews one owned artifact, then stops. |
| Model-invoked | `grilling`, `domain-modeling`, `writing-for-agents`, `codebase-design`, `api-design`, `visual-taste`, `frontend-engineering`, `tdd`, `diagnosing-bugs`, `browser-testing`, `code-review`, `security-review`, `prototype` | Agent loads a specialist only for the current stage's relevant branch. The specialist returns findings or a focused artifact to its caller and cannot advance the lifecycle. |

These 23 skill entrypoints are implemented. `design-principles` is excluded as a separate first-release skill: its reusable checks belong in design direction and UI review, avoiding a third visual authority. `visual-taste` has distinct call sites in direction, implementation and review; `browser-testing` covers browser-specific verification. The source names and decisions are recorded in the audit.

`ask-workflow` recommends one next stage from repository state; it never invokes that stage. `implement` selects one unblocked ticket and works it in one agent session by default. A specialist may be used by a user-invoked stage, and a developer may request one directly, but it cannot silently start another major stage. A finished stage reports its artifact, evidence, remaining uncertainty, and suggested next stage, then awaits a separate developer instruction.

### `setup-devcraft` contract

The developer invokes this skill after the adapter or manual installation makes the DevCraft collection discoverable. It inspects the project root, existing agent instructions, installed skills, verification commands, and tracker evidence. It asks for any missing choice: whether the DevCraft block belongs in `AGENTS.md`, `CLAUDE.md`, or both, and whether tickets belong in local Markdown or GitHub Issues. `AGENTS.md` is recommended for portability; when both files are selected, `CLAUDE.md` imports `AGENTS.md` rather than duplicating rules. Local tickets use `docs/tickets/<feature-slug>/T-001-<ticket-slug>.md`. GitHub Issues requires an authenticated `gh` CLI and uses the repository identified by the configured GitHub origin. Setup records the choice and does not create remote issues, labels, or projects.

Completion requires the installed skill names and required support files to be discoverable in the active host, the chosen instruction file(s) to record the selected tracker, and no pre-existing instructions or tickets to have been overwritten. If setup already matches, it reports that fact and changes nothing. If an existing tracker convention conflicts, it surfaces the conflict for the developer rather than replacing it. It then hands back to the developer or `ask-workflow`; it does not start discovery or specification.

## Default route and profiles

```text
setup-devcraft (once per project)
     ↓
idea → grill-with-docs → product-spec → design-direction → technical-design
     → to-tickets → implement (one ticket) → ui-review → release
```

The route is a guide. `setup-devcraft` is a one-time project setup and may be rerun to repair or change configuration. `ask-workflow` checks whether setup is complete, then existing approved documents, ticket state, and the request type before recommending a step. A bug fix may start with diagnosis; backend-only work may omit visual stages; an existing application reuses its approved direction. No stage is repeated solely to complete the diagram.

| Profile | Planning depth | Implementation and verification |
| --- | --- | --- |
| Lightweight | Compact product and technical decisions; design only for visible UI changes; one ticket only when it helps a fresh session. | Small slices; relevant tests and review. |
| Standard | Approved product, design where relevant, and technical documents; ticket graph for multi-session work. | One ready ticket at a time; full relevant tests, UI review, release checks. |
| Rapid | Timeboxed clarification; one compact approval pass for critical product, design, and technical decisions; few slices. | Critical-path tests, demo and deployment checks; record shortcuts and known limits. |

Profiles change document depth and number of stages, never permission to skip a security boundary, accessibility requirement, failing test, or deployment verification. The active project's `AGENTS.md` may set a default profile; a developer can override it per request.

## Document ownership and gates

| Artifact | Owns | Required handoff |
| --- | --- | --- |
| `docs/product.md` | Users, problem, scope, journeys, functional and nonfunctional outcomes, exclusions, acceptance outcomes. | `product-spec` presents the draft; explicit developer approval records `Status: Approved`. |
| `docs/design.md` | Visual identity, concrete tokens, typography, hierarchy, components, motion, responsive and accessibility rules. | `design-direction` presents concrete decisions before frontend implementation; skip when no UI. |
| `docs/tech-spec.md` | Architecture, data and API contracts, auth boundaries, errors, technology decisions, testing seams. | `technical-design` presents consequential decisions for approval. |
| Local ticket file or GitHub Issue | One demoable slice, blockers, links to relevant spec sections, acceptance criteria, status, verification evidence. | `to-tickets` previews the graph for approval before writing files or creating issues; `implement` updates status only after checks pass. |
| `AGENTS.md` and/or `CLAUDE.md` | Project conventions, document locations, verification commands, profile default, selected tracker, skill invocation guidance. | `setup-devcraft` clarifies the owner file(s) and updates only the DevCraft block; if both are chosen, `CLAUDE.md` imports `AGENTS.md`. |

For generated documents, use `Status: Draft` until the developer explicitly approves that decision set. Approval applies to the artifact revision reviewed; material edits return it to draft. Local tickets use `Draft`, `Ready`, `In progress`, `Blocked`, or `Done`; GitHub Issues remain open until Done, with the same status and blocker fields in the issue body. Completion records exact commands, results, and any unverified criterion. A task with failing checks remains blocked or in progress.

**Conflict rule:** classify the disputed decision by the owner above, show the contradictory passages, and ask the developer to resolve a conflict between approved artifacts. Do not silently prefer the newest document or rewrite an approved one. Tickets point to exact headings or stable anchors; they do not copy entire specs. `implement` reads only relevant sections plus the code it touches.

## Handoff contracts

1. `setup-devcraft` inspects the project and active agent, verifies installed skill names and dependencies, and offers a repair through the host adapter when its source checkout is available. It asks about the instruction file (`AGENTS.md`, `CLAUDE.md`, or both) and tracker (local Markdown or GitHub Issues) when no choice is recorded, verifies GitHub CLI access if needed, records the choices and verification commands, and preserves existing project rules. It creates no ticket or GitHub issue and does not start another workflow.
2. `grill-with-docs` records settled terminology and only consequential ADRs, then summarizes open decisions. It calls on `grilling` and `domain-modeling` by skill name, not a particular provider's Skill tool.
3. `product-spec` consumes clarified decisions and existing code context. It owns product outcomes; technical or visual choices are pointers or open questions for their owners.
4. `design-direction` consumes approved product outcomes and existing brand/UI constraints. Its output specifies actionable values and responsive behavior. `frontend-engineering` implements it later; `ui-review` evaluates the result against it.
5. `technical-design` consumes product and relevant design decisions. It resolves module boundaries, contracts, security boundaries, and test seams without inventing product scope.
6. `to-tickets` consumes approved applicable documents, proposes vertical slices and blockers, obtains approval, then writes local ticket files or creates GitHub Issues according to project setup. A single-session change may proceed without tickets when the developer invokes implementation directly.
7. `implement` checks readiness and dependencies in the configured tracker, makes one slice, invokes only applicable specialists, runs targeted checks and the relevant full suite, reviews the diff, and records evidence. It does not commit, push, or deploy without authorization.
8. `ui-review` measures the built UI against the approved direction and verifies targeted refinements. A change to the direction is a proposed document revision for approval.
9. `release` verifies the actual build, configuration, security-sensitive paths, smoke test, known issues, and recovery path. It distinguishes readiness from a deployment actually performed and verified.

## Portable packaging

The source of truth remains under `skills/user-invoked/` and `skills/model-invoked/`. Each skill is a directory with `SKILL.md` using the Agent Skills standard `name` and `description` frontmatter. Workflow skills also carry optional user-only frontmatter and a Codex sidecar so generic installers preserve explicit invocation controls. Body instructions do not require a proprietary CLI, model, or skill-calling API. The standard-library installer copies the collection, including `setup-devcraft`, into the host's discovery path and filters Codex sidecars from other agents. `npx skills` can install the same source directly. The Python installer refuses to overwrite an unrelated skill of the same name; manual-copy instructions provide a fallback. Once the agent discovers the setup skill, the developer invokes it to verify installation and configure the project. Generated project docs point to installed skill names, not DevCraft source paths.

The two-tier invocation rule needs both an instruction and host support. Adapters add a host's supported user-only metadata. `AGENTS.md` carries the shared project guidance; Claude Code may need `CLAUDE.md` with an `@AGENTS.md` import when its own file takes precedence or its version cannot load `AGENTS.md` directly. When a host offers no verified strict user-only control, the skill body can stop unless the developer explicitly requested that stage, but this is a best-effort convention rather than a security boundary. Avoid shipping duplicate copies into several paths that one agent scans. [Validation](validation.md) reports installed-file checks, live routing evidence, and untested host behavior separately.

## Repository scope

```text
README.md                 installation and usage
AGENTS.md                 this repository's own agent guidance
LICENSES.md               DevCraft license and upstream notices
docs/architecture.md      approved contracts and boundaries
docs/research/             pinned audit and provenance
skills/user-invoked/       major workflow skills that earn independent use
skills/model-invoked/      bounded specialist skills that earn independent use
templates/                 four owned document templates
adapters/                  minimal tested Codex, Claude Code, Cursor installation guidance
tests/                     format, routing, gate, handoff, and scenario checks
examples/                  three concise scenario traces
```

Directories and files exist only when populated. Installer tests cover bootstrap, rerun idempotence, repair, and collision protection. Scenario traces exercise a small CRUD app, full-stack SaaS, and four-hour hackathon without asserting that an unrun agent complied. Live agent tests and deployment claims require separate evidence.

## Approved architectural decisions

- **Per-project choice:** `setup-devcraft` asks whether to use local Markdown in `docs/tickets/` or GitHub Issues, and records the choice. Local Markdown needs no external service; GitHub mode requires authenticated `gh` access. No setup step creates remote issues or labels.
- **One ticket per explicit `implement` invocation.** Upstream parallel `implement-spec` orchestration is excluded.
- **Portable core frontmatter plus adapter metadata.** Strict explicit invocation is claimed only after live verification in a host.
- **Source-grounded adaptation.** The Impeccable engine and workflow sidecars are excluded.
- **One small installer with a manual-copy fallback.** It is idempotent for DevCraft-owned targets and refuses unrelated files.
- **MIT for DevCraft's original prose.** Upstream licenses and notices are recorded in `LICENSES.md`; no upstream files or assets are redistributed.

## Integration risks and unresolved choices

| Risk or choice | Current handling |
| --- | --- |
| Invocation flags and dependency resolution are not standardized by Agent Skills. | Test discovery, user-only routing, named specialist handoffs, and project guidance independently in each available host. Treat untested hosts as documented-only. Core skills say what to do if a dependency is unavailable; they never pretend an import occurred. |
| A setup skill cannot install itself before discovery. | The adapter installs the collection first. `setup-devcraft` then verifies it and configures the project; manual-copy instructions cover hosts without a working adapter. |
| Impeccable's engine and root `DESIGN.md` contract differ from DevCraft's path. | Use an original `docs/design.md` contract; exclude engine, sidecars and command wrappers. |
| Taste targets marketing surfaces, while DevCraft also targets product UI. | Reuse judgment about context, hierarchy, density and motion, not its page recipes or stack restrictions. |
| Approved documents can disagree or drift after edits. | One owner per decision type; compare passages and request a developer resolution. Material edits revert an approved artifact to draft. |
| User-only workflow discovery may degrade with many specialist descriptions. | Keep descriptions narrow, validate install listings, and combine a candidate specialist into an on-demand reference if it adds no independent trigger. |
| Third-party material may carry different notices from the root license. | Copy no external media, fonts, binaries or compiled engines; audit every eventual copied text file and preserve notices. |
| Strict user-only behavior across hosts remains unverified. | Ship Codex, Claude Code and Cursor adapters; describe the metadata as a request to each host, not proof of enforcement. |

The developer approved these boundaries and the concrete skill inventory before implementation.
