# sonar-operator

![Version: 3.1.0](https://img.shields.io/badge/Version-3.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.1.0](https://img.shields.io/badge/AppVersion-3.1.0-informational?style=flat-square)

A Helm chart for EDP Sonar Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/snapshot | sonar-operator | 3.1.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| keycloak.enable | bool | `true` | |
| keycloak.keycloakRealm | string | `"<keycloak-realm>"` | |
| keycloak.keycloakUrl | string | `"https://keycloak.example.com/""` | |
| image.repository | string | `"epamedp/sonar-operator"` | EDP sonar-operator Docker image name. The released image can be found on [Dockerhub](https://hub.docker.com/r/epamedp/sonar-operator) |
| image.tag | string | `"3.1.0"` | EDP sonar-operator Docker image tag. The released image can be found on [Dockerhub](https://hub.docker.com/r/epamedp/sonar-operator/tags) |
| name | string | `"sonar-operator"` | component name |
| sonarUrl | string | `"https://example.com"` | target URL for configurable sonar |
| sonarSecret | string | `"sonar-admin"` | secret name for configurable sonar |