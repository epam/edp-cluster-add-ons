# karpenter-np

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

A Helm chart for karpenter

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| amiID | string | `"ami-XXXXXXXXXXXXXXXXX"` | AMI that used by nodes in EKS cluster |
| clusterName | string | `"eks"` | EKS cluster name, must be the same as in Karpenter configuration |
| cronjob | object | `{"enabled":false,"endTime":"00 18 * * *","startTime":"00 9 * * *"}` | This block enable CronJob to create and delete nodepool |
| instanceType.category[0] | string | `"m"` |  |
| instanceType.category[1] | string | `"c"` |  |
| instanceType.category[2] | string | `"r"` |  |
| instanceType.family[0] | string | `"m5"` |  |
| instanceType.family[1] | string | `"c5"` |  |
| instanceType.family[2] | string | `"r5"` |  |
| instanceType.size[0] | string | `"xlarge"` |  |
| instanceType.size[1] | string | `"2xlarge"` |  |
| instanceType.size[2] | string | `"4xlarge"` |  |
| instanceType.type[0] | string | `"on-demand"` |  |
| instanceType.type[1] | string | `"spot"` |  |
| karpenter.nodeSelector | object | `{}` |  |
| karpenter.tolerations | list | `[]` |  |

