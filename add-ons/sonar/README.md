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
| oidc | object | `{"enabled":false}` | Integration with keycloak |
| sonarqube.deploymentType | string | `"Deployment"` |  |
| sonarqube.env[0].name | string | `"SONAR_TELEMETRY_ENABLE"` |  |
| sonarqube.env[0].value | string | `"false"` |  |
| sonarqube.fullnameOverride | string | `"sonar"` |  |
| sonarqube.ingress.annotations."nginx.ingress.kubernetes.io/cors-allow-headers" | string | `"DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization"` |  |
| sonarqube.ingress.annotations."nginx.ingress.kubernetes.io/cors-allow-methods" | string | `"OPTIONS, GET"` |  |
| sonarqube.ingress.annotations."nginx.ingress.kubernetes.io/cors-allow-origin" | string | `"*"` |  |
| sonarqube.ingress.annotations."nginx.ingress.kubernetes.io/enable-cors" | string | `"true"` |  |
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
| sonarqube.plugins.install[1] | string | `"https://github.com/checkstyle/sonar-checkstyle/releases/download/10.12.1/checkstyle-sonar-plugin-10.12.1.jar"` |  |
| sonarqube.plugins.install[2] | string | `"https://github.com/spotbugs/sonar-findbugs/releases/download/4.2.9/sonar-findbugs-plugin-4.2.9.jar"` |  |
| sonarqube.plugins.install[3] | string | `"https://github.com/jborgers/sonar-pmd/releases/download/3.4.0/sonar-pmd-plugin-3.4.0.jar"` |  |
| sonarqube.plugins.install[4] | string | `"https://github.com/sbaudoin/sonar-ansible/releases/download/v2.5.1/sonar-ansible-plugin-2.5.1.jar"` |  |
| sonarqube.plugins.install[5] | string | `"https://github.com/sbaudoin/sonar-yaml/releases/download/v1.7.0/sonar-yaml-plugin-1.7.0.jar"` |  |
| sonarqube.plugins.install[6] | string | `"https://github.com/Inform-Software/sonar-groovy/releases/download/1.8/sonar-groovy-plugin-1.8.jar"` |  |
| sonarqube.plugins.install[7] | string | `"https://github.com/mc1arke/sonarqube-community-branch-plugin/releases/download/1.14.0/sonarqube-community-branch-plugin-1.14.0.jar"` |  |
| sonarqube.postgresql.enabled | bool | `false` |  |
| sonarqube.prometheusExporter.enabled | bool | `false` |  |
| sonarqube.resources.limits.cpu | string | `"700m"` |  |
| sonarqube.resources.limits.memory | string | `"3Gi"` |  |
| sonarqube.resources.requests.cpu | string | `"100m"` |  |
| sonarqube.resources.requests.memory | string | `"1.5Gi"` |  |

