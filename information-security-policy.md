# CloudSphere Analytics Inc. • Master Information Security Policy

**Policy Reference:** CS-POL-001  
**ISO/IEC 27001:2022 Alignment:** Clause 5.2 (Policy), Controls A.5.1, A.5.2, A.5.3, A.5.4  
**SOC 2 Alignment:** Common Criteria CC1.1, CC1.2, CC2.1  
**Classification:** Public / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Policy Owner:** Chief Information Security Officer (CISO) | Approved By: Board Audit Committee & CEO

---

## 1. Executive Mandate & Purpose
This Master Information Security Policy establishes executive leadership direction and mandatory security standards for protecting the confidentiality, integrity, and availability (CIA triad) of all information assets, customer data, and cloud infrastructure owned, managed, or processed by **CloudSphere Analytics Inc. ("CloudSphere")**.

Compliance with this policy is mandatory for all 150 full-time equivalents (FTEs), part-time employees, contractors, and third-party vendors with access to CloudSphere production systems, corporate identities, or customer telemetry.

---

## 2. Core Information Security Principles
1.  **Defense-in-Depth & Zero Trust Architecture:** Perimeter firewalls alone are never considered sufficient. Every network segment, microservice endpoint, and remote laptop must authenticate and authorize requests via mutual TLS (mTLS) or OAuth2/OIDC.
2.  **Principle of Least Privilege & Separation of Duties:** Logical access to production systems, databases, and customer records is granted strictly on a business-need-to-know basis. Engineers who author source code cannot unilaterally approve pull requests or trigger production deployments without a secondary reviewer.
3.  **Default Deny & Shift-Left Validation:** All firewall, security group, and IAM configurations default to explicit deny. Infrastructure-as-Code (Terraform) and container images are scanned in automated GitHub CI/CD pipelines before cloud deployment.
4.  **Continuous Cryptographic Assurance:** All data in transit across public or untrusted networks must enforce TLS 1.3. All persistent data at rest must enforce AES-256 encryption using AWS KMS Customer Managed Keys (CMK) with automated annual rotation.

---

## 3. Governance Roles & Responsibilities

```
+-------------------------------------------------------------+
|              Board Audit Committee & CEO                    |
|      (Executive Oversight, Risk Appetite, Budget Approval)  |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|          Chief Information Security Officer (CISO)          |
|      (ISMS Strategy, Policy Authority, Incident Escalation) |
+------------------------------+------------------------------+
                               |
         +---------------------+---------------------+
         |                                           |
         v                                           v
+-------------------------------+   +-------------------------------+
|     Lead GRC Analyst          |   |  Head of Infrastructure & SRE |
| (Audit, SoA, Risk Register,   |   | (AWS IAM, Encryption, Backups,|
|  Policy Review, TPRM Oversight|   |  VPC Architecture, CI/CD Gate)|
+-------------------------------+   +-------------------------------+
```

---

## 4. Operational Requirements & Enforceable Standards
*   **Access Management:** All access to corporate SaaS and cloud consoles requires Okta Single Sign-On (SSO) backed by phishing-resistant FIDO2 hardware keys (YubiKey). Password-only logins and SMS OTP are blocked at the identity provider layer.
*   **Quarterly Entitlement Recertification:** The Lead GRC Analyst and department managers must conduct quarterly User Access Reviews (UARs) in Jira Service Management. Any orphaned account or unverified permission must be revoked within 5 business days.
*   **Vulnerability Management:** Critical vulnerabilities (CVSS $\ge 9.0$) identified in production dependencies or container base images must be patched or mitigated within **7 calendar days**. High severity (CVSS 7.0–8.9) within **30 calendar days**.
*   **Logging & Audit Trail:** Multi-region AWS CloudTrail, EKS audit logs, and Okta authentication logs must be shipped to Datadog SIEM and archived to immutable S3 Glacier with log-file validation enabled for a minimum retention period of **365 calendar days**.

---

## 5. Exceptions & Policy Violations
*   **Security Exceptions:** Any temporary deviation from this policy requires a formal Jira ticket (`SEC-EXCEPTION`), documented risk assessment, compensating control definition, and written approval by the CISO. Exceptions are granted for a maximum duration of **90 calendar days**.
*   **Enforcement & Disciplinary Action:** Violations of this policy are subject to disciplinary action up to and including immediate termination of employment, revocation of access credentials, and contractual termination of vendor agreements, alongside potential civil or criminal litigation where applicable by law.
