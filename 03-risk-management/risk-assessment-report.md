# Annual Information Security Risk Assessment Report (FY 2026)
**Entity:** CloudScale Technologies Inc.  
**Classification:** Confidential — Internal ISMS Steering Committee & Board Audit Committee  
**Standard Reference:** ISO/IEC 27001:2022 (Clause 6.1.2, 6.1.3, 8.2, 8.3) & NIST SP 800-30 Rev 1  
**Assessment Date:** February 15, 2026  
**Lead Assessor:** Lead GRC Analyst / ISMS Manager  
**Approver:** Chief Information Security Officer (CISO) & Chief Executive Officer (CEO)

---

## 1. Executive Summary
During Q1 2026, CloudScale Technologies completed its comprehensive annual Information Security and Privacy Risk Assessment across all core digital assets, customer production environments (AWS us-east-1 and eu-west-1), corporate infrastructure, and third-party SaaS vendors.

The assessment evaluated **10 primary operational and information security risk scenarios**. Utilizing CloudScale's calibrated 5x5 Likelihood ($L$) $\times$ Impact ($I$) risk matrix, the organization initially identified:
- **3 High Inherent Risks (Score 15–25)**
- **5 Medium Inherent Risks (Score 6–12)**
- **2 Low Inherent Risks (Score 1–5)**

Following the validation of existing Annex A preventive and detective controls, and factoring in the planned Risk Treatment Plan (RTP) actions, **all residual risks have been reduced to within CloudScale's defined Risk Appetite threshold (Residual Score $\le 12$)**, with zero unmitigated Critical or High residual risks remaining.

---

## 2. Risk Methodology & Assessment Criteria
Risks were calculated using the standard qualitative and semi-quantitative formulas:
$$\text{Inherent Risk} = L_{\text{inherent}} \times I_{\text{inherent}}$$
$$\text{Residual Risk} = \text{Round}\Big(\text{Inherent Risk} \times (1 - E_{\text{control}})\Big)$$

Where Control Effectiveness ($E_{\text{control}}$) is defined as:
- **Major Gap / Missing Control:** $E = 0.00$ (0% mitigation, full inherent risk exposure)
- **Partial Gap / Inconsistent Control:** $E = 0.35$ (35% mitigation)
- **Verified / Fully Implemented Control:** $E = 0.75$ (75% mitigation)

### Risk Classification Thresholds
- **Critical (16 - 25):** Unacceptable; requires emergency board escalation and immediate corrective remediation within 48 hours.
- **High (13 - 15):** Exceeds appetite; requires formal treatment plan and weekly CISO status tracking (remediation within 30 days).
- **Medium (6 - 12):** Within acceptable tolerance; monitored through standard quarterly reviews.
- **Low (1 - 5):** Acceptable; managed under standard operational baselines.

---

## 3. Risk Profile & Comparative Summary

