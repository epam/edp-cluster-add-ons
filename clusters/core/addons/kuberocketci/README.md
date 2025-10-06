# edp-install

![Version: 3.12.3](https://img.shields.io/badge/Version-3.12.3-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.12.3](https://img.shields.io/badge/AppVersion-3.12.3-informational?style=flat-square)

A Helm chart for KubeRocketCI Platform

**Homepage:** <https://docs.kuberocketci.io/>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | edp-install | 3.12.3 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| edp-install.cd-pipeline-operator.capsuleTenant | object | `{"create":false}` | Required tenancyEngine: capsule. Specify Capsule Tenant specification for Environments. |
| edp-install.cd-pipeline-operator.enabled | bool | `true` |  |
| edp-install.cd-pipeline-operator.manageNamespace | bool | `true` | should the operator manage(create/delete) namespaces for stages Refer to the guide for managing namespace (https://docs.kuberocketci.io/docs/operator-guide/auth/namespace-management) |
| edp-install.cd-pipeline-operator.secretManager | string | `"own"` | Flag indicating whether the operator should manage secrets for stages. This parameter controls the provisioning of the 'regcred' secret within deployed environments, facilitating access to private container registries. Set the parameter to "none" under the following conditions:   - If 'global.dockerRegistry.type=ecr' and IRSA is enabled, or   - If 'global.dockerRegistry.type=openshift'. For private registries, choose the most appropriate method to provide credentials to deployed environments. Refer to the guide for managing container registries (https://docs.kuberocketci.io/docs/user-guide/manage-container-registries). Possible values: own/eso/none.   - own: Copies the secret once from the parent namespace, without subsequent reconciliation. If updated in the parent namespace, manual updating in all created namespaces is required.   - eso: The secret will be managed by the External Secrets Operator (requires installation and configuration in the cluster: https://docs.kuberocketci.io/docs/operator-guide/secrets-management/install-external-secrets-operator).   - none: Disables secrets management logic. |
| edp-install.cd-pipeline-operator.tenancyEngine | string | `"none"` | Defines the type of the tenant engine that can be "none", "kiosk" or "capsule"; for Stages with external cluster tenancyEngine will be ignored. Default: none |
| edp-install.codebase-operator.enabled | bool | `true` |  |
| edp-install.edp-headlamp.config.baseURL | string | `""` | base url path at which headlamp should run |
| edp-install.edp-headlamp.config.oidc | object | `{"clientID":"shared","clientSecretKey":"clientSecret","clientSecretName":"keycloak-client-headlamp-secret","enabled":false,"issuerUrl":"","scopes":""}` | For detailed instructions, refer to: https://docs.kuberocketci.io/docs/operator-guide/auth/configure-keycloak-oidc-eks, https://docs.kuberocketci.io/docs/operator-guide/auth/ui-portal-oidc |
| edp-install.edp-headlamp.config.oidc.clientID | string | `"shared"` | OIDC client ID |
| edp-install.edp-headlamp.config.oidc.clientSecretKey | string | `"clientSecret"` | OIDC client secret key |
| edp-install.edp-headlamp.config.oidc.clientSecretName | string | `"keycloak-client-headlamp-secret"` | OIDC client secret name |
| edp-install.edp-headlamp.config.oidc.issuerUrl | string | `""` | Azure Entra: https://sts.windows.net/<tenant-id>/ |
| edp-install.edp-headlamp.config.oidc.scopes | string | `""` | OIDC scopes to be used |
| edp-install.edp-headlamp.enabled | bool | `true` |  |
| edp-install.edp-tekton.enabled | bool | `true` |  |
| edp-install.edp-tekton.gitServers | object | `{}` |  |
| edp-install.edp-tekton.interceptor.enabled | bool | `true` | Deploy KubeRocketCI interceptor as a part of pipeline library when true. Default: true |
| edp-install.edp-tekton.pipelines.image.registry | string | `"docker.io"` | Registry for tekton pipelines images. Default: docker.io |
| edp-install.edp-tekton.pipelines.imagePullSecrets | list | `[]` | List of image pull secrets used by the Tekton ServiceAccount for pulling images from private registries. Example: imagePullSecrets:   - name: regcred |
| edp-install.edp-tekton.tekton-cache.enabled | bool | `true` |  |
| edp-install.edp-tekton.tekton.pruner.create | bool | `true` |  |
| edp-install.externalSecrets.enabled | bool | `false` | Configure External Secrets for KubeRocketCI platform. Deploy SecretStore. Default: false |
| edp-install.externalSecrets.manageCodemieSecretsName | string | `"/edp/codemie-secrets"` |  |
| edp-install.externalSecrets.manageEDPInstallSecrets | bool | `true` | Create necessary secrets for KubeRocketCI installation, using External Secret Operator |
| edp-install.externalSecrets.manageEDPInstallSecretsName | string | `"/edp/deploy-secrets"` | Value name in AWS ParameterStore or AWS SecretsManager. Used when manageEDPInstallSecrets is true |
| edp-install.externalSecrets.manageGitProviderSecretsName | string | `"/edp/git-provider-secrets"` |  |
| edp-install.externalSecrets.secretProvider.aws.region | string | `"eu-central-1"` | AWS Region where secrets are stored, e.g. eu-central-1 |
| edp-install.externalSecrets.secretProvider.aws.role | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | IAM Role to be used for Accessing AWS either Parameter Store or Secret Manager. Format: arn:aws:iam::<AWS_ACCOUNT_ID>:role/<AWS_IAM_ROLE_NAME> |
| edp-install.externalSecrets.secretProvider.aws.service | string | `"ParameterStore"` | Use AWS as a Secret Provider. Can be ParameterStore or SecretsManager |
| edp-install.externalSecrets.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| edp-install.extraQuickLinks | object | `{}` | Define extra Quick Links, more details: https://github.com/epam/edp-codebase-operator/ |
| edp-install.gerrit-operator.enabled | bool | `false` |  |
| edp-install.gitfusion | object | `{"enabled":false}` | Enable GitFusion integration for repository and branch discovery. |
| edp-install.global.adminGroupName | string | `""` |  |
| edp-install.global.apiClusterEndpoint | string | `""` | API Сluster Endpoint configuration for static kubeconfig generation |
| edp-install.global.apiGatewayUrl | string | `""` | API Gateway URL configuration for Widget Functionality |
| edp-install.global.availableClusters | string | `""` | Define the list of available remote clusters to deploy applications. Example: "cluster1, cluster2, cluster3" |
| edp-install.global.developerGroupName | string | `""` |  |
| edp-install.global.dnsWildCard | string | `"example.com"` | a cluster DNS wildcard name |
| edp-install.global.gitProviders | string | `nil` | Can be gerrit, github or gitlab. By default: github |
| edp-install.global.platform | string | `"kubernetes"` | platform type that can be "kubernetes" or "openshift" |
| edp-install.global.viewerGroupName | string | `""` |  |
| edp-install.quickLinks | object | `` | Define platform Quick Links, more details: https://github.com/epam/edp-codebase-operator/ |
| edp-install.quickLinks.logging.provider | string | `""` | Define the provider name for correct URL generation. Available providers: "opensearch", "datadog". If the provider name is not specified, the base URL will be used. |
| edp-install.quickLinks.monitoring.provider | string | `""` | Define the provider name for correct URL generation. Available providers: "grafana", "datadog". If the provider name is not specified, the base URL will be used. |

