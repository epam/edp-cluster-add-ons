# sonarqube

![Version: 8.0.2](https://img.shields.io/badge/Version-8.0.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 9.9.2](https://img.shields.io/badge/AppVersion-9.9.2-informational?style=flat-square)

A Helm chart for Sonarqube

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://SonarSource.github.io/helm-chart-sonarqube | sonarqube | 8.0.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/sonar"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"sonar","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"sonar"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| sonarqube.deploymentType | string | `"Deployment"` |  |
| sonarqube.env | list | `[{"name":"SONAR_TELEMETRY_ENABLE","value":"false"}]` | Uncomment to enable monitoring passcode secret configuration. ref: https://docs.sonarsource.com/sonarqube-server/latest/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus/ monitoringPasscodeSecretName: "monitoring-passcode" monitoringPasscodeSecretKey: "monitoring-passcode" |
| sonarqube.fullnameOverride | string | `"sonar"` |  |
| sonarqube.ingress.annotations."nginx.ingress.kubernetes.io/proxy-body-size" | string | `"64m"` |  |
| sonarqube.ingress.enabled | bool | `true` |  |
| sonarqube.ingress.hosts[0].name | string | `"sonar.example.com"` |  |
| sonarqube.jdbcOverwrite.enable | bool | `true` |  |
| sonarqube.jdbcOverwrite.jdbcSecretName | string | `"sonar-pguser-sonar"` |  |
| sonarqube.jdbcOverwrite.jdbcSecretPasswordKey | string | `"password"` |  |
| sonarqube.jdbcOverwrite.jdbcUrl | string | `"jdbc:postgresql://sonar-primary.sonar:5432/sonar?socketTimeout=1500"` |  |
| sonarqube.jdbcOverwrite.jdbcUsername | string | `"sonar"` |  |
| sonarqube.jvmCeOpts | string | `"-javaagent:/opt/sonarqube/extensions/plugins/sonarqube-community-branch-plugin-1.14.0.jar=ce"` |  |
| sonarqube.jvmOpts | string | `"-javaagent:/opt/sonarqube/extensions/plugins/sonarqube-community-branch-plugin-1.14.0.jar=web"` |  |
| sonarqube.nameOverride | string | `"sonar"` |  |
| sonarqube.plugins.install[0] | string | `"https://github.com/vaulttec/sonar-auth-oidc/releases/download/v2.1.1/sonar-auth-oidc-plugin-2.1.1.jar"` |  |
| sonarqube.plugins.install[1] | string | `"https://github.com/checkstyle/sonar-checkstyle/releases/download/10.20.1/checkstyle-sonar-plugin-10.20.1.jar"` |  |
| sonarqube.plugins.install[2] | string | `"https://github.com/spotbugs/sonar-findbugs/releases/download/v4.3.0/sonar-findbugs-plugin-4.3.0.jar"` |  |
| sonarqube.plugins.install[3] | string | `"https://github.com/jborgers/sonar-pmd/releases/download/3.5.1/sonar-pmd-plugin-3.5.1.jar"` |  |
| sonarqube.plugins.install[4] | string | `"https://github.com/sbaudoin/sonar-ansible/releases/download/v2.5.1/sonar-ansible-plugin-2.5.1.jar"` |  |
| sonarqube.plugins.install[5] | string | `"https://github.com/sbaudoin/sonar-yaml/releases/download/v1.9.1/sonar-yaml-plugin-1.9.1.jar"` |  |
| sonarqube.plugins.install[6] | string | `"https://github.com/Inform-Software/sonar-groovy/releases/download/1.8/sonar-groovy-plugin-1.8.jar"` |  |
| sonarqube.plugins.install[7] | string | `"https://github.com/mc1arke/sonarqube-community-branch-plugin/releases/download/1.14.0/sonarqube-community-branch-plugin-1.14.0.jar"` |  |
| sonarqube.postgresql.enabled | bool | `false` |  |
| sonarqube.prometheusExporter.enabled | bool | `false` |  |
| sonarqube.resources.limits.cpu | string | `"700m"` |  |
| sonarqube.resources.limits.memory | string | `"3Gi"` |  |
| sonarqube.resources.requests.cpu | string | `"100m"` |  |
| sonarqube.resources.requests.memory | string | `"1.5Gi"` |  |

