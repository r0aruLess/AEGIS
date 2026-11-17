# Aegis GRC • Entry-Level GRC Analyst Interview Defense Guide
**Target Roles:** Associate GRC Analyst, Information Security Analyst, Compliance Specialist, IT Auditor  
**Purpose:** Word-for-word talking points, conceptual explanations, and direct answers mapped to this repository.

---

## 🧭 The Golden Rule for Freshers in GRC Interviews

> **"Code is your differentiator, not your identity."**  
> GRC hiring managers are looking for someone who understands **risk, frameworks, evidence, and audit language**. When you speak, lead with the **governance reason** first, and mention the code second as your practical implementation.

---

## 🎯 Top 20 Interview Questions & Model Answers

### Category 1: Frameworks & Standards Mastery

#### Q1: "What are the major differences between ISO/IEC 27001:2013 and ISO/IEC 27001:2022?"
*   **Model Answer:**
    > *"The 2013 edition had 114 controls spread across 14 distinct domains (A.5 through A.18). The 2022 edition streamlined Annex A into **4 themes totaling 93 controls**:
    > 1. **A.5 Organizational Controls (37)**
    > 2. **A.6 People Controls (8)**
    > 3. **A.7 Physical Controls (14)**
    > 4. **A.8 Technological Controls (34)**
    >
    > Furthermore, the 2022 edition introduced 11 brand-new controls that reflect modern cloud architectures—such as **A.5.7 Threat Intelligence**, **A.5.23 Information security for use of cloud services**, **A.8.9 Configuration management**, **A.8.10 Information deletion**, **A.8.12 Data leakage prevention**, and **A.8.28 Secure coding**. In my Aegis GRC project, I implemented all 93 controls using the 2022 theme structure in `controls/iso27001_2022.json`."*

#### Q2: "Can you certify under ISO/IEC 27701 without having ISO 27001?"
*   **Model Answer:**
    > *"Historically under the 2019 edition, ISO 27701 was strictly an extension that could not stand alone. However, on **14 October 2025, ISO/IEC 27701:2025 was republished as a standalone Management System Standard (MSS)**.
    >
    > Under the 2025 edition, it has its own independent management clauses 4 through 10 following the ISO Harmonized Structure, and its own decoupled privacy risk assessment focusing on harm to PII Principals (data subjects) rather than just corporate asset loss. Existing 2019 certificates remain valid during a 3-year transition period until October 2028."*

#### Q3: "What is a Statement of Applicability (SoA) and why is it important?"
*   **Model Answer:**
    > *"The Statement of Applicability (mandated by ISO 27001 Clause 6.1.3 d) is the definitive master document an auditor reviews on Day 1. It lists all 93 Annex A controls and records:
    > 1. Whether the control is **Included or Excluded** from the organizational scope.
    > 2. The **defensible justification** for the decision.
    > 3. Its implementation status and primary evidence source.
    >
    > For example, if a SaaS company hosts 100% of its workloads on AWS and has no physical data centers, they don't simply ignore physical server controls like A.7.5. Instead, in their SoA, they justify inclusion via the **Cloud Shared Responsibility Model**, citing AWS's accredited third-party SOC 2 Type II and ISO 27001 certification reports."*

---

### Category 2: Risk Assessment & Methodology

#### Q4: "How do you distinguish Inherent Risk from Residual Risk?"
*   **Model Answer:**
    > *"**Inherent Risk** is the raw threat exposure that exists in the absence of any security controls (e.g. unencrypted customer database credentials exposed over the internet).
    >
    > **Residual Risk** is the threat level that remains after security controls are implemented and verified. In our project's 5×5 risk engine, a verified, automated control has an effectiveness rating ($E = 0.75$), reducing an inherent score of 20 (Critical) down to a residual score of 6 (Medium). Importantly, residual risk can never be absolute zero because no security control is 100% infallible."*

#### Q5: "What are the four standard Risk Treatment options?"
*   **Model Answer:**
    > *"Under ISO 31000 and ISO 27001 Clause 6.1.3, the four treatment strategies are:
    > 1. **Mitigate:** Deploy technological or procedural controls to reduce likelihood or impact (e.g. implementing MFA for A.8.5).
    > 2. **Transfer:** Offload financial exposure to a third party (e.g. purchasing cyber liability insurance or enforcing vendor indemnification clauses).
    > 3. **Avoid:** Discontinue the risky process or retire the vulnerable software.
    > 4. **Accept:** Executive sign-off (CISO/CEO) for residual risks within organizational appetite."*

#### Q6: "Why did you include a FAIR Monte Carlo simulation alongside a 5×5 heatmap?"
*   **Model Answer:**
    > *"Traditional 5×5 heatmaps are great for operational triage, but academically they suffer from ordinal scale ambiguity—what one person calls 'Medium Impact,' another calls 'High.'
    >
    > The **FAIR (Factor Analysis of Information Risk)** model provides empirical quantitative rigor. Using a 10,000-iteration Monte Carlo simulation with Beta-PERT and lognormal distributions, it calculates **Annualized Loss Expectancy (Mean ALE)** and **90% Value-at-Risk (VaR)** in dollars. This enables executive leadership to perform cost-benefit analysis—for example, deciding whether spending $50,000 on an EDR tool is justified against a $739,000 expected annual loss."*

