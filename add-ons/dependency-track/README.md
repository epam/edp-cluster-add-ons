# dependency-track

![Version: 1.5.5](https://img.shields.io/badge/Version-1.5.5-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v1.12.1](https://img.shields.io/badge/AppVersion-v1.12.1-informational?style=flat-square)

A Helm chart for Dependecy Track

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://evryfs.github.io/helm-charts/ | dependency-track | 1.5.5 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dependency-track.apiserver.env.env[0].name | string | `"ALPINE_OIDC_ENABLED"` |  |
| dependency-track.apiserver.env.env[0].value | string | `"true"` |  |
| dependency-track.apiserver.env.env[1].name | string | `"ALPINE_OIDC_CLIENT_ID"` |  |
| dependency-track.apiserver.env.env[1].value | string | `"deptrack"` |  |
| dependency-track.apiserver.env.env[2].name | string | `"ALPINE_OIDC_ISSUER"` |  |
| dependency-track.apiserver.env.env[2].value | string | `"https://keycloak.example.com/auth/realms/shared"` |  |
| dependency-track.apiserver.env.env[3].name | string | `"ALPINE_OIDC_USERNAME_CLAIM"` |  |
| dependency-track.apiserver.env.env[3].value | string | `"preferred_username"` |  |
| dependency-track.apiserver.env.env[4].name | string | `"ALPINE_OIDC_USER_PROVISIONING"` |  |
| dependency-track.apiserver.env.env[4].value | string | `"true"` |  |
| dependency-track.apiserver.env.env[5].name | string | `"ALPINE_OIDC_TEAMS_CLAIM"` |  |
| dependency-track.apiserver.env.env[5].value | string | `"roles"` |  |
| dependency-track.apiserver.env.env[6].name | string | `"ALPINE_OIDC_TEAM_SYNCHRONIZATION"` |  |
| dependency-track.apiserver.env.env[6].value | string | `"true"` |  |
| dependency-track.apiserver.image.tag | string | `"4.8.2"` |  |
| dependency-track.apiserver.persistentVolume.size | string | `"15Gi"` |  |
| dependency-track.apiserver.resources.limits.cpu | int | `2` |  |
| dependency-track.apiserver.resources.limits.memory | string | `"12Gi"` |  |
| dependency-track.apiserver.resources.requests.cpu | int | `1` |  |
| dependency-track.apiserver.resources.requests.memory | string | `"4608Mi"` |  |
| dependency-track.frontend.env[0].name | string | `"API_BASE_URL"` |  |
| dependency-track.frontend.env[0].value | string | `"https://deptrack.example.com"` |  |
| dependency-track.frontend.env[1].name | string | `"OIDC_ISSUER"` |  |
| dependency-track.frontend.env[1].value | string | `"https://keycloak.example.com/auth/realms/shared"` |  |
| dependency-track.frontend.env[2].name | string | `"OIDC_CLIENT_ID"` |  |
| dependency-track.frontend.env[2].value | string | `"deptrack"` |  |
| dependency-track.frontend.env[3].name | string | `"OIDC_SCOPE"` |  |
| dependency-track.frontend.env[3].value | string | `"openid profile email"` |  |
| dependency-track.frontend.env[4].name | string | `"OIDC_LOGIN_BUTTON_TEXT"` |  |
| dependency-track.frontend.env[4].value | string | `"Login with Keycloak"` |  |
| dependency-track.frontend.env[5].name | string | `"OIDC_FLOW"` |  |
| dependency-track.frontend.env[5].value | string | `"code"` |  |
| dependency-track.frontend.image.tag | string | `"4.8.1"` |  |
| dependency-track.frontend.replicaCount | int | `1` |  |
| dependency-track.fullnameOverride | string | `"deptrack"` |  |
| dependency-track.ingress.annotations."kubernetes.io/ingress.class" | string | `"nginx"` |  |
| dependency-track.ingress.annotations."nginx.ingress.kubernetes.io/proxy-body-size" | string | `"10m"` |  |
| dependency-track.ingress.enabled | bool | `true` |  |
| dependency-track.ingress.host | string | `"deptrack.example.com"` |  |
| dependency-track.ingress.tls.enabled | bool | `false` |  |
| dependency-track.ingress.tls.secretName | string | `""` |  |
| dependency-track.nameOverride | string | `"deptrack"` |  |
| oidc.enabled | bool | `false` |  |

