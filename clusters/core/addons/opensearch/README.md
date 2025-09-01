# opensearch

![Version: 3.2.1](https://img.shields.io/badge/Version-3.2.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.2.0](https://img.shields.io/badge/AppVersion-3.2.0-informational?style=flat-square)

A Helm chart for OpenSearch Stack

## OpenSearch Configuration

Before run helm charts you need to prepare a hash password you can read documentation on https://opensearch.org/docs/latest/security/configuration/yaml/ and run "https://github.com/opensearch-project/security/blob/88b6d23f0c84d83f138cf1a61bbe0145d8dd007e/tools/hash.sh" to generate fo use it in values file"CONSULT OpenSearch FOR HASHED PASSWORD".

Ensure that after applying helm charts you have to run in opensearch pod the following command:

```bash
cd /usr/share/opensearch/plugins/opensearch-security/tools/
./securityadmin.sh -cd ../../../config/opensearch-security/ -icl -nhnv \
 -rev \
 -cacert /usr/share/opensearch/config/admin-certs/ca.crt \
 -cert /usr/share/opensearch/config/admin-certs/tls.crt \
 -key /usr/share/opensearch/config/admin-certs/tls.key
```

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic opensearch-dashboards-account \
  --from-literal=username=<username> \
  --from-literal=password=<password> \
  --from-literal=cookie=<cookie> \
  --from-literal=OIDC_CLIENT_SECRET=<OIDC_CLIENT_SECRET>
```

```bash
kubectl create secret generic fluentbit-creds \
  --from-literal=username=<username> \
  --from-literal=password=<password>
```

```bash
kubectl create secret generic keycloak-client-opensearch-secret \
  --from-literal=clientSecret=<clientSecret>
```

```bash
kubectl create secret generic opensearch-admin-creds \
  --from-literal=username=<username> \
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
  "opensearch-dashboard": {
    "username": "<username>",
    "password": "<password>",
    "cookie": "<cookie>",
    "OIDC_CLIENT_SECRET": "<OIDC_CLIENT_SECRET>"
  },
  "fluentbit": {
    "username": "<username>",
    "password": "<password>"
  },
  "opensearch": {
    "username": "<username>",
    "password": "<password>"
  }
}
```

</details>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://fluent.github.io/helm-charts | fluent-bit | 0.52.0 |
| https://opensearch-project.github.io/helm-charts/ | opensearch | 3.2.1 |
| https://opensearch-project.github.io/helm-charts/ | opensearch-dashboards | 3.2.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/opensearch"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"opensearch","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"opensearch"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| fluent-bit.config.customParsers | string | `"[PARSER]\n    Name docker_no_time\n    Format json\n    Time_Keep Off\n    Time_Key time\n    Time_Format %Y-%m-%dT%H:%M:%S.%L\n\n[PARSER]\n    Name        java_multiline\n    Format      regex\n    Regex       /^(?<time>\\d{4}-\\d{1,2}-\\d{1,2} \\d{1,2}:\\d{1,2}:\\d{1,2}) (?<level>[^\\s]+)(?<message>.*)/\n    Time_Key    time\n    Time_Format %Y-%m-%d %H:%M:%S\n"` |  |
| fluent-bit.config.filters | string | `"[FILTER]\n    Name kubernetes\n    Match kube.*\n    Merge_Log On\n    Keep_Log Off\n    K8S-Logging.Parser On\n    K8S-Logging.Exclude On\n\n# START of EDP logs chain\n[FILTER]\n    Name kubernetes\n    Match kube.edp.*\n    Merge_Log On\n    Keep_Log Off\n    Kube_Tag_Prefix  kube.edp.var.log.containers.\n    K8S-Logging.Parser On\n    K8S-Logging.Exclude On\n"` |  |
| fluent-bit.config.inputs | string | `"[INPUT]\n    Name tail\n    Path /var/log/containers/*.log\n    multiline.parser docker, cri\n    Tag kube.*\n    Mem_Buf_Limit 5MB\n    Skip_Long_Lines On\n\n[INPUT]\n    Name systemd\n    Tag host.*\n    Systemd_Filter _SYSTEMD_UNIT=kubelet.service\n    Read_From_Tail On\n\n[INPUT]\n    # Grab EDP namespace logs to separate index for development team\n    Name tail\n    Tag kube.edp.*\n    Path /var/log/containers/*edp*.log\n    multiline.parser docker, cri\n    Mem_Buf_Limit 5MB\n    Skip_Long_Lines On\n"` |  |
| fluent-bit.config.outputs | string | `"[OUTPUT]\n    Name            es\n    Match           kube.*\n    Host            opensearch-cluster-master\n    Port            9200\n    HTTP_User       ${ES_SUPERUSER_USER}\n    HTTP_Passwd     ${ES_SUPERUSER_PASSWORD}\n    Logstash_Format On\n    Logstash_Prefix logstash-infra\n    Time_Key        @timestamp\n    Replace_Dots    On\n    Retry_Limit     False\n    Trace_Error     Off\n    Suppress_Type_Name On\n    tls             On\n    tls.verify      Off\n\n[OUTPUT]\n    Name            es\n    Match           host.*\n    Host            opensearch-cluster-master\n    Port            9200\n    HTTP_User       ${ES_SUPERUSER_USER}\n    HTTP_Passwd     ${ES_SUPERUSER_PASSWORD}\n    Logstash_Format On\n    Logstash_Prefix logstash-host\n    Time_Key        @timestamp\n    Replace_Dots    On\n    Retry_Limit     False\n    Trace_Error     Off\n    Suppress_Type_Name On\n    tls             On\n    tls.verify      Off\n\n[OUTPUT]\n    Name            es\n    Match           kube.edp.*\n    Host            opensearch-cluster-master\n    Port            9200\n    HTTP_User       ${ES_SUPERUSER_USER}\n    HTTP_Passwd     ${ES_SUPERUSER_PASSWORD}\n    Logstash_Format On\n    Logstash_Prefix logstash-edp\n    Time_Key        @timestamp\n    Replace_Dots    On\n    Retry_Limit     False\n    Trace_Error     Off\n    Suppress_Type_Name On\n    tls             On\n    tls.verify      Off\n"` |  |
| fluent-bit.env[0].name | string | `"ES_SUPERUSER_USER"` |  |
| fluent-bit.env[0].valueFrom.secretKeyRef.key | string | `"username"` |  |
| fluent-bit.env[0].valueFrom.secretKeyRef.name | string | `"fluentbit-creds"` |  |
| fluent-bit.env[1].name | string | `"ES_SUPERUSER_PASSWORD"` |  |
| fluent-bit.env[1].valueFrom.secretKeyRef.key | string | `"password"` |  |
| fluent-bit.env[1].valueFrom.secretKeyRef.name | string | `"fluentbit-creds"` |  |
| fluent-bit.testFramework.enabled | bool | `false` |  |
| oidc.dashboardUrl | string | `"https://opensearch-dashboards.example.com"` |  |
| oidc.enabled | bool | `true` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch.password | string | `"${OPENSEARCH_PASSWORD}"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch.requestHeadersAllowlist[0] | string | `"Authorization"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch.requestHeadersAllowlist[1] | string | `"security_tenant"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch.ssl.certificateAuthorities | string | `"/usr/share/opensearch-dashboards/certs/ca.crt"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch.ssl.verificationMode | string | `"certificate"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch.username | string | `"${OPENSEARCH_USERNAME}"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security."auth.type" | string | `"openid"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.cookie.password | string | `"${COOKIE_PASS}"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.cookie.secure | bool | `false` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.multitenancy."tenants.enable_global" | bool | `true` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.multitenancy."tenants.enable_private" | bool | `true` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.multitenancy."tenants.preferred"[0] | string | `"Private"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.multitenancy."tenants.preferred"[1] | string | `"Global"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.multitenancy.enable_filter | bool | `false` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.multitenancy.enabled | bool | `true` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.openid.base_redirect_url | string | `"https://kibana.example.com"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.openid.client_id | string | `"opensearch"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.openid.client_secret | string | `"${OIDC_CLIENT_SECRET}"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.openid.connect_url | string | `"https://keycloak.example.com/auth/realms/shared/.well-known/openid-configuration"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.openid.header | string | `"Authorization"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.openid.scope | string | `"openid profile email"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.openid.trust_dynamic_headers | bool | `true` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".opensearch_security.openid.verify_hostnames | bool | `false` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".server.host | string | `"0.0.0.0"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".server.ssl.certificate | string | `"/usr/share/opensearch-dashboards/certs/tls.crt"` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".server.ssl.enabled | bool | `false` |  |
| opensearch-dashboards.config."opensearch_dashboards.yml".server.ssl.key | string | `"/usr/share/opensearch-dashboards/certs/tls.key"` |  |
| opensearch-dashboards.extraEnvs[0].name | string | `"OIDC_CLIENT_SECRET"` |  |
| opensearch-dashboards.extraEnvs[0].valueFrom.secretKeyRef.key | string | `"OIDC_CLIENT_SECRET"` |  |
| opensearch-dashboards.extraEnvs[0].valueFrom.secretKeyRef.name | string | `"opensearch-dashboards-account"` |  |
| opensearch-dashboards.fullnameOverride | string | `"opensearch-dashboards"` |  |
| opensearch-dashboards.ingress.enabled | bool | `true` |  |
| opensearch-dashboards.ingress.hosts[0].host | string | `"kibana.example.com"` |  |
| opensearch-dashboards.ingress.hosts[0].paths[0].backend.serviceName | string | `""` |  |
| opensearch-dashboards.ingress.hosts[0].paths[0].backend.servicePort | string | `""` |  |
| opensearch-dashboards.ingress.hosts[0].paths[0].path | string | `"/"` |  |
| opensearch-dashboards.ingress.ingressClassName | string | `"nginx"` |  |
| opensearch-dashboards.nameOverride | string | `"opensearch-dashboards"` |  |
| opensearch-dashboards.opensearchAccount.keyPassphrase.enabled | bool | `false` |  |
| opensearch-dashboards.opensearchAccount.secret | string | `"opensearch-dashboards-account"` |  |
| opensearch-dashboards.secretMounts[0].name | string | `"opensearch-certs"` |  |
| opensearch-dashboards.secretMounts[0].path | string | `"/usr/share/opensearch-dashboards/certs"` |  |
| opensearch-dashboards.secretMounts[0].secretName | string | `"tls-for-dashboards-key-pair"` |  |
| opensearch-dashboards.startupProbe.initialDelaySeconds | int | `60` |  |
| opensearch.config."opensearch.yml" | string | `"cluster.name: opensearch-cluster\n\n# Bind to all interfaces because we don't know what IP address Docker will assign to us.\nnetwork.host: 0.0.0.0\n\n# # minimum_master_nodes need to be explicitly set when bound on a public IP\n# # set to 1 to allow single node clusters\n# discovery.zen.minimum_master_nodes: 1\n\n# Setting network.host to a non-loopback address enables the annoying bootstrap checks. \"Single-node\" mode disables them again.\n#discovery.type: single-node\n\n######## Start OpenSearch Security Demo Configuration ########\n# WARNING: revise all the lines below before you go into production\nplugins:\n  security:\n    nodes_dn:\n      - 'CN=opensearch.cluster.local'\n    ssl:\n      transport:\n        pemcert_filepath: certs/tls.crt\n        pemkey_filepath: certs/tls.key\n        pemtrustedcas_filepath: certs/ca.crt\n        enforce_hostname_verification: false\n      http:\n        enabled: true\n        pemcert_filepath: certs/tls.crt\n        pemkey_filepath: certs/tls.key\n        pemtrustedcas_filepath: certs/ca.crt\n    allow_unsafe_democertificates: false\n    allow_default_init_securityindex: true\n    authcz:\n      admin_dn:\n        - 'CN=admin'\n    audit.type: internal_opensearch\n    enable_snapshot_restore_privilege: true\n    check_snapshot_restore_write_privileges: true\n    restapi:\n      roles_enabled: [\"all_access\", \"security_rest_api_access\"]\n    system_indices:\n      enabled: true\n      indices:\n        [\n          \".opendistro-alerting-config\",\n          \".opendistro-alerting-alert*\",\n          \".opendistro-anomaly-results*\",\n          \".opendistro-anomaly-detector*\",\n          \".opendistro-anomaly-checkpoints\",\n          \".opendistro-anomaly-detection-state\",\n          \".opendistro-reports-*\",\n          \".opendistro-notifications-*\",\n          \".opendistro-notebooks\",\n          \".opendistro-asynchronous-search-response*\",\n        ]\n######## End OpenSearch Security Demo Configuration ########\n"` |  |
| opensearch.extraEnvs[0].name | string | `"DISABLE_INSTALL_DEMO_CONFIG"` |  |
| opensearch.extraEnvs[0].value | string | `"true"` |  |
| opensearch.fullnameOverride | string | `"opensearch"` |  |
| opensearch.nameOverride | string | `"opensearch"` |  |
| opensearch.persistence.enableInitChown | bool | `false` |  |
| opensearch.persistence.storageClass | string | `"gp3-retain"` |  |
| opensearch.resources.requests.cpu | string | `"500m"` |  |
| opensearch.resources.requests.memory | string | `"1024Mi"` |  |
| opensearch.secretMounts[0].name | string | `"opensearch-certs"` |  |
| opensearch.secretMounts[0].path | string | `"/usr/share/opensearch/config/certs"` |  |
| opensearch.secretMounts[0].secretName | string | `"tls-for-opensearch-key-pair"` |  |
| opensearch.secretMounts[1].name | string | `"opensearch-admin-certs"` |  |
| opensearch.secretMounts[1].path | string | `"/usr/share/opensearch/config/admin-certs"` |  |
| opensearch.secretMounts[1].secretName | string | `"tls-for-opensearch-admin-key-pair"` |  |
| opensearch.securityConfig.actionGroupsSecret | string | `nil` |  |
| opensearch.securityConfig.config.data."action_groups.yml" | string | `"_meta:\n  type: \"actiongroups\"\n  config_version: 2"` |  |
| opensearch.securityConfig.config.data."config.yml" | string | `"_meta:\n  type: \"config\"\n  config_version: 2\nconfig:\n  dynamic:\n    http:\n      anonymous_auth_enabled: false\n      xff:\n        enabled: false\n        internalProxies: \"192\\\\.168\\\\.0\\\\.10|192\\\\.168\\\\.0\\\\.11\"\n    authc:\n      basic_internal_auth_domain:\n        description: \"Authenticate via HTTP Basic against internal users database\"\n        http_enabled: true\n        transport_enabled: true\n        order: 0\n        http_authenticator:\n          type: basic\n          challenge: false\n        authentication_backend:\n          type: internal\n\n      openid_auth_domain:\n        http_enabled: true\n        transport_enabled: true\n        order: 1\n        http_authenticator:\n          type: openid\n          challenge: false\n          config:\n            subject_key: preferred_username\n            roles_key: roles\n            openid_connect_url: https://keycloak.example.com/auth/realms/shared/.well-known/openid-configuration\n            openid_connect_idp:\n              enable_ssl: false\n              verify_hostnames: false\n        authentication_backend:\n          type: noop"` |  |
| opensearch.securityConfig.config.data."internal_users.yml" | string | `"_meta:\n  type: \"internalusers\"\n  config_version: 2\nadmin:\n  hash: \"CONSULT OpenSearch FOR HASHED PASSWORD\"\n  reserved: true\n  hidden: false\n  backend_roles:\n  - \"admin\"\n  attributes: {}\n  description: \"Demo admin user\"\n  static: false\nkibanaserver:\n  hash: \"CONSULT OpenSearch FOR HASHED PASSWORD\"\n  reserved: true\n  hidden: false\n  backend_roles: []\n  attributes: {}\n  description: \"Kibanaserver user\"\n  static: false\nlogstash:\n  hash: \"CONSULT OpenSearch FOR HASHED PASSWORD\"\n  reserved: false\n  hidden: false\n  backend_roles:\n  - \"logstash\"\n  attributes: {}\n  description: \"Log injection user\"\n  static: false"` |  |
| opensearch.securityConfig.config.data."nodes_dn.yml" | string | `"_meta:\n  type: \"nodesdn\"\n  config_version: 2\ntrustednodes:\n  nodes_dn:\n    - \"CN=opensearch.cluster.local\""` |  |
| opensearch.securityConfig.config.data."roles.yml" | string | `"_meta:\n  type: \"roles\"\n  config_version: 2\nedp_developer:\n  reserved: false\n  hidden: false\n  cluster_permissions: []\n  index_permissions:\n    - index_patterns:\n        - \"logstash-edp*\"\n      allowed_actions:\n        - \"indices:data/read/*\"\n  tenant_permissions:\n    - tenant_patterns:\n        - \"*\"\n      allowed_actions:\n        - \"kibana:discover/*\""` |  |
| opensearch.securityConfig.config.data."roles_mapping.yml" | string | `"_meta:\n  type: \"rolesmapping\"\n  config_version: 2\nall_access:\n  reserved: true\n  backend_roles:\n  - \"administrator\"\n  - \"admin\"\n  description: \"Maps EDP administrator role and internal admin role to all_access\"\nlogstash:\n  reserved: true\n  backend_roles:\n  - \"logstash\"\n  description: \"Maps log injection role to logstash. It might be logstash, fluent-bit, fluentd, ...\"\nkibana_user:\n  reserved: false\n  backend_roles:\n  - \"kibanauser\"\n  - \"developer\"\n  description: \"Maps kibanauser and EDP developer role to kibana_user\"\nkibana_server:\n  reserved: true\n  users:\n  - \"kibanaserver\"\nedp_developer:\n  reserved: false\n  backend_roles:\n  - \"developer\"\n  description: \"Maps EDP developer role to view kube index\""` |  |
| opensearch.securityConfig.config.data."tenants.yml" | string | `"_meta:\n  type: \"tenants\"\n  config_version: 2\nadmin_tenant:\n  reserved: false\n  description: \"Demo tenant for admin user\""` |  |
| opensearch.securityConfig.config.data."whitelist.yml" | string | `"_meta:\n  type: \"whitelist\"\n  config_version: 2"` |  |
| opensearch.securityConfig.config.securityConfigSecret | string | `""` |  |
| opensearch.securityConfig.configSecret | string | `nil` |  |
| opensearch.securityConfig.enabled | bool | `true` |  |
| opensearch.securityConfig.internalUsersSecret | string | `nil` |  |
| opensearch.securityConfig.path | string | `"/usr/share/opensearch/config/opensearch-security"` |  |
| opensearch.securityConfig.rolesMappingSecret | string | `nil` |  |
| opensearch.securityConfig.rolesSecret | string | `nil` |  |
| opensearch.securityConfig.tenantsSecret | string | `nil` |  |
| opensearch.singleNode | bool | `true` |  |
