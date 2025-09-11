# fluent-bit

![Version: 0.53.0](https://img.shields.io/badge/Version-0.53.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 4.0.7](https://img.shields.io/badge/AppVersion-4.0.7-informational?style=flat-square)

A Helm chart for Fluent Bit

## Secret management

There is two way for creating secret for this add-on: manual by using kubectl command and using External Secret Operator.

<details open>
<summary><b>Kubectl</b></summary>

Run following command to create a secret(s):
```bash
kubectl create secret generic fluentbit-creds \
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
  "fluentbit": {
    "username": "<username>",
    "password": "<password>"
  }
}
```

</details>

## Fluentbit Events

This chart integrates Fluent Bit as a log processor and forwarder, specifically configured to capture Kubernetes and CloudEvents from Tekton.
It relies on the KubeRocketCI's OpenSearch chart for log storage and analysis, providing a cohesive logging solution.

```plaintext
+--------+       +-------------+       +------------+       +-----------+
| Tekton +------>+ CloudEvents +------>+ Fluent Bit +------>+ OpenSearch|
+--------+       +-------------+       +------------+       +-----------+
                                             |
                                             |
                                        +----+----+
                                        | k8s     |
                                        | Events  |
                                        +---------+
```

### Key Features and Configurations:

- **Deployment Mode**: Fluent Bit is deployed as a single instance to efficiently gather events across the cluster.
- **CloudEvents Support**: Custom port configuration (8888) to receive CloudEvents from Tekton Pipelines.
- **RBAC and Access**: Automatically creates RBAC resources with access to Kubernetes events.
- **Elasticsearch Integration**: Environment variables are configured to use credentials from a secret for Elasticsearch access.
- **Monitoring**: A ServiceMonitor is configured for Prometheus scraping, with detailed metric and relabeling configurations.

### Inputs and Outputs:

- **Inputs**: Captures Kubernetes events and HTTP CloudEvents.
- **Outputs**: Configured to forward logs to an OpenSearch cluster with specific formatting and TLS settings.

For further customization and to tailor the Fluent Bit configuration to your needs, please review the `values.yaml` file.

### Calculate duration for PipelineRuns and TaskRuns

To calculate the duration of PipelineRuns and TaskRuns, you can add a scripted field in OpenSearch Dashboards.

Navigate to the **Management** section in OpenSearch Dashboards.
Go to Stack **Management** > **Index Patterns**.
Select the index pattern that contains your data (e.g., logstash-cloudevents-*).
Find and click on the **Scripted fields** tab, then click on **Add scripted field**.
Fill in the **Name** for your field, for example, **duration**.
For the **Language**, ensure that painless is selected.
Set the Script type to **number**.
In the Script field, enter the following code:

```java
long startTimeMillis = 0;
long completionTimeMillis = 0;

// Check for pipelineRun times
if (doc.containsKey('pipelineRun.status.startTime') && !doc['pipelineRun.status.startTime'].empty) {
    startTimeMillis = doc['pipelineRun.status.startTime'].value.getMillis();
}

if (doc.containsKey('pipelineRun.status.completionTime') && !doc['pipelineRun.status.completionTime'].empty) {
    completionTimeMillis = doc['pipelineRun.status.completionTime'].value.getMillis();
}

// Check for taskRun times if pipelineRun times aren't set
if (startTimeMillis == 0 && doc.containsKey('taskRun.status.startTime') && !doc['taskRun.status.startTime'].empty) {
    startTimeMillis = doc['taskRun.status.startTime'].value.getMillis();
}

if (completionTimeMillis == 0 && doc.containsKey('taskRun.status.completionTime') && !doc['taskRun.status.completionTime'].empty) {
    completionTimeMillis = doc['taskRun.status.completionTime'].value.getMillis();
}

// Calculate duration in seconds if both times are available
if (startTimeMillis > 0 && completionTimeMillis > 0) {
    return (completionTimeMillis - startTimeMillis) / 1000;
} else {
    return 0; // Return 0 or some default value if the necessary fields are missing or incomplete
}
```

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://fluent.github.io/helm-charts | fluent-bit | 0.53.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.aws | object | `{"region":"eu-central-1","roleArn":"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"}` | AWS configuration (if provider is `aws`). |
| eso.aws.region | string | `"eu-central-1"` | AWS region. |
| eso.aws.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | AWS role ARN for the ExternalSecretOperator to assume. |
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.provider | string | `"aws"` | Defines provider type. One of `aws`, `generic`, or `vault`. |
| eso.secretPath | string | `"/infra/core/addons/fluent-bit"` | Defines the path to the secret in the provider. If provider is `vault`, this is the path must be prefixed with `secret/`. |
| eso.vault | object | `{"mountPath":"core","role":"fluent-bit","server":"http://vault.vault:8200"}` | Vault configuration (if provider is `vault`). |
| eso.vault.mountPath | string | `"core"` | Mount path for the Kubernetes authentication method. |
| eso.vault.role | string | `"fluent-bit"` | Vault role for the Kubernetes authentication method. |
| eso.vault.server | string | `"http://vault.vault:8200"` | Vault server URL. |
| fluent-bit.config.filters | string | `"# Nest the logs to be under the log key\n[FILTER]\n    Name nest\n    Match http.*\n    Wildcard *\n    Nest_under log\n\n# Rewrite tag. We search for the completionTime field in the pipelineRun status and rewrite the tag\n[FILTER]\n    Name rewrite_tag\n    Match http.*\n    Rule $log['pipelineRun']['status']['completionTime'] ^(.+)$ tkn_pipelinerun true\n    Emitter_Name re_emitted_pipelinerun\n\n[FILTER]\n    Name rewrite_tag\n    Match http.*\n    Rule $log['taskRun']['status']['completionTime'] ^(.+)$ tkn_taskrun true\n    Emitter_Name re_emitted_taskrun\n\n# Drop managed fields and pipelineSpec from the logs\n# We drop the managedFields and pipelineSpec fields from the logs, since they are too big and we don't need them\n[FILTER]\n    name lua\n    match tkn_pipelinerun\n    call drop_managed_fields\n    code function drop_managed_fields(tag, timestamp, record) record[\"log\"][\"pipelineRun\"][\"metadata\"][\"managedFields\"] = nil record[\"log\"][\"pipelineRun\"][\"status\"][\"pipelineSpec\"] = nil return 1, timestamp, record end\n\n[FILTER]\n    name lua\n    match tkn_taskrun\n    call drop_managed_fields\n    code function drop_managed_fields(tag, timestamp, record) record[\"log\"][\"taskRun\"][\"metadata\"][\"managedFields\"] = nil record[\"log\"][\"taskRun\"][\"status\"][\"taskSpec\"] = nil return 1, timestamp, record end\n\n# Restore original log structure for Opensearch processing, by removing the log key\n[FILTER]\n    Name nest\n    Match tkn*\n    Operation lift\n    Nested_under log\n"` |  |
| fluent-bit.config.inputs | string | `"[INPUT]\n    Name kubernetes_events\n    # add the tag \"k8s_events\" to all events coming from this input\n    tag k8s_events\n    # ask k8s API for updates every 30 seconds\n    interval_sec 15\n    # fetch at most 250 items per requests (pagination)\n    kube_request_limit 2500\n    Storage.type filesystem\n\n# Use as the synk for the CloudEvents from Tekton Pipelines\n[INPUT]\n    name http\n    listen 0.0.0.0\n    port 8888\n    Storage.type filesystem\n"` |  |
| fluent-bit.config.outputs | string | `"[OUTPUT]\n    Name            es\n    Match           k8s_events\n    Host            opensearch-cluster-master\n    Port            9200\n    HTTP_User       ${ES_SUPERUSER_USER}\n    HTTP_Passwd     ${ES_SUPERUSER_PASSWORD}\n    Logstash_Format On\n    Logstash_Prefix logstash-events\n    Time_Key        @timestamp\n    Replace_Dots    On\n    Retry_Limit     False\n    Trace_Error     Off\n    Suppress_Type_Name On\n    tls             On\n    tls.verify      Off\n    Storage.total_limit_size 1G\n\n[OUTPUT]\n    Name            es\n    Match           tkn*\n    Host            opensearch-cluster-master\n    Port            9200\n    HTTP_User       ${ES_SUPERUSER_USER}\n    HTTP_Passwd     ${ES_SUPERUSER_PASSWORD}\n    Logstash_Format On\n    Logstash_Prefix logstash-cloudevents\n    Time_Key        @timestamp\n    Replace_Dots    On\n    Retry_Limit     False\n    Trace_Error     Off\n    Suppress_Type_Name On\n    tls             On\n    tls.verify      Off\n    Storage.total_limit_size 1G\n"` |  |
| fluent-bit.config.service | string | `"[SERVICE]\n    Daemon Off\n    Flush {{ .Values.flush }}\n    Log_Level {{ .Values.logLevel }}\n    Parsers_File /fluent-bit/etc/parsers.conf\n    Parsers_File /fluent-bit/etc/conf/custom_parsers.conf\n    HTTP_Server On\n    HTTP_Listen 0.0.0.0\n    HTTP_Port {{ .Values.metricsPort }}\n    Health_Check On\n    Storage.path /var/log/flb-storage/\n    Storage.sync normal\n    Storage.checksum off\n    Storage.backlog.mem_limit 5M\n"` |  |
| fluent-bit.env[0].name | string | `"ES_SUPERUSER_USER"` |  |
| fluent-bit.env[0].valueFrom.secretKeyRef.key | string | `"username"` |  |
| fluent-bit.env[0].valueFrom.secretKeyRef.name | string | `"fluentbit-creds"` |  |
| fluent-bit.env[1].name | string | `"ES_SUPERUSER_PASSWORD"` |  |
| fluent-bit.env[1].valueFrom.secretKeyRef.key | string | `"password"` |  |
| fluent-bit.env[1].valueFrom.secretKeyRef.name | string | `"fluentbit-creds"` |  |
| fluent-bit.extraPorts[0].containerPort | int | `8888` |  |
| fluent-bit.extraPorts[0].name | string | `"cloudevents"` |  |
| fluent-bit.extraPorts[0].port | int | `8888` |  |
| fluent-bit.extraPorts[0].protocol | string | `"TCP"` |  |
| fluent-bit.kind | string | `"Deployment"` |  |
| fluent-bit.rbac.create | bool | `true` |  |
| fluent-bit.rbac.eventsAccess | bool | `true` |  |
| fluent-bit.resources.limits.memory | string | `"128Mi"` |  |
| fluent-bit.resources.requests.cpu | string | `"100m"` |  |
| fluent-bit.resources.requests.memory | string | `"128Mi"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].interval | string | `"10s"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].metricRelabelings[0].action | string | `"replace"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].metricRelabelings[0].regex | string | `"(.*)"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].metricRelabelings[0].replacement | string | `"${1}"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].metricRelabelings[0].sourceLabels[0] | string | `"__meta_kubernetes_service_label_cluster"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].metricRelabelings[0].targetLabel | string | `"cluster"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].path | string | `"/metrics"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].port | string | `"metrics"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].relabelings[0].action | string | `"replace"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].relabelings[0].regex | string | `"^(.*)$"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].relabelings[0].replacement | string | `"$1"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].relabelings[0].separator | string | `";"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].relabelings[0].sourceLabels[0] | string | `"__meta_kubernetes_pod_node_name"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].relabelings[0].targetLabel | string | `"nodename"` |  |
| fluent-bit.serviceMonitor.additionalEndpoints[0].scrapeTimeout | string | `"10s"` |  |
| fluent-bit.serviceMonitor.enabled | bool | `true` |  |
| fluent-bit.serviceMonitor.interval | string | `"10s"` |  |
| fluent-bit.serviceMonitor.metricRelabelings[0].action | string | `"replace"` |  |
| fluent-bit.serviceMonitor.metricRelabelings[0].regex | string | `"(.*)"` |  |
| fluent-bit.serviceMonitor.metricRelabelings[0].replacement | string | `"${1}"` |  |
| fluent-bit.serviceMonitor.metricRelabelings[0].sourceLabels[0] | string | `"__meta_kubernetes_service_label_cluster"` |  |
| fluent-bit.serviceMonitor.metricRelabelings[0].targetLabel | string | `"cluster"` |  |
| fluent-bit.serviceMonitor.relabelings[0].action | string | `"replace"` |  |
| fluent-bit.serviceMonitor.relabelings[0].regex | string | `"^(.*)$"` |  |
| fluent-bit.serviceMonitor.relabelings[0].replacement | string | `"$1"` |  |
| fluent-bit.serviceMonitor.relabelings[0].separator | string | `";"` |  |
| fluent-bit.serviceMonitor.relabelings[0].sourceLabels[0] | string | `"__meta_kubernetes_pod_node_name"` |  |
| fluent-bit.serviceMonitor.relabelings[0].targetLabel | string | `"nodename"` |  |
| fluent-bit.serviceMonitor.scrapeTimeout | string | `"10s"` |  |
| fluent-bit.serviceMonitor.selector.release | string | `"kube-prometheus"` |  |
| fluent-bit.testFramework.enabled | bool | `false` |  |
