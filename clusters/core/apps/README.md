# edp-cluster-add-ons

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

EDP Cluster Addons that extend the Kubernetes Cluster Functionality

**Homepage:** <https://docs.kuberocketci.io/>

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
| argo-cd | object | `{"createNamespace":false,"enable":false,"namespace":"krci"}` | ArgoCD Deployment |
| argo-cd.createNamespace | bool | `false` | whether to create the namespace or not |
| argoProject | string | `"core"` |  |
| atlantis.createNamespace | bool | `false` |  |
| atlantis.enable | bool | `false` |  |
| atlantis.namespace | string | `"atlantis"` |  |
| aws-efs-csi-driver | object | `{"enable":false,"namespace":"kube-system"}` | AWS EFS CSI Driver |
| awx-operator.createNamespace | bool | `false` |  |
| awx-operator.enable | bool | `false` |  |
| awx-operator.namespace | string | `"awx-operator"` |  |
| capsule | object | `{"createNamespace":false,"enable":false,"namespace":"capsule-system"}` | Capsule |
| capsule-tenant | object | `{"enable":false,"namespace":"capsule-system"}` | Capsule Tenant |
| capsule.createNamespace | bool | `false` | whether to create the namespace or not |
| cert-manager | object | `{"createNamespace":false,"enable":false,"namespace":"cert-manager"}` | Cert Manager |
| cert-manager.createNamespace | bool | `false` | whether to create the namespace or not |
| clusterName | string | `"core"` |  |
| defectdojo | object | `{"createNamespace":false,"enable":false,"namespace":"defectdojo"}` | DefectDojo |
| defectdojo.createNamespace | bool | `false` | whether to create the namespace or not |
| dependency-track.createNamespace | bool | `false` |  |
| dependency-track.enable | bool | `false` |  |
| dependency-track.namespace | string | `"dependency-track"` |  |
| destinationServer | string | `"in-cluster"` |  |
| external-secrets.createNamespace | bool | `false` |  |
| external-secrets.enable | bool | `false` |  |
| external-secrets.namespace | string | `"external-secrets"` |  |
| fluent-bit.createNamespace | bool | `false` |  |
| fluent-bit.enable | bool | `false` |  |
| fluent-bit.namespace | string | `"logging"` |  |
| gitfusion.createNamespace | bool | `false` |  |
| gitfusion.enable | bool | `false` |  |
| gitfusion.namespace | string | `"krci"` |  |
| harbor-ha-okd.createNamespace | bool | `false` |  |
| harbor-ha-okd.enable | bool | `false` |  |
| harbor-ha-okd.namespace | string | `"harbor"` |  |
| harbor-ha.createNamespace | bool | `false` |  |
| harbor-ha.enable | bool | `false` |  |
| harbor-ha.namespace | string | `"harbor"` |  |
| harbor.createNamespace | bool | `false` |  |
| harbor.enable | bool | `false` |  |
| harbor.namespace | string | `"harbor"` |  |
| ingress-nginx-external.createNamespace | bool | `false` |  |
| ingress-nginx-external.enable | bool | `false` |  |
| ingress-nginx-external.namespace | string | `"ingress-nginx-external"` |  |
| ingress-nginx.createNamespace | bool | `false` |  |
| ingress-nginx.enable | bool | `false` |  |
| ingress-nginx.namespace | string | `"ingress-nginx"` |  |
| jaeger-operator.createNamespace | bool | `false` |  |
| jaeger-operator.enable | bool | `false` |  |
| jaeger-operator.namespace | string | `"jaeger-operator"` |  |
| karma-dashboard.createNamespace | bool | `false` |  |
| karma-dashboard.enable | bool | `false` |  |
| karma-dashboard.namespace | string | `"monitoring"` |  |
| karpenter-np | object | `{"createNamespace":false,"enable":false,"namespace":"karpenter"}` | Application with Karpenter resources: NodePools and NodeClass |
| karpenter.createNamespace | bool | `false` |  |
| karpenter.enable | bool | `false` |  |
| karpenter.namespace | string | `"karpenter"` |  |
| keda-tenants | object | `{"createNamespace":false,"enable":false,"namespace":"keda"}` | Keda Job Scaler for KRCI deployments |
| keda.createNamespace | bool | `false` |  |
| keda.enable | bool | `false` |  |
| keda.namespace | string | `"keda"` |  |
| keycloak-operator.createNamespace | bool | `false` |  |
| keycloak-operator.enable | bool | `false` |  |
| keycloak-operator.namespace | string | `"keycloak-operator"` |  |
| keycloak-postgresql.createNamespace | bool | `false` |  |
| keycloak-postgresql.enable | bool | `false` |  |
| keycloak-postgresql.namespace | string | `"security"` |  |
| keycloak.createNamespace | bool | `false` |  |
| keycloak.enable | bool | `false` |  |
| keycloak.namespace | string | `"security"` |  |
| krakend.createNamespace | bool | `false` |  |
| krakend.enable | bool | `false` |  |
| krakend.namespace | string | `"krci-krakend"` |  |
| kuberocketci-pipelines.createNamespace | bool | `false` |  |
| kuberocketci-pipelines.enable | bool | `false` |  |
| kuberocketci-pipelines.namespace | string | `"krci"` |  |
| kuberocketci-pipelines.repoUrl | string | `"ssh://git@github.com:22/epmd-edp/helm-helm-pipeline.git"` |  |
| kuberocketci-rbac.createNamespace | bool | `false` |  |
| kuberocketci-rbac.enable | bool | `false` |  |
| kuberocketci-rbac.namespace | string | `"krci-security"` |  |
| kuberocketci.createNamespace | bool | `false` |  |
| kuberocketci.enable | bool | `false` |  |
| kuberocketci.namespace | string | `"krci"` |  |
| minio-operator.createNamespace | bool | `false` |  |
| minio-operator.enable | bool | `false` |  |
| minio-operator.namespace | string | `"minio-operator"` |  |
| moon.createNamespace | bool | `false` |  |
| moon.enable | bool | `false` |  |
| moon.namespace | string | `"moon"` |  |
| nexus-ce.createNamespace | bool | `false` |  |
| nexus-ce.enable | bool | `false` |  |
| nexus-ce.namespace | string | `"nexus"` |  |
| nexus-operator.createNamespace | bool | `false` |  |
| nexus-operator.enable | bool | `false` |  |
| nexus-operator.namespace | string | `"nexus"` |  |
| nexus.createNamespace | bool | `false` |  |
| nexus.enable | bool | `false` |  |
| nexus.namespace | string | `"nexus"` |  |
| oauth2-proxy.createNamespace | bool | `false` |  |
| oauth2-proxy.enable | bool | `false` |  |
| oauth2-proxy.namespace | string | `"oauth2-proxy"` |  |
| opensearch.createNamespace | bool | `false` |  |
| opensearch.enable | bool | `false` |  |
| opensearch.namespace | string | `"logging"` |  |
| opentelemetry-operator.createNamespace | bool | `false` |  |
| opentelemetry-operator.enable | bool | `false` |  |
| opentelemetry-operator.namespace | string | `"opentelemetry-operator"` |  |
| pgadmin.createNamespace | bool | `false` |  |
| pgadmin.enable | bool | `false` |  |
| pgadmin.namespace | string | `"pgadmin"` |  |
| postgres-operator.createNamespace | bool | `false` |  |
| postgres-operator.enable | bool | `false` |  |
| postgres-operator.namespace | string | `"postgres-operator"` |  |
| prometheus-blackbox-exporter.createNamespace | bool | `false` |  |
| prometheus-blackbox-exporter.enable | bool | `false` |  |
| prometheus-blackbox-exporter.namespace | string | `"monitoring"` |  |
| prometheus-operator.createNamespace | bool | `false` |  |
| prometheus-operator.enable | bool | `false` |  |
| prometheus-operator.namespace | string | `"monitoring"` |  |
| redis-operator.createNamespace | bool | `false` |  |
| redis-operator.enable | bool | `false` |  |
| redis-operator.namespace | string | `"redis-operator"` |  |
| repoUrl | string | `"ssh://git@github.com:22/kuberocketci/edp-cluster-add-ons"` |  |
| report-portal.createNamespace | bool | `false` |  |
| report-portal.enable | bool | `false` |  |
| report-portal.namespace | string | `"report-portal"` |  |
| sonar-operator.createNamespace | bool | `false` |  |
| sonar-operator.enable | bool | `false` |  |
| sonar-operator.namespace | string | `"sonar"` |  |
| sonar.createNamespace | bool | `false` |  |
| sonar.enable | bool | `false` |  |
| sonar.namespace | string | `"sonar"` |  |
| storage-class.enable | bool | `false` |  |
| targetRevision | string | `"main"` |  |
| tekton-cache.createNamespace | bool | `false` |  |
| tekton-cache.enable | bool | `false` |  |
| tekton-cache.namespace | string | `"tekton-cache"` |  |
| tekton-custom-task.createNamespace | bool | `false` |  |
| tekton-custom-task.enable | bool | `false` |  |
| tekton-custom-task.namespace | string | `"krci"` |  |
| tekton-dashboard.createNamespace | bool | `false` |  |
| tekton-dashboard.enable | bool | `false` |  |
| tekton-dashboard.namespace | string | `"krci"` |  |
| tekton.createNamespace | bool | `false` |  |
| tekton.enable | bool | `false` |  |
| tekton.namespace | string | `"tekton-pipelines"` |  |
| vault-kms.createNamespace | bool | `false` |  |
| vault-kms.enable | bool | `false` |  |
| vault-kms.namespace | string | `"vault"` |  |
| vault-okd.createNamespace | bool | `false` |  |
| vault-okd.enable | bool | `false` |  |
| vault-okd.namespace | string | `"vault"` |  |
| vault-operator.createNamespace | bool | `false` |  |
| vault-operator.enable | bool | `false` |  |
| vault-operator.namespace | string | `"vault"` |  |
| vault.createNamespace | bool | `false` |  |
| vault.enable | bool | `false` |  |
| vault.namespace | string | `"vault"` |  |

