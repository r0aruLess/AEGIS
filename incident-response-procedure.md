# CloudSphere Analytics Inc. • Incident Management & Regulatory Reporting Procedure

**Procedure Reference:** CS-SOP-004  
**ISO/IEC 27001:2022 Alignment:** Controls A.5.24, A.5.25, A.5.26, A.5.27, A.5.28, A.6.8  
**ISO/IEC 27701:2025 Alignment:** Clause 8.2, Annex A.4.2 (Breach notification to controllers)  
**Classification:** Confidential / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Procedure Owner:** SecOps & Incident Response Lead | Approved By: CISO & General Counsel

---

## 1. Incident Severity Tiers & 24/7 On-Call Architecture

To sustain round-the-clock incident response across a 10-person security team, CloudSphere operates a **hybrid on-call model**:
*   **Tier 1 Off-Hours Alert Monitoring:** Contracted to a 24/7 outsourced Managed Detection and Response partner (**Rapid7 MDR**), who monitors Datadog SIEM, CrowdStrike EDR, and AWS GuardDuty alerts 24/7/365.
*   **Tier 2 & 3 Escalation:** Rapid7 directly pages CloudSphere's primary on-call SecOps engineer via PagerDuty for any verified security incident.

| Severity Tier | Incident Definition & Impact Criteria | Target Triage SLA | Escalation Path | Mandatory Notification Target |
|---|---|---|---|---|
| **SEV-1: Critical** | Confirmed customer PII exfiltration, active ransomware on AWS workloads, unauthorized production database administrative access, or systemic customer analytics outage. | **15 minutes** (Rapid7 MDR / PagerDuty) | PagerDuty high-urgency call to SecOps Lead, CISO, and CTO. CISO notifies CEO and General Counsel within 1 hour. | **72 hours** under EU GDPR (EDPB) / **6 hours** for critical system disruptions under India CERT-In directions. |
| **SEV-2: High** | Targeted credential stuffing on Okta, single production host compromised without lateral movement, critical CVE actively exploited in staging. | **30 minutes** | SecOps Lead and Lead Infrastructure Engineer paged. CISO notified via Slack `#incident-sev2`. | Customer notification evaluated within 24 hours based on DPA clauses. |
| **SEV-3: Medium** | Isolated employee laptop malware blocked by EDR, unapproved S3 bucket configuration flagged in staging, suspicious failed logins. | **4 hours** | Ticket assigned to Security Operations Engineer in Jira Service Management queue. | Internal incident log only. |
| **SEV-4: Low** | Phishing email reported via KnowBe4 button, minor port scan detected on Cloudflare perimeter, routine audit finding. | **24 hours** | Handled during standard business hours by SecOps team. | None. |

---

## 2. Four-Phase Incident Response Lifecycle (NIST SP 800-61 Rev 2)

```
[Phase 1: Detection & Triage]
       │ (Datadog SIEM Alert -> Rapid7 MDR / PagerDuty -> On-Call SecOps Engineer)
       ▼
[Phase 2: Containment & Isolation]
       │ (EKS Pod Quarantine, AWS Security Group Revocation, Okta Session Invalidation)
       ▼
[Phase 3: Eradication & Recovery]
       │ (KMS Key Rotation, Clean AMI/Container Redeployment, Snapshot Restoration)
       ▼
[Phase 4: Post-Incident Review & Evidence Preservation]
       │ (Root Cause Analysis, SHA-256 Forensic Image Vaulting, 30-Day CAP Tracking)
```

### Detailed Phase Runbooks:
1.  **Phase 1: Detection & Initial Triage:**
    *   Incident Commander (SecOps Lead) opens an incident channel in Slack (`#inc-YYYYMMDD-title`) and a dedicated Zoom war room.
    *   Incident ticket created in Jira (`INC-XXXX`) to record timestamped chronologies.
2.  **Phase 2: Short-Term & Long-Term Containment:**
    *   **Host Isolation:** Compromised EKS nodes or MacBooks isolated via CrowdStrike Falcon network containment API.
    *   **Identity Revocation:** Compromised Okta user session terminated immediately via Okta Admin API (`clearUserSessions` and password reset).
    *   **Network Severing:** AWS Security Groups modified via Terraform emergency hotfix to sever communication between affected instances and the Aurora database.
3.  **Phase 3: Eradication & Recovery:**
    *   Vulnerable container images replaced with patched images built from clean GitHub main branch commits.
    *   All AWS IAM credentials, database passwords, and KMS data keys rotated if exposure is suspected.
    *   Database restoration executed from known-good encrypted snapshots verified prior to the breach timestamp.
4.  **Phase 4: Evidence Preservation & Post-Mortem (Root Cause Analysis):**
    *   Memory dumps, container logs, and CloudTrail logs exported to the immutable S3 Compliance Vault with SHA-256 fingerprinting.
    *   Formal Blameless Post-Mortem conducted within **5 business days** with executive leadership, documenting the Root Cause Analysis (RCA) and issuing Jira Corrective Action Plans (CAP) with 30-day resolution SLAs.

---

## 3. Statutory Breach Notification Runbook (GDPR & CERT-In)
When customer personal data (PII) is confirmed compromised:
1.  **Hour 0–2:** CISO and General Counsel convene the Incident Steering Committee.
2.  **Hour 2–6:** General Counsel assesses reporting thresholds under GDPR Article 33 and CERT-In directions. If Indian critical infrastructure or customer records are affected, initial notice is submitted to `incident@cert-in.org.in` using standard CERT-In reporting forms.
3.  **Hour 6–72:** Formal notification transmitted to the lead supervisory authority (e.g., Data Protection Commission of Ireland for EU operations) detailing the nature of the breach, affected customer volumes, likely consequences, and remediation measures taken.
4.  **Enterprise Customer Notification:** Communications team distributes contractual notices to affected B2B enterprise customers within the SLA specified in each client's Data Processing Agreement (typically 48–72 hours).
