# Infrastructure Onboarding Guide

## 1. CI/CD Permissions

- Ensure GitHub repo has access to reusable workflows
- Setup repository secrets for cloud deployment credentials

## 2. Secrets

- Store secrets in Vault or AWS Secrets Manager
- Avoid storing secrets in `env` files

## 3. Deployment

- Deploy to EKS via Helm using `common-chart`
- Add your service to the deployment manifest

## 4. Registration

- All services must register in Backstage (`catalog-info.yaml`)
- Include ownership metadata
