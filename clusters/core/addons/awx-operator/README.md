# awx-operator

![Version: 2.19.1](https://img.shields.io/badge/Version-2.19.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.19.1](https://img.shields.io/badge/AppVersion-2.19.1-informational?style=flat-square)

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic keycloak-client-awx-secret \
  --from-literal=clientSecret=<clientSecret>
```

```bash
kubectl create secret generic awx-admin-password \
  --from-literal=password=<admin-password>
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
  "awx-operator": {
    "admin-password": "<admin-password>",
    "clientSecret": "<clientSecret>"
  }
}
```

</details>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| AWX.enabled | bool | `true` |  |
| AWX.name | string | `"awx"` |  |
| AWX.postgres.dbName | string | `"awx"` |  |
| AWX.postgres.enabled | bool | `true` |  |
| AWX.postgres.host | string | `"awx-primary.awx-operator.svc"` |  |
| AWX.postgres.port | int | `5432` |  |
| AWX.postgres.sslmode | string | `"prefer"` |  |
| AWX.postgres.type | string | `"unmanaged"` |  |
| AWX.postgres.username | string | `"awx"` |  |
| AWX.spec.admin_password_secret | string | `"awx-admin-password"` |  |
| AWX.spec.admin_user | string | `"admin"` |  |
| AWX.spec.image | string | `"quay.io/ansible/awx"` |  |
| AWX.spec.image_version | string | `"24.6.1"` |  |
| AWX.spec.ingress_hosts[0].hostname | string | `"awx.example.com"` |  |
| AWX.spec.ingress_path | string | `"/"` |  |
| AWX.spec.ingress_path_type | string | `"Prefix"` |  |
| AWX.spec.ingress_type | string | `"ingress"` |  |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/infra/core/addons/awx-operator"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| oidc.enabled | bool | `false` |  |
