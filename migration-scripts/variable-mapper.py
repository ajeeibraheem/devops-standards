import yaml
import os

def map_vars(old_env_file, new_env_file):
    with open(old_env_file, 'r') as f:
        old_vars = yaml.safe_load(f)

    mapped_vars = {}
    rename_map = {
        "ENV": "APP_ENV",
        "LEVEL": "LOG_LEVEL",
        "RETRIES": "RETRY_COUNT"
    }

    for k, v in old_vars.items():
        new_key = rename_map.get(k, k)
        mapped_vars[new_key] = v

    with open(new_env_file, 'w') as f:
        yaml.dump(mapped_vars, f, default_flow_style=False)

    print(f"✔ Mapped vars: {new_env_file}")

if __name__ == "__main__":
    map_vars("legacy-env-vars.yaml", "standardized-env-vars.yaml")
