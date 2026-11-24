# Risk Assessment Report

Document reference: CS-RISK-REP-2026-Q2  
Standards: ISO/IEC 27001:2022 (Clause 6.1.2), ISO/IEC 27701:2025 (Clause 6.1.2)  
Assessment window: May 1 to May 15, 2026  
Assessed by: Lead GRC Analyst  
Reviewed by: Head of Infrastructure and SRE  
Approved by: CISO  

---

## 1. Overview of Risks

The security and GRC team reviewed CloudSphere's operational assets, AWS infrastructure, employee laptops, and SaaS vendor accounts during the first two weeks of May 2026.

### Summary Metrics
- Total evaluated scenarios: 8
- Inherent risk: 2 Critical (25%), 4 High (50%), 2 Medium (25%), 0 Low
- Residual risk: 0 Critical, 0 High, 7 Medium (88%), 1 Low (12%)
- Posture: Within defined risk appetite. Every risk above appetite has a funded remediation plan due by Q3 2026.

---

## 2. Analysis

### 5×5 Matrix Findings
- Highest inherent risks: RSK-01 (ransomware threat to Aurora database, score 20) and RSK-02 (credential phishing against Okta administrators, score 20).
- Effect of controls: FIDO2 hardware keys and automated multi-AZ Aurora backups reduce both risks to a residual score of 6 (Medium).

### FAIR Quantitative Estimates
To give the board financial loss projections alongside matrix scores, the team ran a 10,000-iteration FAIR Monte Carlo simulation:
- Mean annual loss expectancy (ALE): $124,350 per year
- 10th percentile (low-loss year): $31,200
- 50th percentile (median year): $112,800
- 90% Value-at-Risk (VaR): $287,500 (losses are expected to stay under this level in 9 out of 10 years)

CloudSphere's security budget is $68,500 across EDR, YubiKeys, MDM, and external penetration tests, protecting against the modeled $287,500 90% VaR exposure.

---

## 3. Residual Risk Sign-Off

The CISO reviewed and signed off on all seven Medium residual risks (scores 6 to 8). Tasks are tracked weekly in the Jira SEC-RISK board.
