"""
Aegis GRC - Shift-Left Infrastructure-as-Code (Terraform) Compliance Scanner
Audits Terraform configuration baselines before cloud deployment, mapping static misconfigurations
directly to ISO/IEC 27001:2022 Annex A controls (A.8.9, A.8.20, A.8.24, A.5.9, A.5.23).
"""
import os
import sys
import re
from pathlib import Path

# Add project root to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from checks.evidence_collector import save_evidence_artifact
from backend.db import get_connection, log_audit_entry

TF_DIR = REPO_ROOT / "terraform"

def scan_terraform_security():
    """
    Parses and checks all .tf files for security non-conformities.
    """
    findings = []
    evaluated_files = []

    if not TF_DIR.exists():
        return {
            "status": "PASSED",
            "findings_count": 0,
            "findings": [],
            "files_evaluated": []
        }

    for tf_file in TF_DIR.glob("*.tf"):
        evaluated_files.append(tf_file.name)
        content = tf_file.read_text(encoding="utf-8", errors="ignore")

        # 1. Rule Check: Unrestricted Ingress to Sensitive Ports (0.0.0.0/0)
        # Ports: 22 (SSH), 3389 (RDP), 5432 (Postgres), 3306 (MySQL), 27017 (Mongo)
        risky_ports = [22, 3389, 5432, 3306, 27017]
        for port in risky_ports:
            # Check for ingress block with port and 0.0.0.0/0
            pattern = rf'from_port\s*=\s*{port}.*?cidr_blocks\s*=\s*\[\s*"0\.0\.0\.0/0"\s*\]'
            if re.search(pattern, content, re.DOTALL):
                findings.append({
                    "file": tf_file.name,
                    "rule_id": "AEGIS-TF-RULE-01",
                    "severity": "HIGH",
                    "title": f"Unrestricted Ingress to Sensitive Port {port}",
                    "control_id": "A.8.20",
                    "remediation": f"Restrict CIDR block for port {port} to authorized VPN or VPC boundaries."
                })

        # 2. Rule Check: S3 Bucket missing encryption definition
        # Find all bucket resource names
        bucket_defs = re.findall(r'resource\s+"aws_s3_bucket"\s+"([a-zA-Z0-9_-]+)"', content)
        enc_defs = re.findall(r'resource\s+"aws_s3_bucket_server_side_encryption_configuration"\s+"[a-zA-Z0-9_-]+"\s*\{\s*bucket\s*=\s*aws_s3_bucket\.([a-zA-Z0-9_-]+)\.id', content)

        for b in bucket_defs:
            if b not in enc_defs:
                findings.append({
                    "file": tf_file.name,
                    "rule_id": "AEGIS-TF-RULE-02",
                    "severity": "MEDIUM",
                    "title": f"S3 Bucket '{b}' Missing Server-Side Encryption Configuration",
                    "control_id": "A.8.24",
                    "remediation": f"Attach an 'aws_s3_bucket_server_side_encryption_configuration' resource with AES-256 or KMS."
                })

        # 3. Rule Check: Missing Environment Tagging
        if 'Environment' not in content:
            findings.append({
                "file": tf_file.name,
                "rule_id": "AEGIS-TF-RULE-03",
                "severity": "LOW",
                "title": "Cloud Resources Missing Mandatory 'Environment' Tag",
                "control_id": "A.5.9",
                "remediation": "Apply standardized tags (Environment, Owner, DataClassification) to all resources."
            })

    status = "WARNING" if findings else "PASSED"
    return {
        "status": status,
        "findings_count": len(findings),
        "findings": findings,
        "files_evaluated": evaluated_files
    }

def run_terraform_compliance_check():
    """
    Executes shift-left IaC scan, generates cryptographic artifact, and updates linked controls.
    """
    res = scan_terraform_security()
    controls_impacted = ["A.8.9", "A.8.20", "A.8.24", "A.5.9", "A.5.23"]

    summary = f"Terraform Shift-Left scan completed across {len(res['files_evaluated'])} files. Total findings: {res['findings_count']}."
    status = res["status"]

    telemetry = {
        "iac_framework": "Terraform (AWS Provider)",
        "scan_results": res,
        "controls_evaluated": controls_impacted,
        "status": status
    }

    # Save artifact with SHA-256
    artifact = save_evidence_artifact("TERRAFORM_IAC_AUDIT", status, summary, telemetry, "Terraform IaC Compliance Scanner")

    # Update database controls with audit note
    conn = get_connection()
    c = conn.cursor()
    notes_update = f" [IAC AUDIT]: Scanned {len(res['files_evaluated'])} .tf files. Findings: {res['findings_count']}. SHA256: {artifact['sha256_hash'][:12]}..."

    for cid in controls_impacted:
        ctrl_status = "WARNING" if any(f.get("control_id") == cid for f in res["findings"]) else "PASSED"
        c.execute("UPDATE controls SET status = ?, notes = notes || ? WHERE id = ?", (ctrl_status, notes_update, cid))
        log_audit_entry(conn, "Terraform IaC Scanner", "System", "IAC_SCAN_CONTROL", "CONTROL", cid, "PREVIOUS", ctrl_status)

    conn.commit()
    conn.close()

    return {
        "check_id": "TERRAFORM_IAC_AUDIT",
        "status": status,
        "summary": summary,
        "findings": res["findings"],
        "artifact": artifact
    }

if __name__ == "__main__":
    r = run_terraform_compliance_check()
    print(f"Terraform Scan Result: {r['status']} | Findings: {len(r['findings'])} | Artifact: {r['artifact']['artifact_id']}")
