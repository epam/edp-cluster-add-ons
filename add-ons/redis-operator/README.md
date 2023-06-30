# redis-operator

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.2.8](https://img.shields.io/badge/AppVersion-3.2.8-informational?style=flat-square)

A Helm chart for Redis Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://spotahome.github.io/redis-operator | redis-operator | 3.2.8 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| redis-operator.fullnameOverride | string | `"redis-operator"` |  |
| redis-operator.nameOverride | string | `"redis-operator"` |  |
| redis-operator.resources.limits.cpu | string | `"100m"` |  |
| redis-operator.resources.limits.memory | string | `"128Mi"` |  |
| redis-operator.resources.requests.cpu | string | `"100m"` |  |
| redis-operator.resources.requests.memory | string | `"128Mi"` |  |

