"""
Unit tests validating Shift-Left Terraform compliance scanner.
"""
import unittest
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from checks.terraform_check import scan_terraform_security, run_terraform_compliance_check

class TestTerraformCheck(unittest.TestCase):
    def test_scan_terraform_security(self):
        res = scan_terraform_security()
        self.assertIn("findings_count", res)
        self.assertGreater(res["findings_count"], 0)

        # Check for specific rule violations
        rule_ids = [f["rule_id"] for f in res["findings"]]
        self.assertIn("AEGIS-TF-RULE-01", rule_ids, "Should detect unrestricted port 5432 ingress")
        self.assertIn("AEGIS-TF-RULE-02", rule_ids, "Should detect unencrypted S3 bucket")

    def test_run_terraform_compliance_check(self):
        res = run_terraform_compliance_check()
        self.assertIn(res["status"], ["PASSED", "WARNING"])
        self.assertIn("artifact", res)
        self.assertTrue(res["artifact"]["artifact_id"].startswith("EVD-"))
        self.assertEqual(len(res["artifact"]["sha256_hash"]), 64)

if __name__ == "__main__":
    unittest.main()
