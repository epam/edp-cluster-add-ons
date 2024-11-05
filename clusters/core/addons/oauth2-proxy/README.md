# oauth2-proxy

![Version: 7.6.0](https://img.shields.io/badge/Version-7.6.0-informational?style=flat-square) ![AppVersion: v7.6.0](https://img.shields.io/badge/AppVersion-v7.6.0-informational?style=flat-square)

A Helm chart for Oauth2 Stack

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://oauth2-proxy.github.io/manifests | oauth2-proxy | 7.1.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/infra/core/addons/oauth2-proxy"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore-proxy"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| oauth2-proxy.config.configFile | string | `"allowed_roles = [\"administrator\", \"developer\"]\ncode_challenge_method=\"S256\"\ncookie_domains = [\"example.com\"]\ncookie_secure = \"false\"\nemail_domains = [ \"*\" ]\ninsecure_oidc_allow_unverified_email = \"true\"\noidc_issuer_url = \"https://keycloak.example.com/auth/realms/<cluster_name>\"\npass_authorization_header = \"true\"\npass_basic_auth = \"false\"\npass_user_headers = \"true\"\nprovider = \"keycloak-oidc\"\nredirect_url = \"https://oauth-oauth2-proxy.example.com/oauth2/callback\"\nreverse_proxy = \"true\"\nskip_jwt_bearer_tokens = \"true\"\nskip_provider_button = \"true\"\nwhitelist_domains = \".example.com\""` |  |
| oauth2-proxy.config.existingSecret | string | `"oauth2-proxy"` |  |
| oauth2-proxy.ingress.enabled | bool | `true` |  |
| oauth2-proxy.ingress.hosts[0] | string | `"oauth-oauth2-proxy.example.com"` |  |

