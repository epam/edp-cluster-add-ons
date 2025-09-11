# ingress-nginx

![Version: 4.13.2](https://img.shields.io/badge/Version-4.13.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.13.2](https://img.shields.io/badge/AppVersion-1.13.2-informational?style=flat-square)

A Helm chart for Nginx Ingress Controller

# Internal and External Ingress Controllers

The **Internal Ingress Controller** is used for internal traffic, while the **External Ingress Controller** is used for external traffic.

                                              ┌────────────────────────────────┐
                                              │ Kubernetes Cluster             │
                                              ├──────────┐                     │
                                              │ NodePort │                     │
                                         ┌────►          ◄──┐                  │
                                         │    │  32443   │  │ ┌───────────┐    │
        ┌───────────────────────┐        │    ├──────────┘  │ │ Internal  │    │
        │ Internal LoadBalancer ├────────┤    │             ├─┤ Ingress   │    │
        └───────────────────────┘        │    ├──────────┐  │ │ Controller│    │
                                         │    │ NodePort │  │ └───────────┘    │
                                         └────►          ◄──┘                  │
                                              │  32080   │                     │
                                              ├──────────┘                     │
                                              │                                │
                                              │                                │
                                              ├──────────┐                     │
                                              │ NodePort │                     │
                                         ┌────►          ◄──┐                  │
                                         │    │  31443   │  │ ┌───────────┐    │
        ┌───────────────────────┐        │    ├──────────┘  │ │ External  │    │
        │ External LoadBalancer ├────────┤    │             ├─┤ Ingress   │    │
        └───────────────────────┘        │    ├──────────┐  │ │ Controller│    │
                                         │    │ NodePort │  │ └───────────┘    │
                                         └────►          ◄──┘                  │
                                              │  31080   │                     │
                                              ├──────────┘                     │
                                              │                                │
                                              └────────────────────────────────┘

To deploy and use the **Internal Ingress Controller** and **External Ingress Controller** in the cluster, follow the steps below:

1. Enable the `Internal Ingress Controller` add-on by setting the `ingress-nginx.enable: true` and `ingress-nginx.createNamespace: true` parameters in the `charts/values.yaml` file.<br>
This will create the `ingress-nginx` namespace and deploy the **Internal Ingress Controller** in the cluster.<br>
Internal Ingress Controller listens to the following node ports: 32080 and 32443.<br>
The `watchIngressWithoutClass` parameter is set to `true`, so the Internal Ingress Controller will watch for all Ingress resources withing the cluster.

> **NOTE:** Internal Ingress Controller is watching for all Ingress resources within a cluster.<br>
You should set the `ingressClassName` parameter in the Ingress resource to `nginx` or leave it empty.

2. Enable the `External Ingress Controller` add-on by setting the `ingress-nginx-external.enable: true` and `ingress-nginx-external.createNamespace: true` parameters in the `charts/values.yaml` file.<br>
This will create the `ingress-nginx-external` namespace and deploy the **External Ingress Controller** in the cluster.<br>
Internal Ingress Controller listens to the following node ports: 31080 and 31443.<br>

> **NOTE:** External Ingress Controller is not watching for all Ingress resources within a cluster.<br>
To use the External Ingress Controller, you need to set the `ingressClassName` parameter in the Ingress resource to `nginx-external`.

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
| ingress-nginx.controller.ingressClassResource.controllerValue | string | `"k8s.io/external-ingress-nginx"` |  |
| ingress-nginx.controller.ingressClassResource.name | string | `"external-nginx"` |  |
| ingress-nginx.controller.podAnnotations."fluentbit.io/parser" | string | `"k8s-nginx-ingress"` |  |
| ingress-nginx.controller.resources.limits.memory | string | `"256Mi"` |  |
| ingress-nginx.controller.resources.requests.cpu | string | `"50m"` |  |
| ingress-nginx.controller.resources.requests.memory | string | `"128M"` |  |
| ingress-nginx.controller.service.nodePorts.http | int | `31080` |  |
| ingress-nginx.controller.service.nodePorts.https | int | `31443` |  |
| ingress-nginx.controller.service.type | string | `"NodePort"` |  |
| ingress-nginx.controller.watchIngressWithoutClass | bool | `false` |  |
| ingress-nginx.defaultBackend.enabled | bool | `true` |  |
| ingress-nginx.metrics.enabled | bool | `true` |  |
| ingress-nginx.serviceAccount.create | bool | `true` |  |
| ingress-nginx.serviceAccount.name | string | `"nginx-ingress-service-account"` |  |
| ingress-nginx.updateStrategy.rollingUpdate.maxUnavailable | int | `1` |  |
| ingress-nginx.updateStrategy.type | string | `"RollingUpdate"` |  |
