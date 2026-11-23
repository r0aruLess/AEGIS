# CloudSphere Analytics Inc. • ISMS & PIMS Scope Statement

**Document Reference:** CS-ISMS-SCOPE-001  
**Standards Alignment:** ISO/IEC 27001:2022 (Clause 4.3) & ISO/IEC 27701:2025 (Clause 4.3)  
**Classification:** Public / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Approved By:** Chief Information Security Officer (CISO) & Chief Executive Officer (CEO)

---

## 1. Scope Boundary & Organizational Context
The Information Security Management System (ISMS) and Privacy Information Management System (PIMS) encompass all operational activities, cloud infrastructure, personnel, and intellectual property assets utilized by **CloudSphere Analytics Inc.** in the design, development, maintenance, and delivery of its multi-tenant B2B customer behavioral analytics SaaS platform.

### In-Scope Boundaries:
1.  **Cloud Workloads & Environments:** Production AWS accounts (`us-east-1` primary and `eu-central-1` EU residency zone), including Amazon EKS container workloads, Aurora PostgreSQL databases, S3 storage buckets, and KMS key management.
2.  **Corporate IT & Identity Services:** Okta Universal Directory, Google Workspace, GitHub Enterprise Cloud, and Datadog SIEM platforms.
3.  **Human Resources & Remote Endpoints:** All 150 full-time equivalents (FTEs) and vetted contractors operating corporate-managed MacBook endpoints equipped with Kandji MDM, FileVault encryption, and EDR agents.

### Explicit Scope Exclusions & Justification:
*   **Physical Data Center Infrastructure:** CloudSphere operates as a **100% remote-first SaaS company with zero owned physical corporate offices or physical data centers**.
*   **Justification:** Physical facility perimeters, biometric building controls, diesel generator utilities, cabling conduits, and server chassis destruction (ISO/IEC 27001:2022 Controls A.7.11, A.7.12, A.7.13, A.7.14) are **excluded from CloudSphere's direct operational boundary**. Assurance is inherited via the **AWS Cloud Shared Responsibility Model**, validated annually through independent inspection of AWS SOC 2 Type II (Criteria CC6.4, CC6.5) and ISO/IEC 27001 certification.

---

## 2. PIMS Role Determination (ISO/IEC 27701:2025 Clause 4.3)
Under the revised requirements of ISO/IEC 27701:2025:
*   **CloudSphere as a PII Processor:** Acts as a Data Processor / Data Fiduciary on behalf of its enterprise B2B customers when processing end-user telemetry, clickstream behavioral logs, and customer account identifiers ingested via CloudSphere SDKs.
*   **CloudSphere as a PII Controller:** Acts as a Data Controller with respect to direct corporate employee records, recruitment data, enterprise client billing contacts, and sales engagement records.
