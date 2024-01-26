# edp-install

![Version: 3.7.5](https://img.shields.io/badge/Version-3.7.5-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.7.5](https://img.shields.io/badge/AppVersion-3.7.5-informational?style=flat-square)

A Helm chart for EDP Install

**Homepage:** <https://epam.github.io/edp-install/>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | edp-install | 3.7.5 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| edp-install.edp-headlamp.config.baseURL | string | `""` | base url path at which headlamp should run |
| edp-install.edp-headlamp.config.oidc.clientID | string | `"shared"` | OIDC client ID |
| edp-install.edp-headlamp.config.oidc.clientSecretKey | string | `"clientSecret"` | OIDC client secret key |
| edp-install.edp-headlamp.config.oidc.clientSecretName | string | `"keycloak-client-headlamp-secret"` | OIDC client secret name |
| edp-install.edp-headlamp.config.oidc.enabled | bool | `true` |  |
| edp-install.edp-headlamp.config.oidc.issuerRealm | string | `""` | OIDC issuer realm |
| edp-install.edp-headlamp.config.oidc.keycloakUrl | string | `"https://keycloak.example.com"` | Keycloak URL |
| edp-install.edp-headlamp.config.oidc.scopes | string | `""` | OIDC scopes to be used |
| edp-install.edp-tekton.dashboard.enabled | bool | `true` | https://epam.github.io/edp-install/operator-guide/oauth2-proxy/ |
| edp-install.edp-tekton.dashboard.ingress.annotations | object | `{}` | Annotations for Ingress resource |
| edp-install.edp-tekton.dashboard.ingress.enabled | bool | `true` | Deploy EDP Dashboard ingress as a part of pipeline library when true. Default: true |
| edp-install.edp-tekton.dashboard.readOnly | bool | `false` | Define mode for Tekton Dashboard. Enable/disaable capability to create/modify/remove Tekton objects via Tekton Dashboard. Default: false. |
| edp-install.edp-tekton.github.host | string | `"github.com"` |  |
| edp-install.edp-tekton.tekton-cache.enabled | bool | `true` |  |
| edp-install.externalSecrets.enabled | bool | `true` | Configure External Secrets for EDP platform. Deploy SecretStore. Default: false |
| edp-install.externalSecrets.manageEDPInstallSecrets | bool | `true` |  |
| edp-install.externalSecrets.manageEDPInstallSecretsName | string | `"/edp/deploy-secrets"` |  |
| edp-install.externalSecrets.secretProvider.aws.role | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` |  |
| edp-install.global.dnsWildCard | string | `"example.com"` | a cluster DNS wildcard name |
| edp-install.global.gitProvider | string | `"github"` | Can be gerrit, github or gitlab. By default: github |
| edp-install.global.platform | string | `"kubernetes"` | platform type that can be "kubernetes" or "openshift" |
| edp-install.oauth2_proxy.enabled | bool | `true` | Install oauth2-proxy as a part of EDP deployment. Default: false |
| edp-install.sso | object | `{"admins":["john@example.com","mike@example.com"],"developers":["john@example.com","mike@example.com"],"enabled":true,"keycloakUrl":"https://keycloak.example.com"}` | Enable SSO for EDP oauth2-proxy. Default: false |
| edp-install.sso.admins | list | `["john@example.com","mike@example.com"]` | Administrators of EDP tenant |
| edp-install.sso.developers | list | `["john@example.com","mike@example.com"]` | Developers of EDP tenant |
| edp-install.sso.keycloakUrl | string | `"https://keycloak.example.com"` | Keycloak URL |

