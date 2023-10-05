# sonar-operator

![Version: 3.1.0](https://img.shields.io/badge/Version-3.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.1.0](https://img.shields.io/badge/AppVersion-3.1.0-informational?style=flat-square)

A Helm chart for EDP Sonar Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | sonar-operator | 3.1.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| annotations | object | `{}` |  |
| extraVolumeMounts | list | `[]` | Additional volumeMounts to be added to the container |
| extraVolumes | list | `[]` | Additional volumes to be added to the pod |
| image.repository | string | `"epamedp/sonar-operator"` | EDP sonar-operator Docker image name. The released image can be found on [Dockerhub](https://hub.docker.com/r/epamedp/sonar-operator) |
| image.tag | string | `"3.1.0"` | EDP sonar-operator Docker image tag. The released image can be found on [Dockerhub](https://hub.docker.com/r/epamedp/sonar-operator/tags) |
| imagePullPolicy | string | `"IfNotPresent"` |  |
| keycloak | object | `{"enable":true,"keycloakRealm":"example","keycloakUrl":"https://keycloak.example.com"}` | Integration with keycloak |
| name | string | `"sonar-operator"` | component name |
| nodeSelector | object | `{}` |  |
| resources.limits.memory | string | `"192Mi"` |  |
| resources.requests.cpu | string | `"50m"` |  |
| resources.requests.memory | string | `"64Mi"` |  |
| sonarSecret | string | `"sonar-admin"` |  |
| sonarUrl | string | `"https://sonar.example.com"` | URL and secret name which use sonar operator for configuring sonar |
| tolerations | list | `[]` |  |

