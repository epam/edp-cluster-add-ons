# kuberocketci-rbac

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

A Helm chart for kuberocketci-rbac

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

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| broker.create | bool | `true` |  |
| broker.name | string | `"broker"` |  |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/edp/eks/addons/kuberocketci-rbac"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| keycloakUrl | string | `"https://example.com"` |  |
| kubernetes | object | `{"enabled":false}` | This block enable the creation of Keycloak operator resources for the EKS OIDC configuration, such as client, client scope, and realm groups. |
| sharedService | string | `"shared"` |  |
