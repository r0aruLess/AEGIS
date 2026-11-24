# CloudSphere Analytics Inc. Data Subject Access Request Fulfillment Procedure

**Procedure Reference:** CS-SOP-PRIV-001  
**Regulatory Alignment:** GDPR (Articles 15 to 22), CCPA/CPRA (Cal. Civ. Code § 1798.100), India DPDP Act 2023 (§ 11 to 14)  
**ISO/IEC 27701:2025 Alignment:** Annex A.2 (Obligations to PII Principals)  
**Classification:** Internal / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Procedure Owner:** Data Protection Officer (DPO) | Approved By: General Counsel

---

## 1. Scope and Fulfillment Timelines

This procedure sets out how CloudSphere handles intake, identity verification, technical retrieval, redaction, and response delivery for Data Subject Access Requests (DSARs). It covers the following statutory rights:
* Right of Access (GDPR Article 15)
* Right to Rectification (Article 16)
* Right to Erasure / Right to Be Forgotten (Article 17)
* Right to Restriction and Data Portability (Articles 18 and 20)

### Fulfillment Deadlines

* Standard Deadline: Within 30 calendar days of verified receipt.
* Complex Request Extension: Up to an additional 60 days for complex requests, provided the DPO sends written justification to the requester within the initial 30-day window.

---

## 2. Five-Stage DSAR Workflow

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

## 3. Operational Runbooks by Stage

### Stage 1: Intake and Logging
1. Requests sent to `privacy@cloudsphere.com` or submitted through the CloudSphere Privacy Trust Center form generate a ticket in the Jira Privacy Queue (`PRIV-XXXX`).
2. The DPO verifies jurisdiction (EU, California, India, or other) and sets a 30-day countdown timer in the Aegis GRC Privacy Hub.

### Stage 2: Identity Verification
* The team never fulfills a DSAR without independent identity verification, since releasing personal data to an unverified requester constitutes a data breach.
* Employees and Job Candidates: Verification runs through Okta single sign-on or a video call with HR.
* Enterprise Customer End-Users: When an end-user submits a request regarding customer analytics data where CloudSphere acts as a data processor, CloudSphere does not export data directly. Under GDPR Article 28, the DPO notifies the enterprise client (the Data Controller) within 3 business days and routes the request for controller instruction.

### Stage 3: Technical Search and Extraction Runbook
After verified authorization, data engineers run approved, parameterized extraction queries:
1. PostgreSQL Search: `SELECT * FROM analytics_events WHERE user_pseudonym_id = :subject_id;`
2. S3 Log Archives: Athena queries partitioned by tenant ID and date range extract raw event telemetry.
3. Corporate Systems (for employee or candidate requests): Google Vault exports relevant email threads; BambooHR exports personnel records.

### Stage 4: Redaction and Legal Review
The DPO and Legal Counsel review the raw extraction dump to confirm:
* The file excludes personal data of third-party individuals, such as coworkers or other customer users.
* The team redacts trade secrets, proprietary algorithms, and internal business plans under statutory exemptions (such as GDPR Article 15(4)).

### Stage 5: Secure Delivery and Audit Logging
1. Engineers package extracted records into an AES-256 encrypted ZIP archive.
2. The team delivers the download link and decryption token through separate communication channels.
3. The DPO logs the completed action, timestamp, and SHA-256 hash of the exported bundle in the GRC audit register.
