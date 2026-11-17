"""
Unit tests validating evidence collector and real check runners.
"""
import unittest
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from checks.evidence_collector import save_evidence_artifact
from checks.github_check import run_github_security_check
from checks.infrastructure_check import run_infrastructure_security_check

class TestSecurityChecks(unittest.TestCase):
    def test_evidence_collector_hashing(self):
        sample_data = {"test_metric": 123, "service": "Aegis Audit"}
        artifact = save_evidence_artifact("TEST_CHECK", "PASSED", "Test summary", sample_data, "Test Runner")

        self.assertTrue(artifact["artifact_id"].startswith("EVD-"))
        self.assertEqual(len(artifact["sha256_hash"]), 64)

        # Verify file exists on disk
        fpath = Path(artifact["file_path"])
        self.assertTrue(fpath.exists())

        with open(fpath, "r", encoding="utf-8") as f:
            saved = json.load(f)
        self.assertEqual(saved["sha256_fingerprint"], artifact["sha256_hash"])

    def test_github_security_check(self):
        res = run_github_security_check()
        self.assertIn(res["status"], ["PASSED", "WARNING"])
        self.assertIn("artifact", res)

    def test_infrastructure_security_check(self):
        res = run_infrastructure_security_check()
        self.assertIn(res["status"], ["PASSED", "WARNING"])
        self.assertIn("artifact", res)

if __name__ == "__main__":
    unittest.main()
