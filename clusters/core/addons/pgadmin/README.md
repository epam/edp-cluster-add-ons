# pgadmin

![Version: 1.49.0](https://img.shields.io/badge/Version-1.49.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 9.7](https://img.shields.io/badge/AppVersion-9.7-informational?style=flat-square)

pgAdmin4 is a web based administration tool for PostgreSQL database

Configuring the OAUTH2_AUTO_CREATE_USER Parameter
The OAUTH2_AUTO_CREATE_USER parameter in the cm-pgadmin4-config.yaml file controls how pgAdmin handles user logins via OAuth2.

When set to 'True', pgAdmin will automatically create a user upon their first successful OAuth2 login, if the user does not already exist in the system.

```yaml
OAUTH2_AUTO_CREATE_USER: 'True'
```
When set to 'False', only users who have been manually added to pgAdmin in advance will be able to log in. New users will not be created automatically, even if OAuth2 authentication is successful.

```yaml
OAUTH2_AUTO_CREATE_USER: 'False'
```
It is recommended to set OAUTH2_AUTO_CREATE_USER: 'False' if you want to restrict access to pgAdmin to a predefined set of users only.

Important Note About Renaming the Admin User
If you want to rename the default administrator user in pgAdmin, you must use the full email address of the user. The Helm chart documentation may be misleading, as it sometimes suggests using only the username without the domain.

```yaml
PGADMIN_DEFAULT_EMAIL: 'admin@example.com'
```

To enable OIDC authentication with Keycloak for pgAdmin4, follow these step-by-step instructions:

1. Uncomment extraConfigmapMounts and envVarsFromSecrets
In your values.yaml file, under the appropriate section (e.g., pgadmin4:), add:

```
  # Keycloak client for pgAdmin4
  extraConfigmapMounts:
    - name: config-local
      configMap: pgadmin4-config
      subPath: config_local.py
      mountPath: "/pgadmin4/config_local.py"
      readOnly: true

  envVarsFromSecrets:
    - pgadmin4-oauth2-secret
```

2. Enable oidc.enabled in values.yaml

```yaml
oidc:
  enabled: false
```

3. Replace idp.example.com in cm-pgadmin4-config.yaml with the actual domain of your Keycloak instance.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://helm.runix.net | pgadmin4 | 1.49.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/pgadmin"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"pgadmin","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"pgadmin"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| oidc.enabled | bool | `false` |  |
| pgadmin4.env.email | string | `"pgadmin4@epam.com"` |  |
| pgadmin4.envVarsExtra[0].name | string | `"CONFIG_DATABASE_URI"` |  |
| pgadmin4.envVarsExtra[0].valueFrom.secretKeyRef.key | string | `"uri"` |  |
| pgadmin4.envVarsExtra[0].valueFrom.secretKeyRef.name | string | `"pgadmin-pguser-pgadmin"` |  |
| pgadmin4.existingSecret | string | `"pgadmin4-password"` |  |
| pgadmin4.ingress.enabled | bool | `true` |  |
| pgadmin4.ingress.hosts[0].host | string | `"pgadmin4.example.com"` |  |
| pgadmin4.ingress.hosts[0].paths[0].path | string | `"/"` |  |
| pgadmin4.ingress.hosts[0].paths[0].pathType | string | `"Prefix"` |  |
| pgadmin4.persistentVolume.enabled | bool | `false` |  |
