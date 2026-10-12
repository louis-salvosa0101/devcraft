---
name: release
description: Verify release readiness and, when separately authorized, deployment evidence. Run only when the developer requests a release review.
disable-model-invocation: true
---

# Release

Activation: the developer requests release readiness or an authorized release. Input is the candidate revision, target environment, deployment method, approved requirements, and known risks.

Check the actual test and build results, environment/configuration requirements, migrations, security-sensitive boundaries, accessibility for shipped UI, observability, smoke path, known issues, and rollback or recovery procedure proportionate to the release. Use `security-review` or `browser-testing` when their risk or UI conditions apply. Record exact commands, environment and outcomes. A missing check is a limitation, not a pass.

Present readiness and unresolved blockers before deployment. Deploy only when the developer has authorized that action in this session or earlier. After deployment, verify the real target with a smoke check and report its result; never infer success from a command exit alone. If deployment fails, preserve evidence and recovery steps.

Done when readiness is evidenced, or the authorized deployment and post-release verification are observed. Do not silently begin another workflow.

Source: adapted from [Addy Osmani's shipping and launch skill](https://github.com/addyosmani/agent-skills/blob/1be8e34187e34647bb83adc3a1323b26ae6f6abe/skills/shipping-and-launch/SKILL.md); its multi-agent `/ship` command is excluded.
