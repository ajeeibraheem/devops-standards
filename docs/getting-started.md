# Getting Started with DevOps Standards

Welcome! Follow these steps to onboard your microservice into the standardized ecosystem.

## 1. Scaffold New Service

Use the Backstage developer portal and choose the template:
> `Create Java Microservice`

## 2. Use Standard CI/CD

Include this workflow file in your repo:
```yaml
uses: org/devops-standards/cicd-templates/java-microservice.yml@main
