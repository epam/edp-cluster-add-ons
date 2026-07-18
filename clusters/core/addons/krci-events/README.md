# krci-events

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

KubeRocketCI event wiring on top of the argo-events add-on — EventSources ingesting platform CloudEvents (Tekton) and Sensors routing them to consumers (KRCI portal, chat webhooks)

This add-on carries the KubeRocketCI-specific wiring of the notification bus: the
`tekton-events` webhook EventSource (the target for Tekton's CloudEvents sink) and the
`notify-portal` Sensor forwarding failed-PipelineRun events to the KRCI portal. It requires
the `argo-events` add-on (engine: controller, CRDs, EventBus) deployed into the same
namespace.

Integration steps are documented at [docs.kuberocketci.io](https://docs.kuberocketci.io).

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| destinations.msteams.enabled | bool | `false` | Deploy this destination's Sensor |
| destinations.msteams.kind | string | `"msteams-card"` | Payload kind |
| destinations.msteams.linkFallbackUrl | string | `"https://docs.kuberocketci.io"` | Card button URL when the route yields no link (e.g. no `pipelineUrl` param); set to the portal base URL |
| destinations.msteams.retryStrategy.duration | string | `"10s"` | Backoff duration between attempts |
| destinations.msteams.retryStrategy.steps | int | `5` | Number of delivery attempts |
| destinations.msteams.routes | list | `["build-failed","deploy-failed"]` | Event types delivered to this destination |
| destinations.msteams.webhookUrl | string | `""` | Power Automate Workflows webhook URL. The URL embeds its own credential (`sig` query parameter) and the Argo Events HTTP trigger cannot reference a Secret for the URL field — supply it from a private values source (e.g. SOPS-encrypted overlay) or replace it directly in the deployed Sensor (`spec.triggers[*].template.http.url`) |
| destinations.portal.enabled | bool | `false` | Deploy this destination's Sensor |
| destinations.portal.kind | string | `"portal"` | Payload kind: portal (KRCI notification contract) | msteams-card (Adaptive Card via Power Automate Workflows webhook) |
| destinations.portal.retryStrategy.duration | string | `"10s"` | Backoff duration between attempts |
| destinations.portal.retryStrategy.steps | int | `5` | Number of delivery attempts |
| destinations.portal.routes | list | `["build-failed","deploy-failed"]` | Event types delivered to this destination |
| destinations.portal.tokenSecret.key | string | `"token"` | Key in the Secret holding the token |
| destinations.portal.tokenSecret.name | string | `"portal-events-token"` | Secret (in this add-on's namespace) holding the token shared with the portal |
| destinations.portal.url | string | `"http://krci-portal.krci.svc:3000/rest/v1/internal/events"` | In-cluster URL of the portal internal events endpoint |
| eventTypes.build-failed.ceType | string | `"dev.tekton.event.pipelinerun.failed.v1"` | CloudEvents type (Ce-Type header) this route matches |
| eventTypes.build-failed.matchData | list | `[{"path":"body.pipelineRun.metadata.labels.app\\.edp\\.epam\\.com/pipelinetype","value":"build"}]` | Additional gjson data-filter matches on the event payload (path syntax: gjson, dots in keys escaped with \) |
| eventTypes.build-failed.notification.bodyTemplate | string | `"{{- $l := .Input.body.pipelineRun.metadata.labels -}}Build pipeline for codebase {{ if $l }}{{ index $l \"app.edp.epam.com/codebase\" | default \"-\" }}{{ else }}-{{ end }} (branch {{ if $l }}{{ index $l \"app.edp.epam.com/codebasebranch\" | default \"-\" }}{{ else }}-{{ end }}) failed in namespace {{ .Input.body.pipelineRun.metadata.namespace }}"` | Body text template (portal notification body) |
| eventTypes.build-failed.notification.buttonLinkKind | string | `"pipelineUrl"` | Card button link source: pipelineUrl (resolve the Tekton pipelineUrl param convention) | template (use buttonLinkTemplate) |
| eventTypes.build-failed.notification.buttonTitle | string | `"Open PipelineRun"` | Card button title |
| eventTypes.build-failed.notification.facts | list | `[{"title":"PipelineRun","valueTemplate":"{{ .Input.body.pipelineRun.metadata.name }}"},{"title":"Namespace","valueTemplate":"{{ .Input.body.pipelineRun.metadata.namespace }}"},{"title":"Codebase","valueTemplate":"{{- $l := .Input.body.pipelineRun.metadata.labels -}}{{- if $l }}{{ index $l \"app.edp.epam.com/codebase\" | default \"-\" }}{{- else }}-{{ end -}}"},{"title":"Branch","valueTemplate":"{{- $l := .Input.body.pipelineRun.metadata.labels -}}{{- if $l }}{{ index $l \"app.edp.epam.com/codebasebranch\" | default \"-\" }}{{- else }}-{{ end -}}"}]` | Card FactSet rows: title + Sprig value template |
| eventTypes.build-failed.notification.idTemplate | string | `"{{ .Input.body.pipelineRun.metadata.uid }}"` | Idempotency key template (portal dedup) |
| eventTypes.build-failed.notification.linkTemplate | string | `"/c/core/cicd/pipelineruns/{{ .Input.body.pipelineRun.metadata.namespace }}/{{ .Input.body.pipelineRun.metadata.name }}"` | Portal in-app link template (portal-relative path) |
| eventTypes.build-failed.notification.namespaceTemplate | string | `"{{ .Input.body.pipelineRun.metadata.namespace }}"` | Namespace template |
| eventTypes.build-failed.notification.severity | string | `"error"` | Severity: info | success | warning | error (drives portal toast variant and card color) |
| eventTypes.build-failed.notification.titleTemplate | string | `"Build failed: {{ .Input.body.pipelineRun.metadata.name }}"` | Title template |
| eventTypes.build-failed.notification.type | string | `"build.failed"` | Notification `type` (portal taxonomy) |
| eventTypes.build-failed.source.eventName | string | `"tekton"` | Event (endpoint) name within the EventSource |
| eventTypes.build-failed.source.eventSourceName | string | `"tekton-events"` | EventSource name the route consumes from |
| eventTypes.deploy-failed.ceType | string | `"dev.tekton.event.pipelinerun.failed.v1"` |  |
| eventTypes.deploy-failed.matchData[0].path | string | `"body.pipelineRun.metadata.labels.app\\.edp\\.epam\\.com/pipelinetype"` |  |
| eventTypes.deploy-failed.matchData[0].value | string | `"deploy"` |  |
| eventTypes.deploy-failed.notification.bodyTemplate | string | `"{{- $l := .Input.body.pipelineRun.metadata.labels -}}Deployment {{ if $l }}{{ index $l \"app.edp.epam.com/cdpipeline\" | default \"-\" }}{{ else }}-{{ end }} (env {{ if $l }}{{ index $l \"app.edp.epam.com/cdstage\" | default \"-\" }}{{ else }}-{{ end }}) failed in namespace {{ .Input.body.pipelineRun.metadata.namespace }}"` |  |
| eventTypes.deploy-failed.notification.buttonLinkKind | string | `"pipelineUrl"` |  |
| eventTypes.deploy-failed.notification.buttonTitle | string | `"Open PipelineRun"` |  |
| eventTypes.deploy-failed.notification.facts[0].title | string | `"PipelineRun"` |  |
| eventTypes.deploy-failed.notification.facts[0].valueTemplate | string | `"{{ .Input.body.pipelineRun.metadata.name }}"` |  |
| eventTypes.deploy-failed.notification.facts[1].title | string | `"Namespace"` |  |
| eventTypes.deploy-failed.notification.facts[1].valueTemplate | string | `"{{ .Input.body.pipelineRun.metadata.namespace }}"` |  |
| eventTypes.deploy-failed.notification.facts[2].title | string | `"Deployment"` |  |
| eventTypes.deploy-failed.notification.facts[2].valueTemplate | string | `"{{- $l := .Input.body.pipelineRun.metadata.labels -}}{{- if $l }}{{ index $l \"app.edp.epam.com/cdpipeline\" | default \"-\" }}{{- else }}-{{ end -}}"` |  |
| eventTypes.deploy-failed.notification.facts[3].title | string | `"Env"` |  |
| eventTypes.deploy-failed.notification.facts[3].valueTemplate | string | `"{{- $l := .Input.body.pipelineRun.metadata.labels -}}{{- if $l }}{{ index $l \"app.edp.epam.com/cdstage\" | default \"-\" }}{{- else }}-{{ end -}}"` |  |
| eventTypes.deploy-failed.notification.idTemplate | string | `"{{ .Input.body.pipelineRun.metadata.uid }}"` |  |
| eventTypes.deploy-failed.notification.linkTemplate | string | `"/c/core/cicd/pipelineruns/{{ .Input.body.pipelineRun.metadata.namespace }}/{{ .Input.body.pipelineRun.metadata.name }}"` |  |
| eventTypes.deploy-failed.notification.namespaceTemplate | string | `"{{ .Input.body.pipelineRun.metadata.namespace }}"` |  |
| eventTypes.deploy-failed.notification.severity | string | `"error"` |  |
| eventTypes.deploy-failed.notification.titleTemplate | string | `"Deploy failed: {{ .Input.body.pipelineRun.metadata.name }}"` |  |
| eventTypes.deploy-failed.notification.type | string | `"deploy.failed"` |  |
| eventTypes.deploy-failed.source.eventName | string | `"tekton"` |  |
| eventTypes.deploy-failed.source.eventSourceName | string | `"tekton-events"` |  |
| monitoring.podMonitor.enabled | bool | `false` | Create PodMonitors scraping EventSource and Sensor pods (requires prometheus-operator) |
| monitoring.podMonitor.interval | string | `"30s"` | Scrape interval |
| tektonEventSource.enabled | bool | `true` | Deploy the webhook EventSource receiving Tekton CloudEvents (the target of the Tekton `config-events` sink) |
| tektonEventSource.endpoint | string | `"/tekton"` | HTTP path of the webhook endpoint |
| tektonEventSource.port | int | `12000` | Service/container port of the webhook endpoint |
