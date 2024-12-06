# report-portal

![Version: 5.10.0](https://img.shields.io/badge/Version-5.10.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 23.2](https://img.shields.io/badge/AppVersion-23.2-informational?style=flat-square)

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
| https://charts.bitnami.com/bitnami | minio | 11.10.3 |
| https://charts.bitnami.com/bitnami | rabbitmq | 10.3.9 |
| https://opensearch-project.github.io/helm-charts/ | opensearch | 2.17.0 |
| https://reportportal.io/kubernetes | reportportal | 5.10.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/infra/core/addons/reportportal"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
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
| rabbitmq.persistence.size | string | `"1Gi"` |  |
| reportportal.elasticsearch.endpoint | string | `"opensearch-cluster-master.report-portal.svc.cluster.local:9200"` |  |
| reportportal.ingress.hosts[0] | string | `"report-portal.example.com"` |  |
| reportportal.ingress.usedomainname | bool | `true` |  |
| reportportal.postgresql.SecretName | string | `"reportportal-postgresql-creds"` |  |
| reportportal.postgresql.endpoint.address | string | `"reportportal-primary.report-portal.svc.cluster.local"` |  |
| reportportal.rabbitmq.SecretName | string | `"reportportal-rabbitmq-creds"` |  |
| reportportal.rabbitmq.endpoint.address | string | `"report-portal-rabbitmq.report-portal.svc.cluster.local"` |  |
| reportportal.rabbitmq.endpoint.apiuser | string | `"user"` |  |
| reportportal.rabbitmq.endpoint.user | string | `"user"` |  |
| reportportal.serviceanalyzer.resources.requests.cpu | string | `"50m"` |  |
| reportportal.serviceanalyzertrain.resources.requests.cpu | string | `"50m"` |  |
| reportportal.serviceapi.resources.requests.cpu | string | `"50m"` |  |
| reportportal.serviceindex.resources.requests.cpu | string | `"50m"` |  |
| reportportal.serviceui.resources.requests.cpu | string | `"50m"` |  |
| reportportal.storage.accesskeyName | string | `"root-user"` |  |
| reportportal.storage.endpoint | string | `"http://report-portal-minio.report-portal.svc.cluster.local:9000"` |  |
| reportportal.storage.endpointshort | string | `"report-portal-minio.report-portal.svc.cluster.local:9000"` |  |
| reportportal.storage.secretName | string | `"reportportal-minio-creds"` |  |
| reportportal.storage.secretkeyName | string | `"root-password"` |  |
| reportportal.storage.type | string | `"minio"` |  |
| reportportal.uat.resources.requests.cpu | string | `"50m"` |  |
| saml.enabled | bool | `false` |  |
