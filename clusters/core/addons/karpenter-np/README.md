# karpenter-np

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

A Helm chart for karpenter

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| amiID | string | `"ami-XXXXXXXXXXXXXXXXX"` | AMI that used by nodes in EKS cluster |
| clusterName | string | `"cluster-name"` | EKS cluster name, must be the same as in Karpenter configuration |
| instanceType.category[0] | string | `"m"` |  |
| instanceType.family[0] | string | `"m7i"` |  |
| instanceType.size[0] | string | `"xlarge"` |  |
| instanceType.type[0] | string | `"on-demand"` |  |
| karpenter.nodeSelector | object | `{}` |  |
| karpenter.tolerations | list | `[]` |  |

