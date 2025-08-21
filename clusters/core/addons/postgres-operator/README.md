# postgres-operator

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 5.8.2](https://img.shields.io/badge/AppVersion-5.8.2-informational?style=flat-square)

A Helm chart for Postgres Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://registry.developers.crunchydata.com/crunchydata | pgo | 5.8.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| pgo.controllerImages.cluster | string | `"registry.developers.crunchydata.com/crunchydata/postgres-operator:ubi9-5.8.2-0"` |  |
| pgo.debug | bool | `false` |  |
| pgo.imagePullSecretNames | list | `[]` |  |
| pgo.relatedImages."postgres_13_gis_3.0".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-13.10-3.0-0"` |  |
| pgo.relatedImages."postgres_13_gis_3.1".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-13.10-3.1-0"` |  |
| pgo.relatedImages."postgres_14_gis_3.1".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-14.7-3.1-0"` |  |
| pgo.relatedImages."postgres_14_gis_3.2".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-14.7-3.2-0"` |  |
| pgo.relatedImages."postgres_14_gis_3.3".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-14.7-3.3-0"` |  |
| pgo.relatedImages."postgres_15_gis_3.3".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-15.8-3.3-2"` |  |
| pgo.relatedImages."postgres_16_gis_3.3".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi9-16.9-3.3-2520"` |  |
| pgo.relatedImages."postgres_16_gis_3.4".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi9-16.9-3.4-2520"` |  |
| pgo.relatedImages."postgres_17_gis_3.4".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi9-17.5-3.4-2520"` |  |
| pgo.relatedImages."postgres_17_gis_3.5".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi9-17.5-3.5-2520"` |  |
| pgo.relatedImages.collector.image | string | `"registry.developers.crunchydata.com/crunchydata/postgres-operator:ubi9-5.8.2-0"` |  |
| pgo.relatedImages.pgbackrest.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-pgbackrest:ubi9-2.54.2-2520"` |  |
| pgo.relatedImages.pgbouncer.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-pgbouncer:ubi9-1.24-2520"` |  |
| pgo.relatedImages.pgexporter.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-exporter:ubi9-0.17.1-2520"` |  |
| pgo.relatedImages.pgupgrade.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-upgrade:ubi9-17.5-2520"` |  |
| pgo.relatedImages.postgres_13.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi8-13.10-0"` |  |
| pgo.relatedImages.postgres_14.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi8-14.7-0"` |  |
| pgo.relatedImages.postgres_15.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi8-15.8-2"` |  |
| pgo.relatedImages.postgres_16.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi9-16.9-2520"` |  |
| pgo.relatedImages.postgres_17.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi9-17.5-2520"` |  |
| pgo.relatedImages.standalone_pgadmin.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-pgadmin4:ubi9-9.2-2520"` |  |
| pgo.resources.controller | object | `{}` |  |
| pgo.resources.upgrade | object | `{}` |  |
| pgo.singleNamespace | bool | `false` |  |

