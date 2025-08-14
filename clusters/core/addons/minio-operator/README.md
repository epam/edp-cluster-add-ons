# minio-operator

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 7.1.1](https://img.shields.io/badge/AppVersion-7.1.1-informational?style=flat-square)

A Helm chart for Minio Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://operator.min.io/ | operator | 7.1.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| operator.fullnameOverride | string | `"minio-operator"` |  |
| operator.nameOverride | string | `"minio-operator"` |  |
| operator.resources.limits.cpu | string | `"100m"` |  |
| operator.resources.limits.memory | string | `"128Mi"` |  |
| operator.resources.requests.cpu | string | `"100m"` |  |
| operator.resources.requests.memory | string | `"128Mi"` |  |

