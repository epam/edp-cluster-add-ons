# kyverno

![Version: 3.9.0](https://img.shields.io/badge/Version-3.9.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.19.0](https://img.shields.io/badge/AppVersion-1.19.0-informational?style=flat-square)

A Helm chart for Kyverno policy engine

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://kyverno.github.io/kyverno | kyverno | 3.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| kyverno.admissionController.replicas | int | `1` |  |
| kyverno.admissionController.resources.limits.memory | string | `"512Mi"` |  |
| kyverno.admissionController.resources.requests.cpu | string | `"100m"` |  |
| kyverno.admissionController.resources.requests.memory | string | `"128Mi"` |  |
| kyverno.backgroundController.enabled | bool | `false` |  |
| kyverno.cleanupController.enabled | bool | `false` |  |
| kyverno.crds.install | bool | `true` |  |
| kyverno.reportsController.enabled | bool | `false` |  |

