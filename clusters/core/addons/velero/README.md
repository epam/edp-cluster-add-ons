# velero

![Version: 11.1.1](https://img.shields.io/badge/Version-11.1.1-informational?style=flat-square) ![AppVersion: 1.17.0](https://img.shields.io/badge/AppVersion-1.17.0-informational?style=flat-square)

A Helm chart for Velero Install

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://vmware-tanzu.github.io/helm-charts | velero | 11.1.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| velero.configuration.backupStorageLocation[0].bucket | string | `"velero-core"` |  |
| velero.configuration.backupStorageLocation[0].config.region | string | `"eu-central-1"` |  |
| velero.configuration.backupStorageLocation[0].name | string | `"default"` |  |
| velero.configuration.backupStorageLocation[0].prefix | string | `"velero"` |  |
| velero.configuration.backupStorageLocation[0].provider | string | `"aws"` |  |
| velero.configuration.volumeSnapshotLocation[0].config.region | string | `"eu-central-1"` |  |
| velero.configuration.volumeSnapshotLocation[0].name | string | `"default"` |  |
| velero.configuration.volumeSnapshotLocation[0].provider | string | `"aws"` |  |
| velero.credentials.useSecret | bool | `false` |  |
| velero.initContainers[0].image | string | `"velero/velero-plugin-for-aws:v1.13.1"` |  |
| velero.initContainers[0].name | string | `"velero-plugin-for-aws"` |  |
| velero.initContainers[0].volumeMounts[0].mountPath | string | `"/target"` |  |
| velero.initContainers[0].volumeMounts[0].name | string | `"plugins"` |  |
| velero.schedules.krci.disabled | bool | `true` |  |
| velero.schedules.krci.labels.cluster | string | `"core"` |  |
| velero.schedules.krci.labels.region | string | `"eu-central-1"` |  |
| velero.schedules.krci.paused | bool | `false` |  |
| velero.schedules.krci.schedule | string | `"0 13 * * 1-5"` |  |
| velero.schedules.krci.template.excludedClusterScopedResources[0] | string | `"persistentvolumes"` |  |
| velero.schedules.krci.template.excludedNamespaceScopedResources[0] | string | `"persistentvolumeclaims"` |  |
| velero.schedules.krci.template.includedNamespaces[0] | string | `"krci"` |  |
| velero.schedules.krci.template.snapshotVolumes | bool | `false` |  |
| velero.schedules.krci.template.storageLocation | string | `"default"` |  |
| velero.schedules.krci.template.ttl | string | `"72h0m0s"` |  |
| velero.schedules.krci.useOwnerReferencesInBackup | bool | `false` |  |
| velero.serviceAccount.server.annotations."eks.amazonaws.com/role-arn" | string | `"arn:aws:iam::01234567890:role/AWSIRSA_Core_Velero"` |  |
| velero.serviceAccount.server.create | bool | `true` |  |
| velero.serviceAccount.server.name | string | `"velero-server"` |  |

