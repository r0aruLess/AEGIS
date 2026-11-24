# Customer Telemetry Data Flow and Trust Boundaries

Document reference: CS-ARCH-DFD-001  
Owner: Head of Infrastructure and SRE  
Approved by: CISO  
Last reviewed: May 15, 2026  

---

## 1. Ingestion Flow

```
[Customer Client Application / Web SDK]
                  │
                  ▼ HTTPS / TLS 1.3 via Cloudflare WAF
[Cloudflare Edge Network]
                  │
                  ▼ mTLS via AWS Application Load Balancer
[AWS EKS Production Cluster / Envoy Proxy]
                  │
                  ▼ Token validation via Okta OAuth2
[Ingestion Microservices]
                  ├──► [Kafka and Kinesis Event Streams (24-hour buffer)]
                  │                 │
                  │                 ▼
                  │    [Analytics Processing Workers]
                  │                 │
                  │                 ├──► [Amazon Aurora PostgreSQL (Aggregated data)]
                  │                 │    Encrypted at rest with KMS, Multi-AZ
                  │                 │
                  │                 └──► [Amazon S3 (Raw partitioned events)]
                  │                      Encrypted with KMS, 30-day lifecycle expiry
                  │
                  └──► [Datadog SIEM (PII stripped / tokenized)]
```

---

## 2. Trust Boundaries

1. Public internet to Cloudflare: Traffic passes through Cloudflare WAF with rate limiting, geo-blocking, and managed OWASP rules.
2. Cloudflare to AWS load balancers: AWS security groups drop any connection not coming from verified Cloudflare IP addresses on port 443.
3. Ingress to microservices: Traffic inside Kubernetes clusters uses Kubernetes network policies and mutual TLS through Envoy proxies.
4. Services to databases and storage: Aurora and S3 live in private subnets with no internet gateway. Workloads connect using IAM roles and port 5432 security groups.
5. Administrative access: No direct SSH or database ports face the internet. Engineers access production by assuming temporary 60-minute IAM roles through AWS IAM Identity Center and Okta WebAuthn.
