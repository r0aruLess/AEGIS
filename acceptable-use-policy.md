# CloudSphere Analytics Inc. • Acceptable Use Policy (AUP)

**Policy Reference:** CS-POL-003  
**ISO/IEC 27001:2022 Alignment:** Controls A.5.10, A.8.1, A.8.2, A.8.7, A.8.12  
**SOC 2 Alignment:** Common Criteria CC6.1, CC6.6, CC6.8  
**Classification:** Internal / Auditor Disclosable  
**Effective Date:** 2026-05-15 | Version: 3.0  
**Policy Owner:** Head of People & IT Operations Lead | Approved By: CISO

---

## 1. Scope & Workforce Applicability
This Acceptable Use Policy defines acceptable, restricted, and prohibited uses of all information technology equipment, endpoints, SaaS tools, networks, and communication channels provided by **CloudSphere Analytics Inc.** to its remote workforce.

---

## 2. Remote Worker Hardware & Endpoint Standards
1.  **Corporate-Owned Devices Only:** All production access, source code development, and customer data processing must take place on corporate-issued Apple MacBook Pro laptops managed via **Kandji Mobile Device Management (MDM)**. Accessing production environments from personal unmanaged computers (BYOD) is strictly prohibited.
2.  **Mandatory Endpoint Configurations (Enforced by Kandji MDM):**
    *   **Full-Disk Encryption:** Apple FileVault 2 (XTS-AES 128) must be enabled at all times with recovery escrowed in Kandji.
    *   **Inactivity Screen Lock:** Laptops automatically lock after **5 minutes of inactivity**, requiring biometric (TouchID) or master passphrase entry.
    *   **Endpoint Detection & Response (EDR):** CrowdStrike Falcon agent must remain running; tampering with or disabling the daemon triggers an immediate high-priority SecOps alert.
    *   **OS Patching:** Operating system security updates must be installed within **14 calendar days** of release; critical zero-day patches are force-rebooted within **72 hours**.
    *   **Removable Storage:** USB mass storage write capability is disabled via MDM configuration profile to prevent data exfiltration.

---

## 3. Acceptable & Prohibited Cloud & Communication Activities
*   **Permitted Use:** Corporate systems are provided for business purposes. Incidental personal use (e.g., checking personal email, reading news) is permitted provided it does not interfere with job duties or violate security baselines.
*   **Prohibited Software & SaaS:** Employees may not install unvetted software or route corporate data through unapproved SaaS services (Shadow IT). Prohibited tools include:
    *   Unapproved file-sharing services (e.g., Personal Dropbox, Mega).
    *   Unauthorized generative AI tools processing Tier 1 customer PII or raw proprietary code (see AI Acceptable Use Policy).
    *   P2P file sharing, torrent software, or cryptocurrency mining clients.
*   **Source Code & Intellectual Property:** All proprietary source code, scripts, configurations, and customer analytics pipelines belong exclusively to CloudSphere. Copying code repositories to personal GitHub accounts, personal drives, or local flash storage is a severe policy violation.

---

## 4. Privacy Expectation & Endpoint Monitoring
Employees have no expectation of privacy when using CloudSphere hardware, networks, or corporate SaaS accounts. CloudSphere monitors endpoint health, software inventories, network connections, and authentication logs to detect security threats, ensure regulatory compliance, and investigate potential policy breaches.
