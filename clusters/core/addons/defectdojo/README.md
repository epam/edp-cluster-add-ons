# defectdojo

![Version: 1.6.205](https://img.shields.io/badge/Version-1.6.205-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.50.0](https://img.shields.io/badge/AppVersion-2.50.0-informational?style=flat-square)

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic defectdojo-extrasecrets \
  --from-literal=DD_SOCIAL_AUTH_KEYCLOAK_SECRET=<oidcClientSecret>
```

```bash
kubectl create secret generic defectdojo-redis-specific \
  --from-literal=redis-password=<redis-password>
```

```bash
kubectl create secret generic defectdojo \
  --from-literal=DD_ADMIN_PASSWORD=<DD_ADMIN_PASSWORD> \
  --from-literal=DD_SECRET_KEY=<DD_SECRET_KEY> \
  --from-literal=DD_CREDENTIAL_AES_256_KEY=<DD_CREDENTIAL_AES_256_KEY> \
  --from-literal=METRICS_HTTP_AUTH_PASSWORD=<METRICS_HTTP_AUTH_PASSWORD>
```

```bash
kubectl create secret generic keycloak-client-defectdojo-secret \
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
  "defectdojo": {
    "oidcClientSecret": "<oidcClientSecret>",
    "rabbitmq-erlang-cookie": "<rabbitmq-erlang-cookie>",
    "rabbitmq-password": "<rabbitmq-password>",
    "DD_ADMIN_PASSWORD": "<DD_ADMIN_PASSWORD>",
    "DD_SECRET_KEY": "<DD_SECRET_KEY>",
    "DD_CREDENTIAL_AES_256_KEY": "<DD_CREDENTIAL_AES_256_KEY>",
    "METRICS_HTTP_AUTH_PASSWORD": "<METRICS_HTTP_AUTH_PASSWORD>",
    "oidcClientSecret": "<oidcClientSecret>"
  }
}
```

</details>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/helm-charts | defectdojo | 1.6.205 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| defectdojo.alternativeHosts[0] | string | `"defectdojo-django.defectdojo"` |  |
| defectdojo.django.ingress.activateTLS | bool | `false` |  |
| defectdojo.django.ingress.enabled | bool | `true` |  |
| defectdojo.django.mediaPersistentVolume.persistentVolumeClaim.size | string | `"2Gi"` |  |
| defectdojo.django.uwsgi.livenessProbe.initialDelaySeconds | int | `20` |  |
| defectdojo.extraConfigs.DD_CSRF_COOKIE_SECURE | string | `"True"` |  |
| defectdojo.extraConfigs.DD_SECURE_SSL_REDIRECT | string | `"False"` |  |
| defectdojo.extraConfigs.DD_SESSION_COOKIE_SECURE | string | `"True"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_ACCESS_TOKEN_URL | string | `"https://keycloak.example.com/auth/realms/shared/protocol/openid-connect/token"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_AUTHORIZATION_URL | string | `"https://keycloak.example.com/auth/realms/shared/protocol/openid-connect/auth"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_KEY | string | `"defectdojo"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_OAUTH2_ENABLED | string | `"True"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_PUBLIC_KEY | string | `"<RS256_KEY>"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_SECRET | string | `"defectdojo-extrasecrets"` |  |
| defectdojo.fullnameOverride | string | `"defectdojo"` |  |
| defectdojo.host | string | `"defectdojo.example.com"` |  |
| defectdojo.initializer.run | bool | `true` |  |
| defectdojo.postgresql.auth.existingSecret | string | `"defectdojo-pguser-defectdojo"` |  |
| defectdojo.postgresql.auth.secretKeys.adminPasswordKey | string | `"password"` |  |
| defectdojo.postgresql.auth.secretKeys.userPasswordKey | string | `"password"` |  |
| defectdojo.postgresql.enabled | bool | `false` |  |
| defectdojo.postgresql.postgresServer | string | `"defectdojo-primary.defectdojo.svc"` |  |
| defectdojo.redis.master.persistence.size | string | `"2Gi"` |  |
| defectdojo.site_url | string | `"https://defectdojo.example.com"` |  |
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/defectdojo"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"defectdojo","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"defectdojo"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| oidc.enabled | bool | `false` |  |
