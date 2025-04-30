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

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic keycloak-client-shared-secret \
  --from-literal=clientSecret=<clientSecret>
```

```bash
kubectl create secret generic keycloak \
  --from-literal=username=<username> \
  --from-literal=password=<password>
```

```bash
kubectl create secret generic keycloak-client-eks-secret \
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
  "keycloak-client-shared-secret":
    {
      "clientSecret": "<clientSecret>",
    },
  "keycloak":
    {
      "username": "<username>",
      "password": "<password>"
    },
  "keycloak-client-eks-secret":
    {
      "clientSecret": "<client>"
    }
}
```

</details>

User Creation Process for Keycloak Integration Across Configurations

<details>
<summary><b>Examples 1: Users management without predefined broker realm:</b></summary>

```
broker:
  # Create the broker realm with corresponding resources.
  create: true
  # If broker create parameter set to false operator create only a client for connection as Identity Provider,
  # in this case be sure you define correct Realm name.
  name: "broker"

# Realm creating for connecting and managing shared services clients, such as Nexus, Sonar, DefectDojo, etc.
sharedService: "shared"
```

Step-by-Step Guide to onboarding User:

Step 1: Create a New User in the `broker` Realm:
1. Go to the `broker` Realm.
2. Navigate `Users` tab and click `Add User` button.
3. Enter the following details:
  * Username: A unique `username` (e.g., `developer123`).
  * Email: The user's `email address` (e.g., `developer@example.com`).
  * First Name: The user's `first name` (e.g., `John`).
  * Last Name: The user's `last name` (e.g., `Doe`).
4. Click Save to save the user's details.
5. Go to the `Credentials` tab:
  * Click `Set Password` button.
  * Enter the new password twice.
    Note: If the password is fixed, toggle the Temporary switch to Off.
(Otherwise, the user will be prompted to change the password upon their first login).
6. Go to the Details tab:
   Copy the `User ID` and `Username`. These values will be required for the next step.

Step 2: Link the User in the `shared` Realm
1. Go to the `shared` Realm.
2. Open `Users` tab and click `Add User` button.
3. Set the same `username` from `step 1.3`.
4. Click Save to create the user.
5. Open the newly created user, go to the `Identity Provider` Links tab:
   Provide the following details from the `step 1.6`:
   * User ID: The `ID` of user copied from the Details tab in the `broker` Realm.
   * Username: The `Username` of user copied from the Details tab in the `broker` Realm.
   * Click `Link` to complete the association.

Step 3: Assign Groups to the User in the `shared` Realm
  - Open the user in the `shared` Realm.
  - Go to the `Groups` tab.
  - Click `Join Group`.
  - Select the `Developer` group and confirm the selection.

Step 4: Assign Roles to the User in the `shared` Realm
  - Go to the Role Mappings tab.
  - In the Available Roles section, select the roles required for the user (e.g., `sonar-developers`).
  - Click Assign to apply the roles.

Result: The user will now be able to:

- Access resources assigned to the `Developer` group.
- Log in to SonarQube with the `sonar-developers` role.

For more details on permissions and the platform's authentication model, refer to the documentation:
[KuberocketCI Documentation — Platform Authentication Model](https://docs.kuberocketci.io/docs/operator-guide/auth/platform-auth-model/)

</details>

<details>
<summary><b>Example 2: Users management with predefined broker realm:</b></summary>

```
broker:
  # Create the broker realm with corresponding resources.
  create: false
  # If broker create parameter set to false operator create only a client for connection as Identity Provider,
  # in this case be sure you define correct Realm name.

existingBroker: "project-realm"

sharedService: "shared"
```

Step-by-Step Guide to onboarding User:

(Optional step) if user does not exist in `project-broker` Realm:

1. Go to the `project-broker` Realm.
2. Navigate `Users` tab and click `Add User` button.
3. Enter the following details:
  * Username: A unique `username` (e.g., `developer123`).
  * Email: The user's `email address` (e.g., `developer@example.com`).
  * First Name: The user's `first name` (e.g., `John`).
  * Last Name: The user's `last name` (e.g., `Doe`).
4. Click Save to save the user's details.

Step 1: Copy `username` and `ID` from existing `project-broker` Realm:
1. Go to the `project-broker` Realm.
2. Select `Users` tab.
3. Enter the following details:
4. Go to the Details tab:
   Copy the `User ID` and `Username`. These values will be required for the next step.

Step 2: Link the User in the `shared` Realm
1. Go to the `shared` Realm.
2. Navigate `Users` tab and click `Add User` button.
3. Set the same `username` from `step 1.3`.
4. Click Save to create the user.
5. Open the newly created user, go to the `Identity Provider` Links tab:
   Provide the following details from the `step 1.4`:
   * User ID: The `ID` of user copied from the Details tab in the `broker` Realm.
   * Username: The `Username` of user copied from the Details tab in the `broker` Realm.
   * Click `Link` to complete the association.

Step 3: Assign Groups to the User in the `shared` Realm
  - Open the user in the `shared` Realm.
  - Go to the `Groups` tab.
  - Click `Join Group`.
  - Select the `Administrator` group and confirm the selection.

Step 4: Assign Roles to the User in the `shared` Realm
  - Go to the Role Mappings tab.
  - In the Available Roles section, select the roles required for the user (e.g., `sonar-administrators`).
  - Click Assign to apply the roles.

Result: The user will now be able to:

- Access resources assigned to the `Administrator` group.
- Log in to SonarQube with the `sonar-administrators` role.

For more details on permissions and the platform's authentication model, refer to the documentation:
[KuberocketCI Documentation — Platform Authentication Model](https://docs.kuberocketci.io/docs/operator-guide/auth/platform-auth-model/)

</details>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| broker.create | bool | `true` |  |
| broker.name | string | `"broker"` |  |
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/kuberocketci-rbac"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"kuberocketci-rbac","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"kuberocketci-rbac"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| keycloakUrl | string | `"https://example.com"` |  |
| kubernetes | object | `{"enabled":false}` | This block enable the creation of Keycloak operator resources for the EKS OIDC configuration, such as client, client scope, and realm groups. |
| sharedService | string | `"shared"` |  |
