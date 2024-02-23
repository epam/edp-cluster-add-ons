# nexus-operator

![Version: 3.2.0](https://img.shields.io/badge/Version-3.2.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.2.0](https://img.shields.io/badge/AppVersion-3.2.0-informational?style=flat-square)

A Helm chart for EDP Nexus Operator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | nexus-operator | 3.2.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.secretName | string | `"/edp/eks/addons/nexus-operator"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |

