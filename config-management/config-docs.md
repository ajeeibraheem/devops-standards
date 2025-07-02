# Config Management Guide

This directory holds default and environment-specific configuration values for services.

## Files

- `default-env-vars.yaml`: Base environment configuration
- `environment-overrides/`: Files per environment (dev, stage, prod)

## Strategy

- Load `default-env-vars.yaml`
- Apply overrides based on current environment
- Avoid hardcoding sensitive values (use references to SSM/Vault)

## Integration Example (Python)

```python
import yaml

def load_env(env):
    with open('default-env-vars.yaml') as f:
        base = yaml.safe_load(f)

    with open(f'environment-overrides/{env}.yaml') as f:
        override = yaml.safe_load(f)

    return {**base, **override}
