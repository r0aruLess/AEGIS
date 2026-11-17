# CloudSphere Analytics Inc. • 5×5 Risk Assessment & Treatment Methodology
**Document Reference:** CS-RISK-METH-001  
**Standard Alignment:** ISO/IEC 27001:2022 (Clause 6.1.2 & 6.1.3), ISO 31000:2018  
**Approved By:** Board Audit Committee & CISO  

---

## 1. 5×5 Likelihood & Impact Scales

### Likelihood Scale (1 to 5)
*   **1 - Rare (< 5% annual probability):** Requires extraordinary nation-state capabilities or extreme conditions.
*   **2 - Unlikely (5% - 20% annual probability):** Not observed in our environment; possible under unusual circumstances.
*   **3 - Possible (21% - 50% annual probability):** Common threat vector (e.g. routine credential stuffing, automated scanning).
*   **4 - Likely (51% - 80% annual probability):** High frequency event observed in peer SaaS companies; repeat alerts.
*   **5 - Almost Certain (> 80% annual probability):** Imminent threat or active configuration vulnerability present.

### Impact Scale (1 to 5)
*   **1 - Negligible (< $10k loss):** Minor staff disruption; zero customer outage or data loss.
*   **2 - Minor ($10k - $50k loss):** Brief service degradation (< 15 mins); isolated non-sensitive internal incident.
*   **3 - Moderate ($50k - $250k loss):** Customer SLA credit breach; minor regulatory notice; non-sensitive data leak.
*   **4 - Major ($250k - $1M loss):** Customer PII compromised; mandatory regulatory reporting (GDPR/DPDP); prolonged outage.
*   **5 - Catastrophic (> $1M loss):** Loss of core database; existential reputational harm; civil liability or license revocation.

---

## 2. Inherent Risk vs. Residual Risk Formula

$$\text{Inherent Risk Score} = \text{Likelihood} \times \text{Impact} \quad (1 \le \text{Score} \le 25)$$

*   **Critical Risk (20 - 25):** Red zone. Immediate executive escalation; remediation required within 48 hours.
*   **High Risk (12 - 19):** Orange zone. Remediation SLA of 14 days.
*   **Medium Risk (6 - 11):** Yellow zone. Monitored risk; scheduled into regular sprint cycles.
*   **Low Risk (1 - 5):** Green zone. Acceptable within organizational risk tolerance.

$$\text{Residual Risk} = \text{Likelihood}_{residual} \times \text{Impact}_{residual}$$
Where controls reduce likelihood and impact proportionally to their verified implementation status ($E = 75\%$ for PASSED, $E = 35\%$ for WARNING, $E = 0\%$ for FAILED).
