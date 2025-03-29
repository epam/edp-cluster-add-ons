# atlantis

![Version: 5.16.0](https://img.shields.io/badge/Version-5.16.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v0.34.0](https://img.shields.io/badge/AppVersion-v0.34.0-informational?style=flat-square)

**Homepage:** <https://www.runatlantis.io>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| lkysow |  |  |
| jamengual |  |  |
| chenrui333 |  |  |
| nitrocode |  |  |
| genpage |  |  |
| gmartinez-sisti |  |  |

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic atlantis-webhook \
  --from-literal=bitbucket_token=<bitbucket_secret> \
  --from-literal=bitbucket_secret=<bitbucket_secret>
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
  "bitbucket_token": "<bitbucket_secret>",
  "bitbucket_secret": "<bitbucket_secret>"
}
```

</details>

## Source Code

* <https://github.com/runatlantis/atlantis>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| atlantis.bitbucket.user | string | `"auto_example"` |  |
| atlantis.defaultTFVersion | string | `"1.5.7"` |  |
| atlantis.image.repository | string | `"epamedp/atlantis"` |  |
| atlantis.image.tag | string | `"0.1.1"` | If not set appVersion field from Chart.yaml is used |
| atlantis.ingress.host | string | `"atlantis.example.com"` |  |
| atlantis.ingress.path | string | `"/"` |  |
| atlantis.orgAllowlist | string | `"bitbucket.org/organization/*"` |  |
| atlantis.repoConfig | string | `"---\nrepos:\n- id: /.*/\n  allowed_overrides: [\"workflow\"]\n  allow_custom_workflows: true\n"` |  |
| atlantis.serviceAccount.annotations | object | `{}` |  |
| atlantis.vcsSecretName | string | `"atlantis-webhook"` |  |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/infra/core/addons/atlantis"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
