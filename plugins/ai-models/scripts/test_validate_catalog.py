#!/usr/bin/env python3
"""Regression checks for errors that can silently invalidate the model inventory."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("validate_catalog", Path(__file__).with_name("validate_catalog.py"))
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
PLUGIN = Path(__file__).resolve().parents[1]


class CatalogValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "plugins" / "ai-models"
        shutil.copytree(PLUGIN, self.root, ignore=shutil.ignore_patterns("__pycache__"))

    def mutate_catalog(self, mutation):
        path = self.root / "catalog.json"
        data = json.loads(path.read_text())
        mutation(data)
        path.write_text(json.dumps(data))

    def assert_failure(self, fragment):
        errors = MODULE.validate(self.root)
        self.assertTrue(any(fragment in message for message in errors), errors)

    def test_current_catalog_passes(self):
        self.assertEqual(MODULE.validate(self.root), [])

    def test_duplicate_identity_rejected(self):
        self.mutate_catalog(lambda d: d["models"][1].update(id=d["models"][0]["id"]))
        self.assert_failure("duplicate model id")

    def test_alias_padding_cannot_change_count(self):
        self.mutate_catalog(lambda d: d["models"].append(dict(d["models"][0])))
        self.assert_failure("expected 60 models, found 61")
        self.assert_failure("duplicate model id")

    def test_reference_escape_rejected(self):
        self.mutate_catalog(lambda d: d["models"][0].update(reference="../../../outside.md"))
        self.assert_failure("reference escapes plugin")

    def test_missing_evidence_rejected(self):
        self.mutate_catalog(lambda d: d["models"][0].update(sources=[], adoption={}))
        self.assert_failure("sources must be a nonempty array")
        self.assert_failure("adoption evidence")

    def test_missing_model_reference_rejected(self):
        data = json.loads((self.root / "catalog.json").read_text())
        (self.root / data["models"][0]["reference"]).unlink()
        self.assert_failure("missing reference")

    def test_missing_near_miss_rejected(self):
        path = self.root / "evals" / "trigger-evals.json"
        data = json.loads(path.read_text())
        family = data["cases"][0]["skill"]
        data["cases"] = [c for c in data["cases"] if not (c["skill"] == family and c["should_trigger"] is False)]
        path.write_text(json.dumps(data))
        self.assert_failure("missing negative eval")

    def test_invalid_frontmatter_separator_rejected(self):
        path = next((self.root / "skills").glob("*/SKILL.md"))
        path.write_text(path.read_text().replace("description: ", "description:", 1))
        self.assert_failure("frontmatter fields need a space")


if __name__ == "__main__":
    unittest.main()
