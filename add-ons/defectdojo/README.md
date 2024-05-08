# defectdojo

![Version: 1.6.127](https://img.shields.io/badge/Version-1.6.127-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.34.1](https://img.shields.io/badge/AppVersion-2.34.1-informational?style=flat-square)

A Helm chart for DefectDojo Install

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/helm-charts | defectdojo | 1.6.127 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| defectdojo.alternativeHosts[0] | string | `"defectdojo-django.defectdojo"` |  |
| defectdojo.django.ingress.activateTLS | bool | `false` |  |
| defectdojo.django.ingress.enabled | bool | `true` |  |
| defectdojo.django.mediaPersistentVolume.persistentVolumeClaim.size | string | `"2Gi"` |  |
| defectdojo.django.uwsgi.livenessProbe.initialDelaySeconds | int | `20` |  |
| defectdojo.extraConfigs.DD_CSRF_COOKIE_SECURE | string | `"True"` |  |
| defectdojo.extraConfigs.DD_SECURE_SSL_REDIRECT | string | `"False"` |  |
| defectdojo.extraConfigs.DD_SESSION_COOKIE_SECURE | string | `"True"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_ACCESS_TOKEN_URL | string | `"https://keycloak.example.com/auth/realms/shared/protocol/openid-connect/token"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_AUTHORIZATION_URL | string | `"https://keycloak.example.com/auth/realms/shared/protocol/openid-connect/auth"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_KEY | string | `"defectdojo"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_OAUTH2_ENABLED | string | `"True"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_PUBLIC_KEY | string | `"<RS256_KEY>"` |  |
| defectdojo.extraConfigs.DD_SOCIAL_AUTH_KEYCLOAK_SECRET | string | `"defectdojo-extrasecrets"` |  |
| defectdojo.fullnameOverride | string | `"defectdojo"` |  |
| defectdojo.host | string | `"defectdojo.example.com"` |  |
| defectdojo.initializer.run | bool | `true` |  |
| defectdojo.postgresql.auth.existingSecret | string | `"defectdojo-pguser-defectdojo"` |  |
| defectdojo.postgresql.auth.secretKeys.adminPasswordKey | string | `"password"` |  |
| defectdojo.postgresql.auth.secretKeys.userPasswordKey | string | `"password"` |  |
| defectdojo.postgresql.enabled | bool | `false` |  |
| defectdojo.postgresql.postgresServer | string | `"defectdojo-primary.defectdojo.svc"` |  |
| defectdojo.rabbitmq.persistence.size | string | `"1Gi"` |  |
| defectdojo.site_url | string | `"https://defectdojo.example.com"` |  |
| defectdojo.tag | string | `"2.34.1"` |  |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.secretName | string | `"/edp/eks/addons/defectdojo"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| oidc.enabled | bool | `false` |  |

