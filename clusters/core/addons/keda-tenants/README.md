# keda-tenants

![Version: 0.1.2](https://img.shields.io/badge/Version-0.1.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

## General Concepts

This application enables scaling of KubeRocketCI resources based on activity in the environment. It leverages Prometheus metrics to monitor the state of resources.
Therefore, a configured Prometheus instance collecting cluster metrics is required for its operation, along with enabled metric export from the NGINX Ingress Controller.

For krci-portal, the chart configures a dedicated KEDA `ScaledObject` that scales the `portal` deployment to zero after the configured idle period and scales it back up when new ingress requests arrive. The scaler uses two Prometheus triggers: recent pod creation in the tenant namespace and recent HTTP requests recorded by the NGINX Ingress Controller.
Both portal triggers use the chart-wide `timeInterval`, so the portal scaler follows the same activity lookback window as the other ScaledObjects in this chart.
The scale boundaries and reaction timing for the portal scaler are controlled by the same top-level values used elsewhere in the chart: `minReplicaCount`, `maxReplicaCount`, `pollingInterval`, `cooldownPeriod`, `thresholdPods`, and `thresholdRequests`.

## Portal Scaling Tuning

The `timeInterval` and `thresholdRequests` parameters should always be tuned together because the HTTP trigger compares the number of ingress requests received during the configured time window against the threshold.

- `timeInterval=3600` and `thresholdRequests=1` means that a single matching request during the last hour is enough to keep `krci-portal` active or scale it up.
- `timeInterval` also controls how long recently created pods in the tenant namespace keep the pod activity trigger active.
- Increasing `timeInterval` while keeping the same `thresholdRequests` makes the scaler less aggressive for scale-down, because old traffic is considered active for longer.
- Increasing `thresholdRequests` while keeping the same `timeInterval` makes scale-up stricter, because more requests are required within the same lookback window.
- `thresholdPods` controls how many newly created pods must appear within the same lookback window before the pod activity trigger becomes active.
- `cooldownPeriod` controls how long KEDA waits before scaling the deployment back to zero after activity disappears.
- `pollingInterval` controls how often KEDA evaluates Prometheus metrics; smaller values react faster but query Prometheus more often.

Current default configuration for `krci-portal` scale-to-zero is `timeInterval=3600`, `thresholdPods=1`, `thresholdRequests=1`, `minReplicaCount=0`, `maxReplicaCount=1`, `pollingInterval=30`, and `cooldownPeriod=300`. Adjust these values together based on whether you want faster wake-up, more stable replicas, or more aggressive resource savings.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| cooldownPeriod | int | `300` | Idle period in seconds before KEDA scales the workload down to the minimum replica count. |
| gitProviders | list | `["github"]` | https://github.com/epam/edp-install/blob/master/deploy-templates/values.yaml#L2 |
| kedaTenants.namespaces | list | `["krci"]` | This value specifies the namespaces where KubeRocketCI deployed. |
| maxReplicaCount | int | `1` | Maximum number of replicas for the scaled workload. |
| minReplicaCount | int | `0` | Minimum number of replicas for the scaled workload. |
| pollingInterval | int | `30` | Interval in seconds for KEDA to poll Prometheus metrics. |
| thresholdPods | int | `1` | Number of newly created pods within the lookback window required to trigger scaling. |
| thresholdRequests | int | `1` | Number of matching HTTP requests within the lookback window required to trigger scaling. |
| timeInterval | string | `"3600"` | Lookback window for activity metrics, in seconds. |
