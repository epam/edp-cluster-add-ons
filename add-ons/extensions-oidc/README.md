# extensions-oidc

![Version: 1.18.1](https://img.shields.io/badge/Version-1.18.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.18.1](https://img.shields.io/badge/AppVersion-1.18.1-informational?style=flat-square)

A Helm chart for extensions-oidc

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | keycloak-operator | 1.18.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| extensionsOIDC.keycloakUrl | string | `"https://keycloak.example.com"` |  |
| extensionsOIDC.mainRealm | string | `"openshift"` |  |
| extensionsOIDC.mainRealmSecret | string | `""` |  |
| keycloak-operator.clusterReconciliationEnabled | bool | `true` |  |

