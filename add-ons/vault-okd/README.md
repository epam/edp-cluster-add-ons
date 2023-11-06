# vault

![Version: 0.25.0](https://img.shields.io/badge/Version-0.25.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.14.0](https://img.shields.io/badge/AppVersion-1.14.0-informational?style=flat-square)

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

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://helm.releases.hashicorp.com | vault | 0.25.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
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
