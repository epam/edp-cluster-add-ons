# minio-operator

![Version: 7.1.1](https://img.shields.io/badge/Version-7.1.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v7.1.1](https://img.shields.io/badge/AppVersion-v7.1.1-informational?style=flat-square)

A Helm chart for Minio Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://operator.min.io/ | operator | 7.1.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| operator.resources.limits.cpu | string | `"100m"` |  |
| operator.resources.limits.memory | string | `"128Mi"` |  |
| operator.resources.requests.cpu | string | `"100m"` |  |
| operator.resources.requests.memory | string | `"128Mi"` |  |

