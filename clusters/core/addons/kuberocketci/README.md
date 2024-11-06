# edp-install

![Version: 3.10.2](https://img.shields.io/badge/Version-3.10.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.10.2](https://img.shields.io/badge/AppVersion-3.10.2-informational?style=flat-square)

A Helm chart for KubeRocketCI Platform

**Homepage:** <https://docs.kuberocketci.io/>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | edp-install | 3.10.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| edp-install.cd-pipeline-operator.secretManager | string | `"own"` | Flag indicating whether the operator should manage secrets for stages. This parameter controls the provisioning of the 'regcred' secret within deployed environments, facilitating access to private container registries. Set the parameter to "none" under the following conditions:   - If 'global.dockerRegistry.type=ecr' and IRSA is enabled, or   - If 'global.dockerRegistry.type=openshift'. For private registries, choose the most appropriate method to provide credentials to deployed environments. Refer to the guide for managing container registries (https://docs.kuberocketci.io/docs/user-guide/manage-container-registries). Possible values: own/eso/none.   - own: Copies the secret once from the parent namespace, without subsequent reconciliation. If updated in the parent namespace, manual updating in all created namespaces is required.   - eso: The secret will be managed by the External Secrets Operator (requires installation and configuration in the cluster: https://docs.kuberocketci.io/docs/operator-guide/secrets-management/install-external-secrets-operator).   - none: Disables secrets management logic. |
| edp-install.cd-pipeline-operator.tenancyEngine | string | `"none"` | Defines the type of the tenant engine that can be "none", "kiosk" or "capsule"; for Stages with external cluster tenancyEngine will be ignored. Default: none |
| edp-install.edp-headlamp.config.oidc | object | `{"clientID":"shared","clientSecretKey":"clientSecret","clientSecretName":"keycloak-client-headlamp-secret","enabled":true,"issuerUrl":""}` | For detailed instructions, refer to: https://docs.kuberocketci.io/docs/operator-guide/auth/configure-keycloak-oidc-eks, https://docs.kuberocketci.io/docs/operator-guide/auth/ui-portal-oidc |
| edp-install.edp-headlamp.config.oidc.clientID | string | `"shared"` | OIDC client ID |
| edp-install.edp-headlamp.config.oidc.clientSecretKey | string | `"clientSecret"` | OIDC client secret key |
| edp-install.edp-headlamp.config.oidc.clientSecretName | string | `"keycloak-client-headlamp-secret"` | OIDC client secret name |
| edp-install.edp-headlamp.config.oidc.issuerUrl | string | `""` | Azure Entra: https://sts.windows.net/<tenant-id>/ |
| edp-install.edp-tekton.dashboard.enabled | bool | `true` | https://docs.kuberocketci.io/docs/operator-guide/auth/oauth2-proxy |
| edp-install.edp-tekton.dashboard.ingress.annotations | object | `{}` | Annotations for Ingress resource |
| edp-install.edp-tekton.dashboard.ingress.enabled | bool | `true` | Deploy KubeRocketCI Dashboard ingress as a part of pipeline library when true. Default: true |
| edp-install.edp-tekton.dashboard.readOnly | bool | `false` | Define mode for Tekton Dashboard. Enable/disaable capability to create/modify/remove Tekton objects via Tekton Dashboard. Default: false. |
| edp-install.edp-tekton.gitServers | object | `{}` |  |
| edp-install.edp-tekton.tekton-cache.enabled | bool | `true` |  |
| edp-install.externalSecrets.enabled | bool | `false` | Configure External Secrets for EDP platform. Deploy SecretStore. Default: false |
| edp-install.externalSecrets.manageCodemieSecretsName | string | `"/edp/codemie-secrets"` |  |
| edp-install.externalSecrets.manageEDPInstallSecrets | bool | `true` |  |
| edp-install.externalSecrets.manageEDPInstallSecretsName | string | `"/edp/deploy-secrets"` | Value name in AWS ParameterStore or AWS SecretsManager. Used when manageEDPInstallSecrets is true |
| edp-install.externalSecrets.manageGitProviderSecretsName | string | `"/edp/git-provider-secrets"` |  |
| edp-install.externalSecrets.secretProvider.aws.role | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` |  |
| edp-install.extraQuickLinks | object | `{}` | Define extra Quick Links, more details: https://github.com/epam/edp-codebase-operator/ |
| edp-install.global.apiGatewayUrl | string | `""` | API Gateway URL configuration for Widget Functionality |
| edp-install.global.dnsWildCard | string | `"example.com"` | a cluster DNS wildcard name |
| edp-install.global.gitProviders | string | `nil` | Can be gerrit, github or gitlab. By default: github |
| edp-install.global.platform | string | `"kubernetes"` | platform type that can be "kubernetes" or "openshift" |
| edp-install.quickLinks | string | `` | Define platform Quick Links, more details: https://github.com/epam/edp-codebase-operator/ |

