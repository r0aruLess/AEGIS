# CloudSphere Analytics Inc. • Data Flow Architecture Diagram
**Document Reference:** CLOUDSPHERE-ARCH-001  
**Classification:** Confidential / Auditor Disclosable  
**Scope:** Production SaaS Ingestion & Storage Pipeline  

---

## Data Ingestion & Boundary Flow Diagram

```text
[ Enterprise Client Browser / API Clients ]
                      │
                      │ HTTPS / TLS 1.3
                      ▼
       [ Cloudflare Edge WAF & DDoS Shield ]
       - Bot management & Rate limiting
       - Geo-fencing & TLS termination
                      │
                      │ Mutual TLS (mTLS)
                      ▼
         [ AWS Application Load Balancer ]
                      │
                      │ Private Subnet Routing
                      ▼
       [ Amazon EKS Kubernetes Cluster ]
       - Microservices: Auth, Analytics, Ingestion
       - Calico Network Policies (Zero Trust)
       - Dynamic PII Masking & Tokenization
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
[ Aurora PostgreSQL ]    [ Amazon S3 Data Lake ]
- AES-256 KMS Encrypted  - SSE-KMS Customer Key
- Multi-AZ Replica       - Automated Lifecycle
- Row-Level Security     - Object-Lock Air-Gap
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
     [ Datadog Centralized SIEM Pipeline ]
     - Immutable Audit Trail & Log Archives
```

---

## Key Data Flow Safeguards:
1.  **Ingress Security (Control A.8.20 & A.8.21):** All client traffic passes through Cloudflare WAF before reaching AWS ALBs.
2.  **Internal Network Isolation (Control A.8.22):** EKS pods run in private VPC subnets with zero public IP addresses.
3.  **Storage Encryption (Control A.8.24):** All persistent data in Aurora and S3 is encrypted with AWS KMS customer-managed keys (CMKs).
4.  **Audit Logging (Control A.8.15):** API calls, logins, and database queries generate immutable CloudTrail and Datadog audit trails.
