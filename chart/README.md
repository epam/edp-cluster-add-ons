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
| atlantis.createNamespace | bool | `false` |  |
| atlantis.enable | bool | `false` |  |
| aws-efs-csi-driver | object | `{"enable":false}` | AWS EFS CSI Driver |
| capsule | object | `{"createNamespace":false,"enable":false}` | Capsule |
| capsule-tenant | object | `{"enable":false}` | Capsule Tenant |
| capsule.createNamespace | bool | `false` | whether to create the namespace or not |
| cert-manager | object | `{"createNamespace":false,"enable":false}` | Cert Manager |
| cert-manager.createNamespace | bool | `false` | whether to create the namespace or not |
| defectdojo | object | `{"createNamespace":false,"enable":false}` | DefectDojo |
| defectdojo.createNamespace | bool | `false` | whether to create the namespace or not |
| dependency-track.createNamespace | bool | `false` |  |
| dependency-track.enable | bool | `false` |  |
| destinationServer | string | `"in-cluster"` |  |
| edp.createNamespace | bool | `false` |  |
| edp.enable | bool | `false` |  |
| external-secrets.createNamespace | bool | `false` |  |
| external-secrets.enable | bool | `false` |  |
| fluent-bit.createNamespace | bool | `false` |  |
| fluent-bit.enable | bool | `false` |  |
| harbor-ha-okd.createNamespace | bool | `false` |  |
| harbor-ha-okd.enable | bool | `false` |  |
| harbor-ha.createNamespace | bool | `false` |  |
| harbor-ha.enable | bool | `false` |  |
| harbor.createNamespace | bool | `false` |  |
| harbor.enable | bool | `false` |  |
| ingress-nginx-external.createNamespace | bool | `false` |  |
| ingress-nginx-external.enable | bool | `false` |  |
| ingress-nginx.createNamespace | bool | `false` |  |
| ingress-nginx.enable | bool | `false` |  |
| jaeger-operator.createNamespace | bool | `false` |  |
| jaeger-operator.enable | bool | `false` |  |
| keycloak-operator.createNamespace | bool | `false` |  |
| keycloak-operator.enable | bool | `false` |  |
| keycloak-postgresql.createNamespace | bool | `false` |  |
| keycloak-postgresql.enable | bool | `false` |  |
| keycloak.createNamespace | bool | `false` |  |
| keycloak.enable | bool | `false` |  |
| krakend.createNamespace | bool | `false` |  |
| krakend.enable | bool | `false` |  |
| kuberocketci-rbac.createNamespace | bool | `false` |  |
| kuberocketci-rbac.enable | bool | `false` |  |
| minio-operator.createNamespace | bool | `false` |  |
| minio-operator.enable | bool | `false` |  |
| nexus-operator.createNamespace | bool | `false` |  |
| nexus-operator.enable | bool | `false` |  |
| nexus.createNamespace | bool | `false` |  |
| nexus.enable | bool | `false` |  |
| oauth2-proxy.createNamespace | bool | `false` |  |
| oauth2-proxy.enable | bool | `false` |  |
| opensearch.createNamespace | bool | `false` |  |
| opensearch.enable | bool | `false` |  |
| opentelemetry-operator.createNamespace | bool | `false` |  |
| opentelemetry-operator.enable | bool | `false` |  |
| postgres-operator.createNamespace | bool | `false` |  |
| postgres-operator.enable | bool | `false` |  |
| prometheus-operator.createNamespace | bool | `false` |  |
| prometheus-operator.enable | bool | `false` |  |
| redis-operator.createNamespace | bool | `false` |  |
| redis-operator.enable | bool | `false` |  |
| repoUrl | string | `"ssh://ci@git.example.com:22/cluster-add-ons"` |  |
| report-portal.createNamespace | bool | `false` |  |
| report-portal.enable | bool | `false` |  |
| sonar-operator.createNamespace | bool | `false` |  |
| sonar-operator.enable | bool | `false` |  |
| sonar.createNamespace | bool | `false` |  |
| sonar.enable | bool | `false` |  |
| storage-class.enable | bool | `false` |  |
| targetRevision | string | `"main"` |  |
| tekton-cache.createNamespace | bool | `false` |  |
| tekton-cache.enable | bool | `false` |  |
| tekton.createNamespace | bool | `false` |  |
| tekton.enable | bool | `false` |  |
| vault-kms.createNamespace | bool | `false` |  |
| vault-kms.enable | bool | `false` |  |
| vault-okd.createNamespace | bool | `false` |  |
| vault-okd.enable | bool | `false` |  |
| vault.createNamespace | bool | `false` |  |
| vault.enable | bool | `false` |  |

