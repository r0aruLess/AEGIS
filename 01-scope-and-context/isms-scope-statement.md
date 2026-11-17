# CloudSphere Analytics Inc. • ISMS & PIMS Scope Statement
**Document Reference:** CS-ISMS-SCOPE-001  
**Standards Alignment:** ISO/IEC 27001:2022 (Clause 4.3) & ISO/IEC 27701:2025 (Clause 4.3)  
**Classification:** Public / Auditor Disclosable  
**Effective Date:** 2026-05-15  
**Version:** 3.0  
**Approved By:** Chief Information Security Officer (CISO) & Chief Executive Officer (CEO)

---

## 1. Scope Boundary
The Information Security Management System (ISMS) and Privacy Information Management System (PIMS) encompass all operational activities, systems, personnel, and intellectual property associated with the development, operation, and maintenance of the **CloudSphere B2B Analytics Platform**.

---

## 2. Organizational Boundaries
The scope includes all 150 full-time employees, authorized contractors, and business functions:
*   Executive Leadership & Governance
*   Software Engineering & DevSecOps
*   Cloud Infrastructure & Site Reliability Engineering (SRE)
*   Product Management & UI/UX Design
*   Customer Support & Customer Success
*   Human Resources & Talent Acquisition
*   Finance, Legal, and Compliance

---

## 3. Physical & Cloud Hosting Boundaries
*   **Physical Facilities:** Corporate office suite located at 100 Montgomery Street, Suite 1400, San Francisco, CA. The facility houses administrative and executive offices; **zero server hardware is hosted on-premise**.
*   **Cloud Production Environments:** Amazon Web Services (AWS) multi-account infrastructure in AWS US-East-1 (Primary) and AWS EU-Central-1 (Secondary / European Privacy Region).
*   **Remote Personnel:** Distributed remote employees operating within the United States, Canada, the European Union, and India, governed under corporate MDM endpoint baselines (Control A.6.7 & A.8.1).

---

## 4. Scope Exclusions & Defensible Justifications
*   **Physical Environmental Controls for Core Servers (A.7.5 & A.7.11):**
    *   *Justification:* CloudSphere operates exclusively as a cloud-native SaaS on AWS. Physical environmental controls (redundant power supplies, fire suppression, diesel generators, physical perimeter fencing) are managed directly by Amazon Web Services under the **Cloud Shared Responsibility Model**. CloudSphere verifies these controls annually via AWS's independent third-party SOC 2 Type II and ISO 27001 certification audit reports.
