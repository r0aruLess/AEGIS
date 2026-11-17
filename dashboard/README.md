# AEGIS GRC Interactive Dashboard Console

## Overview
The AEGIS GRC Dashboard is a responsive, web-based compliance visualization and management console. It visualizes data directly from:
- **`03-risk-management/`**: Live Inherent vs. Residual risk heatmaps, risk register metrics, and treatment progress.
- **`04-statement-of-applicability/`**: ISO/IEC 27001:2022 Annex A control implementation status across all 93 controls (4 themes).
- **`ml_engine/` & `analyzer/`**: Machine Learning classification metrics, spreadsheet analysis results, and automated gap detections.

## Features
1. **Executive KPI Cards:** ISO 27001 readiness percentage, high-risk counts, control pass rates, and active remediation actions.
2. **Interactive Risk Heatmap:** 5x5 Likelihood $\times$ Impact matrix plotting inherent risks against residual post-treatment states.
3. **Annex A Control Explorer:** Filter and inspect controls across Organizational (37), People (8), Physical (14), and Technological (34) themes.
4. **Spreadsheet Analyzer UI:** Upload CSV audit spreadsheets to receive automated risk scores, control gap flags, and tailored remediation playbooks.

## Running the Dashboard
The dashboard connects seamlessly to the Python backend server:
```powershell
uv run python backend/server.py
```
Open `http://127.0.0.1:8000/dashboard/` or open `dashboard/index.html` directly in any modern web browser.