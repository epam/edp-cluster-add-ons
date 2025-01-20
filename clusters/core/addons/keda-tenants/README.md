# keda-tenants

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

## General Concepts

This application enables scaling of KubeRocketCI resources based on activity in the environment. It leverages Prometheus metrics to monitor the state of resources.
Therefore, a configured Prometheus instance collecting cluster metrics is required for its operation, along with enabled metric export from the NGINX Ingress Controller.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| gitProviders | list | `["github"]` | https://github.com/epam/edp-install/blob/master/deploy-templates/values.yaml#L2 |
| kedaTenants.namespaces | list | `["krci"]` | This value specifies the namespaces where KubeRocketCI deployed. |
| timeInterval | string | `"7200"` | Interval in seconds to scale resources. |
