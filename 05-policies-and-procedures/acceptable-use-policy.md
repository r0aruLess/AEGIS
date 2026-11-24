# Acceptable Use Policy

Policy reference: CS-POL-003  
Standards: ISO/IEC 27001:2022 (Controls A.5.10, A.8.1, A.8.2, A.8.7, A.8.12), SOC 2 (CC6.1, CC6.6, CC6.8)  
Effective date: May 15, 2026 (Version 3.0)  
Owner: Head of People and IT Operations Lead  
Approved by: CISO  

---

## 1. Scope

This policy applies to all hardware, networks, SaaS accounts, and communication tools provided to CloudSphere employees and contractors.

---

## 2. Hardware and Endpoint Rules

Work must take place on company-issued MacBooks enrolled in Kandji MDM. Personal computers cannot connect to production environments or internal source repositories.

Kandji enforces the following settings on all laptops:
- FileVault full-disk encryption remains on, with recovery keys backed up to Kandji.
- Screens lock automatically after five minutes of inactivity, requiring TouchID or a password to unlock.
- The CrowdStrike Falcon sensor must run continuously. Disabling the sensor triggers an alert to the SecOps team.
- Operating system updates must install within 14 days of release. Critical zero-day patches force a restart within 72 hours.
- Writing to USB flash drives or external storage is blocked.

---

## 3. Allowed and Prohibited Use

Incidental personal use (like checking personal email or news) is allowed if it does not disrupt work or violate company standards.

The following activities are prohibited:
- Uploading company data to unapproved cloud storage (such as personal Dropbox or Google Drive accounts).
- Pasting client data or proprietary code into external generative AI tools that train on user inputs.
- Running torrent software, P2P file-sharing tools, or cryptocurrency miners.
- Copying source code or database dumps to personal GitHub accounts, personal drives, or unapproved devices.

---

## 4. Endpoint Monitoring

CloudSphere monitors company hardware, network connections, installed applications, and authentication events to detect threats and maintain compliance. Staff do not have an expectation of privacy on company equipment or corporate cloud services.
