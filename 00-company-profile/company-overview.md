# CloudSphere Analytics: Company Overview and Context

CloudSphere Analytics Inc.
Headcount: 150 employees
Corporate registration: Delaware C-Corp, headquartered in San Francisco, CA
Model: Fully remote workforce
Product: B2B SaaS for event telemetry and customer analytics
In-scope systems: AWS production environments (us-east-1 and eu-central-1), corporate IT, and remote staff endpoints
Certifications targeted: ISO/IEC 27001:2022, ISO/IEC 27701:2025, and SOC 2 Type II

---

## 1. Business Operations

CloudSphere sells customer analytics pipelines and churn predictions to roughly 350 business clients worldwide.

The company has no physical offices or data centers. All customer traffic, processing pipelines, and code repositories run on Amazon Web Services. Because CloudSphere handles customer telemetry and account data across multiple jurisdictions, the security and privacy program supports contract requirements and statutory rules including the EU GDPR, the California CPRA, and India's DPDP Act.

---

## 2. Organization and Headcount

CloudSphere employs 150 full-time staff across seven main groups:

```
CloudSphere Analytics Inc. (150 FTEs)
├── Executive Leadership (5): CEO, CISO, CTO, VP Sales, General Counsel
├── Software Engineering (48): Front-end, back-end, platform
├── Infrastructure and SRE (12): Cloud operations, platform reliability, database admins
├── Sales, Marketing, and Customer Support (45): Enterprise accounts, solutions, support
├── Product and Design (15): Product managers, UI/UX designers
├── Finance, HR, and Operations (15): Accounting, recruiting, HR
└── Security, Compliance, and IT (10):
    ├── Chief Information Security Officer (CISO)
    ├── Lead GRC Analyst
    ├── Associate GRC Analyst
    ├── SecOps Lead
    ├── Security Operations Engineer
    ├── DevSecOps Engineer
    ├── Application Security Engineer
    ├── Data Protection Officer (DPO)
    ├── Head of Infrastructure and SRE
    └── IT Operations Lead
```

Security and privacy controls belong to the 10 members of the Security, Compliance, and IT team, with support from Legal and HR. The company does not maintain specialized enterprise roles such as a dedicated facilities manager or forensic director.

---

## 3. Infrastructure Overview

Production workloads run across two AWS regions: us-east-1 for primary traffic and eu-central-1 for European data residency.

- Compute: Amazon EKS on Graviton worker nodes.
- Database: Amazon Aurora PostgreSQL with multi-AZ failover and daily encrypted snapshots.
- Storage: Amazon S3 with customer-managed KMS keys, Object Lock, and 30-day lifecycle deletion rules.
- Identity: Okta with FIDO2 WebAuthn keys (YubiKeys) or Okta Verify. SMS and voice authentication are turned off.
- Edge: Cloudflare Enterprise for WAF filtering, DDoS mitigation, and TLS 1.3 termination.
- CI/CD: GitHub Enterprise Cloud with mandatory two-person code reviews, signed commits, and CodeQL security scans.
- Monitoring: Datadog SIEM, AWS CloudTrail, and Rapid7 MDR for overnight tier-1 triage.

---

## 4. Data Classification

| Level | Description and Examples | Storage and Handling | Systems Used |
|---|---|---|---|
| Tier 1: Restricted | Customer personal data, database credentials, KMS root keys, corporate financial records. | Encrypted with AES-256 KMS, least-privilege IAM, no local downloads, DLP tracking. | Aurora PostgreSQL, AWS Secrets Manager, Okta. |
| Tier 2: Confidential | Source code, sales contracts, vulnerability reports, infrastructure plans. | Corporate SSO required, signed NDA, private repositories. | GitHub Enterprise, Google Workspace, Jira. |
| Tier 3: Internal | Sprint tickets, Slack channels, internal guides. | Google Workspace account required, automatic screen lock enforced. | Slack Enterprise, Notion, Google Drive. |
| Tier 4: Public | Blog posts, public documentation, API documentation. | Reviewed by product marketing before publishing. | Public website via Cloudflare. |
