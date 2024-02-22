# harbor-ha

![Version: 1.13.0](https://img.shields.io/badge/Version-1.13.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.9.0](https://img.shields.io/badge/AppVersion-2.9.0-informational?style=flat-square)

A Helm chart for Harbor with HA

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | minio | 12.6.5 |
| https://charts.bitnami.com/bitnami | redis | 17.11.6 |
| https://helm.goharbor.io | harbor | 1.13.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.secretName | string | `"/edp/eks/addons/harbor-ha"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| harbor.core.configureUserSettings | string | `"{\n  \"auth_mode\": \"oidc_auth\",\n  \"oidc_name\": \"keycloak\",\n  \"oidc_endpoint\": \"https://keycloak.example.com/auth/realms/shared\",\n  \"oidc_client_id\": \"harbor\",\n  \"oidc_client_secret\": \"YOURSECRET\",\n  \"oidc_groups_claim\": \"roles\",\n  \"oidc_admin_group\": \"administrator\",\n  \"oidc_scope\": \"openid,email,profile,roles\",\n  \"oidc_auto_onboard\": \"true\",\n  \"oidc_user_claim\": \"preferred_username\"\n}\n"` |  |
| harbor.core.replicas | int | `2` |  |
| harbor.core.resources.requests.cpu | float | `0.05` |  |
| harbor.core.resources.requests.memory | string | `"150Mi"` |  |
| harbor.core.xsrfKey | string | `"somekey"` |  |
| harbor.database.external.existingSecret | string | `"postgresql-pguser-harbor"` |  |
| harbor.database.external.host | string | `"postgresql-primary.harbor.svc"` |  |
| harbor.database.external.port | string | `"5432"` |  |
| harbor.database.external.username | string | `"harbor"` |  |
| harbor.database.type | string | `"external"` |  |
| harbor.existingSecretAdminPassword | string | `"harbor"` |  |
| harbor.existingSecretAdminPasswordKey | string | `"HARBOR_ADMIN_PASSWORD"` |  |
| harbor.existingSecretSecretKey | string | `"harbor"` |  |
| harbor.expose.ingress.hosts.core | string | `"registry.example.com"` |  |
| harbor.expose.tls.enabled | bool | `false` |  |
| harbor.externalURL | string | `"https://registry.example.com"` |  |
| harbor.fullnameOverride | string | `"harbor"` |  |
| harbor.ipFamily.ipv6.enabled | bool | `false` |  |
| harbor.jobservice.jobLoggers[0] | string | `"database"` |  |
| harbor.jobservice.replicas | int | `2` |  |
| harbor.jobservice.resources.requests.cpu | float | `0.01` |  |
| harbor.jobservice.resources.requests.memory | string | `"50Mi"` |  |
| harbor.jobservice.secret | string | `"SomeSecret"` |  |
| harbor.metrics.enabled | bool | `true` |  |
| harbor.metrics.serviceMonitor.enabled | bool | `true` |  |
| harbor.notary.enabled | bool | `false` |  |
| harbor.persistence.enabled | bool | `true` |  |
| harbor.persistence.imageChartStorage.disableredirect | bool | `true` |  |
| harbor.persistence.imageChartStorage.s3.bucket | string | `"harbor"` |  |
| harbor.persistence.imageChartStorage.s3.existingSecret | string | `"harbor-s3"` |  |
| harbor.persistence.imageChartStorage.s3.regionendpoint | string | `"http://minio.harbor.svc.cluster.local:9000"` |  |
| harbor.persistence.imageChartStorage.type | string | `"s3"` |  |
| harbor.persistence.persistentVolumeClaim.trivy.size | string | `"5Gi"` |  |
| harbor.persistence.persistentVolumeClaim.trivy.storageClass | string | `"ebs-sc"` |  |
| harbor.persistence.resourcePolicy | string | `"keep"` |  |
| harbor.portal.replicas | int | `2` |  |
| harbor.redis.external.addr | string | `"redis-node-0.redis-headless.harbor.svc.cluster.local:26379,redis-node-1.redis-headless.harbor.svc.cluster.local:26379,redis-node-2.redis-headless.harbor.svc.cluster.local:26379"` |  |
| harbor.redis.external.password | string | `"SomeSecret"` |  |
| harbor.redis.external.sentinelMasterSet | string | `"mymaster"` |  |
| harbor.redis.type | string | `"external"` |  |
| harbor.registry.credentials.existingSecret | string | `"harbor"` |  |
| harbor.registry.credentials.username | string | `"harbor_registry_user"` |  |
| harbor.registry.registry.resources.requests.cpu | float | `0.1` |  |
| harbor.registry.registry.resources.requests.memory | string | `"300Mi"` |  |
| harbor.registry.replicas | int | `2` |  |
| harbor.registry.secret | string | `"SomeSecret"` |  |
| harbor.updateStrategy.type | string | `"Recreate"` |  |
| minio.auth.existingSecret | string | `"minio-admin-ui"` |  |
| minio.auth.forceNewKeys | bool | `true` |  |
| minio.fullnameOverride | string | `"minio"` |  |
| minio.ingress.enabled | bool | `true` |  |
| minio.ingress.hostname | string | `"minio-harbor.example.com"` |  |
| minio.mode | string | `"distributed"` |  |
| minio.persistence.size | string | `"10Gi"` |  |
| minio.provisioning.buckets[0].name | string | `"harbor"` |  |
| minio.provisioning.enabled | bool | `true` |  |
| minio.provisioning.policies[0].name | string | `"harbor"` |  |
| minio.provisioning.policies[0].statements[0].actions[0] | string | `"s3:*"` |  |
| minio.provisioning.policies[0].statements[0].effect | string | `"Allow"` |  |
| minio.provisioning.policies[0].statements[0].resources[0] | string | `"arn:aws:s3:::harbor"` |  |
| minio.provisioning.policies[0].statements[0].resources[1] | string | `"arn:aws:s3:::harbor/*"` |  |
| minio.provisioning.usersExistingSecrets[0] | string | `"centralized-minio-users"` |  |
| minio.resources.limits.memory | string | `"5000Mi"` |  |
| minio.resources.requests.cpu | string | `"200m"` |  |
| minio.resources.requests.memory | string | `"250Mi"` |  |
| oidc.enabled | bool | `false` |  |
| redis.auth.existingSecret | string | `"redis-creds"` |  |
| redis.auth.existingSecretPasswordKey | string | `"REDIS_PASSWORD"` |  |
| redis.auth.sentinel | bool | `false` |  |
| redis.fullnameOverride | string | `"redis"` |  |
| redis.master.persistence.size | string | `"1Gi"` |  |
| redis.replica.persistence.size | string | `"1Gi"` |  |
| redis.replica.resources.limits.memory | string | `"512Mi"` |  |
| redis.replica.resources.requests.cpu | string | `"50m"` |  |
| redis.replica.resources.requests.memory | string | `"100Mi"` |  |
| redis.sentinel.enabled | bool | `true` |  |

