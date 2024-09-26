# fluent-bit

![Version: 0.46.11](https://img.shields.io/badge/Version-0.46.11-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.0.7](https://img.shields.io/badge/AppVersion-3.0.7-informational?style=flat-square)

A Helm chart for Fluent Bit

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
| https://fluent.github.io/helm-charts | fluent-bit | 0.46.11 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/edp/eks/addons/fluent-bit"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| fluent-bit.config.inputs | string | `"[INPUT]\n    Name kubernetes_events\n    # add the tag \"k8s_events\" to all events coming from this input\n    tag k8s_events\n    # ask k8s API for updates every 30 seconds\n    interval_sec 15\n    # fetch at most 250 items per requests (pagination)\n    kube_request_limit 2500\n    Storage.type filesystem\n\n# Use as the synk for the CloudEvents from Tekton Pipelines\n[INPUT]\n    name http\n    listen 0.0.0.0\n    port 8888\n    Storage.type filesystem\n"` |  |
| fluent-bit.config.outputs | string | `"[OUTPUT]\n    Name            es\n    Match           k8s_events\n    Host            opensearch-cluster-master\n    Port            9200\n    HTTP_User       ${ES_SUPERUSER_USER}\n    HTTP_Passwd     ${ES_SUPERUSER_PASSWORD}\n    Logstash_Format On\n    Logstash_Prefix logstash-events\n    Time_Key        @timestamp\n    Replace_Dots    On\n    Retry_Limit     False\n    Trace_Error     Off\n    Suppress_Type_Name On\n    tls             On\n    tls.verify      Off\n    Storage.total_limit_size 1G\n\n[OUTPUT]\n    Name            es\n    Match           http.*\n    Host            opensearch-cluster-master\n    Port            9200\n    HTTP_User       ${ES_SUPERUSER_USER}\n    HTTP_Passwd     ${ES_SUPERUSER_PASSWORD}\n    Logstash_Format On\n    Logstash_Prefix logstash-cloudevents\n    Time_Key        @timestamp\n    Replace_Dots    On\n    Retry_Limit     False\n    Trace_Error     Off\n    Suppress_Type_Name On\n    tls             On\n    tls.verify      Off\n    Storage.total_limit_size 1G\n"` |  |
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
