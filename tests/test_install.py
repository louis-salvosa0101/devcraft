import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest


INSTALLER = Path(__file__).resolve().parents[1] / "adapters/install.py"


def run(project: Path, agent: str, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(INSTALLER), "--agent", agent, "--project", str(project), *extra],
        capture_output=True,
        text=True,
        check=False,
    )


class InstallTests(unittest.TestCase):
    def test_every_host_receives_all_skills_with_workflow_only_flags(self):
        for agent, relative in (
            ("codex", ".agents/skills"),
            ("claude-code", ".claude/skills"),
            ("cursor", ".agents/skills"),
        ):
            with self.subTest(agent=agent), TemporaryDirectory() as directory:
                project = Path(directory)
                installed = run(project, agent)
                self.assertEqual(installed.returncode, 0, installed.stderr)
                root = project / relative
                self.assertEqual(len(list(root.glob("*/SKILL.md"))), 23)
                for name in ("setup-devcraft", "ask-workflow", "implement", "release"):
                    self.assertIn(
                        "disable-model-invocation: true",
                        (root / name / "SKILL.md").read_text(encoding="utf-8"),
                    )
                    self.assertEqual((root / name / "agents/openai.yaml").is_file(), agent == "codex")
                for name in ("grilling", "visual-taste", "security-review"):
                    self.assertNotIn(
                        "disable-model-invocation: true",
                        (root / name / "SKILL.md").read_text(encoding="utf-8"),
                    )
                    self.assertFalse((root / name / "agents/openai.yaml").exists())

    def test_install_check_and_rerun(self):
        with TemporaryDirectory() as directory:
            project = Path(directory) / "My App"
            project.mkdir()
            self.assertEqual(run(project, "codex", "--check").returncode, 1)
            first = run(project, "codex")
            self.assertEqual(first.returncode, 0, first.stderr)
            root = project / ".agents/skills"
            self.assertEqual(len(list(root.glob("*/SKILL.md"))), 23)
            self.assertIn(
                "disable-model-invocation: true",
                (root / "implement/SKILL.md").read_text(encoding="utf-8"),
            )
            self.assertNotIn(
                "disable-model-invocation: true",
                (root / "tdd/SKILL.md").read_text(encoding="utf-8"),
            )
            self.assertTrue((root / "implement/agents/openai.yaml").is_file())
            self.assertEqual(run(project, "codex", "--check").returncode, 0)
            rerun = run(project, "codex")
            self.assertEqual(rerun.returncode, 0, rerun.stderr)
            self.assertIn("0 files added", rerun.stdout)

    def test_repairs_missing_file_without_overwriting_user_change(self):
        with TemporaryDirectory() as directory:
            project = Path(directory)
            self.assertEqual(run(project, "claude-code").returncode, 0)
            skill = project / ".claude/skills/tdd/SKILL.md"
            skill.unlink()
            self.assertEqual(run(project, "claude-code").returncode, 0)
            self.assertTrue(skill.is_file())
            skill.write_text("user edit", encoding="utf-8")
            failed = run(project, "claude-code")
            self.assertEqual(failed.returncode, 1)
            self.assertEqual(skill.read_text(encoding="utf-8"), "user edit")

    def test_unrelated_skill_blocks_install_without_partial_changes(self):
        with TemporaryDirectory() as directory:
            project = Path(directory)
            target = project / ".agents/skills/setup-devcraft"
            target.mkdir(parents=True)
            (target / "SKILL.md").write_text("unrelated", encoding="utf-8")
            failed = run(project, "cursor")
            self.assertEqual(failed.returncode, 1)
            self.assertEqual((target / "SKILL.md").read_text(encoding="utf-8"), "unrelated")
            self.assertFalse((project / ".agents/skills/implement").exists())

    def test_refuses_skill_directory_link_outside_project(self):
        with TemporaryDirectory() as directory, TemporaryDirectory() as outside:
            project = Path(directory)
            try:
                (project / ".agents").symlink_to(Path(outside), target_is_directory=True)
            except OSError:
                self.skipTest("Directory symlinks unavailable")
            failed = run(project, "codex")
            self.assertEqual(failed.returncode, 1)
            self.assertFalse(list(Path(outside).iterdir()))


if __name__ == "__main__":
    unittest.main()
