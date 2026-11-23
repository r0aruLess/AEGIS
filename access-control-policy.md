# CloudSphere Analytics Inc. • Corporate Access Control Policy

**Policy Reference:** CS-POL-002  
**ISO/IEC 27001:2022 Alignment:** Controls A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5  
**SOC 2 Alignment:** Common Criteria CC6.1, CC6.2, CC6.3  
**Classification:** Internal / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Policy Owner:** IT Operations & Identity Lead | Approved By: CISO

---

## 1. Purpose & Least Privilege Mandate
This policy establishes mandatory operational rules for granting, modifying, reviewing, and revoking logical and administrative access across all cloud infrastructure, databases, SaaS applications, and network boundaries operated by CloudSphere Analytics Inc.

---

## 2. Authentication & Identity Architecture
1.  **Centralized Identity Provider:** All workforce authentication must route through **Okta Universal Directory**. Standalone local accounts on SaaS tools or AWS accounts are prohibited unless explicitly documented as emergency break-glass credentials.
2.  **Mandatory Phishing-Resistant MFA:**
    *   Authentication requires **FIDO2 WebAuthn** hardware tokens (YubiKey 5 Series) or Okta Verify with Number Matching and biometric verification (TouchID).
    *   SMS, email OTP, and voice call verification are **disabled globally** in Okta sign-on policies.
3.  **Password & Passphrase Standards (Master Directory):**
    *   Minimum length: **16 characters** (or minimum 4-word random passphrase).
    *   Automatic brute-force lockout: Account locked after **5 consecutive failed attempts** for 30 minutes.
    *   Compromised credential checks: Okta ThreatInsight automatically blocks logins matching known dark-web credential dumps.

---

## 3. Production Access & Privilege Escalation (AWS IAM Identity Center)
*   **Zero Permanent Administrative Access:** No employee possesses permanent root or full `AdministratorAccess` permissions in production AWS accounts.
*   **Temporary Role Assumption (JIT Access):**
    *   Engineers requiring elevated access assume temporary, time-bound IAM roles via AWS IAM Identity Center (e.g., `Production-ReadOnly`, `Production-DB-Debugger`).
    *   **Maximum Session Duration:** Configured strictly to **60 minutes** (AWS STS temporary credential expiration).
    *   **Justification & Ticket Linking:** Role assumption requires an approved Jira incident or maintenance ticket ID (`INC-` or `OPS-`) entered into the session justification field.
*   **Production Database Access (Aurora PostgreSQL):** Direct access over port 5432 from local laptops is blocked via AWS Security Groups. Access is mediated exclusively through Teleport / Bastion zero-trust identity proxies with full query logging and session recording.

---

## 4. User Lifecycle Management (Joiners, Movers, Leavers)
*   **Onboarding (Joiners):** Upon HR completion of employment contracts and background screening (Checkr) in BambooHR, automated SCIM provisioning creates Okta identities with baseline `All-Employees` role entitlements. Role-specific access requires a manager-approved Jira ticket.
*   **Role Transitions (Movers):** When an employee transfers departments, the HR notification triggers an automated entitlement review. Historical permissions are purged within **5 business days** to prevent privilege creep.
*   **Offboarding (Leavers - 24-Hour Statutory SLA):**
    *   HR records employee departure in BambooHR, triggering an automated webhook to Okta to immediately suspend the identity.
    *   **Enforcement SLA:** All logical access (Okta SSO, Google Workspace, GitHub, Slack) must be terminated within **24 hours** of the employee's official departure timestamp (or immediately for involuntary terminations).
    *   **Automated Reconciliation Safeguard:** To prevent orphaned accounts from webhook failures, a daily cron reconciliation script audits BambooHR terminated staff against Okta active directory records. Any discrepancy immediately alerts `#sec-ops-alerts` in Slack.

---

## 5. User Access Reviews (UAR) & Recertification
Every calendar quarter (Q1, Q2, Q3, Q4), the Lead GRC Analyst initiates a formal access recertification campaign in Jira Service Management:
1.  Department heads receive auto-generated entitlement rosters for all direct reports across AWS, GitHub, Okta, and Aurora DB.
2.  Managers must review and re-authorize or revoke each permission within **14 calendar days**.
3.  Any permission not explicitly certified within 14 days is escalated to the CISO and automatically scheduled for revocation.
