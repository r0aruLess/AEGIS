# CloudSphere Analytics Inc. Third-Party and Vendor Risk Management Policy

**Policy Reference:** CS-POL-005  
**ISO/IEC 27001:2022 Alignment:** Controls A.5.19, A.5.20, A.5.21, A.5.22, A.5.23  
**SOC 2 Alignment:** Common Criteria CC9.2  
**Classification:** Internal / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Policy Owner:** Lead GRC Analyst | Approved By: CISO & General Counsel

---

## 1. Purpose and Scope

This policy sets mandatory security due diligence, classification tiers, contract terms, and reassessment schedules for all third-party vendors, SaaS tools, and cloud providers CloudSphere Analytics uses.

---

## 2. Vendor Criticality Tiers

| Tier | Criticality Level | Definition and Ingestion Criteria | Mandatory Due Diligence Requirements | Reassessment Cadence |
|---|---|---|---|---|
| **Tier 1** | **Critical Cloud Infrastructure** | Directly hosts, processes, or transmits customer production PII or master analytics datasets (such as AWS, Okta, Datadog). | SOC 2 Type II report (unqualified opinion), ISO 27001 certificate, executed Data Processing Agreement (DPA) with Standard Contractual Clauses (SCCs), completed SIG questionnaire review. | **Annual (every 12 months)** |
| **Tier 2** | **Operational High-Risk** | Stores internal confidential business data, source code, or employee records (such as GitHub, Google Workspace, BambooHR). | SOC 2 Type II or ISO 27001 certificate, vendor security questionnaire, executed NDA and DPA. | **Annual (every 12 months)** |
| **Tier 3** | **Internal Medium-Risk** | Operational productivity and communication tools handling internal data with zero customer PII (such as Slack, Notion, Zoom). | Standard terms of service review, TLS 1.3 encryption verification, privacy policy compliance check. | **Biennial (every 24 months)** |
| **Tier 4** | **Low-Risk Commercial** | Off-the-shelf software, marketing utilities, or open-source libraries with zero access to CloudSphere networks or customer data. | Standard procurement approval; no formal security assessment required. | Upon contract renewal |

---

## 3. Mandatory Procurement Workflow and Approvals

Department heads cannot sign contracts, purchase software, or transmit company data to a vendor without completing the three-gate procurement process:
1. Gate 1 (Security Review): The Associate GRC Analyst issues the CloudSphere SIG Lite Questionnaire or pulls the vendor's SOC 2 Type II report through vendor trust centers. The team scores findings against CloudSphere's 100-point vendor security scoring criteria. The minimum passing score is 75/100.
2. Gate 2 (Legal and Privacy Review): General Counsel reviews vendor terms and executes CloudSphere's standard Data Processing Agreement incorporating cross-border data transfer safeguards.
3. Gate 3 (Final CISO Sign-Off): The CISO approves the vendor in the centralized TPRM Register in Jira (`SEC-VENDOR`). CloudSphere blocks unapproved software at the Okta SSO and corporate credit card procurement gates.

---

## 4. Subprocessor Notification to Customers

Under ISO/IEC 27701:2025 Annex A.4 and GDPR Article 28:
* CloudSphere lists any new subprocessor handling customer telemetry on the public Subprocessor Trust Directory (`trust.cloudsphere.com/subprocessors`).
* The team notifies enterprise customers by email at least 30 calendar days before authorizing the new subprocessor, giving clients a contractual window to review and raise objections.
