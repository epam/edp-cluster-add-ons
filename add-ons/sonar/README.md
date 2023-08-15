# sonarqube

![Version: 1.0.31](https://img.shields.io/badge/Version-1.0.31-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.31](https://img.shields.io/badge/AppVersion-1.0.31-informational?style=flat-square)

A Helm chart for Sonarqube

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://SonarSource.github.io/helm-chart-sonarqube | sonarqube-lts | 1.0.31 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| sonarqube-lts.deploymentType | string | `"Deployment"` |  |
| sonarqube-lts.env[0].name | string | `"SONAR_TELEMETRY_ENABLE"` |  |
| sonarqube-lts.env[0].value | string | `"false"` |  |
| sonarqube-lts.fullnameOverride | string | `"sonar"` |  |
| sonarqube-lts.ingress.enabled | bool | `true` |  |
| sonarqube-lts.ingress.hosts[0].name | string | `"sonar.example.com"` |  |
| sonarqube-lts.jdbcUrlOverride | string | `"jdbc:postgresql://postgresql-primary.sonar.svc:5432/sonar?socketTimeout=1500"` |  |
| sonarqube-lts.nameOverride | string | `"sonar"` |  |
| sonarqube-lts.plugins.install[0] | string | `"https://github.com/vaulttec/sonar-auth-oidc/releases/download/v2.1.1/sonar-auth-oidc-plugin-2.1.1.jar"` |  |
| sonarqube-lts.plugins.install[1] | string | `"https://github.com/checkstyle/sonar-checkstyle/releases/download/9.3/checkstyle-sonar-plugin-9.3.jar"` |  |
| sonarqube-lts.plugins.install[2] | string | `"https://github.com/spotbugs/sonar-findbugs/releases/download/4.2.2/sonar-findbugs-plugin-4.2.2.jar"` |  |
| sonarqube-lts.plugins.install[3] | string | `"https://github.com/jborgers/sonar-pmd/releases/download/3.4.0/sonar-pmd-plugin-3.4.0.jar"` |  |
| sonarqube-lts.plugins.install[4] | string | `"https://github.com/sbaudoin/sonar-ansible/releases/download/v2.5.1/sonar-ansible-plugin-2.5.1.jar"` |  |
| sonarqube-lts.plugins.install[5] | string | `"https://github.com/sbaudoin/sonar-yaml/releases/download/v1.7.0/sonar-yaml-plugin-1.7.0.jar"` |  |
| sonarqube-lts.plugins.install[6] | string | `"https://github.com/Inform-Software/sonar-groovy/releases/download/1.8/sonar-groovy-plugin-1.8.jar"` |  |
| sonarqube-lts.postgresql.enabled | bool | `false` |  |
| sonarqube-lts.postgresql.existingSecret | string | `"postgresql-pguser-sonar"` |  |
| sonarqube-lts.postgresql.existingSecretPasswordKey | string | `"password"` |  |
| sonarqube-lts.postgresql.postgresqlDatabase | string | `"sonarDB"` |  |
| sonarqube-lts.postgresql.postgresqlPassword | string | `"sonarPass"` |  |
| sonarqube-lts.postgresql.postgresqlUsername | string | `"sonar"` |  |
| sonarqube-lts.prometheusExporter.enabled | bool | `false` |  |
| sonarqube-lts.resources.limits.cpu | string | `"700m"` |  |
| sonarqube-lts.resources.limits.memory | string | `"3Gi"` |  |
| sonarqube-lts.resources.requests.cpu | string | `"100m"` |  |
| sonarqube-lts.resources.requests.memory | string | `"1.5Gi"` |  |

