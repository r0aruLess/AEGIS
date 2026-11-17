"""
Unit tests validating cryptographic SHA-256 hash chaining in audit trail.
"""
import unittest
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from backend.db import get_connection, log_audit_entry, hash_data

class TestAuditTrail(unittest.TestCase):
    def test_audit_trail_hash_chain(self):
        conn = get_connection()
        c = conn.cursor()

        # Log 2 sample events
        log_audit_entry(conn, "tester", "Admin", "TEST_ACTION_1", "SYS", "01", "old", "new1")
        log_audit_entry(conn, "tester", "Admin", "TEST_ACTION_2", "SYS", "02", "new1", "new2")

        c.execute("SELECT id, prev_hash, entry_hash FROM audit_trail ORDER BY id DESC LIMIT 2")
        rows = c.fetchall()
        self.assertEqual(len(rows), 2)
        latest = rows[0]
        previous = rows[1]

        # Verify chain: latest's prev_hash must equal previous's entry_hash
        self.assertEqual(latest["prev_hash"], previous["entry_hash"])
        conn.close()

if __name__ == "__main__":
    unittest.main()
