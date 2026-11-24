# CloudSphere Analytics Inc. Internal Audit Findings and Corrective Action Report

**Document Reference:** CS-AUD-REP-2026-Q2  
**Audit Standard:** ISO/IEC 27001:2022 & ISO/IEC 27701:2025  
**Audit Dates:** 2026-05-01 through 2026-05-12  
**Audit Team:** Lead GRC Analyst (Lead Auditor) & Head of Infrastructure (Technical Auditor)  
**Reviewed & Acknowledged By:** Chief Information Security Officer (CISO) & Board Audit Committee  
**Audit Conclusion:** Certification Ready with Conditional Corrective Actions

---

## 1. Audit Findings Summary

| Finding Classification | Count | Status and Summary |
|---|---|---|
| **Major Non-Conformities (MNC)** | **1** | Contractor offboarding delay identified; automated reconciliation job deployed immediately. |
| **Minor Non-Conformities (mNC)** | **2** | Isolated technical gaps; Jira Corrective Action Plans issued with 30-day resolution targets. |
| **Opportunities for Improvement (OFI)** | **3** | Process improvements identified for threat intelligence and DLP coverage. |
| **Satisfactory Conformities** | **42** | Verified automated CI/CD security controls and cryptographic audit ledger. |

---

## 2. Detailed Findings and Root Cause Analysis

### Major Non-Conformity 01 (MNC-01): Delayed Contractor Account Deprovisioning
* Target Control: ISO/IEC 27001:2022 Control A.5.18 (Access rights)
* Condition Observed: During audit sampling of 20 departed personnel over the trailing 6 months, the audit team found that 3 contractor accounts remained active in Okta for 72 hours past contract expiration, exceeding the mandatory 24-hour SLA.
* Root Cause Analysis: The BambooHR webhook that posts contract end dates to Okta timed out during scheduled maintenance. The integration lacked a dead-letter queue or alerting mechanism to flag failed delivery.
* Corrective Action Plan (CAP-01):
  1. Immediate Action: SecOps terminated all 3 contractor accounts immediately and checked access logs for unauthorized activity; no unauthorized access occurred.
  2. Systemic Fix: Infrastructure deployed a daily Python reconciliation job (`check_deprovisioning_sync.py`) comparing BambooHR active rosters against active Okta accounts. Any discrepancy posts directly to `#sec-ops-alerts` in Slack. (Completed 2026-05-08).

### Minor Non-Conformity 01 (mNC-01): Staging Database Restore Drill Timeout
* Target Control: ISO/IEC 27001:2022 Control A.8.13 (Information backup)
* Condition Observed: Automated daily Aurora PostgreSQL snapshots run on schedule and encrypt with KMS. During the Q1 disaster recovery drill, however, an automated restore of a 2TB production replica into a staging sandbox timed out because of a security group rule conflict between VPC subnets.
* Root Cause Analysis: A recent sprint modified the staging VPC security group without updating the IP allowlist used by the disaster recovery restore script.
* Corrective Action Plan (CAP-02): Update Terraform security group rules and run a complete sandbox restore drill by 2026-05-25. Assigned to: Head of Infrastructure.

### Minor Non-Conformity 02 (mNC-02): Manual Cleanup on Diagnostic Log Buckets
* Target Control: ISO/IEC 27001:2022 Control A.8.10 (Information deletion)
* Condition Observed: Production analytics databases enforce automated 30-day data purges after contract termination. Diagnostic logs in `s3://cloudsphere-app-telemetry-archive`, however, still required a manual Jira ticket for cleanup.
* Corrective Action Plan (CAP-03): Apply AWS S3 Object Lifecycle rules enforcing automated 30-day tombstoning and permanent expiration across all telemetry archive buckets by 2026-05-30. Assigned to: DevSecOps Engineer.
