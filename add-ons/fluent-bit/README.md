# fluent-bit

![Version: 0.46.11](https://img.shields.io/badge/Version-0.46.11-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.0.7](https://img.shields.io/badge/AppVersion-3.0.7-informational?style=flat-square)

A Helm chart for Fluent Bit

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://fluent.github.io/helm-charts | fluent-bit | 0.46.11 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.secretName | string | `"/edp/eks/addons/fluent-bit"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| fluent-bit.config.customParsers | string | `"[PARSER]\n    Name docker_no_time\n    Format json\n    Time_Keep Off\n    Time_Key time\n    Time_Format %Y-%m-%dT%H:%M:%S.%L\n\n[PARSER]\n    Name        java_multiline\n    Format      regex\n    Regex       /^(?<time>\\d{4}-\\d{1,2}-\\d{1,2} \\d{1,2}:\\d{1,2}:\\d{1,2}) (?<level>[^\\s]+)(?<message>.*)/\n    Time_Key    time\n    Time_Format %Y-%m-%d %H:%M:%S\n"` |  |
| fluent-bit.config.outputs | string | `"[OUTPUT]\n    Name            es\n    Match           kube.*\n    Host            opensearch-cluster-master\n    Port            9200\n    HTTP_User       ${ES_SUPERUSER_USER}\n    HTTP_Passwd     ${ES_SUPERUSER_PASSWORD}\n    Logstash_Format On\n    Logstash_Prefix kube-fluent-bit\n    Time_Key        @timestamp\n    Replace_Dots    On\n    Retry_Limit     False\n    Trace_Error     Off\n    Suppress_Type_Name On\n    tls             On\n    tls.verify      Off\n"` |  |
| fluent-bit.env[0].name | string | `"ES_SUPERUSER_USER"` |  |
| fluent-bit.env[0].valueFrom.secretKeyRef.key | string | `"username"` |  |
| fluent-bit.env[0].valueFrom.secretKeyRef.name | string | `"fluentbit-creds"` |  |
| fluent-bit.env[1].name | string | `"ES_SUPERUSER_PASSWORD"` |  |
| fluent-bit.env[1].valueFrom.secretKeyRef.key | string | `"password"` |  |
| fluent-bit.env[1].valueFrom.secretKeyRef.name | string | `"fluentbit-creds"` |  |
| fluent-bit.testFramework.enabled | bool | `false` |  |

