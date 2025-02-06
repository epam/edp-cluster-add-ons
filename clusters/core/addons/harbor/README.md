# harbor

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.12.2](https://img.shields.io/badge/AppVersion-1.12.2-informational?style=flat-square)

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic harbor \
  --from-literal=HARBOR_ADMIN_PASSWORD=<HARBOR_ADMIN_PASSWORD> \
  --from-literal=secretKey=<secretKey> \
  --from-literal=REGISTRY_HTPASSWD=<REGISTRY_HTPASSWD> \
  --from-literal=REGISTRY_PASSWD=<REGISTRY_PASSWD> \
```

```bash
kubectl create secret generic keycloak-client-harbor-secret \
  --from-literal=clientSecret=<clientSecret>
```

</details>

<details>
<summary><b>External Secret Operator</b></summary>

Update [values.yaml](values.yaml) to enable ESO:

```yaml
eso:
  # -- Install components of the ESO.
  enabled: true
```

AWS Parameter Store structure:

```json
{
  "harbor": {
    "oidcClientSecret": "<oidcClientSecret>",
    "HARBOR_ADMIN_PASSWORD": "<HARBOR_ADMIN_PASSWORD>",
    "secretKey": "<secretKey>",
    "REGISTRY_HTPASSWD": "<REGISTRY_HTPASSWD>",
    "REGISTRY_PASSWD": "<REGISTRY_PASSWD>",
  }
}
```

</details>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://helm.goharbor.io | harbor | 1.12.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/infra/core/addons/harbor"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
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
| harbor.persistence.persistentVolumeClaim.database.storageClass | string | `"gp3-retain"` |  |
| harbor.persistence.persistentVolumeClaim.jobservice.jobLog.size | string | `"1Gi"` |  |
| harbor.persistence.persistentVolumeClaim.jobservice.jobLog.storageClass | string | `"gp3-retain"` |  |
| harbor.persistence.persistentVolumeClaim.redis.size | string | `"1Gi"` |  |
| harbor.persistence.persistentVolumeClaim.redis.storageClass | string | `"gp3-retain"` |  |
| harbor.persistence.persistentVolumeClaim.registry.size | string | `"30Gi"` |  |
| harbor.persistence.persistentVolumeClaim.registry.storageClass | string | `"gp3-retain"` |  |
| harbor.persistence.persistentVolumeClaim.trivy.size | string | `"5Gi"` |  |
| harbor.persistence.persistentVolumeClaim.trivy.storageClass | string | `"gp3-retain"` |  |
| harbor.persistence.resourcePolicy | string | `"keep"` |  |
| harbor.registry.credentials.existingSecret | string | `"harbor"` |  |
| harbor.registry.credentials.username | string | `"harbor_registry_user"` |  |
| harbor.registry.secret | string | `"SomeSecret"` |  |
| harbor.updateStrategy.type | string | `"Recreate"` |  |
| oidc.enabled | bool | `false` |  |
