# Data Retention and Disposal Policy (POL-005)
**Document Owner:** Data Protection Officer (DPO) & Lead Architect  
**Approved By:** CISO & General Counsel  
**Version:** 2.1  
**Effective Date:** January 10, 2026  
**ISO/IEC 27001:2022 Mapping:** Control A.8.10 (Information deletion), Control A.8.14

---

## 1. Principle of Storage Limitation
In alignment with ISO/IEC 27701:2025 and GDPR Article 5(1)(e), personal data is retained only for as long as necessary to fulfill the documented business purpose or comply with statutory retention mandates.

## 2. Retention Schedules
| Data Category | Specific Record Type | Mandatory Retention Period | Destruction Method |
| :--- | :--- | :--- | :--- |
| **Customer Data** | SaaS Tenant Application Data | Contract Term + 30 Days | Cryptographic erasure / RDS purge |
| **Audit Logs** | Security, Access & System Logs | 365 Days (1 Year) | S3 Glacier automated expiration rule |
| **Financial Records**| Invoices, Tax Records, Billing | 7 Years | Secure physical shredding / digital archive |
| **HR Records** | Employee Personnel Files | Employment Term + 6 Years | HRIS file deletion |
| **Candidate Resumes**| Unsuccessful Job Applicants | 12 Months (with consent) | ATS automated deletion |
| **Source Code** | Git Repositories and Builds | Indefinite (Company IP) | Maintained in protected VCS |

## 3. Secure Disposal & Sanitization Standards
- **Digital Media:** AWS S3 lifecycle rules execute irreversible cryptographic erasure. Local testing media is sanitized according to **NIST SP 800-88 Rev 1 (Clear/Purge)**.
- **Physical Hardware:** End-of-life laptops and hard drives are destroyed by an R2-certified electronic recycling vendor with serialized Certificates of Destruction.