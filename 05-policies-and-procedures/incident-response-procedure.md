# Incident Response Procedure (SOP-003)
**Document Owner:** Incident Commander / Lead SecOps  
**Approved By:** CISO  
**Version:** 2.5  
**Effective Date:** January 15, 2026  
**ISO/IEC 27001:2022 Mapping:** Control A.5.24, A.5.25, A.5.26, A.5.28

---

## 1. Purpose & Incident Phases
This Standard Operating Procedure establishes the protocol for managing information security and privacy incidents following the NIST SP 800-61 / ISO 27035 lifecycle:

```
[Preparation] -> [Detection & Analysis] -> [Containment] -> [Eradication] -> [Recovery] -> [Post-Incident Review]
```

## 2. Incident Classification & Severity Matrix
- **SEV-1 (Critical):** Confirmed active customer data breach, ransomware, or full production outage.  
  *Response SLA:* 15 minutes. *Notification:* C-Suite immediately, Regulators within 72 hours.
- **SEV-2 (High):** Integrity compromise of production microservice, compromised admin credential without confirmed exfiltration.  
  *Response SLA:* 30 minutes.
- **SEV-3 (Medium):** Localized malware on single non-critical endpoint, failed exploit attempt against API.  
  *Response SLA:* 2 hours.
- **SEV-4 (Low):** Phishing email reported by employee, minor policy infraction.  
  *Response SLA:* 24 hours.

## 3. Communication & Regulatory Escalation
- **Customer Notification:** As stipulated in Customer Data Processing Agreements (DPA), affected enterprise customers will be notified within 24 to 48 hours of confirmed breach verification.
- **Regulatory Reporting:** GDPR Art. 33 and India DPDP Act compliance mandates lead supervisory authority notification within **72 hours** of becoming aware of personal data breach.
- **Internal Comms:** Managed exclusively by Legal and Corporate Comms; technical responders are prohibited from public commentary.

## 4. Post-Incident Review (Lessons Learned)
Within 5 business days of incident resolution, the Incident Commander must conduct a blameless post-mortem, document root causes, and enter corrective actions into the CAPA Tracker.