---

### Category 3: Auditing & Audit Findings

#### Q7: "What is the difference between a Major Non-Conformity, a Minor Non-Conformity, and an OFI?"
*   **Model Answer:**
    > *"1. **Major Non-Conformity (MNC):** A systemic breakdown or complete absence of a mandatory requirement (e.g. zero management review meetings conducted, or complete lack of an access control policy). An MNC blocks ISO 27001 certification.
    > 2. **Minor Non-Conformity (mNC):** An isolated failure that does not undermine the whole system (e.g. an annual backup restoration drill timed out, or 3 stale contractor keys were not rotated). It does not block certification, but requires a Corrective Action Plan (CAP) with a 30-to-90-day SLA.
    > 3. **Opportunity for Improvement (OFI):** Auditor advice on best practice enhancements that do not require formal remediation."*

#### Q8: "How would you handle an audit finding assigned to you?"
*   **Model Answer:**
    > *"I follow the formal 4-step remediation lifecycle:
    > 1. **Acknowledge and Contain:** Verify the finding against the standard and contain immediate risk.
    > 2. **Root Cause Analysis (RCA):** Use the '5 Whys' method to determine why the failure occurred (e.g. did a script fail due to a network ACL change?).
    > 3. **Draft Corrective Action Plan (CAP):** Specify corrective steps, assigned owner, and target completion date.
    > 4. **Evidence Collection & Re-test:** Re-run the automated check or produce an updated artifact, compute its SHA-256 hash, and present verified evidence to the auditor to close the finding."*

---

### Category 4: GRC Engineering & Continuous Assurance

#### Q9: "What does 'Shift-Left GRC' mean?"
*   **Model Answer:**
    > *"Shift-Left GRC means integrating compliance policy checks directly into developer IDEs and CI/CD pipelines *before* infrastructure or code ever deploys to production.
    >
    > In Aegis GRC, we created a Terraform static scanner in `checks/terraform_check.py`. When a developer writes Terraform code, our scanner checks for open security groups (`0.0.0.0/0` on port 5432) or unencrypted S3 buckets, mapping the failure to Controls **A.8.20** and **A.8.24** before `terraform apply` is ever run."*

#### Q10: "How do you ensure audit evidence cannot be tampered with?"
*   **Model Answer:**
    > *"In our project, every automated check generates a timestamped JSON artifact stored in `evidence/`. We compute a **SHA-256 cryptographic hash** of the raw telemetry.
    >
    > Furthermore, our SQLite database maintains an **immutable audit ledger** where each event's hash incorporates the hash of the preceding entry (`prev_hash`), creating a cryptographic hash chain. If an unauthorized party modifies a historical row, the hash chain breaks, proving evidence tampering."*

---

### Category 5: Privacy & AI Governance (2026 Trends)

#### Q11: "What is a RoPA and what is a DSAR?"
*   **Model Answer:**
    > *"A **Record of Processing Activities (RoPA)** is mandated by GDPR Article 30 and India's DPDP Act 2023. It inventories all personal data processing activities, specifying the lawful basis (e.g. Contract, Consent, Legitimate Interest), data categories, retention timelines, and cross-border transfer mechanisms.
    >
    > A **Data Subject Access Request (DSAR)** is when an individual exercises their rights under privacy law (e.g. Right to Access Art. 15, Right to Erasure Art. 17). Organizations have a strict **30-day statutory SLA** to fulfill DSAR requests, which we track with live countdown badges in the Aegis Privacy Hub."*

#### Q12: "How does the EU AI Act categorize artificial intelligence risk?"
*   **Model Answer:**
    > *"The EU AI Act establishes four risk tiers:
    > 1. **Prohibited:** Unacceptable risk (social scoring, biometric behavioral manipulation) — strictly banned.
    > 2. **High Risk (Annex III):** Critical infrastructure, CV resume parsers, recruitment scoring, access decisions. Requires fundamental rights impact assessments, human-in-the-loop oversight, and strict data quality audits.
    > 3. **Specific Transparency / Limited Risk:** Chatbots and generative text systems — requires explicit disclosure to users that they are interacting with AI.
    > 4. **Minimal Risk:** Spam filters and IDE syntax tools."*

---

## 💡 Quick Tips for the Interview

1. **Keep `index.html` open on your screen during virtual interviews:**
   If asked to present a project, share your screen and give a 2-minute tour:
   * *Show the ISO 27001:2022 4-theme controls table.*
   * *Show the Statement of Applicability with justifications.*
   * *Show the 5×5 risk matrix and the FAIR Monte Carlo simulation.*
   * *Show the Audit Findings & CAP Tracker.*
2. **Mention you maintain an automated test suite:**
   *"We have 12 automated unit tests in `tests/` verifying our 93-control schema, 5×5 risk math, and cryptographic hash chaining."* This immediately proves attention to detail.
