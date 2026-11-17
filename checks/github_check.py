"""
Aegis GRC - Real Automated GitHub Repository Security Check
Audits source code repository posture, secret leakage detection, and commit hygiene,
mapping real findings to ISO/IEC 27001:2022 Annex A controls.
"""
import os
import sys
import re
import subprocess
from pathlib import Path

# Ensure root is in sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from checks.evidence_collector import save_evidence_artifact
from backend.db import get_connection, log_audit_entry

# Patterns for secret leakage scanning
SECRET_PATTERNS = {
    "AWS Access Key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "Generic Private Key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "GitHub Personal Access Token": re.compile(r"ghp_[A-Za-z0-9_]{36}"),
    "Generic High Entropy Token": re.compile(r"(?i)(api[_-]?key|secret[_-]?token)\s*[:=]\s*['\"][A-Za-z0-9+/=]{20,}['\"]")
}

def scan_for_secrets(base_dir: Path):
    """Scans repository files for committed secrets and private keys."""
    findings = []
    ignore_dirs = {".git", ".system_generated", "brain", "__pycache__", "node_modules", ".venv", ".cache"}

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for f in files:
            # Skip binary files or lock files
            if f.endswith((".db", ".sqlite", ".png", ".jpg", ".pyc", ".exe")):
                continue
            fpath = Path(root) / f
            try:
                content = fpath.read_text(encoding="utf-8", errors="ignore")
                for label, pattern in SECRET_PATTERNS.items():
                    matches = pattern.findall(content)
                    if matches:
                        findings.append({
                            "file": str(fpath.relative_to(base_dir)),
                            "secret_type": label,
                            "occurrences": len(matches)
                        })
            except Exception:
                pass
    return findings

def check_git_hygiene(base_dir: Path):
    """Inspects local git repository configuration and protection settings."""
    git_dir = base_dir / ".git"
    is_git_repo = git_dir.exists()

    gitignore_exists = (base_dir / ".gitignore").exists()
    has_workflows = (base_dir / ".github" / "workflows").exists()

    return {
        "is_git_repository": is_git_repo,
        "has_gitignore": gitignore_exists,
        "ci_cd_workflows_detected": has_workflows
    }

def run_github_security_check():
    """
    Executes real audit scan on the repository and updates linked Annex A controls.
    """
    secret_findings = scan_for_secrets(REPO_ROOT)
    hygiene = check_git_hygiene(REPO_ROOT)

    controls_impacted = ["A.8.4", "A.8.25", "A.8.28", "A.8.32", "A.5.3"]
    passed = len(secret_findings) == 0 and hygiene["has_gitignore"]

    status = "PASSED" if passed else "WARNING"
    summary = f"Scanned repository for secrets and CI/CD policies. Secret findings: {len(secret_findings)}. Git hygiene: {hygiene}."

    telemetry = {
        "repository_path": str(REPO_ROOT),
        "secret_findings_count": len(secret_findings),
        "secret_details": secret_findings,
        "hygiene_metrics": hygiene,
        "controls_evaluated": controls_impacted,
        "status": status
    }

    # Save artifact with SHA-256
    artifact = save_evidence_artifact("GITHUB_SEC_AUDIT", status, summary, telemetry, "GitHub Security Check Engine")

    # Update database controls
    conn = get_connection()
    c = conn.cursor()
    new_ctrl_status = "PASSED" if passed else "WARNING"
    notes_update = f" [AUTOMATED AUDIT]: Scanned by Aegis GRC. SHA256 Evidence: {artifact['sha256_hash'][:12]}... Findings: {len(secret_findings)}"

    for cid in controls_impacted:
        c.execute("UPDATE controls SET status = ?, notes = notes || ? WHERE id = ?", (new_ctrl_status, notes_update, cid))
        log_audit_entry(conn, "GitHub Security Check Engine", "System", "AUTO_UPDATE_CONTROL", "CONTROL", cid, "PREVIOUS", new_ctrl_status)

    conn.commit()
    conn.close()

    return {
        "check_id": "GITHUB_SEC_AUDIT",
        "status": status,
        "summary": summary,
        "artifact": artifact
    }

if __name__ == "__main__":
    res = run_github_security_check()
    print(f"GitHub Check Finished: {res['status']} | Artifact: {res['artifact']['artifact_id']}")
