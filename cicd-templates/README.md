# CI/CD Pipeline Templates

This folder contains standardized pipeline templates for different runtime environments.

## Templates

- `java-microservice.yml`: Reusable CI/CD for Java (Gradle-based) apps
- `node-microservice.yml`: CI/CD for Node.js-based microservices
- `python-lambda.yml`: Packaging and linting for Python AWS Lambda functions

## Usage

Each file is a full pipeline that can be copied or referenced from your service repository. These templates use reusable workflows from the `.github/workflows` folder.

## How to Extend

Each service may override steps by:
- Creating a custom workflow in their own repo
- Referencing reusable workflows from this shared repo
