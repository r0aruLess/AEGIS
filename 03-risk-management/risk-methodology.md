# 5×5 Risk Assessment and Treatment Methodology

Document reference: CS-RISK-METH-001  
Standards: ISO/IEC 27001:2022 (Clauses 6.1.2 and 6.1.3), ISO 31000:2018, NIST SP 800-30 Rev 1  
Effective date: May 15, 2026 (Version 3.0)  
Approved by: Board Audit Committee and CISO  

---

## 1. Scope

This guide defines how CloudSphere calculates, ranks, and handles security and privacy risks.

---

## 2. Likelihood and Impact Scales

### Likelihood (1 to 5)

| Level | Rating | Annual Probability | Definition |
|---|---|---|---|
| 1 | Rare | Under 20% | Nation-state or advanced targeted capability required. |
| 2 | Unlikely | 20% to 50% | Possible under rare conditions; not seen in company history. |
| 3 | Possible | 50% to 100% | Common vector across B2B cloud software. |
| 4 | Likely | 1 to 5 times per year | Regular automated scanning or targeted credential attempts. |
| 5 | Almost certain | More than 5 times per year | Ongoing attempts against exposed APIs or public endpoints. |

### Impact (1 to 5)

| Level | Rating | Financial Loss | Operational and Regulatory Consequences |
|---|---|---|---|
| 1 | Insignificant | Under $25,000 | Minimal disruption, single laptop reset, no regulatory notice. |
| 2 | Minor | $25,000 to $100,000 | Brief outage under 1 hour, internal handling without data leak. |
| 3 | Moderate | $100,000 to $500,000 | Production downtime under 4 hours, SLA credit owed, limited leak. |
| 4 | Major | $500,000 to $2,000,000 | Major outage over 12 hours, GDPR or DPDP notice required, client loss. |
| 5 | Catastrophic | Over $2,000,000 | Permanent data loss, widespread customer PII exposure, fine over $1M. |

---

## 3. Risk Calculation

### Inherent Risk
$$\text{Inherent Score} = \text{Likelihood} \times \text{Impact}$$

- Critical (20 to 25): CISO review within 24 hours.
- High (12 to 19): Remediation plan due within 30 days.
- Medium (6 to 11): Remediation plan due within 60 days.
- Low (1 to 5): Handled in standard operational workflows.

### Control Effectiveness (E)
- Passed (verified technical control): E = 0.75
- Warning (partial or manual control): E = 0.35
- Exempt (inherited cloud control): E = 0.50
- Failed (missing control): E = 0.00

### Residual Risk
Controls reduce likelihood more than impact because the underlying value of the asset and worst-case blast radius remain the same:

$$\text{Residual Likelihood } (L_{\text{res}}) = \max\Big(1, \text{Round}\big(L_{\text{inh}} \times (1 - (E \times 0.65))\big)\Big)$$
$$\text{Residual Impact } (I_{\text{res}}) = \max\Big(1, \text{Round}\big(I_{\text{inh}} \times (1 - (E \times 0.45))\big)\Big)$$
$$\text{Residual Score} = L_{\text{res}} \times I_{\text{res}}$$

---

## 4. Risk Treatment

Every logged risk receives one of four paths:
1. Mitigate: Add technical or administrative safeguards from Annex A.
2. Transfer: Cover with insurance ($5M policy with Chubb) or vendor indemnification.
3. Avoid: Retire the vulnerable system or discontinue the workflow.
4. Accept: Requires sign-off based on score. Department heads can accept scores up to 5. Scores between 6 and 11 require CISO sign-off. Scores of 12 or higher require written approval from the CEO and the Board Audit Committee.
