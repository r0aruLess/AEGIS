# Access Control Policy (POL-002)
**Document Owner:** Head of Security Operations  
**Approved By:** CISO  
**Version:** 3.0  
**Effective Date:** January 1, 2026  
**ISO/IEC 27001:2022 Mapping:** Control A.5.15, A.5.18, A.8.5

---

## 1. Principles of Access Control
Access to CloudScale systems and customer environments is governed strictly by the principles of **Least Privilege**, **Need-to-Know**, and **Separation of Duties**.

## 2. Authentication & Passwords
1. **Multi-Factor Authentication (MFA):** Enforced globally via Okta for 100% of internal workforce accounts and administrative consoles. FIDO2 / WebAuthn hardware keys or phishing-resistant authenticator apps are required. SMS OTP is prohibited.
2. **Password Parameters:** Minimum 14 characters, complexity requirements (alphanumeric + symbol), checked against HaveIBeenPwned compromised credential dictionaries.
3. **Session Controls:** Inactive sessions lock after 15 minutes. Re-authentication is required after 12 hours.

## 3. Access Lifecycle Management
- **Provisioning:** Triggered automatically via BambooHR HRIS integration using SCIM into Okta. Standard role profiles assign default least-privilege packages.
- **Privileged Access:** Production database and AWS root access is strictly restricted. Engineers access production environments via ephemeral, just-in-time (JIT) credentials through Teleport / AWS IAM Identity Center with mandatory justification and ticket association.
- **User Access Reviews (UAR):** Conducted quarterly by the GRC team and department heads. Unused or orphaned accounts are revoked within 48 hours of review completion.
- **Deprovisioning:** HR termination immediately triggers automated Okta account suspension and revocation of all OAuth session tokens within 1 hour.