# CloudSphere Analytics Inc. Incident Management and Regulatory Reporting Procedure

**Procedure Reference:** CS-SOP-004  
**ISO/IEC 27001:2022 Alignment:** Controls A.5.24, A.5.25, A.5.26, A.5.27, A.5.28, A.6.8  
**ISO/IEC 27701:2025 Alignment:** Clause 8.2, Annex A.4.2 (Breach notification to controllers)  
**Classification:** Confidential / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Procedure Owner:** SecOps & Incident Response Lead | Approved By: CISO & General Counsel

---

## 1. Incident Severity Tiers and 24/7 On-Call Model

To maintain 24/7 incident response across a 10-person security team, CloudSphere runs a hybrid on-call model:
* Tier 1 Off-Hours Alert Monitoring: Rapid7 MDR monitors Datadog SIEM, CrowdStrike EDR, and AWS GuardDuty alerts around the clock.
* Tier 2 and 3 Escalation: Rapid7 pages CloudSphere's primary on-call SecOps engineer through PagerDuty for any verified security incident.

| Severity Tier | Incident Definition & Impact Criteria | Target Triage SLA | Escalation Path | Mandatory Notification Target |
|---|---|---|---|---|
| **SEV-1: Critical** | Confirmed customer PII exfiltration, active ransomware on AWS workloads, unauthorized production database admin access, or major analytics outage. | **15 minutes** (Rapid7 MDR / PagerDuty) | PagerDuty high-urgency call to SecOps Lead, CISO, and CTO. CISO notifies CEO and General Counsel within 1 hour. | **72 hours** under EU GDPR (EDPB) / **6 hours** for critical system disruptions under India CERT-In directions. |
| **SEV-2: High** | Targeted credential stuffing on Okta, single production host compromised without lateral movement, critical CVE actively exploited in staging. | **30 minutes** | SecOps Lead and Lead Infrastructure Engineer paged. CISO notified in Slack `#incident-sev2`. | Customer notification evaluated within 24 hours based on DPA terms. |
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

### Detailed Phase Runbooks

1. Phase 1: Detection and Initial Triage:
   * Incident Commander (SecOps Lead) opens an incident channel in Slack (`#inc-YYYYMMDD-title`) and a dedicated Zoom room.
   * The team creates an incident ticket in Jira (`INC-XXXX`) to record timestamped events.
2. Phase 2: Short-Term and Long-Term Containment:
   * Host Isolation: CrowdStrike Falcon network containment API isolates affected EKS nodes or MacBooks.
   * Identity Revocation: Okta Admin API terminates compromised user sessions immediately (`clearUserSessions` and password reset).
   * Network Isolation: Infrastructure team applies Terraform emergency hotfixes to AWS Security Groups to stop traffic between affected instances and Aurora databases.
3. Phase 3: Eradication and Recovery:
   * CI/CD pipelines replace vulnerable container images with patched builds from clean GitHub main branch commits.
   * Engineers rotate AWS IAM credentials, database passwords, and KMS data keys if they suspect exposure.
   * Database administrators restore data from known-good encrypted snapshots verified prior to the breach timestamp.
4. Phase 4: Evidence Preservation and Post-Mortem (Root Cause Analysis):
   * SecOps exports memory dumps, container logs, and CloudTrail logs to the immutable S3 Compliance Vault with SHA-256 hashes.
   * The team holds a blameless post-mortem within 5 business days with executive leadership, documents the root cause analysis, and tracks corrective action plans in Jira with 30-day resolution SLAs.

---

## 3. Statutory Breach Notification Runbook (GDPR and CERT-In)

When the team confirms compromise of customer personal data (PII):
1. Hour 0 to 2: CISO and General Counsel convene the Incident Steering Committee.
2. Hour 2 to 6: General Counsel evaluates reporting requirements under GDPR Article 33 and CERT-In directions. If Indian critical infrastructure or customer records are affected, the team submits initial notice to `incident@cert-in.org.in` using standard CERT-In reporting forms.
3. Hour 6 to 72: SecOps and legal transmit formal notification to the lead supervisory authority (such as the Data Protection Commission of Ireland for EU operations). The notice details the nature of the breach, affected customer volumes, likely consequences, and remediation measures taken.
4. Enterprise Customer Notification: Communications distributes contractual notices to affected B2B enterprise customers within the window specified in each client's Data Processing Agreement (typically 48 to 72 hours).
