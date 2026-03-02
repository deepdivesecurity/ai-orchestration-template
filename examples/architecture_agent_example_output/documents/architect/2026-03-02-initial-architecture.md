# Architecture Summary

This document outlines the initial architecture for the **AWS Threat Modelling Web App**.  The goal of the application is to allow public users to upload their own architecture diagrams, select a threat modelling framework, and receive a generated report identifying threats, mitigations, and risk levels based on the provided data.

## Components and Responsibilities

| Component | Responsibility |
|-----------|----------------|
| Frontend (React SPA) | Single-page application UI, diagram upload, framework selection, display reports. Hosted on S3 + CloudFront for scalability and low latency. |
| API Gateway | Public HTTP endpoint exposing RESTful APIs for diagram handling, threat model processing, and user management. |
| Lambda Functions | Serverless compute executing business logic: diagram ingestion, invoking threat model engines, report generation, authentication hooks. |
| S3 Buckets | Object storage for uploaded diagrams, intermediate artifacts, generated reports, and static assets. |
| DynamoDB | NoSQL store for application metadata: user sessions (if authenticated), threat model results, audit logs, and configuration. |
| Cognito (Optional) | Managed user directory and authentication/authorization if login is required in future iterations. |
| CloudFront | CDN in front of the frontend bucket and optionally APIs for caching and DDoS protection. |
| IAM | Fine‑grained access control for AWS resources. Lambdas will assume roles with least privilege. |

## Data Flow

1. **User Interaction**: A public client loads the SPA from CloudFront.
2. **Diagram Upload**: The SPA posts the file to the backend via API Gateway which triggers a Lambda. The Lambda stores the file in S3 and records metadata in DynamoDB.
3. **Threat Modelling Request**: The client requests processing (frame selection, etc.). A Lambda pulls the diagram, runs algorithms or calls external services, then writes results back to DynamoDB and an S3 report.
4. **Result Delivery**: The SPA polls or receives a notification (via WebSocket or API) and then displays the generated report.
5. **Authentication (Future)**: Cognito handles sign-up/sign-in, issuing tokens used by the SPA and validated by API Gateway/Lambdas.

## Connectivity Matrix

| Source | Destination | Protocol / Port | Control Boundary |
|--------|-------------|-----------------|------------------|
| Client (Browser) | CloudFront (SPA) | HTTPS (443) | Public internet, AWS network boundary |
| Client | API Gateway | HTTPS (443) | Public internet, API Gateway security policies |
| API Gateway | Lambda | Internal AWS invocation | AWS service boundary |
| Lambda | S3 | HTTPS (AWS API) | AWS VPC/S3 boundary (optional VPC endpoints) |
| Lambda | DynamoDB | HTTPS (AWS API) | AWS service boundary |
| Lambda | Cognito | HTTPS | AWS service boundary |

## Security Controls
- **IAM Roles**: Each Lambda has a role scoped to required actions (S3 read/write, DynamoDB read/write, etc.).
- **API Gateway Authorizers**: Cognito or custom authorizer for future auth.
- **S3 Bucket Policies**: Public read only for SPA assets; private for diagrams/reports. Use signed URLs if direct browser uploads are implemented.
- **CloudFront WAF**: Optional for rate limiting and OWASP protections.

## Cost Estimate Summary

Below is a rough starting estimate based on minimal usage (low traffic, small data volumes). Actual costs will vary based on volume of requests, storage, and compute time.

| Component | Basis / Assumption | One-Time Cost (USD) | Monthly Cost (USD) | Annual Cost (USD) | Notes |
|-----------|--------------------|---------------------|--------------------|-------------------|-------|
| S3 (static assets) | 10 GB storage, 1M GETs | 0 | 0.25 | 3 | very small data volume |
| CloudFront | 100 GB data transfer | 0 | 8 | 96 | includes 1M requests |
| API Gateway | 1M requests | 0 | 3.50 | 42 | REST API tier prices |
| Lambda | 1M executions @128MB, 100ms | 0 | 0.20 | 2.40 | free tier may apply |
| DynamoDB | 5 GB storage, 5 RCU/WCU | 0 | 5 | 60 | on-demand or provisioned small table |
| Cognito | 100 MAUs | 0 | 0 | 0 | first 50K free |

**Total Estimated Monthly Cost:** ~$17

**Total Estimated Annual Cost:** ~$204

**Confidence level:** Low – usage assumptions are speculative and will need refinement.

## Diagram Artifacts
- `architecture/diagrams/2026-03-02-initial-architecture.drawio`

## Threat-Model-Ref
See the accompanying threat model analysis:

- `documents/architect/2026-03-02-threat-model.md`

The table within outlines known STRIDE threats and high-level mitigations for the initial serverless architecture.
