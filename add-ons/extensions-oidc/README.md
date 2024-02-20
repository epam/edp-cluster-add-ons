# extensions-oidc

![Version: 1.20.0](https://img.shields.io/badge/Version-1.20.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.20.0](https://img.shields.io/badge/AppVersion-1.20.0-informational?style=flat-square)

A Helm chart for extensions-oidc

```
+-------------------------+   +-----------------+
|     sharedService       |   |      broker     |
|         Realm           |   |      Realm      |
|  +------------------+   |   | +-------------+ |
|  |    idpBroker     |   |   | |sharedService| |
|  | identityProvider +---+---+->    Client   | |
|  +------------------+   |   | +-------------+ |
| +----------+ +--------+ |   +-----------------+
| | sonarqube| | nexus  | |
| |  Client  | | Client | |
| +----------+ +--------+ |
+-------------------------+
```

broker - contains a list of users and basic settings, you can install or use a pre-created Realm, for that set the 'create' parameter to 'false' and ununcomment 'existingBroker' provide the name of the existing realm.

sharedService - contains clients, application integrations, and identity providers for connect to `broker` realm.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | keycloak-operator | 1.20.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.secretName | string | `"/edp/eks/addons/extensionsOIDC"` | Value name in AWS ParameterStore, AWS SecretsManager or GCP Secret Manager. |
| eso.secretStoreName | string | `"aws-parameterstore-oidc"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `gcpsm`. |
| extensionsOIDC.broker.create | bool | `true` |  |
| extensionsOIDC.broker.name | string | `"broker"` |  |
| extensionsOIDC.keycloakUrl | string | `"https://keycloak.example.com"` |  |
| extensionsOIDC.sharedService | string | `"shared"` |  |
| keycloak-operator.clusterReconciliationEnabled | bool | `true` |  |
