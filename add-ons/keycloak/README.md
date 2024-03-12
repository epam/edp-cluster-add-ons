# keycloak

![Version: 2.3.0](https://img.shields.io/badge/Version-2.3.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 22.0.4](https://img.shields.io/badge/AppVersion-22.0.4-informational?style=flat-square)

A Helm chart for Keycloak

# Expose Keycloak

Keycloak add-on provides the ability to split user endpoints and admin endpoints to different Ingress Controllers.<br>
The user endpoints are used for user authentication and authorization, while the admin endpoints are used for Keycloak administration.

To expose external Keycloak endpoint, follow the steps below:

1. Set the `keycloak.ingress.enabled` parameter to `true` to enable the Ingress resource.

2. Set the `keycloak.ingress.ingressClassName` parameter to `external-nginx` to use the External Ingress Controller.

```yaml
keycloak:
  ingress:
    enabled: true
    ingressClassName: "external-nginx"
```

These changes provide the ability to expose Keycloak endpoints according to the rules from [documentation](https://www.keycloak.org/server/reverseproxy#_exposed_path_recommendations).

To expose internal Keycloak endpoint, follow the steps below:

1. Set the `keycloak.ingress.console.enabled` parameter to `true` to enable the Ingress resource for admin console endpoint.
2. Set the `keycloak.ingress.console.ingressClassName` parameter to `nginx` or leave it empty to use the Internal Ingress Controller.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://codecentric.github.io/helm-charts | keycloakx | 2.3.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.secretName | string | `"/edp/eks/addons/keycloak"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore-keycloak"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| keycloakx.autoscaling.behavior.scaleDown.policies[0].periodSeconds | int | `300` |  |
| keycloakx.autoscaling.behavior.scaleDown.policies[0].type | string | `"Pods"` |  |
| keycloakx.autoscaling.behavior.scaleDown.policies[0].value | int | `1` |  |
| keycloakx.autoscaling.behavior.scaleDown.stabilizationWindowSeconds | int | `300` |  |
| keycloakx.autoscaling.enabled | bool | `true` |  |
| keycloakx.autoscaling.labels | object | `{}` |  |
| keycloakx.autoscaling.maxReplicas | int | `3` |  |
| keycloakx.autoscaling.metrics[0].resource.name | string | `"cpu"` |  |
| keycloakx.autoscaling.metrics[0].resource.target.averageUtilization | int | `80` |  |
| keycloakx.autoscaling.metrics[0].resource.target.type | string | `"Utilization"` |  |
| keycloakx.autoscaling.metrics[0].type | string | `"Resource"` |  |
| keycloakx.autoscaling.minReplicas | int | `1` |  |
| keycloakx.command[0] | string | `"/opt/keycloak/bin/kc.sh"` |  |
| keycloakx.command[10] | string | `"--import-realm"` |  |
| keycloakx.command[1] | string | `"--verbose"` |  |
| keycloakx.command[2] | string | `"start"` |  |
| keycloakx.command[3] | string | `"--auto-build"` |  |
| keycloakx.command[4] | string | `"--http-enabled=true"` |  |
| keycloakx.command[5] | string | `"--http-port=8080"` |  |
| keycloakx.command[6] | string | `"--hostname-strict=false"` |  |
| keycloakx.command[7] | string | `"--hostname-strict-https=false"` |  |
| keycloakx.command[8] | string | `"--spi-events-listener-jboss-logging-success-level=info"` |  |
| keycloakx.command[9] | string | `"--spi-events-listener-jboss-logging-error-level=warn"` |  |
| keycloakx.database.database | string | `"keycloak"` |  |
| keycloakx.database.existingSecret | string | `"keycloak-pguser-admin"` |  |
| keycloakx.database.hostname | string | `"keycloak-primary.security.svc"` |  |
| keycloakx.database.port | int | `5432` |  |
| keycloakx.database.username | string | `"admin"` |  |
| keycloakx.database.vendor | string | `"postgres"` |  |
| keycloakx.dbchecker.enabled | bool | `true` |  |
| keycloakx.extraEnv | string | `"- name: KC_HOSTNAME_URL\n  value: \"https://keycloak.example.com/auth\"\n- name: KC_HOSTNAME_ADMIN_URL\n  value: \"https://keycloak.example.com/auth\"\n- name: KEYCLOAK_ADMIN\n  valueFrom:\n    secretKeyRef:\n      name: keycloak-admin-creds\n      key: username\n- name: KEYCLOAK_ADMIN_PASSWORD\n  valueFrom:\n    secretKeyRef:\n      name: keycloak-admin-creds\n      key: password\n- name: JAVA_OPTS_APPEND\n  value: >-\n    -XX:+UseContainerSupport\n    -XX:MaxRAMPercentage=50.0\n    -Djava.awt.headless=true\n    -Djgroups.dns.query={{ include \"keycloak.fullname\" . }}-headless\n"` |  |
| keycloakx.fullnameOverride | string | `"keycloakx"` |  |
| keycloakx.health.enabled | bool | `false` |  |
| keycloakx.ingress.annotations."ingress.kubernetes.io/affinity" | string | `"cookie"` |  |
| keycloakx.ingress.console.enabled | bool | `true` |  |
| keycloakx.ingress.console.ingressClassName | string | `"nginx"` |  |
| keycloakx.ingress.console.rules[0].host | string | `"keycloak-internal.example.com"` |  |
| keycloakx.ingress.console.rules[0].paths[0].path | string | `"{{ tpl .Values.http.relativePath $ | trimSuffix \"/\" }}/"` |  |
| keycloakx.ingress.console.rules[0].paths[0].pathType | string | `"Prefix"` |  |
| keycloakx.ingress.enabled | bool | `true` |  |
| keycloakx.ingress.ingressClassName | string | `"external-nginx"` |  |
| keycloakx.ingress.rules[0].host | string | `"keycloak.example.com"` |  |
| keycloakx.ingress.rules[0].paths[0].path | string | `"{{ tpl .Values.http.relativePath $ | trimSuffix \"/\" }}/realms/"` |  |
| keycloakx.ingress.rules[0].paths[0].pathType | string | `"Prefix"` |  |
| keycloakx.ingress.rules[0].paths[1].path | string | `"{{ tpl .Values.http.relativePath $ | trimSuffix \"/\" }}/resources/"` |  |
| keycloakx.ingress.rules[0].paths[1].pathType | string | `"Prefix"` |  |
| keycloakx.ingress.rules[0].paths[2].path | string | `"{{ tpl .Values.http.relativePath $ | trimSuffix \"/\" }}/robots.txt"` |  |
| keycloakx.ingress.rules[0].paths[2].pathType | string | `"Prefix"` |  |
| keycloakx.ingress.rules[0].paths[3].path | string | `"{{ tpl .Values.http.relativePath $ | trimSuffix \"/\" }}/js/"` |  |
| keycloakx.ingress.rules[0].paths[3].pathType | string | `"Prefix"` |  |
| keycloakx.metrics.enabled | bool | `false` |  |
| keycloakx.nameOverride | string | `"keycloakx"` |  |
| keycloakx.proxy.enabled | bool | `true` |  |
| keycloakx.proxy.mode | string | `"passthrough"` |  |
| keycloakx.replicas | int | `1` |  |
| keycloakx.resources.limits.memory | string | `"2048Mi"` |  |
| keycloakx.resources.requests.cpu | string | `"50m"` |  |
| keycloakx.resources.requests.memory | string | `"512Mi"` |  |
| pgo.enabled | bool | `true` | Enables creating a new database with Postgres operator. |
