import os
import yaml

SOURCE_PIPELINE = ".github/workflows/build.yml"
TEMPLATE_PIPELINE = "cicd-templates/java-microservice.yml"

def migrate_pipeline(service_path):
    src_path = os.path.join(service_path, SOURCE_PIPELINE)
    dst_path = os.path.join(service_path, ".github/workflows/standard-ci.yml")

    with open(TEMPLATE_PIPELINE, 'r') as template_file:
        template_data = yaml.safe_load(template_file)

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w') as f:
        yaml.dump(template_data, f, sort_keys=False)

    print(f"✔ Migrated: {service_path}")

if __name__ == "__main__":
    for service_dir in os.listdir("services/"):
        path = os.path.join("services", service_dir)
        if os.path.isdir(path):
            migrate_pipeline(path)
