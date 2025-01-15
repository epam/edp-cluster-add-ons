# tekton-dashboard

![Version: 0.52.0](https://img.shields.io/badge/Version-0.52.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.52.0](https://img.shields.io/badge/AppVersion-0.52.0-informational?style=flat-square)

A Helm chart for tekton-dashboard

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dashboard.affinity | object | `{}` | Affinity settings for pod assignment |
| dashboard.image.repository | string | `"ghcr.io/tektoncd/dashboard/dashboard-9623576a202fe86c8b7d1bc489905f86"` | Define tekton dashboard docker image name |
| dashboard.image.tag | string | `"v0.52.0"` | Define tekton dashboard docker image tag |
| dashboard.ingress.annotations | object | `{}` | Annotations for Ingress resource |
| dashboard.ingress.enabled | bool | `true` | Enable external endpoint access. Default Ingress/Route host pattern: tekton-{{ .Release.Namespace }}.{{ .Values.global.dnsWildCard }} |
| dashboard.ingress.host | string | `""` | If not defined, it will be created by the pattern "tekton-[namespace].[global DNS wildcard]" |
| dashboard.ingress.tls | list | `[]` | If hosts not defined, they will be created by the pattern "tekton-[namespace].[global DNS wildcard]" |
| dashboard.nameOverride | string | `"tekton-dashboard"` |  |
| dashboard.nodeSelector | object | `{}` | Node labels for pod assignment |
| dashboard.openshift_proxy | object | `{"enabled":false,"image":{"repository":"quay.io/openshift/origin-oauth-proxy","tag":"4.9.0"},"resources":{"limits":{"cpu":"60m","memory":"70Mi"},"requests":{"cpu":"50m","memory":"40Mi"}}}` | For EKS scenario - uncomment dashboard.ingress.annotations block |
| dashboard.openshift_proxy.enabled | bool | `false` | Enable oauth-proxy to include authorization layer on tekton-dashboard. Default: false |
| dashboard.openshift_proxy.image.repository | string | `"quay.io/openshift/origin-oauth-proxy"` | oauth-proxy image repository |
| dashboard.openshift_proxy.image.tag | string | `"4.9.0"` | oauth-proxy image tag |
| dashboard.openshift_proxy.resources | object | `{"limits":{"cpu":"60m","memory":"70Mi"},"requests":{"cpu":"50m","memory":"40Mi"}}` | The resource limits and requests for the Tekton Proxy |
| dashboard.pipelinesNamespace | string | `"tekton-pipelines"` | Namespace where cluster tekton pipelines deployed. Default: tekton-pipelines |
| dashboard.quicklink.enabled | bool | `false` | Enable creation of quick link to the Tekton Dashboard. Default: false |
| dashboard.readOnly | bool | `false` | Define mode for Tekton Dashboard. Enable/disable capability to create/modify/remove Tekton objects via Tekton Dashboard. Default: false |
| dashboard.resources | object | `{"limits":{"cpu":"60m","memory":"70Mi"},"requests":{"cpu":"50m","memory":"40Mi"}}` | The resource limits and requests for the Tekton Dashboard |
| dashboard.tolerations | list | `[]` | Toleration labels for pod assignment |
| dashboard.triggersNamespace | string | `"tekton-pipelines"` | Namespace where cluster tekton triggers deployed. Default: tekton-pipelines |
| global.dnsWildCard | string | `""` | a cluster DNS wildcard name |
| global.platform | string | `"kubernetes"` | platform type that can be "kubernetes" or "openshift" |

