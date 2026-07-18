from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build_sgos_site_tree.py"
SPEC = importlib.util.spec_from_file_location("build_sgos_site_tree", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class BuildSgosSiteTreeTest(unittest.TestCase):
    def test_builds_ordered_nested_tree_and_page_urls(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            site = root / "site"
            (site / "technology").mkdir(parents=True)
            (site / "time" / "night").mkdir(parents=True)
            (site / "unused").mkdir(parents=True)

            (site / "index.html").write_text(
                "<title>Sample Archive</title><h1>情緒研究</h1>",
                encoding="utf-8",
            )
            (site / "technology" / "index.html").write_text(
                "<title>55 technology｜情緒研究</title>"
                "<h1>55 technology / 技術の情緒</h1>",
                encoding="utf-8",
            )
            (site / "technology" / "old-unix.html").write_text(
                "<title>古いUNIXコマンド｜情緒研究</title>",
                encoding="utf-8",
            )
            (site / "time" / "index.html").write_text(
                "<title>11 time｜情緒研究</title>",
                encoding="utf-8",
            )
            (site / "time" / "night" / "index.html").write_text(
                "<title>夜間観測｜情緒研究</title>",
                encoding="utf-8",
            )
            (site / "time" / "night" / "midnight.html").write_text(
                "<title>午前0時｜情緒研究</title>",
                encoding="utf-8",
            )
            (site / "unused" / "hidden.html").write_text(
                "<title>除外ページ</title>",
                encoding="utf-8",
            )

            config = {
                "schema_version": "1.0",
                "site_id": "sample",
                "site_title": "情緒研究",
                "site_url": "https://example.test/",
                "source_dir": "site",
                "exclude_paths": ["unused"],
                "sections": [
                    {"slug": "technology", "title": "55 technology / 技術の情緒"},
                    {"slug": "time", "title": "11 time / 時間"},
                    {"slug": "empty", "title": "空の棚"},
                ],
            }

            result = MODULE.build_tree(config, root)
            MODULE.validate_output(result)

            self.assertEqual(result["tree"][0]["kind"], "page")
            self.assertEqual(result["tree"][0]["url"], "https://example.test/")

            technology = result["tree"][1]
            self.assertEqual(technology["slug"], "technology")
            self.assertEqual(technology["url"], "https://example.test/technology/")
            self.assertEqual(
                technology["children"][0]["url"],
                "https://example.test/technology/old-unix.html",
            )

            time_section = result["tree"][2]
            night = time_section["children"][0]
            self.assertEqual(night["kind"], "group")
            self.assertEqual(night["title"], "夜間観測")
            self.assertEqual(night["url"], "https://example.test/time/night/")
            self.assertEqual(
                night["children"][0]["url"],
                "https://example.test/time/night/midnight.html",
            )

            self.assertFalse(result["tree"][3]["available"])
            self.assertEqual(
                result["counts"],
                {"sections": 3, "pages": 3, "groups": 1},
            )

    def test_rejects_duplicate_urls(self) -> None:
        data = {
            "schema_version": "1.0",
            "tree": [
                {
                    "kind": "page",
                    "title": "A",
                    "url": "https://example.test/a",
                    "children": [],
                },
                {
                    "kind": "page",
                    "title": "B",
                    "url": "https://example.test/a",
                    "children": [],
                },
            ],
        }
        with self.assertRaisesRegex(ValueError, "Duplicate node URL"):
            MODULE.validate_output(data)


if __name__ == "__main__":
    unittest.main()
