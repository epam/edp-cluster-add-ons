# nexus-ce

![Version: 0.1.1](https://img.shields.io/badge/Version-0.1.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.82.0](https://img.shields.io/badge/AppVersion-3.82.0-informational?style=flat-square)

Nexus Community Edition chart for Kubernetes

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://oauth2-proxy.github.io/manifests/ | oauth2-proxy | 6.16.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` |  |
| autoscaling.enabled | bool | `false` |  |
| autoscaling.maxReplicas | int | `100` |  |
| autoscaling.minReplicas | int | `1` |  |
| autoscaling.targetCPUUtilizationPercentage | int | `80` |  |
| database | object | `{"existigSecret":"nexus-ce-pguser-nexus-ce","keys":{"dbname":"dbname","password":"password","port":"5432","url":"host","username":"user"},"pgo":{"enable":true}}` | This block configure database connections for Nexus CE. |
| database.existigSecret | string | `"nexus-ce-pguser-nexus-ce"` | Name of the secret that contains the database credentials. |
| database.keys | object | `{"dbname":"dbname","password":"password","port":"5432","url":"host","username":"user"}` | This block configures the database connection secret fields name for Nexus CE. |
| database.pgo | object | `{"enable":true}` | Use PostgreSQL operator to create and manage database. |
| docker.enabled | bool | `true` |  |
| docker.registries[0].host | string | `"nexus-ce-ci-container.example.com"` |  |
| docker.registries[0].port | int | `5000` |  |
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/nexus-ce"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"nexus-ce","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"nexus-ce"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| fullnameOverride | string | `"nexus-ce"` |  |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"sonatype/nexus3"` |  |
| image.tag | string | `"3.82.0"` |  |
| imagePullSecrets | list | `[]` |  |
| ingress.annotations."nginx.ingress.kubernetes.io/proxy-body-size" | string | `"900m"` |  |
| ingress.className | string | `""` |  |
| ingress.enabled | bool | `true` |  |
| ingress.hosts[0].host | string | `"nexus-ce-ci.example.com"` |  |
| ingress.hosts[0].paths[0].path | string | `"/"` |  |
| ingress.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| ingress.tls | list | `[]` |  |
| livenessProbe.failureThreshold | int | `6` |  |
| livenessProbe.initialDelaySeconds | int | `0` |  |
| livenessProbe.path | string | `"/"` |  |
| livenessProbe.periodSeconds | int | `60` |  |
| livenessProbe.timeoutSeconds | int | `1` |  |
| nameOverride | string | `""` |  |
| nexusAdminPassword | object | `{"secret":{"key":"password","name":"nexus-admin-password"}}` | Initial Nexus CE admin password. |
| nodeSelector | object | `{}` |  |
| oauth2-proxy.config.configFile | string | `"allowed_roles = [\"administrator\", \"developer\"]\nclient_id = \"nexus-ce\"\ncode_challenge_method=\"S256\"\ncookie_csrf_expire=\"5m\"\ncookie_csrf_per_request=\"true\"\ncookie_secure = \"false\"\nemail_domains = [ \"*\" ]\ninsecure_oidc_allow_unverified_email = \"true\"\noidc_issuer_url = \"https://idp.core.kuberocketci.io/realms/shared\"\npass_access_token = \"true\"\npass_authorization_header = \"true\"\npass_basic_auth = \"false\"\nprovider = \"keycloak-oidc\"\nredirect_url = \"https://nexus-ce.example.com/oauth2/callback\"\nskip_jwt_bearer_tokens = \"true\"\nupstreams = [ \"http://nexus-ce:8081\" ]\nwhitelist_domains = [\"*\"]\nsilence_ping_logging = \"true\""` |  |
| oauth2-proxy.config.existingSecret | string | `"oauth2-proxy"` |  |
| oauth2-proxy.enabled | bool | `true` |  |
| oauth2-proxy.ingress.enabled | bool | `true` |  |
| oauth2-proxy.ingress.hosts[0] | string | `"nexus-ce.example.com"` |  |
| oauth2-proxy.redis.enabled | bool | `false` |  |
| oauth2-proxy.redis.replica.replicaCount | int | `1` |  |
| oauth2-proxy.sessionStorage.redis.clientType | string | `"standalone"` |  |
| oauth2-proxy.sessionStorage.redis.cluster.connectionUrls | list | `[]` |  |
| oauth2-proxy.sessionStorage.redis.existingSecret | string | `""` |  |
| oauth2-proxy.sessionStorage.redis.password | string | `""` |  |
| oauth2-proxy.sessionStorage.redis.passwordKey | string | `"redis-password"` |  |
| oauth2-proxy.sessionStorage.redis.sentinel.connectionUrls | list | `[]` |  |
| oauth2-proxy.sessionStorage.redis.sentinel.existingSecret | string | `""` |  |
| oauth2-proxy.sessionStorage.redis.sentinel.masterName | string | `""` |  |
| oauth2-proxy.sessionStorage.redis.sentinel.password | string | `""` |  |
| oauth2-proxy.sessionStorage.redis.sentinel.passwordKey | string | `"redis-sentinel-password"` |  |
| oauth2-proxy.sessionStorage.redis.standalone.connectionUrl | string | `""` |  |
| oauth2-proxy.sessionStorage.type | string | `"cookie"` |  |
| persistentVolume.accessMode | string | `"ReadWriteOnce"` | Access mode for the Persistent Volume. |
| persistentVolume.enabled | bool | `true` |  |
| persistentVolume.existingClaim | string | `""` | Existing Persistent Volume Claim. |
| persistentVolume.storageClass | string | `"ebs-sc"` | Storage class for the Persistent Volume. |
| persistentVolume.storageSize | string | `"20Gi"` | Storage size for the Persistent Volume. |
| podAnnotations | object | `{}` |  |
| podSecurityContext | object | `{}` |  |
| readinessProbe.failureThreshold | int | `6` |  |
| readinessProbe.initialDelaySeconds | int | `0` |  |
| readinessProbe.path | string | `"/"` |  |
| readinessProbe.periodSeconds | int | `60` |  |
| readinessProbe.timeoutSeconds | int | `1` |  |
| replicaCount | int | `1` |  |
| resources | object | `{}` |  |
| securityContext | object | `{}` |  |
| service.port | int | `8081` |  |
| service.type | string | `"ClusterIP"` |  |
| serviceAccount.annotations | object | `{}` |  |
| serviceAccount.create | bool | `true` |  |
| serviceAccount.name | string | `""` |  |
| tolerations | list | `[]` |  |

