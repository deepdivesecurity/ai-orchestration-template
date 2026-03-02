# Threat Model – AWS Serverless Architecture

Below is the STRIDE-based analysis for the proposed architecture of the AWS Threat Modelling Web App.

| **Asset/Component** | **Trust Boundary** | **Threat (STRIDE)** | **Description / Attack Vector** | **High‑Level Mitigation** |
|---------------------|--------------------|---------------------|----------------------------------|---------------------------|
| **SPA (React on S3/CF)** | Internet → CloudFront | **Spoofing** | Attacker serves malicious JS via DNS cache‑poisoning or compromised CDN config. | Enforce HTTPS, HSTS, CloudFront origin authentication, signed URLs. |
| | | **Tampering** | Altered static files in S3 bucket. | Bucket policy (read‑only), enable S3 versioning & MFA‑delete, deploy integrity checks (SRI). |
| | | **Repudiation** | User claims they didn’t make a change (app has no auth). | Add optional logging/trace of user actions; use Cognito to tie events to identities. |
| **API Gateway / Lambda** | CloudFront/Internet → API | **Information Disclosure** | Unauthenticated endpoint leaks diagram metadata or storage keys. | Strict request validation, authorization (Cognito or API keys), least‑privilege IAM. |
| | | **Denial of Service** | Flood requests causing throttling or Lambda cost explosion. | Enable WAF rules, API Gateway throttling, Lambda concurrency limits. |
| | | **Elevation of Privilege** | Lambda misconfiguration allows execution of unauthorized actions. | Use IAM roles scoped per function; remove default wildcards. |
| **S3 Buckets (diagrams/reports)** | API/Lambda → S3 | **Tampering** | Unauthorized write/delete of stored diagrams. | Bucket policies tied to Lambda role; validate object metadata; use encryption at rest. |
| | | **Information Disclosure** | Publicly accessible objects reveal sensitive models. | Block public access, generate pre‑signed URLs with short TTL. |
| **DynamoDB (metadata)** | Lambda → DynamoDB | **Information Disclosure** | Unauthorised reads of table. | IAM policies, fine‑grained access control, encryption (KMS). |
| | | **Tampering** | Data modification via injection or compromised function. | Input sanitisation, use condition expressions, enable point‑in‑time recovery. |
| **Cognito (optional auth)** | Internet → Cognito | **Spoofing** | Attackers brute‑force or replay tokens. | Enable MFA, restrict token lifetimes, use Cognito hosted UI with OIDC. |
| | | **Information Disclosure** | Identity pool misuse leads to excessive IAM access. | Configure least‑privilege roles, monitor with CloudTrail. |
| **Client‑side State (browser)** | Browser storage | **Tampering** | Manipulate diagrams or tokens in local storage. | Avoid storing secrets; sign/verify client data on server. |
| | | **Repudiation** | User clears logs/local data to deny actions. | Server‑side logging of operations with timestamps. |

> **Notes**
> - Trust boundaries are drawn at each AWS managed service integration and between internet‑facing components.
> - Mitigations are high‑level; implementation details belong in the security design section of the architecture documentation.
> - This table can be expanded as the feature set grows (e.g. sharing, collaboration).


