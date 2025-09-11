# capsule

![Version: 0.10.9](https://img.shields.io/badge/Version-0.10.9-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.10.9](https://img.shields.io/badge/AppVersion-0.10.9-informational?style=flat-square)

A Helm chart for capsule

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://projectcapsule.github.io/charts | capsule | 0.10.9 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| capsule.certManager.generateCertificates | bool | `false` |  |
| capsule.customAnnotations.release | string | `"capsule"` |  |
| capsule.manager.options.capsuleUserGroups[0] | string | `"capsule.clastix.io"` |  |
| capsule.manager.options.capsuleUserGroups[1] | string | `"system:serviceaccounts:krci"` |  |
| capsule.manager.resources.limits.cpu | string | `"500m"` |  |
| capsule.manager.resources.limits.memory | string | `"512Mi"` |  |
| capsule.manager.resources.requests.cpu | string | `"200m"` |  |
| capsule.manager.resources.requests.memory | string | `"128Mi"` |  |
| capsule.tls.create | bool | `true` |  |
| capsule.tls.enableController | bool | `true` |  |
| capsule.tolerations[0].operator | string | `"Exists"` |  |

