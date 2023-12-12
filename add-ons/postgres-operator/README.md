# postgres-operator

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 5.4.3](https://img.shields.io/badge/AppVersion-5.4.3-informational?style=flat-square)

A Helm chart for Postgres Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://registry.developers.crunchydata.com/crunchydata | pgo | 5.4.3 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| pgo.controllerImages.cluster | string | `"registry.developers.crunchydata.com/crunchydata/postgres-operator:ubi8-5.3.1-0"` |  |
| pgo.controllerImages.upgrade | string | `"registry.developers.crunchydata.com/crunchydata/postgres-operator-upgrade:ubi8-5.3.1-0"` |  |
| pgo.debug | bool | `false` |  |
| pgo.imagePullSecretNames | list | `[]` |  |
| pgo.relatedImages."postgres_13_gis_3.0".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-13.10-3.0-0"` |  |
| pgo.relatedImages."postgres_13_gis_3.1".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-13.10-3.1-0"` |  |
| pgo.relatedImages."postgres_14_gis_3.1".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-14.7-3.1-0"` |  |
| pgo.relatedImages."postgres_14_gis_3.2".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-14.7-3.2-0"` |  |
| pgo.relatedImages."postgres_14_gis_3.3".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-14.7-3.3-0"` |  |
| pgo.relatedImages."postgres_15_gis_3.3".image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-gis:ubi8-15.2-3.3-0"` |  |
| pgo.relatedImages.pgadmin.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-pgadmin4:ubi8-4.30-10"` |  |
| pgo.relatedImages.pgbackrest.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-pgbackrest:ubi8-2.41-4"` |  |
| pgo.relatedImages.pgbouncer.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-pgbouncer:ubi8-1.18-0"` |  |
| pgo.relatedImages.pgexporter.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres-exporter:ubi8-5.3.1-0"` |  |
| pgo.relatedImages.pgupgrade.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-upgrade:ubi8-5.3.1-0"` |  |
| pgo.relatedImages.postgres_13.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi8-13.10-0"` |  |
| pgo.relatedImages.postgres_14.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi8-14.7-0"` |  |
| pgo.relatedImages.postgres_15.image | string | `"registry.developers.crunchydata.com/crunchydata/crunchy-postgres:ubi8-15.2-0"` |  |
| pgo.resources.controller | object | `{}` |  |
| pgo.resources.upgrade | object | `{}` |  |
| pgo.singleNamespace | bool | `false` |  |

