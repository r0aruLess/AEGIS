"""
Unit tests validating ISO/IEC 27001:2022 and 27701:2025 control schemas and integrity.
"""
import json
import unittest
from pathlib import Path

CONTROLS_DIR = Path(__file__).resolve().parent.parent / "controls"

class TestControlsSchema(unittest.TestCase):
    def test_iso27001_total_and_theme_counts(self):
        file_path = CONTROLS_DIR / "iso27001_2022.json"
        self.assertTrue(file_path.exists(), "iso27001_2022.json must exist")

        with open(file_path, "r", encoding="utf-8") as f:
            controls = json.load(f)

        # 1. Total control count must be exactly 93
        self.assertEqual(len(controls), 93, f"Expected 93 controls, got {len(controls)}")

        # 2. Check 4 themes counts
        themes = {}
        for c in controls:
            t = c.get("theme")
            themes[t] = themes.get(t, 0) + 1

        self.assertEqual(themes.get("Organizational"), 37)
        self.assertEqual(themes.get("People"), 8)
        self.assertEqual(themes.get("Physical"), 14)
        self.assertEqual(themes.get("Technological"), 34)

    def test_control_schema_fields(self):
        file_path = CONTROLS_DIR / "iso27001_2022.json"
        with open(file_path, "r", encoding="utf-8") as f:
            controls = json.load(f)

        required_fields = ["id", "theme", "title", "objective", "owner", "frequency", "evidence_source", "status", "soa_included", "soa_justification"]
        for c in controls:
            for field in required_fields:
                self.assertIn(field, c, f"Control {c.get('id')} missing required field: {field}")
                self.assertIsNotNone(c[field])
            self.assertIn(c["status"], ["PASSED", "WARNING", "FAILED", "EXEMPT"])

    def test_iso27701_standalone_dataset(self):
        file_path = CONTROLS_DIR / "iso27701_2025.json"
        self.assertTrue(file_path.exists(), "iso27701_2025.json must exist")

        with open(file_path, "r", encoding="utf-8") as f:
            controls = json.load(f)

        self.assertGreaterEqual(len(controls), 8)
        for c in controls:
            self.assertIn("transition_note", c)

    def test_oscal_catalog_structure(self):
        file_path = CONTROLS_DIR / "oscal_catalog.json"
        self.assertTrue(file_path.exists())
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("catalog", data)
        self.assertIn("metadata", data["catalog"])
        self.assertEqual(data["catalog"]["metadata"]["oscal-version"], "1.1.0")
        self.assertEqual(len(data["catalog"]["groups"]), 4)

if __name__ == "__main__":
    unittest.main()
