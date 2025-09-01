# prometheus-blackbox-exporter

![Version: 11.3.1](https://img.shields.io/badge/Version-11.3.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v0.27.0](https://img.shields.io/badge/AppVersion-v0.27.0-informational?style=flat-square)

This chart wraps the official [prometheus-blackbox-exporter](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-blackbox-exporter) Helm chart.

## Configuration

Configuration values for the `prometheus-blackbox-exporter` chart can be set in the `values.yaml` file under the `prometheus-blackbox-exporter` key.

Refer to the official chart documentation for all available configuration options.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://prometheus-community.github.io/helm-charts | prometheus-blackbox-exporter | 11.3.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| prometheus-blackbox-exporter.config.modules.http_2xx.http.follow_redirects | bool | `true` |  |
| prometheus-blackbox-exporter.config.modules.http_2xx.http.preferred_ip_protocol | string | `"ip4"` |  |
| prometheus-blackbox-exporter.config.modules.http_2xx.http.valid_http_versions[0] | string | `"HTTP/1.1"` |  |
| prometheus-blackbox-exporter.config.modules.http_2xx.http.valid_http_versions[1] | string | `"HTTP/2.0"` |  |
| prometheus-blackbox-exporter.config.modules.http_2xx.prober | string | `"http"` |  |
| prometheus-blackbox-exporter.config.modules.http_2xx.timeout | string | `"5s"` |  |
