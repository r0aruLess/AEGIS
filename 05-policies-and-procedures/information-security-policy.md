# Information Security Policy

Policy reference: CS-POL-001  
Standards: ISO/IEC 27001:2022 (Clause 5.2, Controls A.5.1 to A.5.4), SOC 2 (CC1.1, CC1.2, CC2.1)  
Effective date: May 15, 2026 (Version 3.0)  
Owner: CISO  
Approved by: CEO and Board Audit Committee  

---

## 1. Purpose

This policy sets security requirements for all staff, contractors, systems, and client data at CloudSphere Analytics.

---

## 2. Security Principles

1. Zero Trust: Every microservice, laptop, and network connection must authenticate directly. Firewalls alone do not grant trust.
2. Least privilege and separation: Engineers cannot push unreviewed code directly to production. Pull requests require an independent reviewer.
3. Deny by default: Security groups, IAM policies, and cloud firewalls block all inbound traffic unless an explicit rule opens a port.
4. Encryption everywhere: Network traffic uses TLS 1.3. Stored data uses AES-256 with customer-managed KMS keys that rotate annually.

---

## 3. Governance and Roles

```
+-------------------------------------------------------------+
|              Board Audit Committee & CEO                    |
|      (Executive oversight, risk limits, budget approval)    |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|          Chief Information Security Officer (CISO)          |
|      (Security strategy, policy sign-off, escalations)      |
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

## 4. Security Rules

- Single sign-on: Work apps use Okta with hardware YubiKeys or Okta Verify. Password-only and SMS logins are blocked.
- Access reviews: The GRC team and department managers review user accounts in Jira every quarter. Unused accounts are removed within five business days.
- Patching: Critical bugs (CVSS 9.0+) in production containers or packages must be patched within 7 days. High-severity bugs (CVSS 7.0–8.9) must be patched within 30 days.
- Logging: AWS CloudTrail, EKS logs, and Okta events ship to Datadog and archive to S3 Glacier with log validation enabled for 365 days.

---

## 5. Exceptions and Violations

- Exceptions: Any temporary exception requires a Jira ticket (SEC-EXCEPTION), a documented mitigation, and written approval from the CISO. Exceptions expire after 90 days.
- Violations: Deliberate failure to follow this policy may lead to revoking system access, ending employment or contracts, and legal action if warranted.
