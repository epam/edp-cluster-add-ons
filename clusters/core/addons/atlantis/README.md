# atlantis

![Version: 5.8.0](https://img.shields.io/badge/Version-5.8.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v0.30.0](https://img.shields.io/badge/AppVersion-v0.30.0-informational?style=flat-square)

A Helm chart for Atlantis https://www.runatlantis.io

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

