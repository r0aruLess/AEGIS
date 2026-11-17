# Vendor Management Policy (POL-004)
**Document Owner:** Head of Procurement & GRC Lead  
**Approved By:** CFO & CISO  
**Version:** 2.0  
**Effective Date:** February 1, 2026  
**ISO/IEC 27001:2022 Mapping:** Control A.5.19, A.5.20, A.5.21, A.5.22

---

## 1. Overview & Vendor Tiering
All external vendors and cloud service providers handling CloudScale confidential data or supporting critical business processes must be evaluated prior to contracting.

### Vendor Classification:
- **Tier 1 (Critical):** Hosts customer data, production infrastructure, or core identity (e.g., AWS, Okta, Datadog).  
  *Requirements:* Annual SOC 2 Type II / ISO 27001 audit report, signed DPA with Standard Contractual Clauses (SCCs), SIG Full/Lite questionnaire, penetration test summary.
- **Tier 2 (Significant):** Internal operational SaaS holding business or employee confidential data (e.g., BambooHR, Slack, HubSpot).  
  *Requirements:* Bi-annual SOC 2 or SIG Lite review, signed security terms.
- **Tier 3 (Low):** Commodity tools with no access to sensitive information (e.g., Figma design licenses, office supplies).  
  *Requirements:* Standard terms of service security review.

## 2. Onboarding Lifecycle
1. **Intake & Scope:** Business sponsor submits procurement request detailing data types processed.
2. **Security & Privacy Due Diligence:** GRC analyst scores vendor against the Vendor Scoring Criteria.
3. **Contract Negotiation:** Legal ensures inclusion of right-to-audit, 24-hour breach notification, and data return/destruction upon termination.
4. **Approval Gate:** CISO sign-off required for Tier 1 and Tier 2 vendors prior to payment.

## 3. Ongoing Review & Offboarding
Tier 1 vendors undergo annual reassessments. Upon contract termination, the vendor must provide formal certification of data sanitization within 30 days.