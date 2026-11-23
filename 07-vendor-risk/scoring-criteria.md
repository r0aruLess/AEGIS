# CloudSphere Analytics Inc. • Third-Party Security Scoring Methodology (100-Point Model)

**Document Reference:** CS-TPRM-METH-001  
**Standard Alignment:** ISO/IEC 27001:2022 Control A.5.19 & SOC 2 Common Criteria CC9.2  
**Classification:** Internal / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Owner:** Lead GRC Analyst | Approved By: CISO

---

## 1. 100-Point Evaluation Model & Passing Thresholds
Every new or renewing vendor undergoes quantitative evaluation by the GRC team using the CloudSphere TPRM Scoring Framework across 5 standardized security dimensions:

| Evaluation Dimension | Maximum Points | Minimum Passing Threshold | Evaluation Focus & Verification Criteria |
|---|---|---|---|
| **1. Certifications & Independent Assurance** | **25 Points** | 15 Points | Independent SOC 2 Type II report with unqualified opinion (20 pts); ISO/IEC 27001:2022 accredited certificate (5 pts). |
| **2. Cryptography & Data Protection** | **20 Points** | 15 Points | Mandatory AES-256 encryption at rest (10 pts); TLS 1.3 in transit (5 pts); Customer-Managed Keys (CMK) support (5 pts). |
| **3. Identity & Access Governance** | **20 Points** | 12 Points | Mandatory SAML 2.0 / OIDC SSO integration (10 pts); Phishing-resistant MFA enforcement (5 pts); SCIM deprovisioning (5 pts). |
| **4. Vulnerability & Incident Management** | **20 Points** | 12 Points | Documented 72-hour breach notification SLA (10 pts); Regular third-party penetration testing (5 pts); Responsible disclosure / bug bounty (5 pts). |
| **5. Privacy & Regulatory Compliance** | **15 Points** | 10 Points | Executed DPA with Standard Contractual Clauses (10 pts); Dedicated Data Protection Officer (DPO) (3 pts); Subprocessor transparency (2 pts). |

### Overall Scoring Tiers & Approvals:
*   **Tier A (90–100 Points): Approved Supplier.** Fast-track approval; 2-year reassessment cycle.
*   **Tier B (75–89 Points): Conditionally Approved.** Standard approval; mandatory annual reassessment.
*   **Tier C (60–74 Points): Elevated Risk / Remediation Required.** Requires written risk acceptance from CISO and compensating controls.
*   **Tier D (< 60 Points): Unacceptable Risk / Rejected.** Procurement blocked at corporate payment gate.
