# krci-security-operator

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

A Helm chart for the KubeRocketCI krci-security-operator add-on, which imports the Trivy Operator reports of every namespace into DefectDojo

**Homepage:** <https://docs.kuberocketci.io/>

This add-on is a thin wrapper around the [krci-security-operator](https://github.com/KubeRocketCI/krci-security-operator)
component chart. The operator imports the Trivy Operator reports of every namespace into DefectDojo, one test per
workload container and report kind under the product of the namespace's scope (stage, tenant or platform), and
closes the findings of workloads and namespaces that are gone. In the cluster it only reads, apart from its
leader-election Lease and events.

## Prerequisites

- The `trivy-operator` add-on, or another Trivy Operator that writes `VulnerabilityReport` and `ExposedSecretReport`
  objects.
- A DefectDojo, for example the `defectdojo` add-on, and an API v2 token for it.
- With `eso.enabled` (the default): the `external-secrets` add-on, and the DefectDojo URL and token at
  `eso.secretPath` as the properties `defectdojo.url` and `defectdojo.token`.

## Turning it on

1. Provide the credentials through ESO, or set `eso.enabled: false` and create the Secret by hand:

   ```bash
   kubectl create secret generic defectdojo-credentials -n krci-security \
     --from-literal=url=https://defectdojo.example.com \
     --from-literal=token=<api-token>
   ```

2. Set `krci-security-operator.clusterName` to the name of the cluster: the operator closes only the tests that carry
   this name.
3. Enable the add-on in `clusters/core/apps/values.yaml`.

The component [docs](https://github.com/KubeRocketCI/krci-security-operator/blob/main/docs/trivy.md) describe the
naming in DefectDojo, the closing rules and the limitations.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | krci-security-operator | 0.1.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/krci-security-operator"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. The secret holds the properties `defectdojo.url` and `defectdojo.token`. |
| eso.vault | object | `{"mountPath":"core","role":"krci-security-operator","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"krci-security-operator"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| krci-security-operator.clusterName | string | `"in-cluster"` | Cluster name. Every imported test carries the tag `krci-cluster:<clusterName>`, and the operator closes only the tests that carry it, so every cluster that writes into one DefectDojo needs its own name. |
| krci-security-operator.defectdojo.secretName | string | `"defectdojo-credentials"` | Secret in the add-on namespace with the keys `url` and `token` of the cluster's DefectDojo |
| krci-security-operator.excludeNamespaces | list | `[]` | Glob patterns of namespaces that are skipped |
| krci-security-operator.scopes.platform | bool | `true` | Import the reports of the remaining (platform) namespaces |
| krci-security-operator.scopes.stage | bool | `true` | Import the reports of namespaces that belong to a KubeRocketCI Stage |
| krci-security-operator.scopes.tenant | bool | `true` | Import the reports of tenant namespaces (label `app.edp.epam.com/tenant`) that belong to no Stage |
