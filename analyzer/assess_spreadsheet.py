"""
Aegis GRC - Automated Spreadsheet Risk & Gap Analyzer
Loads an Excel or CSV file of raw IT audit findings or vulnerabilities, predicts the ISO 27001:2022
Annex A control, calculates Inherent Risk, flags Control Gaps, computes Residual Risk, and outputs
actionable fix recommendations tailored to each finding.
"""
import os
import sys
import csv
import json
from pathlib import Path

# Add project root to sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from ml_engine.train_model import get_trained_classifier, RECOMMENDATIONS_PLAYBOOK

CONTROL_TITLES = {
    "A.8.5": "Secure authentication",
    "A.8.24": "Use of cryptography",
    "A.8.13": "Information backup",
    "A.8.20": "Networks security",
    "A.8.4": "Access to source code",
    "A.8.1": "User endpoint devices",
    "A.5.18": "Access rights",
    "A.5.19": "Information security in supplier relationships",
    "A.8.28": "Secure coding",
    "A.6.1": "Screening",
    "A.6.3": "Information security awareness education and training",
    "A.6.7": "Remote working",
    "A.8.9": "Configuration management",
    "A.8.11": "Data masking",
    "A.8.12": "Data leakage prevention",
    "A.8.15": "Logging",
    "A.8.16": "Monitoring activities",
    "A.5.7": "Threat intelligence",
    "A.5.23": "Information security for use of cloud services",
    "A.5.29": "Information security during disruption"
}

def calculate_risk_and_gaps(finding_text, likelihood, impact, control_status, model=None):
    """
    Core GRC Calculation Engine:
    - Predicts Control ID
    - Inherent Risk = Likelihood (1-5) * Impact (1-5)
    - Control Effectiveness: PASSED = 75%, WARNING = 35%, FAILED = 0%
    - Residual Risk calculation
    - Actionable recommendation lookup
    """
    # 1. Predict Control ID
    pred_control = "A.8.28" # Default
    confidence = 0.85
    if model:
        pred_control, confidence = model.predict_one(finding_text)

    ctrl_name = CONTROL_TITLES.get(pred_control, "General Information Security Control")

    # 2. Inherent Risk Math
    l = max(1, min(5, int(likelihood)))
    i = max(1, min(5, int(impact)))
    inh_score = l * i

    inh_tier = "Low"
    if inh_score >= 20: inh_tier = "Critical"
    elif inh_score >= 12: inh_tier = "High"
    elif inh_score >= 6: inh_tier = "Medium"

    # 3. Control Gap Assessment
    status = str(control_status).upper().strip()
    if status in ["PASSED", "IMPLEMENTED", "EFFECTIVE"]:
        eff = 0.75
        gap_detected = "No Gap (Control Verified)"
        ctrl_badge = "PASSED"
    elif status in ["WARNING", "PARTIAL", "IN PROGRESS"]:
        eff = 0.35
        gap_detected = "Partial Gap (Control Incomplete)"
        ctrl_badge = "WARNING"
    else:
        eff = 0.00
        gap_detected = "Major Gap (Control Missing / Failed)"
        ctrl_badge = "FAILED"

    # 4. Residual Risk Math
    res_l = max(1, round(l * (1 - (eff * 0.65))))
    res_i = max(1, round(i * (1 - (eff * 0.45))))
    res_score = res_l * res_i

    res_tier = "Low"
    if res_score >= 20: res_tier = "Critical"
    elif res_score >= 12: res_tier = "High"
    elif res_score >= 6: res_tier = "Medium"

    # 5. Tailored Fix Recommendation
    recommendation = RECOMMENDATIONS_PLAYBOOK.get(
        pred_control,
        f"Implement baseline technical safeguards and verify compliance against ISO/IEC 27001:2022 Control {pred_control} ({ctrl_name})."
    )

    return {
        "finding_text": finding_text,
        "predicted_control_id": pred_control,
        "control_name": ctrl_name,
        "model_confidence": round(confidence * 100, 1),
        "inherent_likelihood": l,
        "inherent_impact": i,
        "inherent_score": inh_score,
        "inherent_tier": inh_tier,
        "control_status": ctrl_badge,
        "gap_detected": gap_detected,
        "control_effectiveness_pct": round(eff * 100),
        "residual_likelihood": res_l,
        "residual_impact": res_i,
        "residual_score": res_score,
        "residual_tier": res_tier,
        "recommendation": recommendation
    }

