# opentelemetry-operator

![Version: 0.95.1](https://img.shields.io/badge/Version-0.95.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.134.0](https://img.shields.io/badge/AppVersion-0.134.0-informational?style=flat-square)

A Helm chart for Open Telemetry Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://open-telemetry.github.io/opentelemetry-helm-charts | opentelemetry-operator | 0.95.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| opentelemetry-operator.fullnameOverride | string | `"opentelemetry-operator"` |  |
| opentelemetry-operator.manager.collectorImage.repository | string | `"otel/opentelemetry-collector-k8s"` |  |

