# argo-events

![Version: 2.4.23](https://img.shields.io/badge/Version-2.4.23-informational?style=flat-square) ![AppVersion: v1.9.11](https://img.shields.io/badge/AppVersion-v1.9.11-informational?style=flat-square)

A Helm chart for Argo Events — the event-driven automation framework used as the KubeRocketCI notification bus (Tekton CloudEvents ingestion, JetStream EventBus, and notification Sensors)

This add-on installs the [Argo Events](https://argoproj.github.io/argo-events/) engine for the
KubeRocketCI notification bus: the controller, CRDs, and (values-gated) the `default`
JetStream EventBus. It contains no KRCI-specific wiring — EventSources and Sensors are
managed by the `krci-events` add-on, which must be deployed into the same namespace.

Integration steps are documented at [docs.kuberocketci.io](https://docs.kuberocketci.io).

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://argoproj.github.io/argo-helm | argo-events | 2.4.23 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| argo-events.controller.metrics.enabled | bool | `false` | Expose controller metrics service |
| argo-events.controller.metrics.serviceMonitor.enabled | bool | `false` | Create a ServiceMonitor for the controller (requires prometheus-operator) |
| argo-events.controller.replicas | int | `1` | Number of controller replicas |
| argo-events.crds.install | bool | `true` | Install Argo Events CRDs with the chart |
| argo-events.crds.keep | bool | `true` | Keep CRDs on chart uninstall |
| eventBus.enabled | bool | `true` | Deploy the `default` JetStream EventBus |
| eventBus.jetstream.persistence.storageClassName | string | `""` | StorageClass for the JetStream volumes; empty string uses the cluster default |
| eventBus.jetstream.persistence.volumeSize | string | `"1Gi"` | Volume size per JetStream replica |
| eventBus.jetstream.replicas | int | `3` | JetStream replicas (minimum 3 for a quorum) |
| eventBus.jetstream.version | string | `"latest"` | JetStream version supported by the Argo Events controller; `latest` resolves to the newest supported version |
| monitoring.eventBusPodMonitor.enabled | bool | `false` | Create a PodMonitor scraping the EventBus NATS exporter sidecar (requires prometheus-operator) |
| monitoring.eventBusPodMonitor.interval | string | `"30s"` | Scrape interval |
