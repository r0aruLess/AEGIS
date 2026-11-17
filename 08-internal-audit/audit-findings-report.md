# Internal Audit Findings Report (FY 2026)
**Audit Identification:** IA-ISO27001-2026-Q1  
**Entity:** CloudScale Technologies Inc.  
**Lead Auditor:** Independent GRC Auditor  
**Audit Conclusion Date:** February 28, 2026

---

## 1. Executive Summary & Audit Opinion
Based on the sampling of controls across CloudScale's ISMS, the internal audit concludes that the management system is **substantially conforming** to ISO/IEC 27001:2022 requirements. 

No Major Non-Conformities were detected. Two (2) Minor Non-Conformities and one (1) Opportunity for Improvement (OFI) were identified. All identified non-conformities have established management action plans and are tracked in the CAPA register.

---

## 2. Detailed Findings Matrix

### Finding IA-2026-01: Container Vulnerability Patching SLA Breach
- **Classification:** Minor Non-Conformity
- **ISO 27001:2022 Clause:** Control A.8.8 (Management of technical vulnerabilities)
- **Condition:** Inspection of production ECR registries revealed 2 container base images harboring Critical CVEs exceeding the 14-day remediation SLA (observed age: 22 days).
- **Root Cause:** CI/CD build pipelines currently warn on Critical CVEs but do not break the build on pre-release branches.
- **Corrective Action Plan (CAPA):** Configure GitHub Actions Trivy scanner with `--exit-code 1` on severity `CRITICAL`.
- **Target Closure Date:** March 31, 2026. Owner: Lead DevOps Engineer.

### Finding IA-2026-02: Missing Annual SOC 2 Report for Tier-2 Vendor
- **Classification:** Minor Non-Conformity
- **ISO 27001:2022 Clause:** Control A.5.19 (Information security in supplier relationships)
- **Condition:** One SaaS vendor (LeadFlow) had an expired SOC 2 Type II report on file without documented evidence of annual request.
- **Root Cause:** Vendor review reminders were manually tracked on spreadsheets without automated alerting.
- **Corrective Action Plan (CAPA):** Deploy automated 60-day vendor contract renewal audit alerts in the GRC vendor dashboard.
- **Target Closure Date:** April 15, 2026. Owner: GRC Analyst.