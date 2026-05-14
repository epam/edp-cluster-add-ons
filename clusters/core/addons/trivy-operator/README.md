# trivy-operator

![Version: 0.31.0](https://img.shields.io/badge/Version-0.31.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.29.0](https://img.shields.io/badge/AppVersion-0.29.0-informational?style=flat-square)

A Helm chart for Trivy Operator - Kubernetes-native security toolkit

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://aquasecurity.github.io/helm-charts/ | trivy-operator | 0.31.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| trivy-operator.compliance.specs[0] | string | `"eks-cis-1.4"` |  |
| trivy-operator.compliance.specs[1] | string | `"k8s-nsa-1.0"` |  |
| trivy-operator.compliance.specs[2] | string | `"k8s-pss-baseline-0.1"` |  |
| trivy-operator.compliance.specs[3] | string | `"k8s-pss-restricted-0.1"` |  |
| trivy-operator.excludeNamespaces | string | `"kube-system,kube-public,kube-node-lease,trivy-system,sentinel,edp-delivery"` |  |
| trivy-operator.nodeCollector.useNodeSelector | bool | `false` |  |
| trivy-operator.operator.accessGlobalSecretsAndServiceAccount | bool | `false` |  |
| trivy-operator.operator.builtInTrivyServer | bool | `true` |  |
| trivy-operator.operator.cacheReportTTL | string | `"168h"` |  |
| trivy-operator.operator.clusterSbomCacheEnabled | bool | `true` |  |
| trivy-operator.operator.privateRegistryScanSecretsNames.trivy-system | string | `"docker-pull"` |  |
| trivy-operator.operator.sbomGenerationEnabled | bool | `true` |  |
| trivy-operator.operator.scanJobsConcurrentLimit | int | `3` |  |
| trivy-operator.operator.scanJobsInSameNamespace | bool | `false` |  |
| trivy-operator.operator.scannerReportTTL | string | `"168h"` |  |
| trivy-operator.targetNamespaces | string | `"argocd"` |  |
| trivy-operator.trivy.ignoreUnfixed | bool | `true` |  |
| trivy-operator.trivy.severity | string | `"HIGH,CRITICAL"` |  |
| trivy-operator.trivy.supportedConfigAuditKinds | string | `"Workload,Service,Role,ClusterRole,Ingress"` |  |

