# Architectural Decisions

Document major decisions and reasoning.

## ID: 001
Date: 2026-03-02
Status: Proposed
Context: The project is an AWS Threat Modelling Web App and we need to establish the initial technology stack and deployment architecture.
Decision: Adopt an AWS serverless architecture. Frontend will be a React single‑page app hosted on S3 with CloudFront CDN. Backend APIs will run on AWS Lambda behind API Gateway. User-uploaded diagrams and generated reports will be stored in S3. Application metadata and threat model results will persist in DynamoDB. AWS Cognito will provide authentication if needed. This aligns with public availability, scalability, and budget constraints typical of a new project.
Consequences: Simplifies infrastructure management, leverages pay‑per‑use pricing, and speeds up development. Introduces service dependencies on AWS and a learning curve for serverless design. Future changes to non‑AWS providers will require architectural review.
