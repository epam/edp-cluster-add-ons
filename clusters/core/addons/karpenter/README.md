# karpenter

![Version: 1.6.1](https://img.shields.io/badge/Version-1.6.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.6.1](https://img.shields.io/badge/AppVersion-1.6.1-informational?style=flat-square)

A Helm chart for karpenter

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://public.ecr.aws/karpenter | karpenter | 1.6.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| karpenter.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[0].matchExpressions[0].key | string | `"karpenter.sh/nodepool"` |  |
| karpenter.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[0].matchExpressions[0].operator | string | `"DoesNotExist"` |  |
| karpenter.controller.resources.limits.cpu | int | `1` |  |
| karpenter.controller.resources.limits.memory | string | `"1Gi"` |  |
| karpenter.controller.resources.requests.cpu | int | `1` |  |
| karpenter.controller.resources.requests.memory | string | `"1Gi"` |  |
| karpenter.replicas | int | `1` |  |
| karpenter.serviceAccount | object | `{"annotations":{"eks.amazonaws.com/role-arn":"arn:aws:iam::0123456789:role/KarpenterControllerRole-<ClusterName>"}}` | Karpenter IAM role to manage cluster nodes |
| karpenter.settings | object | `{"clusterName":"cluster_name"}` | EKS cluster name |

