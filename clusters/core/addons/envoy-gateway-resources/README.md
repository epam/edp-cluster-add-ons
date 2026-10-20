# envoy-gateway-resources

![Version: 1.9.1](https://img.shields.io/badge/Version-1.9.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.9.1](https://img.shields.io/badge/AppVersion-1.9.1-informational?style=flat-square)

Envoy Gateway custom resources (GatewayClass, Gateway, EnvoyProxy, ClientTrafficPolicy, BackendTrafficPolicy)

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| krciEnvDaemon.enabled | bool | `false` | Send the gateway access log to the krci-env-daemon add-on over OpenTelemetry, so that it can wake KEDA-scaled environments on their first request. The stdout access log stays. |
| krciEnvDaemon.host | string | `"krci-env-daemon.krci-env-daemon.svc.cluster.local"` | Host of the daemon's OTLP receiver: Service krci-env-daemon in the namespace krci-env-daemon. |
| krciEnvDaemon.port | int | `4317` | Port of the daemon's OTLP receiver. |

