# dependency-track

![Version: 2.9.0](https://img.shields.io/badge/Version-2.9.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 5.2.1](https://img.shields.io/badge/AppVersion-5.2.1-informational?style=flat-square)

## Upgrading from Dependency-Track 4

Dependency-Track 5 has no in-place upgrade from version 4, and chart 2.x is not compatible with chart 0.x/1.x. Use this add-on for a new installation. To move an existing 4.x instance, delete the old application together with its PostgreSQL cluster (`deptrack`) and its volumes, then deploy this version. All previous data is lost: projects, components, teams, API keys, OIDC group mappings and analyzer credentials. Back up the database first if you need the old data.

After the first start:

1. Create an OIDC group (for example `administrator`) in **Administration > Access Management > OpenID Connect Groups** and map it to the team `Administrators`, otherwise users logging in with Keycloak have no permissions.
2. Create an API key for CI and give its team the permissions `BOM_UPLOAD`, `PROJECT_CREATION_UPLOAD`, `VIEW_PORTFOLIO`, `VIEW_VULNERABILITY`, `VIEW_POLICY_VIOLATION` and `VIEW_BADGES`.
3. Re-enter analyzer credentials (for example the Sonatype OSS Index token) in **Administration > Analyzers**.

## Secret management

Dependency-Track encrypts the secrets it stores (for example analyzer tokens) with a key encryption key (KEK). The chart does not generate it and the API server does not start without it. Create the secret before the first sync:

```bash
kubectl create namespace dependency-track
kubectl -n dependency-track create secret generic dependency-track-kek \
  --from-literal=kek="$(openssl rand -base64 32)"
```

> **Note:** Keep the KEK in a safe place. If it is lost or changed, the secrets stored in the database cannot be decrypted.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://dependencytrack.github.io/helm-charts | dependency-track | 2.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dependency-track.apiServer.extraEnv[0].name | string | `"DT_OIDC_ENABLED"` |  |
| dependency-track.apiServer.extraEnv[0].value | string | `"true"` |  |
| dependency-track.apiServer.extraEnv[1].name | string | `"DT_OIDC_CLIENT_ID"` |  |
| dependency-track.apiServer.extraEnv[1].value | string | `"deptrack"` |  |
| dependency-track.apiServer.extraEnv[2].name | string | `"DT_OIDC_ISSUER"` |  |
| dependency-track.apiServer.extraEnv[2].value | string | `"https://keycloak.example.com/auth/realms/shared"` |  |
| dependency-track.apiServer.extraEnv[3].name | string | `"DT_OIDC_USERNAME_CLAIM"` |  |
| dependency-track.apiServer.extraEnv[3].value | string | `"preferred_username"` |  |
| dependency-track.apiServer.extraEnv[4].name | string | `"DT_OIDC_USER_PROVISIONING"` |  |
| dependency-track.apiServer.extraEnv[4].value | string | `"true"` |  |
| dependency-track.apiServer.extraEnv[5].name | string | `"DT_OIDC_TEAMS_CLAIM"` |  |
| dependency-track.apiServer.extraEnv[5].value | string | `"roles"` |  |
| dependency-track.apiServer.extraEnv[6].name | string | `"DT_OIDC_TEAM_SYNCHRONIZATION"` |  |
| dependency-track.apiServer.extraEnv[6].value | string | `"true"` |  |
| dependency-track.apiServer.topology | string | `"monolith"` |  |
| dependency-track.apiServer.web.replicaCount | int | `1` |  |
| dependency-track.apiServer.web.resources.limits.cpu | string | `"2"` |  |
| dependency-track.apiServer.web.resources.limits.memory | string | `"4608Mi"` |  |
| dependency-track.apiServer.web.resources.requests.cpu | string | `"1"` |  |
| dependency-track.apiServer.web.resources.requests.memory | string | `"768Mi"` |  |
| dependency-track.database.existingSecret.name | string | `"deptrack-pguser-deptrack"` |  |
| dependency-track.database.existingSecret.passwordKey | string | `"password"` |  |
| dependency-track.database.existingSecret.usernameKey | string | `"user"` |  |
| dependency-track.database.jdbcUrl | string | `"jdbc:postgresql://deptrack-primary.dependency-track.svc:5432/deptrack?reWriteBatchedInserts=true"` |  |
| dependency-track.fileStorage.local.size | string | `"20Gi"` |  |
| dependency-track.fileStorage.provider | string | `"local"` |  |
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
| dependency-track.secretManagement.database.kek.existingSecret.key | string | `"kek"` |  |
| dependency-track.secretManagement.database.kek.existingSecret.name | string | `"dependency-track-kek"` |  |
| dependency-track.secretManagement.database.kek.mode | string | `"config"` |  |
| dependency-track.secretManagement.provider | string | `"database"` |  |
| oidc.enabled | bool | `false` |  |
