# nexus

![Version: 61.0.3](https://img.shields.io/badge/Version-61.0.3-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.70.3](https://img.shields.io/badge/AppVersion-3.70.3-informational?style=flat-square)

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic keycloak-client-nexus-secret \
  --from-literal=clientSecret=<clientSecret>
```

```bash
kubectl create secret generic oauth2-proxy \
  --from-literal=client-id=<clientSecret> \
  --from-literal=client-secret=<clientSecret> \
  --from-literal=cookie-secret=<clientSecret>
```

</details>

<details>
<summary><b>External Secret Operator</b></summary>

Update [values.yaml](values.yaml) to enable ESO:

```yaml
eso:
  # -- Install components of the ESO.
  enabled: true
```

AWS Parameter Store structure:

```json
{
  "keycloak-client-nexus-secret": {
    "clientSecret": "<clientSecret>"
  },
  "oauth2-proxy": {
    "client-id": "<clientSecret>",
    "client-secret": "<client>",
    "cookie-secret": "<cookie-secret>"
  }
}
```

</details>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://oauth2-proxy.github.io/manifests/ | oauth2-proxy | 6.16.1 |
| https://sonatype.github.io/helm3-charts/ | nexus-repository-manager | 61.0.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/nexus"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"nexus","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"nexus"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| nexus-repository-manager.deployment.initContainers[0].command[0] | string | `"mkdir"` |  |
| nexus-repository-manager.deployment.initContainers[0].command[1] | string | `"-p"` |  |
| nexus-repository-manager.deployment.initContainers[0].command[2] | string | `"/nexus-data/etc"` |  |
| nexus-repository-manager.deployment.initContainers[0].image | string | `"busybox"` |  |
| nexus-repository-manager.deployment.initContainers[0].imagePullPolicy | string | `"IfNotPresent"` |  |
| nexus-repository-manager.deployment.initContainers[0].name | string | `"fmp-volume-permission"` |  |
| nexus-repository-manager.deployment.initContainers[0].volumeMounts[0].mountPath | string | `"/nexus-data"` |  |
| nexus-repository-manager.deployment.initContainers[0].volumeMounts[0].name | string | `"nexus-data"` |  |
| nexus-repository-manager.fullnameOverride | string | `"nexus"` |  |
| nexus-repository-manager.image.tag | string | `"3.70.3"` |  |
| nexus-repository-manager.ingress.annotations."nginx.ingress.kubernetes.io/proxy-body-size" | string | `"900m"` |  |
| nexus-repository-manager.ingress.enabled | bool | `true` |  |
| nexus-repository-manager.ingress.hostRepo | string | `"nexus-ci.example.com"` |  |
| nexus-repository-manager.nameOverride | string | `"nexus"` |  |
| nexus-repository-manager.nexus.docker.enabled | bool | `true` |  |
| nexus-repository-manager.nexus.docker.registries[0].host | string | `"nexus-ci-container.example.com"` |  |
| nexus-repository-manager.nexus.docker.registries[0].port | int | `5000` |  |
| nexus-repository-manager.nexus.env[0].name | string | `"NEXUS_SECURITY_RANDOMPASSWORD"` |  |
| nexus-repository-manager.nexus.env[0].value | string | `"false"` |  |
| nexus-repository-manager.nexus.properties.data."jetty.request.header.size" | int | `100000` |  |
| nexus-repository-manager.nexus.properties.data."nexus.scripts.allowCreation" | bool | `true` |  |
| nexus-repository-manager.nexus.properties.override | bool | `true` |  |
| nexus-repository-manager.nexus.resources.limits.memory | string | `"6Gi"` |  |
| nexus-repository-manager.nexus.resources.requests.cpu | string | `"100m"` |  |
| nexus-repository-manager.nexus.resources.requests.memory | string | `"2Gi"` |  |
| nexus-repository-manager.persistence.enabled | bool | `true` |  |
| nexus-repository-manager.persistence.storageSize | string | `"30Gi"` |  |
| nexus-repository-manager.serviceAccount.name | string | `"nexus-repo"` |  |
| oauth2-proxy.config.configFile | string | `"allowed_roles = [\"administrator\", \"developer\"]\nclient_id = \"nexus\"\ncode_challenge_method=\"S256\"\ncookie_csrf_expire=\"5m\"\ncookie_csrf_per_request=\"true\"\ncookie_secure = \"false\"\nemail_domains = [ \"*\" ]\ninsecure_oidc_allow_unverified_email = \"true\"\noidc_issuer_url = \"https://keycloak.example.com/auth/realms/<cluster_name>\"\npass_access_token = \"true\"\npass_authorization_header = \"true\"\npass_basic_auth = \"false\"\nprovider = \"keycloak-oidc\"\nredirect_url = \"https://nexus.example.com/oauth2/callback\"\nskip_jwt_bearer_tokens = \"true\"\nupstreams = [ \"http://nexus:8081\" ]\nwhitelist_domains = [\"*\"]\nsilence_ping_logging = \"true\""` |  |
| oauth2-proxy.config.existingSecret | string | `"oauth2-proxy"` |  |
| oauth2-proxy.enabled | bool | `false` |  |
| oauth2-proxy.ingress.enabled | bool | `true` |  |
| oauth2-proxy.ingress.hosts[0] | string | `"nexus.example.com"` |  |
