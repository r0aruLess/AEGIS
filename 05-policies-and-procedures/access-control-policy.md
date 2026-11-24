# Access Control Policy

Policy reference: CS-POL-002  
Standards: ISO/IEC 27001:2022 (Controls A.5.15–A.5.18, A.8.2, A.8.3, A.8.5), SOC 2 (CC6.1–CC6.3)  
Effective date: May 15, 2026 (Version 3.0)  
Owner: IT Operations Lead  
Approved by: CISO  

---

## 1. Scope

This policy governs account creation, authentication, administrative privileges, and account removal across CloudSphere's infrastructure, databases, and software tools.

---

## 2. Authentication Requirements

- Identity provider: All workforce accounts route through Okta. Local accounts on individual tools or AWS accounts are prohibited, except for documented emergency break-glass credentials.
- Multi-factor authentication: Logins require a FIDO2 hardware key (YubiKey 5 series) or Okta Verify with biometric verification (TouchID). SMS, voice calls, and email codes are disabled.
- Password settings: Master accounts must use at least 16 characters or a four-word random phrase. Accounts lock for 30 minutes after five consecutive failed attempts.
- Credential monitoring: Okta ThreatInsight runs automatically to block logins using known compromised passwords.

---

## 3. Production and Cloud Access

- Administrative accounts: No employee has permanent root or AdministratorAccess permissions in production AWS accounts.
- Temporary roles: Engineers access production using temporary IAM roles in AWS IAM Identity Center (such as Production-ReadOnly or Production-DB-Debugger). Sessions expire automatically after 60 minutes.
- Ticket requirement: Assuming a production role requires entering an approved Jira ticket number (INC- or OPS-) in the session request.
- Database connections: Engineers cannot connect to Aurora port 5432 directly from their laptops. Access runs through a Teleport proxy that logs every query and records sessions.

---

## 4. Account Lifecycle

- New hires: Once HR completes background checks via Checkr in BambooHR, automated SCIM provisioning creates an Okta account with base employee permissions. Additional tool access requires a manager-approved Jira ticket.
- Internal transfers: When an employee changes teams, HR sends a notice that starts a permissions review. Access granted for the old role is revoked within five business days.
- Departures: HR records the departure in BambooHR, which sends an automated webhook to Okta to suspend the account immediately. All access (Okta, Google Workspace, GitHub, Slack) must terminate within 24 hours of departure, or immediately for involuntary departures.
- Daily sync check: A daily script checks BambooHR records against active Okta accounts. If an account was not suspended after a termination event, an alert posts to the #sec-ops-alerts channel in Slack.

---

## 5. Quarterly Access Reviews

At the end of each quarter, the GRC team initiates an access review in Jira Service Management:
1. Department heads receive lists of their team members' permissions across AWS, GitHub, Okta, and databases.
2. Managers must confirm or remove each entitlement within 14 calendar days.
3. If a manager does not review a permission within 14 days, the access is escalated to the CISO and scheduled for removal.
