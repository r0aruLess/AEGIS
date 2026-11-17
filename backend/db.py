"""
Aegis GRC - Database Engine & Cryptographic Audit Ledger
Uses SQLite with WAL mode, parameterized transactions, and cryptographic SHA-256 hash chaining.
"""
import sqlite3
import json
import hashlib
import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "aegis_grc.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    return conn

def hash_data(data: str) -> str:
    """Compute SHA-256 hash of UTF-8 string."""
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def init_db():
    """Initializes schema and seeds baseline controls if not already loaded."""
    conn = get_connection()
    c = conn.cursor()

    # 1. Controls Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS controls (
        id TEXT PRIMARY KEY,
        framework TEXT NOT NULL,
        theme TEXT NOT NULL,
        title TEXT NOT NULL,
        objective TEXT NOT NULL,
        control_type TEXT,
        properties TEXT,
        concepts TEXT,
        capability TEXT,
        domain TEXT,
        owner TEXT NOT NULL,
        frequency TEXT NOT NULL,
        evidence_source TEXT NOT NULL,
        status TEXT NOT NULL,
        inherent_likelihood INTEGER NOT NULL,
        inherent_impact INTEGER NOT NULL,
        soa_included INTEGER NOT NULL DEFAULT 1,
        soa_justification TEXT,
        notes TEXT,
        last_reviewed TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    """)

    # 2. Cryptographic Audit Trail Table (Immutable ledger with previous hash linking)
    c.execute("""
    CREATE TABLE IF NOT EXISTS audit_trail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        user TEXT NOT NULL,
        role TEXT NOT NULL,
        action TEXT NOT NULL,
        target_type TEXT NOT NULL,
        target_id TEXT NOT NULL,
        prior_value TEXT,
        new_value TEXT,
        evidence_hash TEXT NOT NULL,
        prev_hash TEXT NOT NULL,
        entry_hash TEXT NOT NULL
    )
    """)

    # 3. Defensible 5x5 Risk Register
    c.execute("""
    CREATE TABLE IF NOT EXISTS risks (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        inherent_likelihood INTEGER NOT NULL,
        inherent_impact INTEGER NOT NULL,
        inherent_score INTEGER NOT NULL,
        control_id TEXT,
        control_effectiveness REAL NOT NULL DEFAULT 0.0,
        residual_likelihood INTEGER NOT NULL,
        residual_impact INTEGER NOT NULL,
        residual_score INTEGER NOT NULL,
        treatment TEXT NOT NULL,
        owner TEXT NOT NULL,
        status TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    """)

    # 4. Evidence Artifacts
    c.execute("""
    CREATE TABLE IF NOT EXISTS evidence_artifacts (
        id TEXT PRIMARY KEY,
        check_id TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        status TEXT NOT NULL,
        summary TEXT NOT NULL,
        payload_json TEXT NOT NULL,
        sha256_hash TEXT NOT NULL,
        verified_by TEXT NOT NULL
    )
    """)

    # 5. RoPA (Records of Processing Activities)
    c.execute("""
    CREATE TABLE IF NOT EXISTS ropa_activities (
        id TEXT PRIMARY KEY,
        activity_name TEXT NOT NULL,
        department TEXT NOT NULL,
        controller_role TEXT NOT NULL,
        data_categories TEXT NOT NULL,
        data_subjects TEXT NOT NULL,
        legal_basis TEXT NOT NULL,
        retention_period TEXT NOT NULL,
        cross_border_transfer TEXT NOT NULL,
        security_measures TEXT NOT NULL
    )
    """)

    # 6. DSAR Requests Tracker (Data Subject Access Requests)
    c.execute("""
    CREATE TABLE IF NOT EXISTS dsar_requests (
        id TEXT PRIMARY KEY,
        subject_name TEXT NOT NULL,
        request_type TEXT NOT NULL,
        submission_date TEXT NOT NULL,
        due_date TEXT NOT NULL,
        status TEXT NOT NULL,
        dpo_assigned TEXT NOT NULL,
        action_log TEXT
    )
    """)

    # 7. Vendor / Third-Party Risk Register
    c.execute("""
    CREATE TABLE IF NOT EXISTS vendors (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        tier TEXT NOT NULL,
        data_shared TEXT NOT NULL,
        soc2_certified INTEGER NOT NULL,
        iso27001_certified INTEGER NOT NULL,
        dpa_signed INTEGER NOT NULL,
        sig_score INTEGER NOT NULL,
        last_assessed TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    # 8. AI Systems Inventory (ISO 42001 & EU AI Act)
    c.execute("""
    CREATE TABLE IF NOT EXISTS ai_systems (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        purpose TEXT NOT NULL,
        model_type TEXT NOT NULL,
        eu_ai_act_tier TEXT NOT NULL,
        human_in_loop INTEGER NOT NULL,
        data_protection_measures TEXT NOT NULL,
        status TEXT NOT NULL,
        last_reviewed TEXT NOT NULL
    )
    """)

    # 9. Audit Findings & Corrective Action Plans (CAP)
    c.execute("""
    CREATE TABLE IF NOT EXISTS audit_findings (
        id TEXT PRIMARY KEY,
        audit_standard TEXT NOT NULL,
        control_id TEXT NOT NULL,
        finding_type TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        root_cause TEXT NOT NULL,
        corrective_action TEXT NOT NULL,
        owner TEXT NOT NULL,
        due_date TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    conn.commit()

    # Seed controls if table is empty
    c.execute("SELECT COUNT(*) as cnt FROM controls")
    if c.fetchone()["cnt"] == 0:
        seed_baseline_data(conn)
    else:
        # Check if audit_findings need seeding
        c.execute("SELECT COUNT(*) as cnt FROM audit_findings")
        if c.fetchone()["cnt"] == 0:
            seed_audit_findings(conn)

    conn.close()

def log_audit_entry(conn, user: str, role: str, action: str, target_type: str, target_id: str, prior_val: str, new_val: str):
    """Appends an immutable audit entry into the hash-chained audit log."""
    c = conn.cursor()
    c.execute("SELECT entry_hash FROM audit_trail ORDER BY id DESC LIMIT 1")
    row = c.fetchone()
    prev_hash = row["entry_hash"] if row else "0000000000000000000000000000000000000000000000000000000000000000"

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    evidence_payload = f"{user}|{role}|{action}|{target_type}|{target_id}|{prior_val}|{new_val}|{now}"
    evidence_hash = hash_data(evidence_payload)

    # Hash chain linking
    entry_payload = f"{prev_hash}|{evidence_hash}|{now}"
    entry_hash = hash_data(entry_payload)

    c.execute("""
    INSERT INTO audit_trail (timestamp, user, role, action, target_type, target_id, prior_value, new_value, evidence_hash, prev_hash, entry_hash)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (now, user, role, action, target_type, target_id, str(prior_val), str(new_val), evidence_hash, prev_hash, entry_hash))
    conn.commit()

def calculate_defensible_risk(inherent_likelihood: int, inherent_impact: int, control_status: str, treatment: str):
    """
    Defensible GRC 5x5 Risk Methodology:
    Likelihood (1-5) * Impact (1-5) = Inherent Score (1-25)
    Effectiveness:
      PASSED -> 0.70 - 0.80 mitigation
      WARNING -> 0.35 mitigation
      FAILED / NONE -> 0.00 mitigation
    Treatment impact applies:
      Mitigate -> Lowers likelihood & impact via controls
      Transfer -> Lowers financial impact
      Avoid -> Eliminates activity (residual ~ 1)
      Accept -> Retains residual within tolerance
    """
    inh_score = inherent_likelihood * inherent_impact

    effectiveness = 0.0
    if control_status == "PASSED":
        effectiveness = 0.75
    elif control_status == "WARNING":
        effectiveness = 0.35
    elif control_status == "EXEMPT":
        effectiveness = 0.50
    else:
        effectiveness = 0.00

    # Calculate residual likelihood & impact
    if treatment == "Avoid":
        res_l = 1
        res_i = 1
    elif treatment == "Transfer":
        res_l = max(1, round(inherent_likelihood * (1 - (effectiveness * 0.5))))
        res_i = max(1, round(inherent_impact * 0.4))  # Insurance absorbs impact
    else: # Mitigate or Accept
        res_l = max(1, round(inherent_likelihood * (1 - (effectiveness * 0.65))))
        res_i = max(1, round(inherent_impact * (1 - (effectiveness * 0.45))))

    res_score = res_l * res_i
    return inh_score, effectiveness, res_l, res_i, res_score

def seed_audit_findings(conn):
    c = conn.cursor()
    audit_findings = [
        ("mNC-01", "ISO/IEC 27001:2022", "A.8.13", "Minor Non-Conformity", "Backup Restoration Verification Timeout",
         "Review of Q1 2026 disaster recovery drill logs showed automated database restoration script timed out at step 4.",
         "Network ACL changes applied in February 2026 blocked cross-VPC peering routes for test restore workers.",
         "Deploy automated test restore runner in isolated staging VPC with explicit IAM permissions. Re-run drill.",
         "Head of Infrastructure", "2026-06-15", "Open"),
        ("mNC-02", "ISO/IEC 27001:2022", "A.5.18", "Minor Non-Conformity", "Stale Ex-Employee IAM Service Account Keys",
         "Five legacy AWS IAM programmatic access keys generated by exited contractor remained active without rotation.",
         "Manual offboarding checklist failed to correlate user-generated IAM programmatic access keys.",
         "Deploy AWS Config rule iam-user-unused-credentials-check with auto-remediation Lambda to disable keys > 30 days old.",
         "IT Security Lead", "2026-06-01", "In Progress"),
        ("OFI-01", "ISO/IEC 27701:2025", "Clause 6.1.2", "Opportunity for Improvement", "Decouple Privacy Risk Impact from Corporate Asset Loss",
         "Current risk register evaluates privacy impacts on corporate brand reputation alongside data subject harm.",
         "Legacy 2019 extension methodology conflated corporate CIA impact with fundamental rights of PII principals.",
         "Establish independent privacy impact scoring matrix dedicated solely to data subject harms for ISO 27701:2025.",
         "Data Protection Officer", "2026-07-01", "Under Review")
    ]
    for item in audit_findings:
        c.execute("""
        INSERT OR REPLACE INTO audit_findings (
            id, audit_standard, control_id, finding_type, title, description, root_cause, corrective_action, owner, due_date, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, item)
    conn.commit()

def seed_baseline_data(conn):
    """Seed controls from JSON and baseline risk registers, RoPA, vendors, and AI inventory."""
    c = conn.cursor()
    now_date = datetime.date.today().isoformat()
    now_ts = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # Load 27001 controls
    iso27001_path = Path(__file__).parent.parent / "controls" / "iso27001_2022.json"
    if iso27001_path.exists():
        with open(iso27001_path, "r", encoding="utf-8") as f:
            controls_27001 = json.load(f)
            for item in controls_27001:
                c.execute("""
                INSERT OR REPLACE INTO controls (
                    id, framework, theme, title, objective, control_type, properties, concepts, capability, domain,
                    owner, frequency, evidence_source, status, inherent_likelihood, inherent_impact,
                    soa_included, soa_justification, notes, last_reviewed, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    item["id"], "ISO-27001", item["theme"], item["title"], item["objective"],
                    item.get("control_type", "Preventive"),
                    json.dumps(item.get("properties", [])),
                    json.dumps(item.get("concepts", [])),
                    item.get("capability", "Governance"),
                    item.get("domain", "Governance_and_Ecosystem"),
                    item.get("owner", "CISO"),
                    item.get("frequency", "Continuous (Automated)"),
                    item.get("evidence_source", "AWS / GitHub / Okta API"),
                    item.get("status", "PASSED"),
                    item.get("inherent_likelihood", 3),
                    item.get("inherent_impact", 4),
                    1 if item.get("soa_included", True) else 0,
                    item.get("soa_justification", "Mandatory baseline control."),
                    item.get("notes", "Baseline established."),
                    now_date, now_ts
                ))

    # Load 27701 controls
    iso27701_path = Path(__file__).parent.parent / "controls" / "iso27701_2025.json"
    if iso27701_path.exists():
        with open(iso27701_path, "r", encoding="utf-8") as f:
            controls_27701 = json.load(f)
            for item in controls_27701:
                c.execute("""
                INSERT OR REPLACE INTO controls (
                    id, framework, theme, title, objective, control_type, properties, concepts, capability, domain,
                    owner, frequency, evidence_source, status, inherent_likelihood, inherent_impact,
                    soa_included, soa_justification, notes, last_reviewed, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    item["id"], "ISO-27701", item.get("role", "PII Controller"), item["title"], item["objective"],
                    "Preventive", json.dumps(["Confidentiality"]), json.dumps(["Protect"]), "Legal_and_compliance",
                    "Governance_and_Ecosystem", item.get("owner", "Data Protection Officer"),
                    "Quarterly", "OneTrust / DocuSign / AWS VPC Logs", item.get("status", "PASSED"),
                    item.get("inherent_likelihood", 3), item.get("inherent_impact", 5), 1,
                    f"Required for ISO/IEC 27701:2025 PIMS standalone compliance. {item.get('transition_note', '')}",
                    item.get("transition_note", "PIMS 2025 alignment"), now_date, now_ts
                ))

    # Seed Baseline 5x5 Risks
    baseline_risks = [
        ("RSK-01", "Ransomware infection and production database extortion", "Cybersecurity", 4, 5, "A.8.7", "Mitigate", "SOC Lead", "In Progress"),
        ("RSK-02", "Privileged credential harvesting via phishing", "Identity", 4, 5, "A.8.5", "Mitigate", "IT Security Lead", "Mitigated"),
        ("RSK-03", "Accidental PII data leak via public S3 bucket", "Cloud / Privacy", 3, 5, "A.8.12", "Mitigate", "DevSecOps Lead", "Mitigated"),
        ("RSK-04", "Upstream open-source supply chain package compromise", "Software Engineering", 4, 4, "A.5.21", "Mitigate", "DevSecOps Lead", "Mitigated"),
        ("RSK-05", "Catastrophic cloud region outage causing prolonged downtime", "Resilience", 3, 5, "A.5.30", "Mitigate", "Head of Infrastructure", "Review Needed"),
        ("RSK-06", "Statutory non-compliance with DPDP Act 2023 / GDPR cross-border", "Regulatory / Privacy", 3, 5, "PIMS.A.3.1", "Mitigate", "DPO", "Mitigated"),
        ("RSK-07", "Stale ex-employee access tokens in GitHub / Cloud IAM", "Access Control", 4, 4, "A.5.18", "Mitigate", "IT Security Lead", "In Progress"),
        ("RSK-08", "Critical third-party payment processor outage", "Third Party", 2, 4, "A.5.19", "Transfer", "Vendor Risk Lead", "Accepted")
    ]

    for rid, title, cat, inh_l, inh_i, cid, treat, owner, stat in baseline_risks:
        inh_s, eff, res_l, res_i, res_s = calculate_defensible_risk(inh_l, inh_i, "PASSED" if "Mitigated" in stat else "WARNING", treat)
        c.execute("""
        INSERT OR REPLACE INTO risks (
            id, title, category, inherent_likelihood, inherent_impact, inherent_score,
            control_id, control_effectiveness, residual_likelihood, residual_impact, residual_score,
            treatment, owner, status, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (rid, title, cat, inh_l, inh_i, inh_s, cid, eff, res_l, res_i, res_s, treat, owner, stat, now_ts))

    # Seed RoPA Records
    ropa_items = [
        ("ROPA-01", "User Authentication & Identity Federation", "Engineering", "Joint Controller", "Email, Hashed Password, MFA Tokens, IP Address", "Registered Application Users", "Contract Performance (GDPR Art 6(1)(b))", "Duration of active account + 30 days post-deletion", "None (Stored within National AWS Region)", "AES-256 at rest, TLS 1.3 in transit, Bcrypt key derivation"),
        ("ROPA-02", "Customer Billing & Payment Invoicing", "Finance", "Controller", "Billing Address, Tax ID, Last 4 digits of CC, Transaction Logs", "Subscribed B2B Customers", "Legal Obligation (Tax Code) & Contract", "7 years (Statutory financial ledger retention)", "US Adequacy / Standard Contractual Clauses (Stripe Inc.)", "PCI-DSS Level 1 tokenization via payment gateway"),
        ("ROPA-03", "Employee Recruitment & Background Screening", "Human Resources", "Controller", "Full Name, Resume, Criminal History Check, Educational Verifications", "Job Applicants", "Consent & Legitimate Interest", "1 year for unsuccessful candidates; duration of employment for hires", "None", "Restricted HR Okta Group, Role-Based Access Control"),
        ("ROPA-04", "Customer Support Helpdesk Inquiries", "Customer Success", "Controller", "Name, Business Email, Support Ticket Narrative, System Diagnostics", "Client IT Administrators", "Legitimate Interest", "3 years post-resolution", "Adequacy Decision (Zendesk / AWS)", "End-to-End Encryption, DLP regex redaction of credentials")
    ]

    for item in ropa_items:
        c.execute("""
        INSERT OR REPLACE INTO ropa_activities (
            id, activity_name, department, controller_role, data_categories, data_subjects,
            legal_basis, retention_period, cross_border_transfer, security_measures
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, item)

    # Seed DSAR Tracker
    dsar_items = [
        ("DSAR-2026-001", "Dr. Alexander Wright", "Right of Access (Article 15)", "2026-11-01", "2026-12-01", "Completed", "Data Protection Officer", "Identity verified via 2FA. Telemetry archive dispatched securely."),
        ("DSAR-2026-002", "Elena Rostova", "Right to Erasure (Article 17)", "2026-11-10", "2026-12-10", "In Progress", "Data Protection Officer", "Identity verified. S3 lifecycle deletion job scheduled. Backup purge pending."),
        ("DSAR-2026-003", "Marcus Chen", "Right to Rectification (Article 16)", "2026-11-15", "2026-12-15", "Under Review", "Lead Database Administrator", "Customer profile contact details correction in progress.")
    ]

    for item in dsar_items:
        c.execute("""
        INSERT OR REPLACE INTO dsar_requests (
            id, subject_name, request_type, submission_date, due_date, status, dpo_assigned, action_log
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, item)

    # Seed Third-Party Vendors
    vendor_items = [
        ("VND-01", "Amazon Web Services (AWS)", "Cloud Infrastructure (IaaS)", "Tier 1 - Critical", "All Production Data, Backups, Encryption Keys", 1, 1, 1, 98, "2026-09-15", "Approved"),
        ("VND-02", "Okta Inc.", "Identity & Access Provider (IDaaS)", "Tier 1 - Critical", "Corporate Employee Directory, SSO Tokens, MFA State", 1, 1, 1, 95, "2026-08-20", "Approved"),
        ("VND-03", "GitHub (Microsoft)", "Source Code Hosting & CI/CD", "Tier 1 - Critical", "Proprietary Source Code, Build Secrets", 1, 1, 1, 96, "2026-07-10", "Approved"),
        ("VND-04", "Datadog Inc.", "Observability & SIEM Logging", "Tier 2 - High", "Server Telemetry, Application Logs, Metric Metadata", 1, 1, 1, 92, "2026-05-30", "Approved"),
        ("VND-05", "Checkr Inc.", "Employee Background Verification", "Tier 3 - Medium", "Candidate SSN, Criminal Records, Employment History", 1, 0, 1, 88, "2026-04-12", "Approved")
    ]

    for item in vendor_items:
        c.execute("""
        INSERT OR REPLACE INTO vendors (
            id, name, category, tier, data_shared, soc2_certified, iso27001_certified, dpa_signed, sig_score, last_assessed, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, item)

    # Seed AI Systems (ISO 42001 & EU AI Act)
    ai_items = [
        ("AI-SYS-01", "Customer Support Response Synthesizer", "Generative response drafting for customer support tickets", "LLM (Gemini 1.5 Flash / Claude 3.5)", "Specific Transparency / Limited Risk", 1, "RAG filtering, PII redaction proxy, human approval required before sending", "Operational", "2026-10-01"),
        ("AI-SYS-02", "Automated Candidate Resume Screening Engine", "Automated resume parsing and applicant qualification ranking", "Custom Embedding Model + Gradient Boosted Decision Trees", "High Risk", 1, "Statistical demographic parity audit, bias mitigation, manual human recruiter override", "Under Review", "2026-09-18"),
        ("AI-SYS-03", "Static Code Security & Style Assistant", "Real-time vulnerability and security flaw detection during IDE coding", "Local AST Classifier & Pre-trained Transformer", "Minimal / No Risk", 1, "Air-gapped repository scanning, zero external telemetry egress", "Operational", "2026-11-05")
    ]

    for item in ai_items:
        c.execute("""
        INSERT OR REPLACE INTO ai_systems (
            id, name, purpose, model_type, eu_ai_act_tier, human_in_loop, data_protection_measures, status, last_reviewed
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, item)

    # Seed Audit Findings (from Internal Audit Report)
    audit_findings = [
        ("mNC-01", "ISO/IEC 27001:2022", "A.8.13", "Minor Non-Conformity", "Backup Restoration Verification Timeout",
         "Review of Q1 2026 disaster recovery drill logs showed automated database restoration script timed out at step 4.",
         "Network ACL changes applied in February 2026 blocked cross-VPC peering routes for test restore workers.",
         "Deploy automated test restore runner in isolated staging VPC with explicit IAM permissions. Re-run drill.",
         "Head of Infrastructure", "2026-06-15", "Open"),
        ("mNC-02", "ISO/IEC 27001:2022", "A.5.18", "Minor Non-Conformity", "Stale Ex-Employee IAM Service Account Keys",
         "Five legacy AWS IAM programmatic access keys generated by exited contractor remained active without rotation.",
         "Manual offboarding checklist failed to correlate user-generated IAM programmatic access keys.",
         "Deploy AWS Config rule iam-user-unused-credentials-check with auto-remediation Lambda to disable keys > 30 days old.",
         "IT Security Lead", "2026-06-01", "In Progress"),
        ("OFI-01", "ISO/IEC 27701:2025", "Clause 6.1.2", "Opportunity for Improvement", "Decouple Privacy Risk Impact from Corporate Asset Loss",
         "Current risk register evaluates privacy impacts on corporate brand reputation alongside data subject harm.",
         "Legacy 2019 extension methodology conflated corporate CIA impact with fundamental rights of PII principals.",
         "Establish independent privacy impact scoring matrix dedicated solely to data subject harms for ISO 27701:2025.",
         "Data Protection Officer", "2026-07-01", "Under Review")
    ]

    for item in audit_findings:
        c.execute("""
        INSERT OR REPLACE INTO audit_findings (
            id, audit_standard, control_id, finding_type, title, description, root_cause, corrective_action, owner, due_date, status
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, item)

    # Initial audit log seed
    log_audit_entry(conn, "system_seed", "Admin", "INITIALIZE_DATABASE", "SYSTEM", "AEGIS_CORE", "None", "ISO 27001:2022 & 27701:2025 Baseline Seeded")
    conn.commit()

if __name__ == "__main__":
    init_db()
    print("Aegis GRC SQLite Database initialized and seeded successfully.")
