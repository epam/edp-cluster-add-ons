# edp-install

![Version: 3.3.0](https://img.shields.io/badge/Version-3.3.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.3.0](https://img.shields.io/badge/AppVersion-3.3.0-informational?style=flat-square)

A Helm chart for EDP Install

**Homepage:** <https://epam.github.io/edp-install/>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | edp-install | 3.3.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| edp-install.argocd.enabled | bool | `true` |  |
| edp-install.argocd.url | string | `"https://argocd-edp.example.com"` |  |
| edp-install.awsRegion | string | `"eu-central-1"` |  |
| edp-install.dockerRegistry.url | string | `"012345678910.dkr.ecr.eu-central-1.amazonaws.com"` |  |
| edp-install.edp-headlamp.config.oidc.clientID | string | `"shared"` |  |
| edp-install.edp-headlamp.config.oidc.enabled | bool | `true` |  |
| edp-install.edp-tekton.gitlab.host | string | `"gitlab.example.com"` |  |
| edp-install.edp-tekton.kaniko.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_Kaniko"` |  |
| edp-install.externalSecrets.enabled | bool | `true` |  |
| edp-install.externalSecrets.manageEDPInstallSecrets | bool | `true` |  |
| edp-install.externalSecrets.manageEDPInstallSecretsName | string | `"/edp/deploy-secrets"` |  |
| edp-install.externalSecrets.secretProvider.aws.role | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` |  |
| edp-install.gerrit-operator.enabled | bool | `false` |  |
| edp-install.global.admins[0] | string | `"john@example.com"` |  |
| edp-install.global.admins[1] | string | `"mike@example.com"` |  |
| edp-install.global.developers[0] | string | `"john@example.com"` |  |
| edp-install.global.developers[1] | string | `"mike@example.com"` |  |
| edp-install.global.dnsWildCard | string | `"example.com"` |  |
| edp-install.global.edpName | string | `"edp"` |  |
| edp-install.global.gitProvider | string | `"gitlab"` |  |
| edp-install.global.keycloakUrl | string | `"https://keycloak.example.com"` |  |
| edp-install.global.kioskEnabled | bool | `false` |  |
| edp-install.global.platform | string | `"kubernetes"` |  |
| edp-install.global.webConsole.url | string | `"https://XXXXXXXXXXXXXXXXXXXXXX.gr7.eu-central-1.eks.amazonaws.com"` |  |
| edp-install.kaniko.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_Kaniko"` |  |
| edp-install.nexus-operator.nexus.storage.class | string | `"ebs-sc"` |  |
| edp-install.sonar-operator.sonar.storage.data.class | string | `"ebs-sc"` |  |
| edp-install.sonar-operator.sonar.storage.database.class | string | `"ebs-sc"` |  |

