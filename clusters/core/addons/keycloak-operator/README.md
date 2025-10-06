# keycloak-operator

![Version: 1.29.0](https://img.shields.io/badge/Version-1.29.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.29.0](https://img.shields.io/badge/AppVersion-1.29.0-informational?style=flat-square)

A Helm chart for keycloak-operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | keycloak-operator | 1.29.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| keycloak-operator.clusterReconciliationEnabled | bool | `true` | If clusterReconciliationEnabled is true, the operator reconciles all Keycloak instances in the cluster;  otherwise, it only reconciles instances in the same namespace by default, and cluster-scoped resources are ignored. |

