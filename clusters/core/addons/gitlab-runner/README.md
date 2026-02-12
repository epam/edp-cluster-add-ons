# gitlab-runner

![Version: 0.85.0](https://img.shields.io/badge/Version-0.85.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 18.8.0](https://img.shields.io/badge/AppVersion-18.8.0-informational?style=flat-square)

A Helm chart for Gitlab Runner Controller

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.gitlab.io | gitlab-runner | 0.85.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/gitlab-runner"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.vault | object | `{"mountPath":"core","role":"gitlab","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"gitlab"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| gitlab-runner.gitlabUrl | string | `"https://git.example.com"` |  |
| gitlab-runner.metrics.enabled | bool | `false` |  |
| gitlab-runner.metrics.port | int | `9252` |  |
| gitlab-runner.metrics.portName | string | `"metrics"` |  |
| gitlab-runner.metrics.serviceMonitor.enabled | bool | `true` |  |
| gitlab-runner.nodeSelector | object | `{}` |  |
| gitlab-runner.rbac.create | bool | `true` |  |
| gitlab-runner.resources | object | `{}` |  |
| gitlab-runner.runners.secret | string | `"gitlab-runner-token"` |  |
| gitlab-runner.service.enabled | bool | `true` |  |
| gitlab-runner.tolerations | list | `[]` |  |

