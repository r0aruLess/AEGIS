# Third-Party Vendor Risk Scoring & Tiering Methodology
**Standard:** CloudScale TPRM Framework (aligned with ISO 27001:2022 A.5.19 & NIST SP 800-161)  
**Owner:** GRC Lead & Vendor Management Office

---

## 1. Vendor Inherent Risk Tiering
Before security questionnaire evaluation, vendors are assigned an **Inherent Risk Tier** based on their access profile:
- **Tier 1 (Critical):** Cloud hosts storing production customer data, Identity Providers (IdP), source code repositories.
- **Tier 2 (Significant):** SaaS applications storing internal employee data, marketing lists, financial data.
- **Tier 3 (Low):** Non-sensitive productivity tools, hardware vendors, marketing creative agencies.

## 2. Questionnaire Scoring Formula
Vendors are scored across 10 evaluation domains (total 100 possible points):
$$\text{Security Score} = \sum_{i=1}^{n} (\text{Domain Weight} \times \text{Compliance Ratio})$$

### Approval Gates:
- **Score $\ge 85$:** Approved with standard annual review.
- **Score $70 - 84$:** Approved conditionally; requires Corrective Action Plan (CAP) within 60 days.
- **Score $< 70$:** Rejected; requires CISO risk acceptance exception to onboard.