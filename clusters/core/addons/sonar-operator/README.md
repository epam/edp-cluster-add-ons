# sonar-operator

![Version: 3.1.1](https://img.shields.io/badge/Version-3.1.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.1.1](https://img.shields.io/badge/AppVersion-3.1.1-informational?style=flat-square)

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
| https://epam.github.io/edp-helm-charts/stable | sonar-operator | 3.1.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/infra/core/addons/sonar-operator"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| oidc.enabled | bool | `false` |  |
| oidc.keycloakRealm | string | `"shared"` |  |
| oidc.keycloakUrl | string | `"https://keycloak.example.com"` |  |
| sonar-operator.affinity | object | `{}` |  |
| sonar-operator.annotations | object | `{}` |  |
| sonar-operator.extraVolumeMounts | list | `[]` | Additional volumeMounts to be added to the container |
| sonar-operator.extraVolumes | list | `[]` | Additional volumes to be added to the pod |
| sonar-operator.image.repository | string | `"epamedp/sonar-operator"` | EDP sonar-operator Docker image name. The released image can be found on [Dockerhub](https://hub.docker.com/r/epamedp/sonar-operator) |
| sonar-operator.image.tag | string | `"3.1.1"` | EDP sonar-operator Docker image tag. The released image can be found on [Dockerhub](https://hub.docker.com/r/epamedp/sonar-operator/tags) |
| sonar-operator.imagePullPolicy | string | `"IfNotPresent"` |  |
| sonar-operator.name | string | `"sonar-operator"` | component name |
| sonar-operator.nodeSelector | object | `{}` |  |
| sonar-operator.resources.limits.memory | string | `"192Mi"` |  |
| sonar-operator.resources.requests.cpu | string | `"50m"` |  |
| sonar-operator.resources.requests.memory | string | `"64Mi"` |  |
| sonar-operator.tolerations | list | `[]` |  |
| sonarSecret | string | `"sonar-admin-password"` | This is credantials name with administator rights for sonar. |
| sonarUrl | string | `"https://sonar.example.com"` | URL and secret name which use sonar operator for configuring sonar |
