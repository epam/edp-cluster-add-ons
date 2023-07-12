# nexus

![Version: 56.0.0](https://img.shields.io/badge/Version-56.0.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.56.0](https://img.shields.io/badge/AppVersion-3.56.0-informational?style=flat-square)

A Helm chart for Nexus

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://sonatype.github.io/helm3-charts/ | nexus-repository-manager | 56.0.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| nexus-repository-manager.ingress.annotations."nginx.ingress.kubernetes.io/proxy-body-size" | string | `"0"` |  |
| nexus-repository-manager.ingress.enabled | bool | `true` |  |
| nexus-repository-manager.ingress.hostPath | string | `"/"` |  |
| nexus-repository-manager.ingress.hostRepo | string | `"nexus.example.com"` |  |
| nexus-repository-manager.ingress.ingressClassName | string | `"nginx"` |  |
| nexus-repository-manager.persistence.accessMode | string | `"ReadWriteOnce"` |  |
| nexus-repository-manager.persistence.enabled | bool | `true` |  |
| nexus-repository-manager.persistence.storageClass | string | `"ebs-sc"` |  |
| nexus-repository-manager.persistence.storageSize | string | `"30Gi"` |  |
| nexus-repository-manager.resources.limits.memory | string | `"6Gi"` |  |
| nexus-repository-manager.resources.requests.cpu | string | `"100m"` |  |
| nexus-repository-manager.resources.requests.memory | string | `"2Gi"` |  |

