# ISMS and PIMS Scope Statement

Document reference: CS-ISMS-SCOPE-001  
Standards: ISO/IEC 27001:2022 (Clause 4.3), ISO/IEC 27701:2025 (Clause 4.3)  
Effective date: May 15, 2026 (Version 3.0)  
Approved by: CISO and CEO  

---

## 1. Scope Boundaries

This management system covers the infrastructure, staff, and workflows that deliver CloudSphere's analytics platform.

### Included Systems and Assets
1. Production cloud workloads: AWS accounts in us-east-1 and eu-central-1, covering EKS clusters, Aurora databases, S3 storage, and KMS key management.
2. Corporate identity and tooling: Okta, Google Workspace, GitHub Enterprise, and Datadog.
3. Personnel and endpoints: All 150 staff members and contract personnel using company-issued MacBooks managed by Kandji MDM, FileVault encryption, and CrowdStrike EDR.

### Physical Exclusions and Justification
CloudSphere has no physical offices or data centers.

Physical perimeter security, building entry access, utility lines, cabling, and hardware destruction (ISO 27001 controls A.7.11, A.7.12, A.7.13, and A.7.14) fall under the AWS Shared Responsibility Model. CloudSphere reviews AWS SOC 2 Type II reports and ISO 27001 certificates each year to confirm physical safeguards remain effective.

---

## 2. Privacy Roles under ISO 27701:2025

- PII Processor: CloudSphere processes user clickstream events, device telemetry, and account identifiers on behalf of business clients using the CloudSphere SDK.
- PII Controller: CloudSphere acts as a controller for internal employee records, candidate files, billing details, and sales contacts.
