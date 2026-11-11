# trivy-operator

![Version: 0.37.0](https://img.shields.io/badge/Version-0.37.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.35.0](https://img.shields.io/badge/AppVersion-0.35.0-informational?style=flat-square)

A Helm chart for Trivy Operator - Kubernetes-native security toolkit

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://aquasecurity.github.io/helm-charts/ | trivy-operator | 0.37.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| trivy-operator.compliance.specs[0] | string | `"eks-cis-1.4"` |  |
| trivy-operator.compliance.specs[1] | string | `"k8s-nsa-1.0"` |  |
| trivy-operator.compliance.specs[2] | string | `"k8s-pss-baseline-0.1"` |  |
| trivy-operator.compliance.specs[3] | string | `"k8s-pss-restricted-0.1"` |  |
| trivy-operator.excludeNamespaces | string | `"kube-system,kube-public,kube-node-lease,trivy-system,sentinel,krci"` |  |
| trivy-operator.nodeCollector.useNodeSelector | bool | `false` |  |
| trivy-operator.operator.accessGlobalSecretsAndServiceAccount | bool | `false` |  |
| trivy-operator.operator.builtInTrivyServer | bool | `true` |  |
| trivy-operator.operator.clusterSbomCacheEnabled | bool | `false` |  |
| trivy-operator.operator.sbomGenerationEnabled | bool | `false` |  |
| trivy-operator.operator.scanJobsConcurrentLimit | int | `3` |  |
| trivy-operator.operator.scannerReportTTL | string | `"168h"` |  |
| trivy-operator.targetNamespaces | string | `""` |  |
| trivy-operator.trivy.command | string | `"rootfs"` |  |
| trivy-operator.trivy.ignoreUnfixed | bool | `true` |  |
| trivy-operator.trivy.severity | string | `"HIGH,CRITICAL"` |  |
| trivy-operator.trivy.supportedConfigAuditKinds | string | `"Workload,Service,Role,ClusterRole,Ingress"` |  |
| trivy-operator.trivyOperator.scanJobPodTemplateContainerSecurityContext.allowPrivilegeEscalation | bool | `false` |  |
| trivy-operator.trivyOperator.scanJobPodTemplateContainerSecurityContext.capabilities.drop[0] | string | `"ALL"` |  |
| trivy-operator.trivyOperator.scanJobPodTemplateContainerSecurityContext.privileged | bool | `false` |  |
| trivy-operator.trivyOperator.scanJobPodTemplateContainerSecurityContext.readOnlyRootFilesystem | bool | `true` |  |
| trivy-operator.trivyOperator.scanJobPodTemplateContainerSecurityContext.runAsNonRoot | bool | `true` |  |
| trivy-operator.trivyOperator.scanJobPodTemplateContainerSecurityContext.runAsUser | int | `65534` |  |
| trivy-operator.trivyOperator.scanJobPodTemplatePodSecurityContext.runAsGroup | int | `65534` |  |
| trivy-operator.trivyOperator.scanJobPodTemplatePodSecurityContext.runAsNonRoot | bool | `true` |  |
| trivy-operator.trivyOperator.scanJobPodTemplatePodSecurityContext.runAsUser | int | `65534` |  |
| trivy-operator.trivyOperator.scanJobPodTemplatePodSecurityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| trivy-operator.trivyOperator.scanJobsInSameNamespace | bool | `false` |  |

