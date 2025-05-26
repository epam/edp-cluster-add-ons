# nexus-operator

![Version: 3.5.0](https://img.shields.io/badge/Version-3.5.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.5.0](https://img.shields.io/badge/AppVersion-3.5.0-informational?style=flat-square)

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic ci-nexus \
  --from-literal=password=<password>
```

```bash
kubectl create secret generic nexus-admin-password \
  --from-literal=user=<clientSecret> \
  --from-literal=password=<clientSecret>
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
  "nexus": {
    "user": "<user>",
    "password": "<password>"
  },
  "ci-nexus": {
    "password": "<password>"
  }
}
```

</details>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | nexus-operator | 3.5.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/nexus-operator"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"nexus-operator","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"nexus-operator"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| storageType | object | `{"container":{"bucketName":"krci-container","type":"pvc"},"dotnet":{"bucketName":"krci-container","type":"pvc"},"maven":{"bucketName":"krci-container","type":"pvc"},"npm":{"bucketName":"krci-container","type":"pvc"},"python":{"bucketName":"krci-container","type":"pvc"},"region":"us-east-1","yum":{"bucketName":"krci-container","type":"pvc"}}` | To enable the S3 storage type, must be define role for Nexus service account. |
| storageType.container.bucketName | string | `"krci-container"` | Defines the name of the S3 bucket. |
| storageType.container.type | string | `"pvc"` | Could be one of the following: "pvc", "s3". |
| storageType.region | string | `"us-east-1"` | Mandatory field for S3 storage type. |
