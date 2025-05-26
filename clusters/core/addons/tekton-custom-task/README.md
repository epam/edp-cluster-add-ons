# tekton-custom-task

![Version: 0.2.0](https://img.shields.io/badge/Version-0.2.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.2.0](https://img.shields.io/badge/AppVersion-0.2.0-informational?style=flat-square)

A Helm chart for tekton-custom-task

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | tekton-custom-task | 0.2.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| tekton-custom-task.affinity | object | `{}` |  |
| tekton-custom-task.annotations | object | `{}` |  |
| tekton-custom-task.image.repository | string | `"epamedp/tekton-custom-task"` | tekton-custom-task Docker image name. The released image can be found on [Dockerhub](https://hub.docker.com/r/epamedp/tekton-custom-task) |
| tekton-custom-task.image.tag | string | `""` | tekton-custom-task Docker image tag. The released image can be found on [Dockerhub](https://hub.docker.com/r/epamedp/tekton-custom-task) |
| tekton-custom-task.imagePullPolicy | string | `"IfNotPresent"` |  |
| tekton-custom-task.imagePullSecrets | list | `[]` | Optional array of imagePullSecrets containing private registry credentials # Ref: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry |
| tekton-custom-task.name | string | `"tekton-custom-task"` | component name |
| tekton-custom-task.nodeSelector | object | `{}` |  |
| tekton-custom-task.resources.limits.memory | string | `"192Mi"` |  |
| tekton-custom-task.resources.requests.cpu | string | `"50m"` |  |
| tekton-custom-task.resources.requests.memory | string | `"64Mi"` |  |
| tekton-custom-task.tolerations | list | `[]` |  |

