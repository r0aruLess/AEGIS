# Methodology and Assumptions Guide

## 1. Governance & Risk Framework Alignment
CloudScale's Information Security Management System (ISMS) is engineered in strict accordance with:
- **ISO/IEC 27001:2022:** Requirements (Clauses 4-10) and Annex A Controls (93 controls organized under Organizational, People, Physical, Technological).
- **ISO/IEC 27701:2025:** Published October 14, 2025, restructuring PIMS from an extension into a standalone management system.
- **NIST SP 800-30 Rev 1:** Guide for Conducting Risk Assessments.
- **AICPA SOC 2 Type II:** Trust Services Criteria (Security, Availability, Confidentiality).

## 2. Inherent vs. Residual Risk Calculation
- **Inherent Risk:**
  $$\text{Inherent Risk} = L_{\text{inherent}} \times I_{\text{inherent}}$$
  Evaluates likelihood and impact assuming no controls are in place or that existing controls have completely failed.
- **Control Gap Determination:**
  - *Major Gap:* Control is missing, disabled, or unconfigured. (Effectiveness $E = 0.00$)
  - *Partial Gap:* Control is implemented inconsistently, manual, or lacking testing. ($E = 0.35$)
  - *Verified:* Control is fully configured, tested, and validated by evidence. ($E = 0.75$)
- **Residual Risk:**
  $$\text{Residual Risk} = \text{Round}\Big(\text{Inherent Risk} \times (1 - E_{\text{control}})\Big)$$

## 3. Assumptions
- CloudScale operates as a cloud-native SaaS vendor hosted on AWS. Physical data center controls (A.7.1, A.7.2, A.7.4) are inherited from AWS's certified SOC 2 and ISO 27001 accreditations.
- Workforce is 100% remote/hybrid, prioritizing cloud identity (Okta), endpoint MDM, and automated CI/CD security scanning.