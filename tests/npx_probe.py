"""Optional integration check for the latest Skills CLI in a temporary project."""

from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    agent = sys.argv[1] if len(sys.argv) > 1 else "codex"
    if agent not in {"codex", "claude-code", "cursor"}:
        print("agent must be codex, claude-code, or cursor", file=sys.stderr)
        return 2
    npx = shutil.which("npx.cmd" if sys.platform == "win32" else "npx")
    if not npx:
        print("npx unavailable", file=sys.stderr)
        return 2
    with TemporaryDirectory() as directory:
        project = Path(directory)
        command = [
            npx, "--yes", "skills@latest", "add", str(ROOT), "--skill", "*",
            "--agent", agent, "--copy", "--yes",
        ]
        result = subprocess.run(command, cwd=project, capture_output=True, text=True,
                                encoding="utf-8", errors="replace", timeout=120, check=False)
        root = project / (".claude/skills" if agent == "claude-code" else ".agents/skills")
        skill = root / "setup-devcraft/SKILL.md"
        installed = list(root.glob("*/SKILL.md"))
        print(f"{agent}: CLI exit={result.returncode}; installed={len(installed)}")
        if skill.is_file():
            print(skill.read_text(encoding="utf-8").split("---", 2)[1])
            print(f"Codex metadata={(skill.parent / 'agents/openai.yaml').is_file()}")
        if result.returncode:
            print(result.stderr[-1500:], file=sys.stderr)
        return 0 if result.returncode == 0 and len(installed) == 23 and skill.is_file() else 1


if __name__ == "__main__":
    raise SystemExit(main())
