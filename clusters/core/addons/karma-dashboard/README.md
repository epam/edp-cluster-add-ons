# karma

![Version: 2.13.1](https://img.shields.io/badge/Version-2.13.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v0.131](https://img.shields.io/badge/AppVersion-v0.131-informational?style=flat-square)

A Helm chart for Karma - an UI for Prometheus Alertmanager

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://wiremind.github.io/wiremind-helm-charts | karma | 2.13.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| karma.env[0].name | string | `"ALERTMANAGER_URI"` |  |
| karma.env[0].value | string | `"http://prom-alertmanager.monitoring.svc:9093/"` |  |
| karma.ingress.enabled | bool | `true` |  |
| karma.ingress.hosts[0] | string | `"karma-dashboard.example.com"` |  |
| karma.ingress.path | string | `"/"` |  |

