# oauth2-proxy

![Version: 8.2.0](https://img.shields.io/badge/Version-8.2.0-informational?style=flat-square) ![AppVersion: v7.12.0](https://img.shields.io/badge/AppVersion-v7.12.0-informational?style=flat-square)

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic oauth2-proxy \
  --from-literal=client-id=<client-id> \
  --from-literal=client-secret=<client-secret> \
  --from-literal=cookie-secret=<cookie-secret>
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
  "oauth2-proxy": {
    "client-id": "<client-id>",
    "client-secret": "<client-secret>",
    "cookie-secret": "<cookie-secret>"
  }
}
```

</details>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://oauth2-proxy.github.io/manifests | oauth2-proxy | 8.2.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/oauth2-proxy"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"oauth2-proxy","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"oauth2-proxy"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| oauth2-proxy.config.configFile | string | `"allowed_roles = [\"administrator\", \"developer\"]\ncode_challenge_method=\"S256\"\ncookie_domains = [\"example.com\"]\ncookie_secure = \"false\"\nemail_domains = [ \"*\" ]\ninsecure_oidc_allow_unverified_email = \"true\"\noidc_issuer_url = \"https://keycloak.example.com/auth/realms/<cluster_name>\"\npass_authorization_header = \"true\"\npass_basic_auth = \"false\"\npass_user_headers = \"true\"\nprovider = \"keycloak-oidc\"\nredirect_url = \"https://oauth-oauth2-proxy.example.com/oauth2/callback\"\nreverse_proxy = \"true\"\nskip_jwt_bearer_tokens = \"true\"\nskip_provider_button = \"true\"\nwhitelist_domains = \".example.com\""` |  |
| oauth2-proxy.config.existingSecret | string | `"oauth2-proxy"` |  |
| oauth2-proxy.ingress.enabled | bool | `true` |  |
| oauth2-proxy.ingress.hosts[0] | string | `"oauth-oauth2-proxy.example.com"` |  |
