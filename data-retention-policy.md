# CloudSphere Analytics Inc. • Data Retention & Secure Disposal Policy

**Policy Reference:** CS-POL-006  
**ISO/IEC 27001:2022 Alignment:** Controls A.8.10 (Information deletion), A.8.14 (Redundancy)  
**ISO/IEC 27701:2025 Alignment:** Clauses 6.5, 7.4 (PIMS Data Retention & Disposal)  
**Classification:** Internal / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Policy Owner:** Data Protection Officer (DPO) & Head of Infrastructure | Approved By: CISO

---

## 1. Purpose & Data Minimization Principles
This policy defines statutory and contractual retention periods, automated purging technical architectures, and cryptographic sanitization standards across all databases, cloud storage buckets, and endpoint hardware operated by CloudSphere Analytics Inc.

---

## 2. Master Data Retention Schedule

| Data Category | Data Sub-Types | Regulatory / Business Basis | Mandatory Retention Period | Automated Purging Architecture |
|---|---|---|---|---|
| **Customer Telemetry & Raw Events** | Ingested clickstream logs, device telemetry, raw JSON event payloads. | Customer Master Services Agreement (MSA) | **Duration of contract + 30 calendar days** | AWS S3 Lifecycle Rule (`ExpireAfterDays: 30`) with automated partition tombstoning. |
| **Aggregated Customer Analytics** | Pre-computed hourly/daily rollups, reporting dashboards, churn scores. | Contractual SLA reporting | **Duration of contract + 90 calendar days** | Automated PostgreSQL deletion worker executed via cron; hard purge across tenant partitions. |
| **Security & Operational Audit Logs** | AWS CloudTrail, EKS audit logs, Okta authentication logs, Datadog SIEM events. | ISO 27001 Control A.8.15 & SOC 2 CC7.2 | **365 calendar days (1 year)** | S3 Object Lock compliance mode; transitioned to S3 Glacier Flexible Archive after 90 days, purged at 365 days. |
| **Employee & Payroll Records** | Tax records, payroll slips, employment agreements, background checks. | IRS, California Labor Code, statutory tax rules | **7 years post-termination** | Google Vault retention rules; access restricted strictly to Head of People and Corporate Controller. |
| **Customer Financial & Billing Data** | Stripe invoices, transaction logs, enterprise wire receipts. | GAAP & Corporate Tax Laws | **7 years** | Stripe automated vaulting; corporate accounting exports stored in encrypted financial S3 bucket. |

---

## 3. Cryptographic Erasure & Hardware Sanitization Standards
1.  **Cloud Database Record Purging (PostgreSQL):** When customer contract termination or an approved Right-to-Erasure (DSAR) request is received, the data engineering pipeline triggers `tenant_purge_worker`. Records are scrubbed using cryptographic hard delete (`DELETE FROM analytics WHERE tenant_id = X`). To prevent lingering data in automated snapshot archives, backups are naturally rotated out under the 30-day snapshot expiration lifecycle.
2.  **S3 Object Storage Sanitization:** S3 bucket objects are tagged with tenant identifiers. Upon termination, a tombstone event triggers permanent deletion of all historical versions, followed by cryptographic erasure of the KMS key material associated with that customer's tenant partition.
3.  **Physical Endpoint Laptop Sanitization:** When a remote employee departs CloudSphere, their MacBook laptop is sanitized via Kandji MDM executing an automated Apple APFS cryptographic wipe (`eraseinstall --erase-system-volume`). This destroys all cryptographic keys on the Apple Secure Enclave, rendering all residual disk sectors mathematically unrecoverable in compliance with **NIST SP 800-88 Rev 1 (Clear/Purge)** guidelines.
