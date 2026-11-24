# CloudSphere Analytics Inc. Annual ISMS and PIMS Internal Audit Plan

**Document Reference:** CS-AUD-PLAN-2026  
**Standards Targeted:** ISO/IEC 27001:2022 (Clause 9.2) & ISO/IEC 27701:2025 (Clause 9.2)  
**Classification:** Internal / Auditor Disclosable  
**Audit Execution Window:** 2026-05-01 through 2026-05-12  
**Lead Auditor:** Lead GRC Analyst | Technical Auditor: Head of Infrastructure & SRE | Sponsor: CISO & Audit Committee

---

## 1. Audit Objectives and Scope

This annual internal audit evaluates the operational effectiveness, design adequacy, and regulatory compliance of CloudSphere's Information Security Management System (ISMS) and Privacy Information Management System (PIMS) before Stage 1 external certification.

### Audit Scope

* All 93 Annex A controls and Clauses 4 through 10 of ISO/IEC 27001:2022.
* Core privacy obligations and Annex A controller/processor requirements of ISO/IEC 27701:2025.
* Technical cloud infrastructure hosted on AWS (`us-east-1` and `eu-central-1`).
* Remote employee laptops and identity services (Okta, Google Workspace, GitHub).

---

## 2. Audit Sampling Strategy and Evidence Methodology

Following ISO 19011:2018 guidelines for auditing management systems:
1. Sampling Size: A defensible sample of 45 of 93 ISO 27001 controls across all 4 themes (Organizational, People, Physical, Technological) and 8 of 10 ISO 27701 clauses.
2. Evidence Inspection Methods:
   * Inquiry and Interview: Structured interviews with 8 control owners across Engineering, People Ops, Legal, and IT.
   * Direct Observation: Live walkthroughs of GitHub pull request branch protection, AWS IAM temporary credential assumption, and Kandji MDM policy enforcement.
   * Inspection of Artifacts: Independent review of 85 cryptographic SHA-256 evidence digests stored in the Aegis GRC Evidence Vault.
   * Re-Performance Testing: Independent re-execution of Trivy container scans and manual inspection of the BambooHR-to-Okta deprovisioning log.
