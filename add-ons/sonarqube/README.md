# sonarqube

![Version: 10.1.0](https://img.shields.io/badge/Version-10.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 10.1.0](https://img.shields.io/badge/AppVersion-10.1.0-informational?style=flat-square)

A Helm chart for Sonarqube

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://SonarSource.github.io/helm-chart-sonarqube | sonarqube | 10.1.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| sonarqube.ingress.enabled | bool | `true` |  |
| sonarqube.ingress.hosts[0].name | string | `"sonarqube.example.com"` |  |
| sonarqube.jdbcOverwrite.enable | string | `"enable"` |  |
| sonarqube.jdbcOverwrite.jdbcSecretName | string | `"postgresql-pguser-sonarqube"` |  |
| sonarqube.jdbcOverwrite.jdbcSecretPasswordKey | string | `"password"` |  |
| sonarqube.jdbcOverwrite.jdbcUrl | string | `"jdbc:postgresql://postgresql-primary.sonarqube.svc:5432/sonarqube?socketTimeout=1500"` |  |
| sonarqube.jdbcOverwrite.jdbcUsername | string | `"sonarqube"` |  |
| sonarqube.postgresql.enabled | bool | `false` |  |
| sonarqube.resources.limits.cpu | string | `"700m"` |  |
| sonarqube.resources.limits.memory | string | `"3Gi"` |  |
| sonarqube.resources.requests.cpu | string | `"100m"` |  |
| sonarqube.resources.requests.memory | string | `"1.5Gi"` |  |

