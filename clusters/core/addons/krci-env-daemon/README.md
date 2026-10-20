# krci-env-daemon

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

A Helm chart for the KubeRocketCI krci-env-daemon add-on, which wakes KEDA-scaled environments on their first request through Envoy Gateway

**Homepage:** <https://docs.kuberocketci.io/>

This add-on is a thin wrapper around the [krci-env-daemon](https://github.com/KubeRocketCI/krci-env-daemon)
component chart. The daemon reads the access log of the platform gateway, wakes a KEDA-scaled environment on
its first request, shows a waiting page while the workloads start, and lets KEDA scale them to zero after the
idle window. It is not in the request path.

## Prerequisites

- The `envoy-gateway` and `envoy-gateway-resources` add-ons (Envoy Gateway v1.9 or later), with the
  environments served through HTTPRoutes on `main-gateway`.
- The `keda` add-on (KEDA 2.17 or later).

## Turning it on

1. Enable this add-on, with an entry in `environments` for every namespace of keda-tenants
   `kedaTenants.namespaces`.
2. Set `krciEnvDaemon.enabled: true` in `envoy-gateway-resources`: the gateway sends its access log to the
   daemon.
3. Set `trigger: krci-env-daemon` in `keda-tenants`: the tenant ScaledObjects use the daemon's scaler.

To turn it off, take the steps in reverse order. While a ScaledObject points at a daemon that is not running,
KEDA keeps the workload at its current replicas.

An open Portal tab keeps its environment awake, because the Portal keeps calling its API. The component
README lists the other limitations.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | krci-env-daemon | 0.1.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| krci-env-daemon.environments | list | `[{"namespace":"krci"}]` | The environments the daemon serves, one per namespace of keda-tenants `kedaTenants.namespaces`. `namespace` gives the daemon read access. `route` (the environment's krci-portal HTTPRoute) and `hostnames` (the hosts of that route) add the waiting page shown while the environment starts. |
| krci-env-daemon.idle | string | `"15m"` | How long an environment stays awake after its last request through the gateway or its last running pipeline. KEDA scales its workloads to zero a keda-tenants `cooldownPeriod` later. |
