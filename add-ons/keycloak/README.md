# keycloak

![Version: 0.1.1](https://img.shields.io/badge/Version-0.1.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0](https://img.shields.io/badge/AppVersion-1.0-informational?style=flat-square)

A Helm chart for Keycloak

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://codecentric.github.io/helm-charts | keycloakx | 2.2.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
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
| keycloakx.database.existingSecret | string | `"keycloak-postgresql"` |  |
| keycloakx.database.hostname | string | `"postgresql"` |  |
| keycloakx.database.port | int | `5432` |  |
| keycloakx.database.username | string | `"admin"` |  |
| keycloakx.database.vendor | string | `"postgres"` |  |
| keycloakx.dbchecker.enabled | bool | `true` |  |
| keycloakx.extraEnv | string | `"- name: KC_PROXY\n  value: \"passthrough\"\n- name: KEYCLOAK_ADMIN\n  valueFrom:\n    secretKeyRef:\n      name: keycloak-admin-creds\n      key: username\n- name: KEYCLOAK_ADMIN_PASSWORD\n  valueFrom:\n    secretKeyRef:\n      name: keycloak-admin-creds\n      key: password\n- name: JAVA_OPTS_APPEND\n  value: >-\n    -XX:+UseContainerSupport\n    -XX:MaxRAMPercentage=50.0\n    -Djava.awt.headless=true\n    -Djgroups.dns.query={{ include \"keycloak.fullname\" . }}-headless\n"` |  |
| keycloakx.extraInitContainers | string | `"- name: realm-provider\n  image: busybox\n  imagePullPolicy: IfNotPresent\n  command:\n    - sh\n  args:\n    - -c\n    - |\n      echo '{\"realm\": \"openshift\",\"enabled\": true}' > /opt/keycloak/data/import/openshift.json\n  volumeMounts:\n    - name: realm\n      mountPath: /opt/keycloak/data/import\n"` |  |
| keycloakx.extraVolumeMounts | string | `"- name: realm\n  mountPath: /opt/keycloak/data/import\n"` |  |
| keycloakx.extraVolumes | string | `"- name: realm\n  emptyDir: {}\n"` |  |
| keycloakx.fullnameOverride | string | `"keycloakx"` |  |
| keycloakx.image.tag | string | `"20.0.3"` |  |
| keycloakx.ingress.annotations."ingress.kubernetes.io/affinity" | string | `"cookie"` |  |
| keycloakx.ingress.annotations."kubernetes.io/ingress.class" | string | `"nginx"` |  |
| keycloakx.ingress.enabled | bool | `true` |  |
| keycloakx.ingress.rules[0].host | string | `"keycloak.example.com"` |  |
| keycloakx.ingress.rules[0].paths[0].path | string | `"{{ tpl .Values.http.relativePath $ | trimSuffix \"/\" }}/"` |  |
| keycloakx.ingress.rules[0].paths[0].pathType | string | `"Prefix"` |  |
| keycloakx.nameOverride | string | `"keycloakx"` |  |
| keycloakx.replicas | int | `1` |  |
| keycloakx.resources.limits.memory | string | `"2048Mi"` |  |
| keycloakx.resources.requests.cpu | string | `"50m"` |  |
| keycloakx.resources.requests.memory | string | `"512Mi"` |  |

