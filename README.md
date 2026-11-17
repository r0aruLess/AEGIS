# Aegis GRC

An automated security compliance platform that turns messy audit findings into clear ISO 27001 controls and defensible risk scores.

**Status:** 12/12 Tests Passing | **Python:** 3.12+ | **Accuracy:** 84% (LinearSVC) | **License:** MIT

---

## What is Aegis GRC?

In most companies, **Governance, Risk, and Compliance (GRC)** is managed through manual, disconnected spreadsheets once a year. When security scanners find hundreds of vulnerabilities (like CVEs or cloud misconfigurations), compliance analysts have to spend weeks manually sorting through them, guessing their risk level, and trying to match them to compliance checklists (like ISO 27001 or SOC 2).

**Aegis GRC automates this workflow:**

1. **AI Classification (84% Accuracy):** Ingests raw findings and maps them to ISO 27001 Annex A controls (e.g. `A.8.28 Secure Coding`) using a local scikit-learn NLP model.
2. **Defensible Risk Math:** Eliminates guesswork with transparent formulas:
   * `Inherent Risk = Likelihood (1–5) × Impact (1–5)`
   * `Control Gap Evaluation` (Major Gap, Partial Gap, or Verified)
   * `Residual Risk` dampened mathematically by verified control effectiveness.
3. **Continuous Assurance:** Automated scanners inspect repository code, Terraform IaC, and database integrity, logging **SHA-256 evidence digests** into an immutable audit trail.
4. **100% Local & Offline:** Requires **zero external API keys**. No vulnerability data ever leaves your computer.

> **The Reference Scenario:** Because real corporate security audits are strictly confidential under NDA, this project models an authentic 150-person B2B SaaS company (**CloudScale Technologies Inc.**) running on AWS cloud infrastructure.

---

## Quickstart

### 1. Install Dependencies
```bash
# Clone the repository
git clone https://github.com/your-username/aegis-grc.git
cd aegis-grc

# Sync virtual environment (using uv or standard pip)
uv sync
# Or: pip install scikit-learn pandas numpy matplotlib
```

### 2. Run Automated Tests
```bash
uv run python -m unittest discover -s tests
```
*(All 12 unit tests should pass in under 1 second).*

### 3. Start the Web Console
```bash
uv run python backend/server.py
```
Open your browser and navigate to:
```text
http://127.0.0.1:8000/
```

---

## How to Test Spreadsheet Ingestion

1. On the web dashboard, click the **`📥 Ingest & Analyze Spreadsheet`** tab.
2. Click **Choose File** and upload:
   ```text
   data/sample_audit_findings_upload.csv
   ```
   *(Or click **⚡ Load 50 Real Vulnerabilities Demo** to test with 50 real CVE and CIS findings).*
3. The platform will automatically map each finding to an ISO 27001 control, calculate Inherent and Residual risk scores, detect control gaps, and let you export a remediated CSV report.

---

## Automated Security Checks (CLI)

You can also run continuous compliance checks directly from your terminal:

```bash
# 1. Scan codebase for hardcoded secrets, AWS keys, and private keys
uv run python checks/github_check.py

# 2. Audit SQLite database integrity and system TLS 1.2 / 1.3 ciphers
uv run python checks/infrastructure_check.py

# 3. Scan Terraform IaC files for open 0.0.0.0/0 firewall ports
uv run python checks/terraform_check.py
```
*Each scan generates a SHA-256 hashed evidence JSON file in the `evidence/` directory.*

---

## Project Structure

```text
aegis-grc/
├── README.md
├── 00-company-profile/ ... 11-research/    ← Complete GRC portfolio (policies, SoA, audits)
├── analyzer/                               ← Spreadsheet risk & gap calculation engine
├── backend/                                ← Lightweight REST API & SQLite audit logger
├── checks/                                 ← Continuous assurance scanners (GitHub, Terraform, TLS)
├── dashboard/                              ← Interactive web console & UI
├── data/                                   ← Datasets (sample upload & 50 CVE demo)
├── ml_engine/                              ← NLP control classifier (LinearSVC, 84% accuracy)
├── tests/                                  ← Automated test suite (12 unit tests)
├── evidence/                               ← Generated SHA-256 evidence bundles
├── pyproject.toml                          ← Python dependencies
├── .gitignore
└── LICENSE
```

---

## License

Released under the [MIT License](LICENSE).  
*Disclaimer: CloudScale Technologies Inc. is a reference company created for portfolio and educational demonstration purposes.*
imits, subcontracting data, notification of data breaches, records of cross-border transfers).
