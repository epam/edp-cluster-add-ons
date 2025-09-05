# report-portal

![Version: 25.8.29](https://img.shields.io/badge/Version-25.8.29-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 25.1.8](https://img.shields.io/badge/AppVersion-25.1.8-informational?style=flat-square)

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic keycloak-client-report-portal-secret \
  --from-literal=clientSecret=<clientSecret>
```

```bash
kubectl create secret generic reportportal-rabbitmq-creds \
  --from-literal=rabbitmq-erlang-cookie=<rabbitmq-erlang-cookie> \
  --from-literal=rabbitmq-password=<rabbitmq-password>
```

```bash
kubectl create secret generic reportportal-postgresql-creds \
  --from-literal=postgresql-password=<pstgresql-password> \
  --from-literal=postgresql-postgres-password=<postgresql-postgres-password>
```

```bash
kubectl create secret generic reportportal-minio-creds \
  --from-literal=root-password=<root-password> \
  --from-literal=root-user=<root-user>
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
  "reportportal": {
    "clientSecret": "<clientSecret>",
    "rabbitmq-cookie": "<rabbitmq-cookie>",
    "rabbitmq-password": "<rabbitmq-password>",
    "postgresql-password": "<postgresql-password>",
    "postgresql-postgres-password": "<postgresql-postgres-password>",
    "root-password": "<root-password>",
    "root-user": "<root-user>"
  }
}
```

</details>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | minio | 17.0.16 |
| https://charts.bitnami.com/bitnami | rabbitmq | 16.0.11 |
| https://opensearch-project.github.io/helm-charts/ | opensearch | 2.35.0 |
| https://reportportal.io/kubernetes | reportportal | 25.8.29 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/reportportal"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"report-portal","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"report-portal"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| minio.auth.existingSecret | string | `"reportportal-minio-creds"` |  |
| minio.persistence.size | string | `"1Gi"` |  |
| opensearch.extraEnvs[0].name | string | `"DISABLE_INSTALL_DEMO_CONFIG"` |  |
| opensearch.extraEnvs[0].value | string | `"true"` |  |
| opensearch.extraEnvs[1].name | string | `"DISABLE_SECURITY_PLUGIN"` |  |
| opensearch.extraEnvs[1].value | string | `"true"` |  |
| opensearch.persistence.size | string | `"3Gi"` |  |
| opensearch.resources.requests.cpu | string | `"100m"` |  |
| opensearch.resources.requests.memory | string | `"2Gi"` |  |
| opensearch.singleNode | bool | `true` |  |
| opensearch.startupProbe.initialDelaySeconds | int | `45` |  |
| rabbitmq.auth.existingErlangSecret | string | `"reportportal-rabbitmq-creds"` |  |
| rabbitmq.auth.existingPasswordSecret | string | `"reportportal-rabbitmq-creds"` |  |
| rabbitmq.extraConfiguration | string | `"max_message_size = 134217728"` |  |
| rabbitmq.extraEnvVars[0].name | string | `"RABBITMQ_FEATURE_FLAGS"` |  |
| rabbitmq.extraEnvVars[0].value | string | `"stream_single_active_consumer"` |  |
| rabbitmq.extraPlugins | string | `"rabbitmq_auth_backend_ldap rabbitmq_consistent_hash_exchange rabbitmq_shovel rabbitmq_shovel_management\n"` |  |
| rabbitmq.persistence.size | string | `"1Gi"` |  |
| reportportal.database.endpoint | string | `"reportportal-primary.report-portal.svc.cluster.local"` |  |
| reportportal.database.secretName | string | `"reportportal-postgresql-creds"` |  |
| reportportal.ingress.hosts[0] | string | `"report-portal.example.com"` |  |
| reportportal.ingress.usedomainname | bool | `true` |  |
| reportportal.minio.install | bool | `false` |  |
| reportportal.msgbroker.apiuser | string | `"user"` |  |
| reportportal.msgbroker.endpoint | string | `"report-portal-rabbitmq.report-portal.svc.cluster.local"` |  |
| reportportal.msgbroker.secretName | string | `"reportportal-rabbitmq-creds"` |  |
| reportportal.msgbroker.user | string | `"user"` |  |
| reportportal.opensearch.install | bool | `false` |  |
| reportportal.rabbitmq.install | bool | `false` |  |
| reportportal.searchengine.endpoint | string | `"opensearch-cluster-master.report-portal.svc.cluster.local"` |  |
| reportportal.searchengine.secretName | string | `nil` |  |
| reportportal.serviceanalyzer.resources.requests.cpu | string | `"50m"` |  |
| reportportal.serviceanalyzertrain.resources.requests.cpu | string | `"50m"` |  |
| reportportal.serviceapi.resources.requests.cpu | string | `"50m"` |  |
| reportportal.serviceindex.resources.requests.cpu | string | `"50m"` |  |
| reportportal.serviceui.resources.requests.cpu | string | `"50m"` |  |
| reportportal.storage.accesskeyName | string | `"root-user"` |  |
| reportportal.storage.endpoint | string | `"report-portal-minio.report-portal.svc.cluster.local"` |  |
| reportportal.storage.endpointshort | string | `"report-portal-minio.report-portal.svc.cluster.local"` |  |
| reportportal.storage.secretName | string | `"reportportal-minio-creds"` |  |
| reportportal.storage.secretkeyName | string | `"root-password"` |  |
| reportportal.storage.type | string | `"minio"` |  |
| reportportal.uat.resources.requests.cpu | string | `"50m"` |  |
| reportportal.uat.superadminInitPasswd.passwordKeyName | string | `"superadmin-password"` |  |
| reportportal.uat.superadminInitPasswd.secretName | string | `"reportportal-superadmin-password"` |  |
| saml.enabled | bool | `false` |  |
