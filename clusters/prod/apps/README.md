# edp-cluster-add-ons

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

EDP Cluster Addons that extend the Kubernetes Cluster Functionality

**Homepage:** <https://docs.kuberocketci.io/>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| epmd-edp | <SupportEPMD-EDP@epam.com> | <https://solutionshub.epam.com/solution/epam-delivery-platform> |
| sergk |  | <https://github.com/SergK> |

## Source Code

* <https://github.com/epam/edp-cluster-add-ons>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| argoProject | string | `"core"` |  |
| clusterName | string | `"prod"` |  |
| destinationServer | string | `"prod"` |  |
| repoUrl | string | `"ssh://git@github.com:22/kuberocketci/edp-cluster-add-ons"` |  |
| targetRevision | string | `"main"` |  |
| vault-remote-rbac.createNamespace | bool | `false` |  |
| vault-remote-rbac.enable | bool | `false` |  |
| vault-remote-rbac.namespace | string | `"vault"` |  |

