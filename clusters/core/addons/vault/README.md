# vault

![Version: 0.24.1](https://img.shields.io/badge/Version-0.24.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.13.1](https://img.shields.io/badge/AppVersion-1.13.1-informational?style=flat-square)

A Helm chart for Vault

## Vault configuration

Ensure you have `jq` installed:

* Initialize Vault and unseal it:

```bash
kubectl exec vault-0 -- vault operator init -key-shares=1 -key-threshold=1 -format=json > cluster-keys.json
VAULT_UNSEAL_KEY=$(cat cluster-keys.json | jq -r ".unseal_keys_b64[]")
kubectl exec vault-0 -- vault operator unseal $VAULT_UNSEAL_KEY
```

* Add nodes to cluster:

```bash
# join
kubectl exec vault-1 -- vault operator raft join http://vault-0.vault-internal:8200
kubectl exec vault-2 -- vault operator raft join http://vault-0.vault-internal:8200
# unseal
kubectl exec vault-1 -- vault operator unseal $VAULT_UNSEAL_KEY
kubectl exec vault-2 -- vault operator unseal $VAULT_UNSEAL_KEY
```

* Check cluster status:

```bash
CLUSTER_ROOT_TOKEN=$(cat cluster-keys.json | jq -r ".root_token")
kubectl exec vault-0 -- vault login $CLUSTER_ROOT_TOKEN
kubectl exec vault-0 -- vault operator raft list-peers
```

Read more [here](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-google-cloud-gke)

## Enable OIDC

Enable OIDC

```bash
vault auth enable oidc
```

Configure OIDC

```bash
vault write auth/oidc/config \
oidc_discovery_url="https://vault.example.com/auth/realms/shared" \
oidc_client_id="vault" \
oidc_client_secret="<OIDC-Client-Secret>" \
default_role="reader"
```

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
| https://helm.releases.hashicorp.com | vault | 0.24.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| vault.fullnameOverride | string | `"vault"` |  |
| vault.server.dataStorage.enabled | bool | `true` |  |
| vault.server.dataStorage.size | string | `"1Gi"` |  |
| vault.server.dataStorage.storageClass | string | `"gp3"` |  |
| vault.server.ha.enabled | bool | `true` |  |
| vault.server.ha.raft.enabled | bool | `true` |  |
| vault.server.ha.replicas | int | `3` |  |
| vault.server.ingress.enabled | bool | `true` |  |
| vault.server.ingress.hosts[0].host | string | `"vault.example.com"` |  |
| vault.server.ingress.hosts[0].paths[0] | string | `"/"` |  |
| vault.server.standalone.enabled | bool | `false` |  |
| vault.ui.enabled | bool | `true` |  |
