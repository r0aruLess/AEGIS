# ISO/IEC 27001:2022 Gap Assessment Summary

Document reference: CS-GRC-GAP-2026-Q1  
Target standard: ISO/IEC 27001:2022 (Annex A controls and Clauses 4–10)  
Assessment date: April 20, 2026  
Assessed by: Lead GRC Analyst and Head of Infrastructure  
Reviewed by: CISO  
Readiness score: 86.0% (Stage 1 audit ready)  

---

## 1. Summary of Findings

The GRC team reviewed CloudSphere's controls against all 93 Annex A controls in ISO/IEC 27001:2022 ahead of external certification.

### Status Breakdown
- Passed (80 controls, 86.0%): Verified through automated technical checks, configuration files, or approved policies.
- Warning (9 controls, 9.7%): Partially in place. Remediation tasks are open in Jira with 30-to-60-day deadlines.
- Exempt (4 controls, 4.3%): Physical facility controls (A.7.11 to A.7.14) inherited from AWS under the Shared Responsibility Model.
- Failed (0 controls): No critical control failures found.

---

## 2. Open Gaps and Remediation Plans

| Control | Theme | Status | Identified Gap | Owner | Action and Due Date |
|---|---|---|---|---|---|
| A.5.7 Threat intelligence | Organizational | Warning | Feed intake relies on CISA alerts without automated commercial feeds. | SecOps Lead | Add AlienVault OTX and AWS GuardDuty feeds by June 15, 2026. |
| A.8.10 Information deletion | Technological | Warning | Database deletions run automatically via API, but S3 log cleanup still requires a manual ticket. | Head of Infrastructure | Add S3 lifecycle rules to expire logs after 30 days by May 30, 2026. |
| A.8.12 Data leakage prevention | Technological | Warning | Laptops use basic MDM file restrictions without deep content inspection. | IT Operations Lead | Turn on Google Workspace DLP and Slack Enterprise DLP by June 30, 2026. |
| A.8.13 Information backup | Technological | Warning | Daily Aurora backups run, but the Q1 staging restore test timed out over a security group rule. | Head of Infrastructure | Fix VPC routing rules and rerun the restore test by May 25, 2026. |
