"""Optional read-only Codex routing probe; run explicitly, not in unittest discovery."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = {
    "crud": {
        "AGENTS.md": "# Project\nUse DevCraft lightweight profile. Local tickets in docs/tickets/.\n",
        "docs/product.md": "# Contacts\nStatus: Approved\nCreate, list and delete personal contacts.\n",
        "docs/tech-spec.md": "# Architecture\nStatus: Approved\nLocal SQLite storage; validate contact fields.\n",
        "docs/tickets/contacts/T-001-create-contact.md": "# Create contact\nStatus: Ready\nBuild form, persistence, list and validation test.\n",
    },
    "saas": {
        "AGENTS.md": "# Project\nUse DevCraft standard profile. Local tickets in docs/tickets/.\n",
        "docs/product.md": "# Expense approvals\nStatus: Approved\nTeam members submit an expense with amount, category, date, and receipt. A team approver accepts or rejects it with a reason. Submitters see current status and decision history. No cross-team visibility. MVP excludes payments and accounting export. Acceptance: submit, review, decide, and view history in the web UI.\n",
        "docs/tech-spec.md": "# Architecture\nStatus: Approved\nWeb client and API with tenant-scoped reads, role checks on decisions, an append-only decision event, validation errors, and API tests.\n",
    },
    "hackathon": {
        "AGENTS.md": "# Project\n## DevCraft\nSetup complete: all 23 skills are installed. Use the rapid profile. Four hours to demo an action-list extractor. Local tickets use docs/tickets/<feature>/T-###-<slug>.md, created with the first ticket. Specs live in docs/product.md, docs/design.md, and docs/tech-spec.md. No verification command exists until the app is bootstrapped. Major stages require an explicit developer request.\n",
    },
}


def main():
    if not shutil.which("codex"):
        print("Codex CLI unavailable", file=sys.stderr)
        return 2
    selected = sys.argv[1:] or list(SCENARIOS)
    failed = False
    for scenario in selected:
        files = SCENARIOS[scenario]
        with TemporaryDirectory() as directory:
            project = Path(directory)
            for relative, content in files.items():
                path = project / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
            installed = subprocess.run(
                [sys.executable, str(ROOT / "adapters/install.py"), "--agent", "codex", "--project", str(project)],
                capture_output=True, text=True, encoding="utf-8", errors="replace", check=False,
            )
            if installed.returncode:
                print(installed.stderr, file=sys.stderr)
                return installed.returncode
            command = [
                "codex", "exec", "-C", str(project), "--skip-git-repo-check", "--ephemeral",
                "-s", "read-only", "--json",
                "Use the installed $ask-workflow skill. Recommend exactly one next DevCraft stage for this project and its prerequisite. Do not start that stage or edit files.",
            ]
            try:
                result = subprocess.run(
                    command, capture_output=True, text=True, encoding="utf-8",
                    errors="replace", timeout=180, check=False,
                )
            except subprocess.TimeoutExpired:
                print(f"{scenario}: timeout")
                failed = True
                continue
            messages = []
            for line in result.stdout.splitlines():
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if event.get("type") == "item.completed" and event.get("item", {}).get("type") == "agent_message":
                    messages.append(event["item"].get("text", ""))
            print(f"{scenario}: exit={result.returncode}; response={messages[-1] if messages else '(none)'}")
            if result.returncode or not messages:
                failed = True
                print(result.stderr[-1000:], file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
