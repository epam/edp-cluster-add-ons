# capsule

![Version: 0.14.3](https://img.shields.io/badge/Version-0.14.3-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.14.3](https://img.shields.io/badge/AppVersion-0.14.3-informational?style=flat-square)

A Helm chart for capsule

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://projectcapsule.github.io/charts | capsule | 0.14.3 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| capsule.certManager.generateCertificates | bool | `false` |  |
| capsule.customAnnotations.release | string | `"capsule"` |  |
| capsule.manager.options.users[0].kind | string | `"Group"` |  |
| capsule.manager.options.users[0].name | string | `"projectcapsule.dev"` |  |
| capsule.manager.options.users[1].kind | string | `"Group"` |  |
| capsule.manager.options.users[1].name | string | `"capsule.clastix.io"` |  |
| capsule.manager.options.users[2].kind | string | `"Group"` |  |
| capsule.manager.options.users[2].name | string | `"system:serviceaccounts:krci"` |  |
| capsule.manager.resources.limits.cpu | string | `"500m"` |  |
| capsule.manager.resources.limits.memory | string | `"512Mi"` |  |
| capsule.manager.resources.requests.cpu | string | `"200m"` |  |
| capsule.manager.resources.requests.memory | string | `"128Mi"` |  |
| capsule.tls.create | bool | `true` |  |
| capsule.tls.enableController | bool | `true` |  |
| capsule.tolerations[0].operator | string | `"Exists"` |  |
| capsule.webhooks.hooks.metadata.matchConditions[0].expression | string | `"!has(request.subResource) || request.subResource == \"\""` |  |
| capsule.webhooks.hooks.metadata.matchConditions[0].name | string | `"ignore-subresources"` |  |
| capsule.webhooks.hooks.metadata.matchConditions[1].expression | string | `"request.resource.resource != \"events\""` |  |
| capsule.webhooks.hooks.metadata.matchConditions[1].name | string | `"ignore-events"` |  |
| capsule.webhooks.hooks.metadata.matchConditions[2].expression | string | `"request.operation != \"UPDATE\" || !has(object.metadata.deletionTimestamp)"` |  |
| capsule.webhooks.hooks.metadata.matchConditions[2].name | string | `"skip-objects-being-deleted"` |  |

