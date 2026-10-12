from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class SkillSourceTests(unittest.TestCase):
    def test_portable_entrypoints_have_unique_valid_names_and_sources(self):
        names = set()
        for tier in ("user-invoked", "model-invoked"):
            for path in (ROOT / "skills" / tier).glob("*/SKILL.md"):
                text = path.read_text(encoding="utf-8")
                match = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n(?:disable-model-invocation: true\n)?---\n", text)
                self.assertIsNotNone(match, str(path))
                name, description = match.groups()
                self.assertEqual(name, path.parent.name)
                self.assertNotIn(name, names)
                names.add(name)
                self.assertLessEqual(len(description), 1024)
                self.assertEqual("disable-model-invocation: true" in text, tier == "user-invoked")
                self.assertEqual((path.parent / "agents/openai.yaml").is_file(), tier == "user-invoked")
                self.assertIn("Source", text)
        self.assertEqual(len(names), 23)

    def test_local_document_links_resolve(self):
        for path in (ROOT / "README.md", ROOT / "LICENSES.md", *(ROOT / "docs").rglob("*.md")):
            text = path.read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if "://" in target or target.startswith("#"):
                    continue
                destination = (path.parent / target.split("#", 1)[0]).resolve()
                self.assertTrue(destination.exists(), f"{path}: {target}")


if __name__ == "__main__":
    unittest.main()
