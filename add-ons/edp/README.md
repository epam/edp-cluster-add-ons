# edp-install

![Version: 3.6.0](https://img.shields.io/badge/Version-3.6.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.6.0](https://img.shields.io/badge/AppVersion-3.6.0-informational?style=flat-square)

A Helm chart for EDP Install

**Homepage:** <https://epam.github.io/edp-install/>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | edp-install | 3.6.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| edp-install.edp-headlamp.config.oidc.clientID | string | `"shared"` |  |
| edp-install.edp-headlamp.config.oidc.enabled | bool | `true` |  |
| edp-install.edp-headlamp.config.oidc.keycloakUrl | string | `"https://keycloak.example.com"` |  |
| edp-install.edp-tekton.github.host | string | `"github.com"` |  |
| edp-install.externalSecrets.enabled | bool | `true` |  |
| edp-install.externalSecrets.manageEDPInstallSecrets | bool | `true` |  |
| edp-install.externalSecrets.manageEDPInstallSecretsName | string | `"/edp/deploy-secrets"` |  |
| edp-install.externalSecrets.secretProvider.aws.role | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` |  |
| edp-install.global.dnsWildCard | string | `"example.com"` |  |
| edp-install.global.dockerRegistry.space | string | `"edp"` |  |
| edp-install.global.dockerRegistry.type | string | `"harbor"` |  |
| edp-install.global.dockerRegistry.url | string | `"registry.example.com"` |  |
| edp-install.global.gitProvider | string | `"github"` |  |
| edp-install.global.platform | string | `"kubernetes"` |  |
| edp-install.sso.admins[0] | string | `"john@example.com"` |  |
| edp-install.sso.admins[1] | string | `"mike@example.com"` |  |
| edp-install.sso.developers[0] | string | `"john@example.com"` |  |
| edp-install.sso.developers[1] | string | `"mike@example.com"` |  |
| edp-install.sso.enabled | bool | `true` |  |
| edp-install.sso.keycloakUrl | string | `"https://keycloak.example.com"` |  |

