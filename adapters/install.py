"""Install DevCraft skills into a project's agent discovery directory."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


SOURCE = Path(__file__).resolve().parents[1] / "skills"
TARGETS = {
    "codex": Path(".agents/skills"),
    "cursor": Path(".agents/skills"),
    "claude-code": Path(".claude/skills"),
}
MARKER = ".devcraft-installed"


def skill_files(agent: str) -> dict[str, dict[str, bytes]]:
    skills: dict[str, dict[str, bytes]] = {}
    for tier in ("user-invoked", "model-invoked"):
        for directory in sorted((SOURCE / tier).iterdir()):
            if not directory.is_dir():
                continue
            name = directory.name
            if name in skills:
                raise ValueError(f"Duplicate skill name: {name}")
            files = {
                str(path.relative_to(directory)).replace("\\", "/"): path.read_bytes()
                for path in directory.rglob("*")
                if path.is_file()
            }
            if "SKILL.md" not in files:
                raise ValueError(f"Missing SKILL.md: {directory}")
            body = files["SKILL.md"].decode("utf-8").replace("\r\n", "\n")
            files["SKILL.md"] = body.encode("utf-8")
            if not body.startswith(f"---\nname: {name}\n"):
                raise ValueError(f"Invalid skill name in {directory}")
            if tier == "user-invoked":
                if "\ndisable-model-invocation: true\n" not in body:
                    raise ValueError(f"Missing user-only metadata: {directory}")
                if "agents/openai.yaml" not in files:
                    raise ValueError(f"Missing Codex metadata: {directory}")
                if agent != "codex":
                    files.pop("agents/openai.yaml")
            files[MARKER] = b"Installed from DevCraft. Edit the source skill instead.\n"
            skills[name] = files
    return skills


def install(project: Path, agent: str, check: bool = False) -> tuple[int, int]:
    if not project.is_dir():
        raise ValueError(f"Project directory does not exist: {project}")
    project = project.resolve()
    target_root = project / TARGETS[agent]
    if not target_root.resolve().is_relative_to(project):
        raise ValueError(f"Skill directory resolves outside the project: {target_root}")
    skills = skill_files(agent)
    missing: list[tuple[Path, bytes]] = []
    conflicts: list[Path] = []
    for name, files in skills.items():
        target = target_root / name
        if not target.resolve().is_relative_to(project):
            conflicts.append(target)
            continue
        if target.exists() and not (target / MARKER).is_file():
            conflicts.append(target)
            continue
        for relative, expected in files.items():
            path = target / relative
            if not path.resolve().is_relative_to(project):
                conflicts.append(path)
                continue
            if path.exists():
                if not path.is_file() or path.read_bytes() != expected:
                    conflicts.append(path)
            else:
                missing.append((path, expected))
    if conflicts:
        raise ValueError(
            "Existing files differ; no files changed. Review before replacing:\n"
            + "\n".join(f"  {path}" for path in conflicts)
        )
    if check:
        return len(skills), len(missing)
    for path, content in missing:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    return len(skills), len(missing)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=TARGETS, required=True)
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true", help="Only inspect the installation")
    args = parser.parse_args()
    try:
        total, missing = install(args.project.resolve(), args.agent, args.check)
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    if args.check:
        print(f"{total} skills expected; {missing} files missing")
        return 1 if missing else 0
    print(f"{total} skills installed; {missing} files added")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
