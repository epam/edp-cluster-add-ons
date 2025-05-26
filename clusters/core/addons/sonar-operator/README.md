# sonar-operator

![Version: 3.3.0](https://img.shields.io/badge/Version-3.3.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.3.0](https://img.shields.io/badge/AppVersion-3.3.0-informational?style=flat-square)

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):

```bash
kubectl create secret generic sonar-admin-password \
  --from-literal=user=<user> \
  --from-literal=password=<password>
```

```bash
kubectl create secret generic sonar-view-user \
  --from-literal=password=<password>
```

```bash
kubectl create secret generic ci-sonar \
  --from-literal=password=<password>
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
  "sonarqube": {
    "user": "<clientSecret>",
    "password": "<password>"
  },
  "sonar-view-user": {
    "password": "<password>"
  },
  "sonarqube-ci-user": {
    "password": "<password>"
  }
}
```

</details>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://epam.github.io/edp-helm-charts/stable | sonar-operator | 3.3.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/sonar-operator"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"sonar-operator","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"sonar-operator"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| oidc.enabled | bool | `false` |  |
| oidc.keycloakRealm | string | `"shared"` |  |
| oidc.keycloakUrl | string | `"https://keycloak.example.com"` |  |
| sonar-operator.affinity | object | `{}` |  |
| sonar-operator.annotations | object | `{}` |  |
| sonar-operator.extraVolumeMounts | list | `[]` | Additional volumeMounts to be added to the container |
| sonar-operator.extraVolumes | list | `[]` | Additional volumes to be added to the pod |
| sonar-operator.image.repository | string | `"epamedp/sonar-operator"` | EDP sonar-operator Docker image name. The released image can be found on [Dockerhub](https://hub.docker.com/r/epamedp/sonar-operator) |
| sonar-operator.image.tag | string | `""` | EDP sonar-operator Docker image tag. The released image can be found on [Dockerhub](https://hub.docker.com/r/epamedp/sonar-operator/tags) |
| sonar-operator.imagePullPolicy | string | `"IfNotPresent"` |  |
| sonar-operator.imagePullSecrets | list | `[]` | Optional array of imagePullSecrets containing private registry credentials # Ref: https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry |
| sonar-operator.name | string | `"sonar-operator"` | component name |
| sonar-operator.nodeSelector | object | `{}` |  |
| sonar-operator.resources.limits.memory | string | `"192Mi"` |  |
| sonar-operator.resources.requests.cpu | string | `"50m"` |  |
| sonar-operator.resources.requests.memory | string | `"64Mi"` |  |
| sonar-operator.tolerations | list | `[]` |  |
| sonarSecret | string | `"sonar-admin-password"` | This is credantials name with administator rights for sonar. |
| sonarUrl | string | `"https://sonar.example.com"` | URL and secret name which use sonar operator for configuring sonar |
