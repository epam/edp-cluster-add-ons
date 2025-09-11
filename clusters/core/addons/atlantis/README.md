# atlantis

![Version: 5.18.2](https://img.shields.io/badge/Version-5.18.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v0.35.1](https://img.shields.io/badge/AppVersion-v0.35.1-informational?style=flat-square)

**Homepage:** <https://www.runatlantis.io>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| lkysow |  |  |
| jamengual |  |  |
| chenrui333 |  |  |
| nitrocode |  |  |
| genpage |  |  |
| gmartinez-sisti |  |  |

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic atlantis-webhook \
  --from-literal=bitbucket_token=<bitbucket_secret> \
  --from-literal=bitbucket_secret=<bitbucket_secret>
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
  "bitbucket_token": "<bitbucket_secret>",
  "bitbucket_secret": "<bitbucket_secret>"
}
```

</details>

## Source Code

* <https://github.com/runatlantis/atlantis>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://oauth2-proxy.github.io/manifests | oauth2-proxy | 8.2.0 |
| https://runatlantis.github.io/helm-charts | atlantis | 5.18.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| atlantis.atlantisUrl | string | `"atlantis.example.com"` |  |
| atlantis.bitbucket | object | `{"user":"auto_example"}` | Uncomment to enable Basic Auth mode ref: https://www.runatlantis.io/docs/security. basicAuthSecretName: atlantis-creds |
| atlantis.defaultTFVersion | string | `"1.5.7"` |  |
| atlantis.ingress.enabled | bool | `true` |  |
| atlantis.ingress.host | string | `"atlantis.example.com"` |  |
| atlantis.ingress.path | string | `"/"` |  |
| atlantis.orgAllowlist | string | `"bitbucket.org/organization/*"` |  |
| atlantis.repoConfig | string | `"---\nrepos:\n- id: /.*/\n  allowed_overrides: [\"workflow\"]\n  allow_custom_workflows: true\n"` |  |
| atlantis.serviceAccount.annotations | object | `{}` |  |
| atlantis.vcsSecretName | string | `"atlantis-webhook"` |  |
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/atlantis"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"atlantis","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"atlantis"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| oauth2-proxy.config.configFile | string | `"allowed_roles = [\"administrator\", \"developer\"]\nclient_id = \"atlantis\"\ncode_challenge_method=\"S256\"\ncookie_csrf_expire=\"5m\"\ncookie_csrf_per_request=\"true\"\ncookie_domains = [\"atlantis.example.com\"]\ncookie_secure = \"true\"\nemail_domains = [ \"*\" ]\ninsecure_oidc_allow_unverified_email = \"true\"\noidc_issuer_url = \"https://keycloak.example.com/realms/<realm_name>\"\npass_access_token = \"true\"\npass_authorization_header = \"true\"\npass_basic_auth = \"false\"\nprovider = \"keycloak-oidc\"\nredirect_url = \"https://atlantis.example.com/oauth2/callback\"\nskip_jwt_bearer_tokens = \"true\"\nupstreams = [ \"http://atlantis:80\" ]\nwhitelist_domains = [\".example.com\"]\nsilence_ping_logging = \"true\""` |  |
| oauth2-proxy.config.existingSecret | string | `"oauth2-proxy"` |  |
| oauth2-proxy.enabled | bool | `false` |  |
| oauth2-proxy.extraArgs.skip-auth-regex | string | `"^/events$"` |  |
| oauth2-proxy.ingress.enabled | bool | `true` |  |
| oauth2-proxy.ingress.hosts[0] | string | `"atlantis.example.com"` |  |
| oidc.enabled | bool | `false` |  |
