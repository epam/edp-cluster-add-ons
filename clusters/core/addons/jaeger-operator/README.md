# jaeger-operator

![Version: 2.57.0](https://img.shields.io/badge/Version-2.57.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.61.0](https://img.shields.io/badge/AppVersion-1.61.0-informational?style=flat-square)

A Helm chart for Jaeger Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://jaegertracing.github.io/helm-charts | jaeger-operator | 2.57.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| jaeger-operator.fullnameOverride | string | `"jaeger-operator"` |  |
| jaeger-operator.jaeger.create | bool | `true` |  |
| jaeger-operator.jaeger.spec.ingress.annotations."nginx.ingress.kubernetes.io/auth-signin" | string | `"https://oauth-edp.example.com/oauth2/start?rd=https://$host$request_uri"` |  |
| jaeger-operator.jaeger.spec.ingress.annotations."nginx.ingress.kubernetes.io/auth-url" | string | `"http://oauth2-proxy.edp.svc.cluster.local:8080/oauth2/auth"` |  |
| jaeger-operator.jaeger.spec.ingress.enabled | bool | `true` |  |
| jaeger-operator.jaeger.spec.ingress.hosts[0] | string | `"jaeger.example.com"` |  |

