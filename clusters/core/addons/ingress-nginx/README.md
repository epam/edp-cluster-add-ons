# ingress-nginx

![Version: 4.13.2](https://img.shields.io/badge/Version-4.13.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.13.2](https://img.shields.io/badge/AppVersion-1.13.2-informational?style=flat-square)

A Helm chart for Nginx Ingress Controller

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://kubernetes.github.io/ingress-nginx | ingress-nginx | 4.13.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| ingress-nginx.controller.addHeaders.Strict-Transport-Security | string | `"max-age=63072000; includeSubDomains"` |  |
| ingress-nginx.controller.addHeaders.X-Content-Type-Options | string | `"nosniff"` |  |
| ingress-nginx.controller.addHeaders.X-Frame-Options | string | `"SAMEORIGIN"` |  |
| ingress-nginx.controller.allowSnippetAnnotations | bool | `true` |  |
| ingress-nginx.controller.config.client-header-buffer-size | string | `"64k"` |  |
| ingress-nginx.controller.config.http2-max-field-size | string | `"64k"` |  |
| ingress-nginx.controller.config.http2-max-header-size | string | `"64k"` |  |
| ingress-nginx.controller.config.keep-alive | string | `"10"` |  |
| ingress-nginx.controller.config.large-client-header-buffers | string | `"4 64k"` |  |
| ingress-nginx.controller.config.proxy-buffer-size | string | `"8k"` |  |
| ingress-nginx.controller.config.proxy-real-ip-cidr | string | `"192.168.0.0/20"` |  |
| ingress-nginx.controller.config.ssl-redirect | string | `"true"` |  |
| ingress-nginx.controller.config.upstream-keepalive-timeout | string | `"120"` |  |
| ingress-nginx.controller.config.use-forwarded-headers | string | `"true"` |  |
| ingress-nginx.controller.metrics.enabled | bool | `true` |  |
| ingress-nginx.controller.metrics.serviceMonitor.additionalLabels.release | string | `"prometheus"` |  |
| ingress-nginx.controller.metrics.serviceMonitor.enabled | bool | `true` |  |
| ingress-nginx.controller.podAnnotations."fluentbit.io/parser" | string | `"k8s-nginx-ingress"` |  |
| ingress-nginx.controller.resources.limits.memory | string | `"256Mi"` |  |
| ingress-nginx.controller.resources.requests.cpu | string | `"50m"` |  |
| ingress-nginx.controller.resources.requests.memory | string | `"128M"` |  |
| ingress-nginx.controller.service.nodePorts.http | int | `32080` |  |
| ingress-nginx.controller.service.nodePorts.https | int | `32443` |  |
| ingress-nginx.controller.service.type | string | `"NodePort"` |  |
| ingress-nginx.controller.watchIngressWithoutClass | bool | `true` |  |
| ingress-nginx.defaultBackend.enabled | bool | `true` |  |
| ingress-nginx.serviceAccount.create | bool | `true` |  |
| ingress-nginx.serviceAccount.name | string | `"nginx-ingress-service-account"` |  |
| ingress-nginx.updateStrategy.rollingUpdate.maxUnavailable | int | `1` |  |
| ingress-nginx.updateStrategy.type | string | `"RollingUpdate"` |  |

