# CloudSphere Analytics Inc. • Organizational Profile & Context
**Company Name:** CloudSphere Analytics Inc. ("CloudSphere")  
**Headcount:** 150 Full-Time Equivalents (FTEs)  
**Headquarters:** San Francisco, CA (Hybrid / Remote-First)  
**Industry:** B2B Enterprise Software-as-a-Service (Cloud Analytics)  
**ISMS Scope:** Production Cloud SaaS Infrastructure, Corporate IT, and Remote Workforces  

---

## 1. Executive Summary
CloudSphere Analytics is a high-growth, venture-backed B2B SaaS organization providing predictive behavioral analytics and customer intelligence pipelines to over 350 enterprise clients globally.

Operating in a hybrid remote-first model across North America and Europe, CloudSphere handles high volumes of client business data and telemetry. Maintaining rigorous information security and privacy compliance is essential to satisfy client contractual requirements, pass enterprise vendor security reviews, and achieve certification against **ISO/IEC 27001:2022** and **ISO/IEC 27701:2025**.

---

## 2. Headcount & Departmental Distribution (150 FTEs)
*   **Software Engineering & DevOps (60):** Front-end, back-end, platform infrastructure, and SRE.
*   **Sales, Marketing & Customer Success (45):** Enterprise account management, solutions engineering.
*   **Product Management & UI/UX Design (15):** Feature planning and user research.
*   **Finance, Legal, and HR Operations (20):** Corporate governance, talent acquisition, legal counsel.
*   **Information Security & Compliance (10):** CISO, 2 GRC analysts, 3 SecOps/SOC engineers, 2 application security engineers, 1 Data Protection Officer (DPO), 1 IT operations lead.

---

## 3. Technology Architecture & Cloud Footprint
CloudSphere operates a **100% cloud-native serverless and containerized infrastructure** on Amazon Web Services (AWS):
*   **Compute:** Amazon Elastic Kubernetes Service (EKS) across multi-AZ worker nodes.
*   **Database:** Amazon Aurora PostgreSQL (Multi-AZ with encrypted read replicas).
*   **Object Storage:** Amazon S3 with mandatory KMS customer-managed keys (CMK) and object-lock versioning.
*   **Identity & Access:** Okta Universal Directory with enforced phishing-resistant FIDO2 WebAuthn MFA.
*   **Perimeter & Edge:** Cloudflare Enterprise WAF, DDoS protection, and SSL/TLS 1.3 termination.
*   **Code & CI/CD:** GitHub Enterprise Cloud with enforced branch protection and CodeQL SAST.
*   **Observability:** Datadog SIEM, AWS CloudTrail, and PagerDuty escalation bridges.

---

## 4. Information Classification Scheme
| Tier | Classification Level | Examples | Handling Guidelines |
|---|---|---|---|
| **Tier 1** | **Restricted / Critical** | Customer personal data (PII), database credentials, KMS root keys, corporate financial records. | Strict least-privilege RBAC, AES-256 encryption, DLP monitoring, zero export to local machines. |
| **Tier 2** | **Confidential** | Proprietary source code, system architecture diagrams, internal audit findings, employee records. | Authenticated corporate SSO access only, NDAs enforced, private GitHub repositories. |
| **Tier 3** | **Internal Use** | Internal Slack communications, general corporate policies, company all-hands recordings. | Available to all authenticated full-time employees and screened contractors. |
| **Tier 4** | **Public** | Marketing website, published documentation, public whitepapers, press releases. | No access restrictions; public dissemination approved by marketing. |
