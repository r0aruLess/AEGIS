# CloudSphere Analytics Inc. • 5×5 Risk Assessment & Treatment Methodology

**Document Reference:** CS-RISK-METH-001  
**Standard Alignment:** ISO/IEC 27001:2022 (Clauses 6.1.2 & 6.1.3), ISO 31000:2018, NIST SP 800-30 Rev 1  
**Classification:** Internal / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Approved By:** Board Audit Committee & Chief Information Security Officer (CISO)

---

## 1. Purpose & Scope
This methodology establishes the formal principles, mathematical scoring algorithms, risk tolerance thresholds, and treatment strategies governing all information security and privacy risk assessments across CloudSphere Analytics Inc.

---

## 2. 5×5 Likelihood & Impact Qualitative Scales

### Likelihood Scale (1 to 5)
| Level | Rating | Annual Frequency Benchmark | Description & Environmental Context |
|---|---|---|---|
| **1** | Rare | Less than once every 5 years (< 20%) | Requires sophisticated nation-state / advanced persistent threat (APT) capabilities. |
| **2** | Unlikely | Once every 2 to 5 years (20% – 50%) | Possible under rare conditions; not observed in CloudSphere's historical telemetry. |
| **3** | Possible | Once every 1 to 2 years (50% – 100%) | Credible threat vector commonly observed across B2B SaaS cloud environments. |
| **4** | Likely | Multiple times per year (1 – 5 times/yr) | Frequent external automated threat activity (e.g., targeted credential phishing, port scanning). |
| **5** | Almost Certain | Monthly or continuous (> 5 times/yr) | Threat actions actively observed against exposed internet endpoints or public APIs. |

### Impact Scale (1 to 5)
| Level | Rating | Financial Impact ($ USD) | Operational & Regulatory Impact |
|---|---|---|---|
| **1** | Insignificant | < $25,000 | Negligible disruption; isolated endpoint re-image; no regulatory notification required. |
| **2** | Minor | $25,000 – $100,000 | Brief non-critical service disruption (< 1 hour); internal containment with zero PII exposure. |
| **3** | Moderate | $100,000 – $500,000 | Production service impairment (< 4 hours); contractual SLA penalty triggered; localized data leak. |
| **4** | Major | $500,000 – $2,000,000 | Significant customer analytics outage (> 12 hours); statutory breach notification (GDPR/DPDP); major enterprise churn. |
| **5** | Catastrophic | > $2,000,000 | Systemic unrecoverable data loss; widespread customer PII exfiltration; regulatory fine > $1M; existential brand damage. |

---

## 3. Mathematical Risk Calculation Engine

### A. Inherent Risk Scoring:
$$\text{Inherent Risk Score} = \text{Likelihood}_{\text{inherent}} \times \text{Impact}_{\text{inherent}}$$
*   **Scale:** 1 to 25.
*   **Critical Risk:** Score 20 to 25 (Immediate executive escalation; CISO containment review within 24 hours).
*   **High Risk:** Score 12 to 19 (Remediation plan required within 30 days).
*   **Medium Risk:** Score 6 to 11 (Remediation plan required within 60 days).
*   **Low Risk:** Score 1 to 5 (Acceptable within standard operational baseline).

### B. Control Effectiveness ($E$):
When mitigating controls are linked from the ISO 27001:2022 Annex A ledger:
*   **Verified / Automated Technical Control (PASSED):** $E = 0.75$ (75% risk mitigation).
*   **Incomplete / Inconsistent / Manual Control (WARNING):** $E = 0.35$ (35% risk mitigation).
*   **Compensating / Inherited Cloud Control (EXEMPT):** $E = 0.50$ (50% risk mitigation).
*   **Missing or Failed Control (FAILED):** $E = 0.00$ (0% risk mitigation).

### C. Defensible Residual Risk Calculation:
To prevent unrealistic, mathematically flawed jumps where a single control reduces catastrophic impact to zero:
$$\text{Residual Likelihood } (L_{\text{res}}) = \max\Big(1, \text{Round}\big(L_{\text{inh}} \times (1 - (E \times 0.65))\big)\Big)$$
$$\text{Residual Impact } (I_{\text{res}}) = \max\Big(1, \text{Round}\big(I_{\text{inh}} \times (1 - (E \times 0.45))\big)\Big)$$
$$\text{Residual Risk Score} = L_{\text{res}} \times I_{\text{res}}$$

> **Methodology Justification:** Technical and procedural controls primarily reduce the **likelihood** of threat exploitation ($E \times 0.65$). However, because the inherent asset value and maximum theoretical data blast radius remain, controls only moderately dampen theoretical **impact** ($E \times 0.45$). This ensures that high-impact threats (e.g., database compromise) maintain a defensible residual footprint rather than being falsely zeroed out.

---

## 4. Risk Treatment Strategies & Acceptance Criteria
Under ISO/IEC 27001:2022 Clause 6.1.3, every identified risk must be assigned one of four formal treatment paths:
1.  **Mitigate:** Implement technical, organizational, or physical safeguards from Annex A to reduce residual score below appetite.
2.  **Transfer:** Purchase commercial cyber liability insurance (current policy: $5M aggregate limit with Chubb) or enforce contractual indemnity clauses with third-party vendors.
3.  **Avoid:** Discontinue the risky technical architecture, terminate high-risk vendor contracts, or purge legacy datasets.
4.  **Accept:** Formal executive sign-off required. Risks with residual score $\le 5$ can be accepted by the Head of Department. Residual scores between 6 and 11 require CISO sign-off. Residual scores $\ge 12$ require CEO and Board Audit Committee written approval.
