# vault

![Version: 0.25.0](https://img.shields.io/badge/Version-0.25.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.14.0](https://img.shields.io/badge/AppVersion-1.14.0-informational?style=flat-square)

A Helm chart for Vault

## Quick Start

1. Get Vault root token from the `vault-root-token` kubernetes secret:

    ```bash
    VAULT_ROOT_TOKEN=$(kubectl get secret vault-root-token -o jsonpath='{.data.VAULT_ROOT_TOKEN}' -n vault | base64 --decode)
    ```

2. Create secret record in Vault with root token got on the previous step:

    ```bash
    curl \
    -H "X-Vault-Token: $VAULT_ROOT_TOKEN" \
    -H "Content-Type: application/json" \
    -X POST \
    -d '{"data":{"abc":"123"}}' \
    $VAULT_ADDR/v1/edp-project/data/example
    ```

3. Get `roleId` from the `vault-approle-secret` kubernetes secret:

    ```bash
    VAULT_APPROLE_ROLE_ID=$(kubectl get secret vault-approle-secret -o jsonpath='{.data.role-id}' -n vault | base64 --decode)
    ```

4. Create Custom Resource `kind: SecretStore` with role-id got on the previous step:

    ```yaml
    apiVersion: external-secrets.io/v1beta1
    kind: SecretStore
    metadata:
      name: vault-backend
    spec:
      provider:
        vault:
          server: "http://vault.vault.svc.cluster.local:8200"
          version: "v2"
          auth:
            appRole:
              path: "approle"
              roleId: "$VAULT_APPROLE_ROLE_ID" # `roleId` value from `vault-approle-secret` secret
              secretRef:
                name: "vault-approle-secret"
                key: "secret-id"
    ```

5. Create Custom Resource `kind: ExternalSecret` with SecretStore name created on the previous step:

    ```yaml
    apiVersion: external-secrets.io/v1beta1
    kind: ExternalSecret
    metadata:
      name: vault-external-secret
    spec:
      refreshInterval: "15s"
      secretStoreRef:
        name: vault-backend # the name of `kind: SecretStore`
        kind: SecretStore
      data:
        - secretKey: example
          remoteRef:
            key: edp-project/data/example
            property: abc
    ```
6. To check if the integration is successful, run the command below, the output should be "123":

    ```bash
    kubectl get secret vault-external-secret -o jsonpath='{.data.example}' | base64 --decode
    ```

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://helm.releases.hashicorp.com | vault | 0.25.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/infra/core/addons/vault"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| job.clusterApiUrl | string | `"https://cluster-api.com"` |  |
| job.keycloakUrl | string | `"https://keycloak.example.com/auth/realms/shared"` |  |
| job.vaultUrl | string | `"vault.example.com"` |  |
| oidc.enabled | bool | `false` |  |
| vault.fullnameOverride | string | `"vault"` |  |
| vault.server.dataStorage.enabled | bool | `true` |  |
| vault.server.dataStorage.size | string | `"1Gi"` |  |
| vault.server.ha.enabled | bool | `true` |  |
| vault.server.ha.raft.config | string | `"ui = true\nlistener \"tcp\" {\n  address = \"[::]:8200\"\n  cluster_address = \"[::]:8201\"\n  tls_disable = 1\n}\n\nstorage \"raft\" {\n  path = \"/vault/data\"\n    retry_join {\n    leader_api_addr = \"http://vault-0.vault-internal:8200\"\n  }\n  retry_join {\n    leader_api_addr = \"http://vault-1.vault-internal:8200\"\n  }\n  retry_join {\n    leader_api_addr = \"http://vault-2.vault-internal:8200\"\n  }\n}\n\nservice_registration \"kubernetes\" {}\n\nseal \"awskms\" {\n  region     = \"eu-central-1\"\n  kms_key_id = \"KMS_KEY_ID\"\n  role_arn = \"arn:aws:iam::012345678910:role/AWSIRSA_Shared_Vault\"\n  web_identity_token_file = \"/var/run/secrets/eks.amazonaws.com/serviceaccount/token\"\n}\n"` |  |
| vault.server.ha.raft.enabled | bool | `true` |  |
| vault.server.ha.raft.setNodeId | bool | `true` |  |
| vault.server.ha.replicas | int | `3` |  |
| vault.server.ingress.enabled | bool | `true` |  |
| vault.server.ingress.hosts[0].host | string | `"vault.example.com"` |  |
| vault.server.ingress.hosts[0].paths[0] | string | `"/"` |  |
| vault.server.serviceAccount.annotations."eks.amazonaws.com/role-arn" | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_Vault"` |  |
| vault.server.standalone.enabled | bool | `false` |  |
| vault.ui.enabled | bool | `true` |  |
