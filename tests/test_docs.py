"""Small regression tests for the documentation checker, not runtime tests."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

module = importlib.util.spec_from_file_location("check_docs", Path(__file__).resolve().parents[1] / "scripts/check_docs.py")
check = importlib.util.module_from_spec(module)
module.loader.exec_module(check)


class DocumentationCheckerTests(unittest.TestCase):
    def test_fenced_examples_do_not_create_links_or_headings(self):
        prose, anchors, figures, errors = check.scan("# Real\n```text\n# Fake\n[x](missing.md)\n```\n")
        self.assertNotIn("missing.md", prose)
        self.assertEqual(anchors, {"real"})
        self.assertEqual(figures, [])
        self.assertEqual(errors, [])

    def test_unclosed_fence_is_error(self):
        self.assertTrue(check.scan("# Doc\n```mermaid\nflowchart TB\n")[3])

    def test_mermaid_is_extracted(self):
        diagrams = check.scan("```mermaid\nflowchart TB\n A --> B\n```\n")[2]
        self.assertEqual(diagrams[0]["source"], "flowchart TB\n A --> B\n")
        self.assertEqual(diagrams[0]["line"], 1)

    def test_duplicate_heading_anchors(self):
        self.assertEqual(check.scan("## Work\n## Work\n")[1], {"work", "work-1"})

    def test_matching_fence_character_required(self):
        self.assertTrue(check.scan("```text\n~~~\n")[3])

    def test_missing_local_target_and_anchor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "README.md"
            path.write_text("# Real\n")
            count, errors = check.link_errors(path, "[a](missing.md) [b](#missing)", root)
            self.assertEqual(count, 2)
            self.assertEqual(len(errors), 2)

    def test_valid_encoded_local_path_and_anchor(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "README.md"
            target = root / "a file.md"
            target.write_text("# Local heading\n")
            self.assertEqual(check.link_errors(path, "[ok](a%20file.md#local-heading)", root), (1, []))

    def test_repository_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertTrue(check.link_errors(root / "README.md", "[x](../outside.md)", root)[1])

    def test_external_link_is_not_claimed_checked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertEqual(check.link_errors(root / "README.md", "[web](https://example.invalid/a#b)", root), (0, []))

    def test_sandbox_link_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.assertTrue(check.link_errors(root / "README.md", "[x](sandbox:/missing)", root)[1])


if __name__ == "__main__":
    unittest.main()
