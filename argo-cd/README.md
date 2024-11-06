# argo-cd

![Version: 7.6.12](https://img.shields.io/badge/Version-7.6.12-informational?style=flat-square) ![AppVersion: v2.12.6](https://img.shields.io/badge/AppVersion-v2.12.6-informational?style=flat-square)

A Helm chart for Argo CD Install

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://argoproj.github.io/argo-helm | argo-cd | 7.6.12 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| argo-cd.configs.cm."exec.enabled" | bool | `true` |  |
| argo-cd.configs.cm."oidc.config" | string | `"name: Keycloak\nissuer: https://keycloak.example/auth/realms/shared\nclientID: argocd-tenant\nclientSecret: $keycloak-client-argocd-secret:clientSecret\nrequestedScopes:\n  - openid\n  - profile\n  - email\n  - groups\n"` |  |
| argo-cd.configs.cm."resource.exclusions" | string | `"- apiGroups:\n  - \"tekton.dev\"\n  kinds:\n  - \"PipelineRun\"\n  clusters:\n  - \"*\"\n"` |  |
| argo-cd.configs.cm.url | string | `"https://argocd.example.com"` |  |
| argo-cd.configs.params."application.namespaces" | string | `"krci"` |  |
| argo-cd.configs.params."applicationsetcontroller.namespaces" | string | `"krci"` |  |
| argo-cd.configs.params."server.insecure" | bool | `true` |  |
| argo-cd.configs.rbac."policy.csv" | string | `"# default global admins\ng, ArgoCDAdmins, role:admin\n# Default global developers\ng, ArgoCDReadOnly, role:readonly\n"` |  |
| argo-cd.configs.rbac.scopes | string | `"[groups]"` |  |
| argo-cd.configs.secret.createSecret | bool | `true` | Create the argocd-secret |
| argo-cd.configs.ssh.knownHosts | string | `"# -- list of known host in format:\n# [host]:port key-type key\n# Example\n# [ssh.github.com]:443 ssh-rsa qgSdfOuiYhew/+afhQnvjfjhnhnqgSdfOuiYhew/+afhQnvjfjhnhn\n"` |  |
| argo-cd.dex.enabled | bool | `false` |  |
| argo-cd.global.domain | string | `"argocd.example.com"` | Default domain used by all components # Used for ingresses, certificates, SSO, notifications, etc. |
| argo-cd.redis.enabled | bool | `true` |  |
| argo-cd.server.env[0].name | string | `"ARGOCD_API_SERVER_REPLICAS"` |  |
| argo-cd.server.env[0].value | string | `"1"` |  |
| argo-cd.server.ingress | object | `{"enabled":false,"hostname":"argocd.example.com"}` | Enable after nginx-ingress is installed |
| argo-cd.server.replicas | int | `1` |  |
| eso.enabled | bool | `false` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/infra/core/addons/argocd"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| oidc.enabled | bool | `false` |  |

