# vault

![Version: 0.25.0](https://img.shields.io/badge/Version-0.25.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.20.1](https://img.shields.io/badge/AppVersion-1.20.1-informational?style=flat-square)

A Helm chart for Vault

## Vault configuration

Ensure you have `jq` installed:

Create Role:

Create `reader.hcl` file

```bash
path "/secret/*" {
    capabilities = ["read", "list"]
}
```

```bash
cat reader.hcl | vault policy write reader -
```

```bash
vault write auth/oidc/role/reader \
bound_audiences="vault" \
allowed_redirect_uris="https://vault.example.com/oidc/oidc/callback" \
allowed_redirect_uris="https://vault.example.com/ui/vault/auth/oidc/oidc/callback" \
user_claim="sub" \
policies=reader
```

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):

```bash
kubectl create secret generic keycloak-client-vault-secret \
  --from-literal=clientSecret=<clientSecret>
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
  "vaultOIDC": {
    "oidcClientSecret": "<oidcClientSecret>"
  }
}
```

</details>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://helm.releases.hashicorp.com | vault | 0.30.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/vault-okd"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"vault-okd","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"vault-okd"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| job.clusterApiUrl | string | `"https://api.example.com:6443"` |  |
| job.keycloakUrl | string | `"https://keycloak.example.com/auth/realms/shared"` |  |
| oidc.enabled | bool | `false` |  |
| vault.fullnameOverride | string | `"vault"` |  |
| vault.global.openshift | bool | `true` |  |
| vault.server.dataStorage.enabled | bool | `true` |  |
| vault.server.dataStorage.size | string | `"1Gi"` |  |
| vault.server.ha.enabled | bool | `true` |  |
| vault.server.ha.raft.config | string | `"ui = true\nlistener \"tcp\" {\n  address = \"[::]:8200\"\n  cluster_address = \"[::]:8201\"\n  tls_disable = 1\n}\n\nstorage \"raft\" {\n  path = \"/vault/data\"\n    retry_join {\n    leader_api_addr = \"http://vault-0.vault-internal:8200\"\n  }\n  retry_join {\n    leader_api_addr = \"http://vault-1.vault-internal:8200\"\n  }\n  retry_join {\n    leader_api_addr = \"http://vault-2.vault-internal:8200\"\n  }\n}\n\nservice_registration \"kubernetes\" {}\n"` |  |
| vault.server.ha.raft.enabled | bool | `true` |  |
| vault.server.ha.raft.setNodeId | bool | `true` |  |
| vault.server.ha.replicas | int | `3` |  |
| vault.server.route.activeService | bool | `true` |  |
| vault.server.route.enabled | bool | `true` |  |
| vault.server.route.host | string | `"vault.example.com"` |  |
| vault.server.route.tls.insecureEdgeTerminationPolicy | string | `"Redirect"` |  |
| vault.server.route.tls.termination | string | `"edge"` |  |
| vault.server.standalone.enabled | bool | `false` |  |
| vault.ui.enabled | bool | `true` |  |
