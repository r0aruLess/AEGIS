# CloudSphere Analytics Inc. • Third-Party & Vendor Risk Management (TPRM) Policy

**Policy Reference:** CS-POL-005  
**ISO/IEC 27001:2022 Alignment:** Controls A.5.19, A.5.20, A.5.21, A.5.22, A.5.23  
**SOC 2 Alignment:** Common Criteria CC9.2  
**Classification:** Internal / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Policy Owner:** Lead GRC Analyst | Approved By: CISO & General Counsel

---

## 1. Purpose & Supplier Risk Framework
This policy defines the mandatory security due diligence, risk classification tiers, contractual safeguards, and recurring reassessment cycles required for all third-party vendors, SaaS tools, and cloud providers utilized by CloudSphere Analytics Inc.

---

## 2. Vendor Criticality Tiers

| Tier | Criticality Level | Definition & Ingestion Criteria | Mandatory Due Diligence Requirements | Reassessment Cadence |
|---|---|---|---|---|
| **Tier 1** | **Critical Cloud Infrastructure** | Directly hosts, processes, or transmits customer production PII or master analytics datasets. (e.g., AWS, Okta, Datadog). | SOC 2 Type II Report (unqualified opinion), ISO 27001 cert, executed Data Processing Agreement (DPA) with Standard Contractual Clauses (SCCs), full SIG Core/Lite questionnaire review. | **Annual (every 12 months)** |
| **Tier 2** | **Operational High-Risk** | Stores internal confidential business data, source code, or employee records. (e.g., GitHub, Google Workspace, BambooHR). | SOC 2 Type II or ISO 27001 certificate, vendor security questionnaire, executed NDA and DPA. | **Annual (every 12 months)** |
| **Tier 3** | **Internal Medium-Risk** | Operational productivity and communication tools handling internal data with zero customer PII. (e.g., Slack, Notion, Zoom). | Standard terms of service review, TLS 1.3 encryption verification, privacy policy compliance check. | **Biennial (every 24 months)** |
| **Tier 4** | **Low-Risk Commercial** | Off-the-shelf software, marketing utilities, or open-source libraries with zero access to CloudSphere networks or data. | Standard procurement approval; no formal security assessment required. | Upon contract renewal |

---

## 3. Mandatory Procurement Workflow & Approvals
No department head may enter into a contract, purchase software, or transmit company data to a vendor without completing the **Three-Gate Procurement Process**:
1.  **Gate 1 (Security Review):** Associate GRC Analyst sends the CloudSphere SIG Lite Questionnaire (or obtains the vendor's SOC 2 Type II report via vendor trust centers). Findings scored against CloudSphere's 100-point vendor security scoring criteria. Minimum passing score: **75/100**.
2.  **Gate 2 (Legal & Privacy Review):** General Counsel reviews vendor terms and executes CloudSphere's standardized Data Processing Agreement (DPA) incorporating cross-border data transfer safeguards (SCCs).
3.  **Gate 3 (Final CISO Sign-Off):** CISO approves the vendor in the centralized TPRM Register in Jira (`SEC-VENDOR`). Unvetted software is blocked at the Okta SSO and corporate credit card procurement gates.

---

## 4. Subprocessor Notification to Customers
Under ISO/IEC 27701:2025 Annex A.4 and GDPR Article 28:
*   Any new subprocessor engaged by CloudSphere that processes customer telemetry must be updated on CloudSphere's public Subprocessor Trust Directory (`trust.cloudsphere.com/subprocessors`).
*   Enterprise customers must be notified via automated email **at least 30 calendar days prior** to the authorization of the new subprocessor, providing contractual opportunity to object.
