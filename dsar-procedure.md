# CloudSphere Analytics Inc. • Data Subject Access Request (DSAR) Fulfillment Procedure

**Procedure Reference:** CS-SOP-PRIV-001  
**Regulatory Alignment:** GDPR (Articles 15–22), CCPA/CPRA (Cal. Civ. Code § 1798.100), India DPDP Act 2023 (§ 11–14)  
**ISO/IEC 27701:2025 Alignment:** Annex A.2 (Obligations to PII Principals)  
**Classification:** Internal / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Procedure Owner:** Data Protection Officer (DPO) | Approved By: General Counsel

---

## 1. Scope & Statutory Timelines
This Standard Operating Procedure governs the intake, identity verification, technical search, redaction, and response delivery for all Data Subject Access Requests (DSARs) submitted by individuals exercising statutory privacy rights:
*   **Right of Access (Article 15)**
*   **Right to Rectification (Article 16)**
*   **Right to Erasure / "To Be Forgotten" (Article 17)**
*   **Right to Restriction & Data Portability (Articles 18 & 20)**

### Statutory Fulfillment SLA:
*   **Standard Deadline:** Within **30 calendar days** of verified receipt.
*   **Complex Request Extension:** Up to an additional **60 days** for unusually complex requests, provided written justification is communicated to the data subject within the initial 30-day window.

---

## 2. Five-Stage DSAR Processing Workflow

```
[Stage 1: Intake & Logging]
       │ (Privacy Portal Form -> Jira PRIV-XXXX Ticket -> 30-Day SLA Timer Starts)
       ▼
[Stage 2: Identity Verification]
       │ (Government ID Check / Magic Link Tokenization / Zero PII Leakage)
       ▼
[Stage 3: Data Retrieval & Extraction]
       │ (PostgreSQL Tenant Query, S3 Event Extraction, BambooHR/Greenhouse Dump)
       ▼
[Stage 4: Third-Party Redaction & Legal Review]
       │ (Scrub Non-Subject Data, Proprietary IP, Legal Privilege Review)
       ▼
[Stage 5: Secure Delivery & Audit Closure]
       │ (Encrypted ZIP with One-Time Passcode -> SHA-256 Hashed Log Entry)
```

---

## 3. Detailed Stage Operational Runbooks

### Stage 1: Intake & Logging
1.  Requests received via email (`privacy@cloudsphere.com`) or the CloudSphere Privacy Trust Center form automatically generate a ticket in the Jira Privacy Queue (`PRIV-XXXX`).
2.  The DPO verifies jurisdiction (EU, California, India, or Global) and sets the 30-day countdown timer in the Aegis GRC Privacy Hub.

### Stage 2: Identity Verification (Preventing Fraudulent Data Leaks)
*   **CRITICAL SAFEGUARD:** Never fulfill a DSAR without independent identity verification. Delivering personal data to an unverified requester constitutes an actionable security breach.
*   **Direct Employees/Candidates:** Verification conducted via corporate Okta authentication or video verification with HR.
*   **Enterprise Customer End-Users (CloudSphere as Processor):** If an individual submits a DSAR directly to CloudSphere regarding customer analytics data, CloudSphere **must not** unilaterally export data. Under GDPR Article 28, the DPO notifies the enterprise client (Data Controller) within **3 business days**, forwarding the request for controller authorization.

### Stage 3: Technical Search & Extraction Runbook
Upon verified authorization, the data engineering team executes pre-approved parameterized extraction scripts:
1.  **PostgreSQL Search:** `SELECT * FROM analytics_events WHERE user_pseudonym_id = :subject_id;`
2.  **S3 Log Archives:** Athena query partitioned by customer tenant ID and date range to extract raw event telemetry.
3.  **Corporate Systems (if employee/candidate):** Google Vault export of email correspondence involving the requester; BambooHR employee file export.

### Stage 4: Redaction & Legal Review
The DPO and Legal Counsel review the raw extraction dump to ensure:
*   No personal data belonging to third-party individuals (e.g., coworkers or other customer users) is inadvertently included.
*   Trade secrets, proprietary code algorithms, and confidential business strategies are redacted under statutory exemptions (e.g., GDPR Article 15(4)).

### Stage 5: Secure Delivery & Cryptographic Logging
1.  Extracted records are packaged into a password-protected AES-256 encrypted ZIP archive.
2.  The download link and decryption token are delivered via separate, secure communication channels.
3.  The DPO logs the completed action, timestamp, and SHA-256 fingerprint of the exported bundle into the immutable GRC audit ledger.
