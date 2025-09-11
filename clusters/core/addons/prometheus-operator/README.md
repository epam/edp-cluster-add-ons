# prometheus-operator

![Version: 77.6.0](https://img.shields.io/badge/Version-77.6.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v0.85.0](https://img.shields.io/badge/AppVersion-v0.85.0-informational?style=flat-square)

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic grafana-admin-creds \
  --from-literal=username=<username> \
  --from-literal=password=<password>
```

```bash
kubectl create secret generic keycloak-client-grafana-secret \
  --from-literal=GF_AUTH_GENERIC_OAUTH_CLIENT_SECRET=<clientSecret> \
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
  "grafana": {
    "username": "<username>",
    "password": "<password>"
  },
  "keycloak-client-grafana-secret": {
    "clientSecret": "<clientSecret>"
  }
}
```

</details>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://prometheus-community.github.io/helm-charts | kube-prometheus-stack | 77.6.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/prometheus-operator"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"prometheus-operator","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"prometheus-operator"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| kube-prometheus-stack.alertmanager.alertmanagerSpec.resources.limits.memory | string | `"300Mi"` |  |
| kube-prometheus-stack.alertmanager.alertmanagerSpec.resources.requests.cpu | string | `"10m"` |  |
| kube-prometheus-stack.alertmanager.alertmanagerSpec.resources.requests.memory | string | `"200Mi"` |  |
| kube-prometheus-stack.alertmanager.config.inhibit_rules[0].equal[0] | string | `"prometheus"` |  |
| kube-prometheus-stack.alertmanager.config.inhibit_rules[0].source_match.alertname | string | `"Watchdog"` |  |
| kube-prometheus-stack.alertmanager.config.inhibit_rules[0].target_match_re.alertname | string | `".+Overcommit"` |  |
| kube-prometheus-stack.alertmanager.config.receivers[0].name | string | `"null"` |  |
| kube-prometheus-stack.alertmanager.config.receivers[1].name | string | `"msteams"` |  |
| kube-prometheus-stack.alertmanager.config.receivers[1].webhook_configs[0].url | string | `"http://prometheus-msteams:2000/alert-sandbox"` |  |
| kube-prometheus-stack.alertmanager.config.route.group_by[0] | string | `"alertname"` |  |
| kube-prometheus-stack.alertmanager.config.route.group_interval | string | `"5m"` |  |
| kube-prometheus-stack.alertmanager.config.route.group_wait | string | `"30s"` |  |
| kube-prometheus-stack.alertmanager.config.route.receiver | string | `"msteams"` |  |
| kube-prometheus-stack.alertmanager.config.route.repeat_interval | string | `"12h"` |  |
| kube-prometheus-stack.alertmanager.config.route.routes[0].receiver | string | `"msteams"` |  |
| kube-prometheus-stack.alertmanager.config.route.routes[1].match.alertname | string | `"Watchdog"` |  |
| kube-prometheus-stack.alertmanager.config.route.routes[1].receiver | string | `"null"` |  |
| kube-prometheus-stack.alertmanager.enabled | bool | `false` |  |
| kube-prometheus-stack.alertmanager.ingress.enabled | bool | `true` |  |
| kube-prometheus-stack.alertmanager.ingress.hosts[0] | string | `"alertmanager.example.com"` |  |
| kube-prometheus-stack.defaultRules.rules.etcd | bool | `false` |  |
| kube-prometheus-stack.fullnameOverride | string | `"prom"` |  |
| kube-prometheus-stack.grafana."grafana.ini"."auth.generic_oauth".allow_sign_up | bool | `true` |  |
| kube-prometheus-stack.grafana."grafana.ini"."auth.generic_oauth".api_url | string | `"https://keycloak.example.com/auth/realms/shared/protocol/openid-connect/userinfo"` |  |
| kube-prometheus-stack.grafana."grafana.ini"."auth.generic_oauth".auth_url | string | `"https://keycloak.example.com/auth/realms/shared/protocol/openid-connect/auth"` |  |
| kube-prometheus-stack.grafana."grafana.ini"."auth.generic_oauth".client_id | string | `"grafana"` |  |
| kube-prometheus-stack.grafana."grafana.ini"."auth.generic_oauth".enabled | bool | `true` |  |
| kube-prometheus-stack.grafana."grafana.ini"."auth.generic_oauth".role_attribute_path | string | `"contains(roles[*], 'administrator') && 'Admin' || contains(roles[*], 'developer') && 'Editor' || 'Viewer'"` |  |
| kube-prometheus-stack.grafana."grafana.ini"."auth.generic_oauth".scopes | string | `"openid profile email roles"` |  |
| kube-prometheus-stack.grafana."grafana.ini"."auth.generic_oauth".token_url | string | `"https://keycloak.example.com/auth/realms/shared/protocol/openid-connect/token"` |  |
| kube-prometheus-stack.grafana."grafana.ini".analytics.check_for_updates | bool | `false` |  |
| kube-prometheus-stack.grafana."grafana.ini".auth.disable_signout_menu | bool | `true` |  |
| kube-prometheus-stack.grafana."grafana.ini".auth.oauth_auto_login | bool | `true` |  |
| kube-prometheus-stack.grafana."grafana.ini".server.root_url | string | `"https://grafana.example.com"` |  |
| kube-prometheus-stack.grafana.admin.existingSecret | string | `"grafana-admin-creds"` |  |
| kube-prometheus-stack.grafana.admin.passwordKey | string | `"password"` |  |
| kube-prometheus-stack.grafana.admin.userKey | string | `"username"` |  |
| kube-prometheus-stack.grafana.envFromSecret | string | `"keycloak-client-grafana-secret"` |  |
| kube-prometheus-stack.grafana.fullnameOverride | string | `"grafana"` |  |
| kube-prometheus-stack.grafana.ingress.annotations."nginx.ingress.kubernetes.io/configuration-snippet" | string | `"more_set_headers X-Frame-Options: none;"` |  |
| kube-prometheus-stack.grafana.ingress.enabled | bool | `true` |  |
| kube-prometheus-stack.grafana.ingress.hosts[0] | string | `"grafana.example.com"` |  |
| kube-prometheus-stack.grafana.ingress.pathType | string | `"ImplementationSpecific"` |  |
| kube-prometheus-stack.grafana.ingress.paths[0] | string | `"/"` |  |
| kube-prometheus-stack.grafana.persistence.enabled | bool | `true` |  |
| kube-prometheus-stack.grafana.persistence.size | string | `"1Gi"` |  |
| kube-prometheus-stack.grafana.persistence.storageClassName | string | `"gp3-retain"` |  |
| kube-prometheus-stack.grafana.resources.limits.memory | string | `"128Mi"` |  |
| kube-prometheus-stack.grafana.resources.requests.cpu | string | `"25m"` |  |
| kube-prometheus-stack.grafana.resources.requests.memory | string | `"72Mi"` |  |
| kube-prometheus-stack.kubeControllerManager.enabled | bool | `false` |  |
| kube-prometheus-stack.kubeEtcd.enabled | bool | `false` |  |
| kube-prometheus-stack.kubeScheduler.enabled | bool | `false` |  |
| kube-prometheus-stack.nameOverride | string | `"prom"` |  |
| kube-prometheus-stack.prometheus.additionalServiceMonitors | list | `[]` |  |
| kube-prometheus-stack.prometheus.ingress.enabled | bool | `false` |  |
| kube-prometheus-stack.prometheus.ingress.hosts[0] | string | `"prometheus.example.com"` |  |
| kube-prometheus-stack.prometheus.prometheusSpec.scrapeConfigNamespaceSelector | string | `nil` |  |
| kube-prometheus-stack.prometheusOperator.resources.limits.memory | string | `"256Mi"` |  |
| kube-prometheus-stack.prometheusOperator.resources.requests.cpu | string | `"100m"` |  |
| kube-prometheus-stack.prometheusOperator.resources.requests.memory | string | `"128Mi"` |  |
| oidc.enabled | bool | `false` |  |
