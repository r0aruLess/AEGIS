# Data Subject Access Request (DSAR) Procedure (SOP-PRIV-001)
**Owner:** Data Protection Officer (DPO)  
**Effective Date:** January 1, 2026  
**Regulatory Scope:** GDPR (Articles 15-22), CCPA/CPRA, India DPDP Act 2023  
**Standard Response SLA:** Within 30 calendar days

---

## 1. Workflow Lifecycle
1. **Intake & Logging:** Requests received via `privacy@cloudscale.io` or web form are immediately logged into the GRC Privacy Tracker with a unique ID (`DSAR-YYYY-XXXX`).
2. **Identity Verification:** DPO verifies requestor identity via government ID check or signed email authentication from the enterprise customer domain.
3. **Data Discovery & Retrieval:**
   - Database queries run across RDS, DynamoDB, and ClickHouse data lakes.
   - SaaS sub-processors (Okta, Zendesk, Stripe) queried for auxiliary logs.
4. **Redaction & Review:** Legal and DPO review compiled archives to redact proprietary business trade secrets or third-party personal data.
5. **Secure Delivery:** Data is encrypted into a password-protected zip file and delivered via secure cloud link (expires in 7 days).
6. **Closure & Record Retention:** Request audit log is archived for 3 years as proof of regulatory fulfillment.