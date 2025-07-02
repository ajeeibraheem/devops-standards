# Common Helm Chart

This chart provides a base deployment structure for microservices running in Kubernetes.

## Features

- Standard resource definitions (Deployment, Service)
- Environment variable templating
- Health probe support
- Configurable replica count and image

## Usage

```bash
helm upgrade --install my-service ./common-chart \
  --set image.repository=myrepo/service \
  --set image.tag=1.0.0 \
  --namespace production
