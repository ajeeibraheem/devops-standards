# 🛠️ devops-standards

[![CI Status](https://github.com/<your-org>/devops-standards/actions/workflows/ci.yml/badge.svg)](https://github.com/<your-org>/devops-standards/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-available-brightgreen)](docs/)
[![Helm Chart](https://img.shields.io/badge/helm-chart-blue)](helm-charts/)

---

This repository contains standardized DevOps assets used across 1000+ microservices. It serves as the central source of reusable CI/CD workflows, Helm deployment templates, secrets strategy, configuration structures, and platform automation tools.

---

## 🔧 Features

- ✅ Reusable GitHub Actions workflows
- 🧱 Helm `common-chart` for Kubernetes deployments
- 🔐 Vault/AWS Secrets Manager integration
- ⚙️ Environment config overlays (YAML-based)
- 🔁 Migration scripts for legacy CI/CD
- 📜 Policies-as-code (OPA + Conftest)
- 🧰 Backstage scaffolding templates
- 📚 Documentation for onboarding and usage

---

## 📂 Repo Structure

| Folder | Description |
|--------|-------------|
| `.github/workflows/` | Reusable GitHub Actions |
| `cicd-templates/` | One-click templates for service pipelines |
| `helm-charts/` | Helm chart for standardized deployment |
| `config-management/` | Env config defaults + overrides |
| `secrets-management/` | Vault policy + rotation script |
| `policies/` | OPA + Conftest rules |
| `backstage-templates/` | Templates for self-service scaffolding |
| `migration-scripts/` | Tools to migrate old services |
| `docs/` | Onboarding, standards, and usage guides |

---

## 🚀 Getting Started

```bash
# Use a template in your microservice
.github/workflows/ci.yml:
uses: org/devops-standards/.github/workflows/reusable-build-java.yml@main
