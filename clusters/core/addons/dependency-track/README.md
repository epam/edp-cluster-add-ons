# dependency-track

![Version: 0.35.0](https://img.shields.io/badge/Version-0.35.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v4.13.3](https://img.shields.io/badge/AppVersion-v4.13.3-informational?style=flat-square)

A Helm chart for Dependecy Track

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://dependencytrack.github.io/helm-charts | dependency-track | 0.35.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dependency-track.apiServer.extraEnv[0].name | string | `"ALPINE_DATABASE_MODE"` |  |
| dependency-track.apiServer.extraEnv[0].value | string | `"external"` |  |
| dependency-track.apiServer.extraEnv[10].name | string | `"ALPINE_OIDC_TEAMS_CLAIM"` |  |
| dependency-track.apiServer.extraEnv[10].value | string | `"roles"` |  |
| dependency-track.apiServer.extraEnv[11].name | string | `"ALPINE_OIDC_TEAM_SYNCHRONIZATION"` |  |
| dependency-track.apiServer.extraEnv[11].value | string | `"true"` |  |
| dependency-track.apiServer.extraEnv[1].name | string | `"ALPINE_DATABASE_URL"` |  |
| dependency-track.apiServer.extraEnv[1].value | string | `"jdbc:postgresql://deptrack-primary.dependency-track.svc:5432/deptrack"` |  |
| dependency-track.apiServer.extraEnv[2].name | string | `"ALPINE_DATABASE_DRIVER"` |  |
| dependency-track.apiServer.extraEnv[2].value | string | `"org.postgresql.Driver"` |  |
| dependency-track.apiServer.extraEnv[3].name | string | `"ALPINE_DATABASE_USERNAME"` |  |
| dependency-track.apiServer.extraEnv[3].value | string | `"deptrack"` |  |
| dependency-track.apiServer.extraEnv[4].name | string | `"ALPINE_DATABASE_PASSWORD"` |  |
| dependency-track.apiServer.extraEnv[4].valueFrom.secretKeyRef.key | string | `"password"` |  |
| dependency-track.apiServer.extraEnv[4].valueFrom.secretKeyRef.name | string | `"deptrack-pguser-deptrack"` |  |
| dependency-track.apiServer.extraEnv[5].name | string | `"ALPINE_OIDC_ENABLED"` |  |
| dependency-track.apiServer.extraEnv[5].value | string | `"true"` |  |
| dependency-track.apiServer.extraEnv[6].name | string | `"ALPINE_OIDC_CLIENT_ID"` |  |
| dependency-track.apiServer.extraEnv[6].value | string | `"deptrack"` |  |
| dependency-track.apiServer.extraEnv[7].name | string | `"ALPINE_OIDC_ISSUER"` |  |
| dependency-track.apiServer.extraEnv[7].value | string | `"https://keycloak.example.com/auth/realms/shared"` |  |
| dependency-track.apiServer.extraEnv[8].name | string | `"ALPINE_OIDC_USERNAME_CLAIM"` |  |
| dependency-track.apiServer.extraEnv[8].value | string | `"preferred_username"` |  |
| dependency-track.apiServer.extraEnv[9].name | string | `"ALPINE_OIDC_USER_PROVISIONING"` |  |
| dependency-track.apiServer.extraEnv[9].value | string | `"true"` |  |
| dependency-track.apiServer.persistentVolume.enabled | bool | `false` |  |
| dependency-track.apiServer.resources.limits.cpu | string | `"2"` |  |
| dependency-track.apiServer.resources.limits.memory | string | `"4608Mi"` |  |
| dependency-track.apiServer.resources.requests.cpu | string | `"1"` |  |
| dependency-track.apiServer.resources.requests.memory | string | `"768Mi"` |  |
| dependency-track.frontend.apiBaseUrl | string | `"https://deptrack.example.com"` |  |
| dependency-track.frontend.extraEnv[0].name | string | `"OIDC_ISSUER"` |  |
| dependency-track.frontend.extraEnv[0].value | string | `"https://keycloak.example.com/auth/realms/shared"` |  |
| dependency-track.frontend.extraEnv[1].name | string | `"OIDC_CLIENT_ID"` |  |
| dependency-track.frontend.extraEnv[1].value | string | `"deptrack"` |  |
| dependency-track.frontend.extraEnv[2].name | string | `"OIDC_SCOPE"` |  |
| dependency-track.frontend.extraEnv[2].value | string | `"openid profile email"` |  |
| dependency-track.frontend.extraEnv[3].name | string | `"OIDC_LOGIN_BUTTON_TEXT"` |  |
| dependency-track.frontend.extraEnv[3].value | string | `"Login with Keycloak"` |  |
| dependency-track.frontend.extraEnv[4].name | string | `"OIDC_FLOW"` |  |
| dependency-track.frontend.extraEnv[4].value | string | `"code"` |  |
| dependency-track.frontend.replicaCount | int | `1` |  |
| dependency-track.frontend.resources.limits.cpu | string | `"500m"` |  |
| dependency-track.frontend.resources.limits.memory | string | `"128Mi"` |  |
| dependency-track.frontend.resources.requests.cpu | string | `"150m"` |  |
| dependency-track.frontend.resources.requests.memory | string | `"64Mi"` |  |
| dependency-track.fullnameOverride | string | `"deptrack"` |  |
| dependency-track.ingress.annotations."kubernetes.io/ingress.class" | string | `"nginx"` |  |
| dependency-track.ingress.annotations."nginx.ingress.kubernetes.io/proxy-body-size" | string | `"10m"` |  |
| dependency-track.ingress.enabled | bool | `true` |  |
| dependency-track.ingress.hostname | string | `"deptrack.example.com"` |  |
| dependency-track.ingress.tls | list | `[]` |  |
| dependency-track.nameOverride | string | `"deptrack"` |  |
| oidc.enabled | bool | `false` |  |

