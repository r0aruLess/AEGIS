# CloudSphere Analytics Inc. • ISO/IEC 27001:2022 Baseline Gap Assessment

**Document Reference:** CS-GRC-GAP-2026-Q1  
**Target Standard:** ISO/IEC 27001:2022 (Annex A 93 Controls & Management Clauses 4–10)  
**Conducted By:** Lead GRC Analyst & Head of Infrastructure  
**Reviewed By:** Chief Information Security Officer (CISO)  
**Assessment Date:** 2026-04-20 | Overall Readiness Score: **86.0% (Stage 1 Audit Ready)**

---

## 1. Executive Summary & Audit Posture
A comprehensive internal baseline gap assessment was executed across all 93 controls of ISO/IEC 27001:2022 to benchmark CloudSphere's information security posture prior to formal Stage 1 external certification.

### Quantitative Readiness Breakdown:
*   **Fully Implemented & Verified Controls (PASSED):** **80 controls (86.0%)** — Technical controls validated via automated SHA-256 evidence digests or policy inspection.
*   **Partially Implemented Controls (WARNING):** **9 controls (9.7%)** — Remediation action plans logged in Jira with 30–60 day target completion dates.
*   **Controls Excluded with Justification (EXEMPT):** **4 controls (4.3%)** — Physical data center utilities (A.7.11–A.7.14) inherited from AWS under Shared Responsibility.
*   **Major Deficiencies (FAILED):** **0 controls** — No catastrophic systemic security absences identified.

---

## 2. Key Gaps Identified & Corrective Actions

| Control ID & Title | Theme | Baseline Status | Specific Gap Description | Assigned Owner | Corrective Action & Target Date |
|---|---|---|---|---|---|
| **A.5.7 Threat intelligence** | Organizational | WARNING | Threat intelligence ingest is currently ad-hoc via open-source feeds (CISA KEV); lacks commercial feed integration. | SecOps Lead | Integrate AlienVault OTX and AWS GuardDuty automated threat feeds by 2026-06-15. |
| **A.8.10 Information deletion** | Technological | WARNING | Customer data deletion is automated in Aurora PostgreSQL via API, but S3 log archive cleanup requires manual ticket sign-off. | Head of Infrastructure | Deploy S3 Object Lifecycle expiration rules (30-day automated tombstoning) by 2026-05-30. |
| **A.8.12 Data leakage prevention** | Technological | WARNING | Endpoint DLP relies on Kandji MDM native restrictions; no content-inspection DLP agent deployed on remote engineer endpoints. | IT Operations Lead | Roll out Google Workspace DLP rules and Nightfall DLP for Slack Enterprise by 2026-06-30. |
| **A.8.13 Information backup** | Technological | WARNING | Automated Aurora PostgreSQL daily snapshots exist; however, Q1 staging restore drill timed out due to a security group rule mismatch. | Head of Infrastructure | Reconfigure VPC peering rules and complete automated monthly sandbox restore validation by 2026-05-25. |
