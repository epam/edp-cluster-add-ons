# kube-audit-rest

![Version: 1.0.26](https://img.shields.io/badge/Version-1.0.26-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.26](https://img.shields.io/badge/AppVersion-1.0.26-informational?style=flat-square)

A Helm chart for Kube Audit REST - a simple logger of mutation/creation requests to the k8s API

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| args | list | `["--logger-filename=/dev/stdout"]` | kube-audit-rest binary args |
| automountServiceAccountToken | bool | `false` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"ghcr.io/richardoc/kube-audit-rest"` |  |
| image.tag | string | `"1.0.26-distroless"` |  |
| metricsPort | int | `55555` | Prometheus metrics port |
| podSecurityContext.fsGroup | int | `255999` |  |
| podSecurityContext.runAsGroup | int | `255999` |  |
| podSecurityContext.runAsUser | int | `255999` |  |
| replicas | int | `1` |  |
| resources.limits.cpu | string | `"1"` |  |
| resources.limits.memory | string | `"32Mi"` |  |
| resources.requests.cpu | string | `"2m"` |  |
| resources.requests.memory | string | `"10Mi"` |  |
| securityContext.allowPrivilegeEscalation | bool | `false` |  |
| securityContext.capabilities.drop[0] | string | `"ALL"` |  |
| securityContext.readOnlyRootFilesystem | bool | `true` |  |
| serverPort | int | `9090` | HTTPS server port |
| service.port | int | `443` |  |
| service.type | string | `"ClusterIP"` |  |
| tls | object | `{"certManager":{"enabled":true,"issuerRef":{"kind":"Issuer","name":"selfsigned-issuer"}},"duration":"8760h","renewBefore":"720h"}` | TLS certificate configuration kube-audit-rest requires TLS for the webhook |
| tls.certManager | object | `{"enabled":true,"issuerRef":{"kind":"Issuer","name":"selfsigned-issuer"}}` | Use cert-manager to generate certificates |
| tls.duration | string | `"8760h"` | Certificate duration (e.g. 8760h = 1 year) |
| tls.renewBefore | string | `"720h"` | Certificate renew before expiry |
| tmpSizeLimit | string | `"2Gi"` | Volume size limit for audit log tmp storage |
| webhook | object | `{"failurePolicy":"Ignore","rules":[{"apiGroups":["*"],"apiVersions":["*"],"operations":["CREATE","UPDATE","DELETE"],"resources":["*/*"],"scope":"*"}],"timeoutSeconds":1}` | ValidatingWebhookConfiguration settings |
| webhook.failurePolicy | string | `"Ignore"` | Fail open so audit failures don't block API calls |
| webhook.rules | list | `[{"apiGroups":["*"],"apiVersions":["*"],"operations":["CREATE","UPDATE","DELETE"],"resources":["*/*"],"scope":"*"}]` | Rules for which API calls to audit |
| webhook.timeoutSeconds | int | `1` | Timeout in seconds for webhook calls |

