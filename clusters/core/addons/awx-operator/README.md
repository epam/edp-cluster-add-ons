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
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/awx-operator"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"awx-operator","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"awx-operator"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| oidc.enabled | bool | `false` |  |