| Risk ID | Risk Scenario | Asset / Process | Inherent L | Inherent I | Inherent Score | Inherent Level | Applicable ISO 27001 Control | Control Status | Residual Score | Residual Level | Treatment Strategy |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **RSK-001** | AWS S3 customer backup bucket misconfiguration exposes tenant PII | S3 Data Lakes | 4 | 5 | **20** | **Critical** | A.8.12 (Data leakage prevention) | Verified ($E=0.75$) | **5** | **Low** | Mitigate via SCPs, AWS Macie, Terraform policy |
| **RSK-002** | Credential stuffing / unauthorized admin console access | Okta SSO / Admin UI | 4 | 4 | **16** | **Critical** | A.8.5 (Secure authentication) | Verified ($E=0.75$) | **4** | **Low** | Mitigate via FIDO2 WebAuthn & Phishing-resistant MFA |
| **RSK-003** | Zero-day remote code execution in container runtime | EKS Production Cluster | 3 | 5 | **15** | **High** | A.8.8 (Vulnerability mgmt) | Partial ($E=0.35$) | **10** | **Medium** | Mitigate via automated CI/CD container scanning (Trivy) |
| **RSK-004** | Unencrypted database backups stored in cold storage | RDS PostgreSQL Snapshots | 3 | 4 | **12** | **Medium** | A.8.24 (Use of cryptography) | Verified ($E=0.75$) | **3** | **Low** | Mitigate via AWS KMS CMK envelope encryption |
| **RSK-005** | Production database exposed to public Internet via security group drift | RDS Aurora Cluster | 2 | 5 | **10** | **Medium** | A.8.20 (Network security) | Verified ($E=0.75$) | **3** | **Low** | Mitigate via IaC drift detection & AWS Config rules |
| **RSK-006** | Developer hardcodes production API secret in public GitHub repository | GitHub Enterprise | 3 | 3 | **9** | **Medium** | A.8.28 (Secure coding) | Verified ($E=0.75$) | **2** | **Low** | Mitigate via GitGuardian pre-commit hooks & secret scanning |
| **RSK-007** | Sub-processor data breach at third-party marketing analytics vendor | SaaS Marketing Vendor | 3 | 3 | **9** | **Medium** | A.5.19 (Information security in supplier relationships) | Partial ($E=0.35$) | **6** | **Medium** | Mitigate via annual SIG Lite questionnaire & DPA enforcement |
| **RSK-008** | Delayed employee termination revoking SaaS access permissions | HRIS & Active Directory | 2 | 4 | **8** | **Medium** | A.6.5 (Responsibilities after termination) | Verified ($E=0.75$) | **2** | **Low** | Mitigate via automated SCIM deprovisioning from BambooHR |
| **RSK-009** | Lack of tested disaster recovery runbook causing extended RTO breach | Core Microservices | 2 | 4 | **8** | **Medium** | A.8.14 (Redundancy of information processing facilities) | Partial ($E=0.35$) | **5** | **Low** | Mitigate via bi-annual cross-region DR tabletop & failover drill |
| **RSK-010** | Insider data exfiltration prior to key staff resignation | Workstations & Endpoint Laptops | 2 | 2 | **4** | **Low** | A.8.12 (Data leakage prevention) | Verified ($E=0.75$) | **1** | **Low** | Accept & Monitor via MDM endpoint DLP agents |

---

## 4. Key Assessment Findings & Observations
1. **Strengths:**
   - Identity federation via Okta with enforced WebAuthn/FIDO2 MFA has eliminated single-factor attack vectors for corporate and administrative access.
   - Core databases enforce AES-256 KMS customer-managed key encryption at rest and TLS 1.3 in transit.
   - Shift-left CI/CD pipelines prevent common static secrets from being committed to source control.

2. **Opportunities for Improvement (Control Gaps):**
   - **Container Vulnerability Management (A.8.8):** While base OS images are scanned monthly, intermediate container layers in feature branches lacked real-time blocking on Critical CVEs.
   - **Third-Party Continuous Monitoring (A.5.19):** Vendor reviews were performed during initial procurement but lacked automated trigger reviews when sub-processors changed.
   - **Cross-Region DR Failover Testing (A.8.14):** Backup restoration tests were executed quarterly, but end-to-end DNS failover simulations between us-east-1 and eu-west-1 had not occurred in the past 12 months.

---

## 5. Risk Treatment Recommendations & Timetable
| Recommendation | Target Control | Owner | Target Completion | Resource / Budget |
| :--- | :--- | :--- | :--- | :--- |
| Enforce Trivy automated container blocking in GitHub Actions | A.8.8 | Lead DevOps Engineer | Q2 2026 (April 15) | Existing toolchain |
| Deploy automated Vendor Risk Management tracker & annual SIG review | A.5.19 | GRC Analyst | Q2 2026 (May 30) | GRC operational hours |
| Conduct full simulated failover drill for customer-facing APIs | A.8.14 | Infrastructure Lead | Q3 2026 (July 20) | Cloud staging budget |

---

## 6. Formal Sign-Off
- **Assessed By:** GRC Analyst / ISMS Lead — *CloudScale Technologies*  
- **Reviewed By:** Chief Information Security Officer (CISO) — *CloudScale Technologies*  
- **Approved By:** Audit Committee Chair, Board of Directors — *CloudScale Technologies*