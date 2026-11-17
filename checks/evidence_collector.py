"""
Aegis GRC - Evidence Artifact Engine
Collects and cryptographically hashes compliance scan telemetry into immutable evidence bundles.
"""
import os
import sys
import json
import hashlib
import datetime
from pathlib import Path

# Ensure root is in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from backend.db import get_connection, log_audit_entry

EVIDENCE_DIR = REPO_ROOT / "evidence"

def save_evidence_artifact(check_id: str, status: str, summary: str, telemetry: dict, verified_by: str = "Automated GRC Pipeline"):
    """
    Saves evidence artifact to disk with SHA-256 integrity fingerprint and records in database.
    """
    EVIDENCE_DIR.mkdir(exist_ok=True)
    now_ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
    raw_payload = json.dumps(telemetry, sort_keys=True, indent=2)
    sha256_hash = hashlib.sha256(raw_payload.encode("utf-8")).hexdigest()

    artifact_id = f"EVD-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}-{check_id}"
    artifact_filename = f"{artifact_id}.json"
    artifact_path = EVIDENCE_DIR / artifact_filename

    artifact_data = {
        "artifact_id": artifact_id,
        "check_id": check_id,
        "timestamp": now_ts,
        "status": status,
        "summary": summary,
        "sha256_fingerprint": sha256_hash,
        "verified_by": verified_by,
        "telemetry": telemetry
    }

    with open(artifact_path, "w", encoding="utf-8") as f:
        json.dump(artifact_data, f, indent=2)

    # Persist in SQLite
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
    INSERT OR REPLACE INTO evidence_artifacts (
        id, check_id, timestamp, status, summary, payload_json, sha256_hash, verified_by
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (artifact_id, check_id, now_ts, status, summary, raw_payload, sha256_hash, verified_by))

    log_audit_entry(conn, verified_by, "System", "COLLECT_EVIDENCE", "CHECK", check_id, "NONE", sha256_hash)
    conn.commit()
    conn.close()

    return {
        "artifact_id": artifact_id,
        "file_path": str(artifact_path),
        "sha256_hash": sha256_hash,
        "status": status,
        "summary": summary
    }
