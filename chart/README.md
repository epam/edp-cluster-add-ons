# edp-cluster-add-ons

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

EDP Cluster Addons that extend the Kubernetes Cluster Functionality

**Homepage:** <https://epam.github.io/edp-install/>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| epmd-edp | <SupportEPMD-EDP@epam.com> | <https://solutionshub.epam.com/solution/epam-delivery-platform> |
| sergk |  | <https://github.com/SergK> |

## Source Code

* <https://github.com/epam/edp-cluster-add-ons>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| argo-cd | object | `{"createNamespace":false,"enable":false}` | ArgoCD Deployment |
| argo-cd.createNamespace | bool | `false` | whether to create the namespace or not |
| aws-efs-csi-driver | object | `{"enable":true}` | AWS EFS CSI Driver |
| certmanager | object | `{"createNamespace":true,"enable":true}` | Cert Manager |
| certmanager.createNamespace | bool | `true` | whether to create the namespace or not |
| defectdojo | object | `{"createNamespace":true,"enable":true}` | DefectDojo |
| defectdojo.createNamespace | bool | `true` | whether to create the namespace or not |
| dependency-track.createNamespace | bool | `true` |  |
| dependency-track.enable | bool | `true` |  |
| edp.createNamespace | bool | `true` |  |
| edp.enable | bool | `true` |  |
| extensions-oidc.createNamespace | bool | `true` |  |
| extensions-oidc.enable | bool | `true` |  |
| external-secrets.createNamespace | bool | `true` |  |
| external-secrets.enable | bool | `true` |  |
| fluent-bit.createNamespace | bool | `false` |  |
| fluent-bit.enable | bool | `false` |  |
| harbor-ha-okd.createNamespace | bool | `true` |  |
| harbor-ha-okd.enable | bool | `false` |  |
| harbor-ha.createNamespace | bool | `true` |  |
| harbor-ha.enable | bool | `true` |  |
| harbor.createNamespace | bool | `true` |  |
| harbor.enable | bool | `true` |  |
| ingress-nginx.createNamespace | bool | `true` |  |
| ingress-nginx.enable | bool | `true` |  |
| jaeger-operator.createNamespace | bool | `true` |  |
| jaeger-operator.enable | bool | `true` |  |
| keycloak-postgresql.createNamespace | bool | `false` |  |
| keycloak-postgresql.enable | bool | `false` |  |
| keycloak.createNamespace | bool | `true` |  |
| keycloak.enable | bool | `true` |  |
| minio-operator.createNamespace | bool | `true` |  |
| minio-operator.enable | bool | `true` |  |
| nexus.createNamespace | bool | `true` |  |
| nexus.enable | bool | `true` |  |
| opensearch.createNamespace | bool | `true` |  |
| opensearch.enable | bool | `true` |  |
| opentelemetry-operator.createNamespace | bool | `true` |  |
| opentelemetry-operator.enable | bool | `true` |  |
| postgres-operator.createNamespace | bool | `true` |  |
| postgres-operator.enable | bool | `true` |  |
| prometheus-operator.createNamespace | bool | `true` |  |
| prometheus-operator.enable | bool | `true` |  |
| redis-operator.createNamespace | bool | `true` |  |
| redis-operator.enable | bool | `true` |  |
| sonar-operator.createNamespace | bool | `true` |  |
| sonar-operator.enable | bool | `true` |  |
| sonar.createNamespace | bool | `true` |  |
| sonar.enable | bool | `true` |  |
| storage-class.enable | bool | `true` |  |
| tekton.createNamespace | bool | `true` |  |
| tekton.enable | bool | `true` |  |
| vault-kms.createNamespace | bool | `true` |  |
| vault-kms.enable | bool | `false` |  |
| vault-okd.createNamespace | bool | `true` |  |
| vault-okd.enable | bool | `true` |  |
| vault.createNamespace | bool | `true` |  |
| vault.enable | bool | `true` |  |

