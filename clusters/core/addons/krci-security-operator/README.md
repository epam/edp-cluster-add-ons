# krci-security-operator

![Version: 0.2.0](https://img.shields.io/badge/Version-0.2.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.2.0](https://img.shields.io/badge/AppVersion-0.2.0-informational?style=flat-square)

A Helm chart for the KubeRocketCI krci-security-operator add-on, which imports the Trivy Operator reports of every namespace into DefectDojo

**Homepage:** <https://docs.kuberocketci.io/>

This add-on is a thin wrapper around the [krci-security-operator](https://github.com/KubeRocketCI/krci-security-operator)
component chart. The operator imports the Trivy Operator reports of every namespace into DefectDojo: one product
`<clusterName>/<namespace>` per namespace under the Product Type `defectdojo.productType`, engagement
`trivy-operator`, one test per report kind, workload and container. It closes the findings of workloads, containers
and namespaces that are gone. In the cluster it only reads, apart from its leader-election Lease and events.

## Prerequisites

- The `trivy-operator` add-on, or another Trivy Operator that writes `VulnerabilityReport` and `ExposedSecretReport`
  objects.
- DefectDojo 3.5.200 or later, for example the `defectdojo` add-on. Earlier versions may work but are not tested.
- A DefectDojo API v2 token. The token options and the recommended least-privilege setup are in
  [DefectDojo API token](https://github.com/KubeRocketCI/krci-security-operator/blob/main/docs/trivy.md#defectdojo-api-token).
- With `eso.enabled` (the default): the `external-secrets` add-on, and the DefectDojo URL and token at
  `eso.secretPath` as the properties `defectdojo.url` and `defectdojo.token`.

## Turning it on

1. Provide the credentials through ESO, or set `eso.enabled: false` and create the Secret by hand:

   ```bash
   kubectl create secret generic defectdojo-credentials -n krci-security \
     --from-literal=url=https://defectdojo.example.com \
     --from-literal=token=<api-token>
   ```

2. Set `krci-security-operator.clusterName` to the name of the cluster. It is required and must be unique in the
   DefectDojo: the operator closes only the tests of its own cluster. The add-on does not render without it.
3. Keep `krci-security-operator.defectdojo.productType` the same in every cluster that writes into the same DefectDojo.
4. Enable the add-on in `clusters/core/apps/values.yaml`.

The component [docs](https://github.com/KubeRocketCI/krci-security-operator/blob/main/docs/trivy.md) describe the
naming in DefectDojo, the closing rules and the limitations.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | krci-security-operator | 0.2.0 |

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
| krci-security-operator.clusterName | string | `""` | Required, no default: set it per cluster. Unique name of this cluster in the DefectDojo, a lowercase RFC 1123 DNS label. Every namespace product is named `<clusterName>/<namespace>`, and the operator closes only the tests of its own cluster. The add-on does not render while it is empty. |
| krci-security-operator.defectdojo.productType | string | `"KubeRocketCI"` | DefectDojo Product Type of the namespace products. Use one value for every cluster that writes into the same DefectDojo; a product that exists under another Product Type fails its reimports |
| krci-security-operator.defectdojo.secretName | string | `"defectdojo-credentials"` | Secret in the add-on namespace with the keys `url` and `token` of the cluster's DefectDojo |
| krci-security-operator.excludeNamespaces | list | `[]` | Glob patterns of namespaces that are skipped. The tests of an excluded namespace are closed |