def process_audit_spreadsheet(input_csv_path, output_csv_path=None):
    """
    Processes an entire CSV assessment spreadsheet, applies ML + GRC calculus,
    and writes out the tailored report.
    """
    model = get_trained_classifier()

    input_path = Path(input_csv_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input assessment spreadsheet not found: {input_path}")

    results = []
    with open(input_path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            finding = row.get("Finding_Text") or row.get("Description") or row.get("Threat") or "Security configuration issue"
            
            # Map CVSS or manual scores
            l = row.get("Likelihood") or 3
            i = row.get("Impact") or 4
            if "CVSS_Base_Score" in row and row["CVSS_Base_Score"]:
                try:
                    cvss = float(row["CVSS_Base_Score"])
                    i = min(5, max(1, round(cvss / 2.0)))
                    l = 4 if cvss >= 7.0 else 3
                except Exception:
                    pass

            status = row.get("Control_Status") or row.get("Status") or "FAILED"

            assessment = calculate_risk_and_gaps(finding, l, i, status, model)
            if "Finding_ID" in row:
                assessment["finding_id"] = row["Finding_ID"]
            elif "ID" in row:
                assessment["finding_id"] = row["ID"]
            else:
                assessment["finding_id"] = f"AUD-{len(results)+1:03d}"

            results.append(assessment)

    # Output CSV Report
    if not output_csv_path:
        output_csv_path = REPO_ROOT / "data" / "remediated_grc_audit_report.csv"
    else:
        output_csv_path = Path(output_csv_path)

    fieldnames = [
        "Finding_ID", "Finding_Description", "Predicted_ISO27001_Control", "Control_Name",
        "ML_Confidence_Pct", "Inherent_Likelihood", "Inherent_Impact", "Inherent_Score",
        "Inherent_Risk_Tier", "Control_Status", "Control_Gap_Assessment",
        "Control_Effectiveness_Pct", "Residual_Likelihood", "Residual_Impact",
        "Residual_Score", "Residual_Risk_Tier", "Tailored_Remediation_Recommendation"
    ]

    with open(output_csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for r in results:
            writer.writerow([
                r.get("finding_id", "AUD-001"),
                r["finding_text"],
                r["predicted_control_id"],
                r["control_name"],
                f"{r['model_confidence']}%",
                r["inherent_likelihood"],
                r["inherent_impact"],
                r["inherent_score"],
                r["inherent_tier"],
                r["control_status"],
                r["gap_detected"],
                f"{r['control_effectiveness_pct']}%",
                r["residual_likelihood"],
                r["residual_impact"],
                r["residual_score"],
                r["residual_tier"],
                r["recommendation"]
            ])

    print("=================================================================")
    print("  AEGIS GRC SPREADSHEET RISK & GAP ASSESSMENT COMPLETED")
    print("=================================================================")
    print(f"  Processed Findings:      {len(results)} rows")
    print(f"  High/Critical Inherent:  {sum(1 for r in results if r['inherent_score'] >= 12)}")
    print(f"  Identified Control Gaps: {sum(1 for r in results if 'Gap' in r['gap_detected'])}")
    print(f"  Exported Remediated File: {output_csv_path}")
    print("=================================================================")

    return results

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AEGIS GRC — Automated Spreadsheet Risk & Gap Analyzer")
    parser.add_argument("--input", "-i", type=str, default=str(REPO_ROOT / "data" / "real_vulnerabilities_dataset.csv"), help="Path to input CSV audit spreadsheet")
    parser.add_argument("--output", "-o", type=str, default=str(REPO_ROOT / "data" / "remediated_grc_audit_report.csv"), help="Path to output remediated CSV report")
    args = parser.parse_args()

    print(f"Ingesting and assessing: {args.input}")
    process_audit_spreadsheet(args.input, args.output)
