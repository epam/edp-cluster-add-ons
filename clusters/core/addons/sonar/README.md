# sonarqube

![Version: 2025.3.1](https://img.shields.io/badge/Version-2025.3.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2025.3.1](https://img.shields.io/badge/AppVersion-2025.3.1-informational?style=flat-square)

A Helm chart for Sonarqube

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://SonarSource.github.io/helm-chart-sonarqube | sonarqube | 2025.3.1 |

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
| sonarqube.community.enabled | bool | `true` |  |
| sonarqube.deploymentType | string | `"Deployment"` |  |
| sonarqube.env | list | `[{"name":"SONAR_TELEMETRY_ENABLE","value":"false"}]` | Uncomment to enable monitoring passcode secret configuration. ref: https://docs.sonarsource.com/sonarqube-server/latest/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus/ monitoringPasscodeSecretName: "monitoring-passcode" monitoringPasscodeSecretKey: "monitoring-passcode" |
| sonarqube.extraInitContainers[0].command[0] | string | `"sh"` |  |
| sonarqube.extraInitContainers[0].command[1] | string | `"-c"` |  |
| sonarqube.extraInitContainers[0].command[2] | string | `"wget -O /tmp/sonarqube-webapp.zip https://github.com/mc1arke/sonarqube-community-branch-plugin/releases/download/25.5.0/sonarqube-webapp.zip && unzip -o /tmp/sonarqube-webapp.zip -d /web && chmod -R 755 /web && chown -R 1000:0 /web && rm -f /tmp/sonarqube-webapp.zip\n"` |  |
| sonarqube.extraInitContainers[0].image | string | `"busybox:1.37"` |  |
| sonarqube.extraInitContainers[0].name | string | `"download-webapp"` |  |
| sonarqube.extraInitContainers[0].volumeMounts[0].mountPath | string | `"/web"` |  |
| sonarqube.extraInitContainers[0].volumeMounts[0].name | string | `"webapp"` |  |
| sonarqube.extraVolumeMounts[0].mountPath | string | `"/opt/sonarqube/web"` |  |
| sonarqube.extraVolumeMounts[0].name | string | `"webapp"` |  |
| sonarqube.extraVolumes[0].emptyDir | object | `{}` |  |
| sonarqube.extraVolumes[0].name | string | `"webapp"` |  |
| sonarqube.fullnameOverride | string | `"sonar"` |  |
| sonarqube.image.repository | string | `"sonarqube"` |  |
| sonarqube.image.tag | string | `"25.5.0.107428-community"` |  |
| sonarqube.ingress.annotations."nginx.ingress.kubernetes.io/proxy-body-size" | string | `"64m"` |  |
| sonarqube.ingress.enabled | bool | `true` |  |
| sonarqube.ingress.hosts[0].name | string | `"sonar.example.com"` |  |
| sonarqube.jdbcOverwrite.enable | bool | `true` |  |
| sonarqube.jdbcOverwrite.jdbcSecretName | string | `"sonar-pguser-sonar"` |  |
| sonarqube.jdbcOverwrite.jdbcSecretPasswordKey | string | `"password"` |  |
| sonarqube.jdbcOverwrite.jdbcUrl | string | `"jdbc:postgresql://sonar-primary.sonar:5432/sonar?socketTimeout=1500"` |  |
| sonarqube.jdbcOverwrite.jdbcUsername | string | `"sonar"` |  |
| sonarqube.jvmCeOpts | string | `"-javaagent:/opt/sonarqube/extensions/plugins/sonarqube-community-branch-plugin-25.5.0.jar=ce"` |  |
| sonarqube.jvmOpts | string | `"-javaagent:/opt/sonarqube/extensions/plugins/sonarqube-community-branch-plugin-25.5.0.jar=web"` |  |
| sonarqube.nameOverride | string | `"sonar"` |  |
| sonarqube.plugins.install[0] | string | `"https://github.com/sonar-auth-oidc/sonar-auth-oidc/releases/download/v3.0.0/sonar-auth-oidc-plugin-3.0.0.jar"` |  |
| sonarqube.plugins.install[1] | string | `"https://github.com/checkstyle/sonar-checkstyle/releases/download/10.20.1/checkstyle-sonar-plugin-10.20.1.jar"` |  |
| sonarqube.plugins.install[2] | string | `"https://github.com/spotbugs/sonar-findbugs/releases/download/4.2.9/sonar-findbugs-plugin-4.2.9.jar"` |  |
| sonarqube.plugins.install[3] | string | `"https://github.com/jborgers/sonar-pmd/releases/download/3.5.1/sonar-pmd-plugin-3.5.1.jar"` |  |
| sonarqube.plugins.install[4] | string | `"https://github.com/sbaudoin/sonar-ansible/releases/download/v2.5.1/sonar-ansible-plugin-2.5.1.jar"` |  |
| sonarqube.plugins.install[5] | string | `"https://github.com/sbaudoin/sonar-yaml/releases/download/v1.9.1/sonar-yaml-plugin-1.9.1.jar"` |  |
| sonarqube.plugins.install[6] | string | `"https://github.com/Inform-Software/sonar-groovy/releases/download/1.8/sonar-groovy-plugin-1.8.jar"` |  |
| sonarqube.plugins.install[7] | string | `"https://github.com/mc1arke/sonarqube-community-branch-plugin/releases/download/25.5.0/sonarqube-community-branch-plugin-25.5.0.jar"` |  |
| sonarqube.postgresql.enabled | bool | `false` |  |
| sonarqube.prometheusExporter.enabled | bool | `false` |  |
| sonarqube.resources.limits.cpu | string | `"700m"` |  |
| sonarqube.resources.limits.memory | string | `"3Gi"` |  |
| sonarqube.resources.requests.cpu | string | `"100m"` |  |
| sonarqube.resources.requests.memory | string | `"1.5Gi"` |  |
| sonarqube.sonarProperties."sonar.ce.javaAdditionalOpts" | string | `"-javaagent:/opt/sonarqube/extensions/plugins/sonarqube-community-branch-plugin-25.5.0.jar=ce"` |  |
| sonarqube.sonarProperties."sonar.web.javaAdditionalOpts" | string | `"-javaagent:/opt/sonarqube/extensions/plugins/sonarqube-community-branch-plugin-25.5.0.jar=web"` |  |

