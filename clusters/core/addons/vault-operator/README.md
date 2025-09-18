# vault-operator

![Version: 1.23.0](https://img.shields.io/badge/Version-1.23.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.23.0](https://img.shields.io/badge/AppVersion-1.23.0-informational?style=flat-square)

A Helm chart for Vault Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://ghcr.io/bank-vaults/helm-charts | vault-operator | 1.23.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| vault-operator.affinity | object | `{"podAntiAffinity":{"requiredDuringSchedulingIgnoredDuringExecution":[{"labelSelector":{"matchLabels":{"app.kubernetes.io/instance":"vault-operator","app.kubernetes.io/name":"vault-operator"}},"topologyKey":"kubernetes.io/hostname"}]}}` | [Affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#affinity-and-anti-affinity) configuration. See the [API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling) for details. |
| vault-operator.bankVaults.image.repository | string | `"ghcr.io/bank-vaults/bank-vaults"` | Bank-Vaults image repository. |
| vault-operator.bankVaults.image.tag | string | `"v1.31.3"` | Bank-Vaults image tag (pinned to supported Bank-Vaults version). |
| vault-operator.crdAnnotations | object | `{}` | Annotations to be added to CRDs. |
| vault-operator.fullnameOverride | string | `""` | A name to substitute for the full names of resources. |
| vault-operator.image.bankVaultsRepository | string | `""` | Bank-Vaults image repository **Deprecated:** use `bankVaults.image.repository` instead. |
| vault-operator.image.bankVaultsTag | string | `""` | Bank-Vaults image tag **Deprecated:** use `bankVaults.image.tag` instead. |
| vault-operator.image.imagePullSecrets | list | `[]` | Reference to one or more secrets to be used when [pulling images](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#create-a-pod-that-uses-your-secret) (from private registries). (`global.imagePullSecrets` is also supported) |
| vault-operator.image.pullPolicy | string | `"IfNotPresent"` | [Image pull policy](https://kubernetes.io/docs/concepts/containers/images/#updating-images) for updating already existing images on a node. |
| vault-operator.image.repository | string | `"ghcr.io/bank-vaults/vault-operator"` | Name of the image repository to pull the container image from. |
| vault-operator.image.tag | string | `""` | Image tag override for the default value (chart appVersion). |
| vault-operator.labels | object | `{}` | Labels to be added to deployments. |
| vault-operator.livenessProbe.initialDelaySeconds | int | `60` |  |
| vault-operator.livenessProbe.periodSeconds | int | `10` |  |
| vault-operator.livenessProbe.successThreshold | int | `1` |  |
| vault-operator.livenessProbe.timeoutSeconds | int | `1` |  |
| vault-operator.monitoring.serviceMonitor.additionalLabels | object | `{}` |  |
| vault-operator.monitoring.serviceMonitor.enabled | bool | `false` | Enable Prometheus ServiceMonitor. See the [documentation](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/design.md#servicemonitor) and the [API reference](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api.md#servicemonitor) for details. |
| vault-operator.monitoring.serviceMonitor.metricRelabelings | list | `[]` |  |
| vault-operator.monitoring.serviceMonitor.relabelings | list | `[]` |  |
| vault-operator.nameOverride | string | `""` | A name in place of the chart name for `app:` labels. |
| vault-operator.nodeSelector | object | `{}` | [Node selector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) configuration. |
| vault-operator.pdb.create | bool | `true` | Create pod disruption budget if replicaCount > 1. |
| vault-operator.pdb.minAvailable | int | `1` | Min available for PDB. |
| vault-operator.podAnnotations | object | `{}` | Annotations to be added to pods. |
| vault-operator.podLabels | object | `{}` | Labels to be added to pods. |
| vault-operator.podSecurityContext | object | `{}` | Pod [security context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-pod). See the [API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context) for details. |
| vault-operator.priorityClassName | string | `""` | Specify a priority class name to set [pod priority](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority). |
| vault-operator.psp.enabled | bool | `false` |  |
| vault-operator.psp.vaultSA | string | `"vault"` |  |
| vault-operator.readinessProbe.periodSeconds | int | `10` |  |
| vault-operator.readinessProbe.successThreshold | int | `1` |  |
| vault-operator.readinessProbe.timeoutSeconds | int | `1` |  |
| vault-operator.replicaCount | int | `2` | Number of replicas (pods) to launch. |
| vault-operator.resources | object | `{"limits":{"memory":"512Mi"},"requests":{"cpu":"100m","memory":"128Mi"}}` | Container resource [requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/). See the [API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#resources) for details. |
| vault-operator.securityContext | object | `{}` | Container [security context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-the-security-context-for-a-container). See the [API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context-1) for details. |
| vault-operator.service.annotations | object | `{}` | Annotations to be added to the service. |
| vault-operator.service.externalPort | int | `80` |  |
| vault-operator.service.internalPort | int | `8080` |  |
| vault-operator.service.name | string | `""` | The name of the service to use. If not set, a name is generated using the fullname template. |
| vault-operator.service.type | string | `"ClusterIP"` | Kubernetes [service type](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types). |
| vault-operator.serviceAccount.annotations | object | `{}` | Annotations to be added to the service account. |
| vault-operator.serviceAccount.create | bool | `true` | Enable service account creation. |
| vault-operator.serviceAccount.name | string | `""` | The name of the service account to use. If not set and create is true, a name is generated using the fullname template. |
| vault-operator.syncPeriod | string | `"5m"` |  |
| vault-operator.terminationGracePeriodSeconds | int | `10` |  |
| vault-operator.tolerations | list | `[]` | [Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) for node taints. See the [API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#scheduling) for details. |
| vault-operator.watchNamespace | string | `"vault"` | The namespace where the operator watches for vault CR objects. If not defined all namespaces are watched. |

