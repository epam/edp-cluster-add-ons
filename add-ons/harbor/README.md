# harbor

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.12.2](https://img.shields.io/badge/AppVersion-1.12.2-informational?style=flat-square)

A Helm chart for Harbor

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://helm.goharbor.io | harbor | 1.12.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| harbor.core.configureUserSettings | string | `"{\n  \"auth_mode\": \"oidc_auth\",\n  \"oidc_name\": \"keycloak\",\n  \"oidc_endpoint\": \"https://keycloak.example.com/auth/realms/shared\",\n  \"oidc_client_id\": \"harbor\",\n  \"oidc_client_secret\": \"YOURSECRET\",\n  \"oidc_groups_claim\": \"roles\",\n  \"oidc_admin_group\": \"administrator\",\n  \"oidc_scope\": \"openid,email,profile,roles\",\n  \"oidc_auto_onboard\": \"true\",\n  \"oidc_user_claim\": \"preferred_username\"\n}\n"` |  |
| harbor.core.xsrfKey | string | `"somekey"` |  |
| harbor.database.internal.password | string | `"somesecret"` |  |
| harbor.existingSecretAdminPassword | string | `"harbor"` |  |
| harbor.existingSecretAdminPasswordKey | string | `"HARBOR_ADMIN_PASSWORD"` |  |
| harbor.existingSecretSecretKey | string | `"harbor"` |  |
| harbor.expose.ingress.hosts.core | string | `"registry.example.com"` |  |
| harbor.expose.ingress.hosts.notary | string | `"notary.example.com"` |  |
| harbor.expose.tls.enabled | bool | `false` |  |
| harbor.externalURL | string | `"https://registry.example.com"` |  |
| harbor.fullnameOverride | string | `"harbor"` |  |
| harbor.ipFamily.ipv6.enabled | bool | `false` |  |
| harbor.jobservice.secret | string | `"SomeSecret"` |  |
| harbor.persistence.enabled | bool | `true` |  |
| harbor.persistence.persistentVolumeClaim.database.size | string | `"2Gi"` |  |
| harbor.persistence.persistentVolumeClaim.database.storageClass | string | `"ebs-sc"` |  |
| harbor.persistence.persistentVolumeClaim.jobservice.jobLog.size | string | `"1Gi"` |  |
| harbor.persistence.persistentVolumeClaim.jobservice.jobLog.storageClass | string | `"ebs-sc"` |  |
| harbor.persistence.persistentVolumeClaim.redis.size | string | `"1Gi"` |  |
| harbor.persistence.persistentVolumeClaim.redis.storageClass | string | `"ebs-sc"` |  |
| harbor.persistence.persistentVolumeClaim.registry.size | string | `"30Gi"` |  |
| harbor.persistence.persistentVolumeClaim.registry.storageClass | string | `"ebs-sc"` |  |
| harbor.persistence.persistentVolumeClaim.trivy.size | string | `"5Gi"` |  |
| harbor.persistence.persistentVolumeClaim.trivy.storageClass | string | `"ebs-sc"` |  |
| harbor.persistence.resourcePolicy | string | `"keep"` |  |
| harbor.registry.credentials.existingSecret | string | `"harbor"` |  |
| harbor.registry.credentials.username | string | `"harbor_registry_user"` |  |
| harbor.registry.secret | string | `"SomeSecret"` |  |
| harbor.updateStrategy.type | string | `"Recreate"` |  |
| oidc.enabled | bool | `false` |  |

