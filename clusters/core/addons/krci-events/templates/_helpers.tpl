{{/*
Sprig template (rendered by Argo Events, not Helm) resolving the notification timestamp:
Ce-Time header when present, otherwise current time. Missing headers must never abort a
trigger (dataKey has no fallback semantics — always use templates for optional fields).
*/}}
{{- define "krci-events.tpl.timestamp" -}}
{{ `{{- $t := "" -}}{{- with .Input.header }}{{ with index . "Ce-Time" }}{{ $t = index . 0 }}{{ end }}{{ end -}}{{- if eq $t "" }}{{ $t = now | date "2006-01-02T15:04:05Z" }}{{ end -}}{{ $t }}` }}
{{- end }}

{{/*
Sprig template resolving the Tekton pipelineUrl link contract:
spec.params.pipelineUrl (explicit override) -> status.pipelineSpec.params[pipelineUrl].default
(pipelines-library convention) -> fallback URL (.fallback). The $(context.pipelineRun.*)
placeholders are substituted from the event's own metadata.
*/}}
{{- define "krci-events.tpl.pipelineUrl" -}}
{{ printf `{{- $pr := .Input.body.pipelineRun -}}{{- $url := "" -}}{{- with $pr.spec }}{{ range .params }}{{ if eq .name "pipelineUrl" }}{{ $url = .value }}{{ end }}{{ end }}{{ end -}}{{- if eq $url "" }}{{ with $pr.status }}{{ with .pipelineSpec }}{{ range .params }}{{ if eq .name "pipelineUrl" }}{{ $url = .default }}{{ end }}{{ end }}{{ end }}{{ end }}{{ end -}}{{- if eq $url "" }}{{ $url = %q }}{{ end -}}{{- $url | replace "$(context.pipelineRun.namespace)" $pr.metadata.namespace | replace "$(context.pipelineRun.name)" $pr.metadata.name -}}` .fallback }}
{{- end }}

{{/*
Trigger payload for kind=portal: the canonical KRCI notification contract.
Context: routeName, route.
*/}}
{{- define "krci-events.payload.portal" -}}
{{- $n := .routeName }}{{- $r := .route.notification }}
- src:
    dependencyName: {{ $n }}
    dataTemplate: {{ $r.idTemplate | quote }}
  dest: id
- src:
    dependencyName: {{ $n }}
    value: {{ $r.type | quote }}
  dest: type
- src:
    dependencyName: {{ $n }}
    value: {{ $r.severity | quote }}
  dest: severity
- src:
    dependencyName: {{ $n }}
    dataTemplate: {{ $r.titleTemplate | quote }}
  dest: title
- src:
    dependencyName: {{ $n }}
    dataTemplate: {{ $r.bodyTemplate | quote }}
  dest: body
- src:
    dependencyName: {{ $n }}
    dataTemplate: {{ $r.namespaceTemplate | quote }}
  dest: namespace
- src:
    dependencyName: {{ $n }}
    dataTemplate: {{ $r.linkTemplate | quote }}
  dest: link
- src:
    dependencyName: {{ $n }}
    dataTemplate: {{ include "krci-events.tpl.timestamp" . | quote }}
  dest: timestamp
{{- end }}

{{/*
Trigger payload for kind=msteams-card: message envelope + Adaptive Card 1.4 with an
attention-colored title, a FactSet from route facts, and an Action.OpenUrl button.
Context: routeName, route, dest.
*/}}
{{- define "krci-events.payload.msteams-card" -}}
{{- $n := .routeName }}{{- $r := .route.notification }}{{- $d := .dest }}
{{- $color := get (dict "error" "attention" "warning" "warning" "success" "good" "info" "default") ($r.severity | default "info") | default "default" }}
- src:
    dependencyName: {{ $n }}
    value: message
  dest: type
- src:
    dependencyName: {{ $n }}
    value: application/vnd.microsoft.card.adaptive
  dest: attachments.0.contentType
- src:
    dependencyName: {{ $n }}
    value: AdaptiveCard
  dest: attachments.0.content.type
- src:
    dependencyName: {{ $n }}
    value: "1.4"
  dest: attachments.0.content.version
- src:
    dependencyName: {{ $n }}
    value: http://adaptivecards.io/schemas/adaptive-card.json
  dest: attachments.0.content.$schema
- src:
    dependencyName: {{ $n }}
    value: Full
  dest: attachments.0.content.msteams.width
- src:
    dependencyName: {{ $n }}
    value: TextBlock
  dest: attachments.0.content.body.0.type
- src:
    dependencyName: {{ $n }}
    dataTemplate: {{ $r.titleTemplate | quote }}
  dest: attachments.0.content.body.0.text
- src:
    dependencyName: {{ $n }}
    value: bolder
  dest: attachments.0.content.body.0.weight
- src:
    dependencyName: {{ $n }}
    value: large
  dest: attachments.0.content.body.0.size
- src:
    dependencyName: {{ $n }}
    value: {{ $color }}
  dest: attachments.0.content.body.0.color
- src:
    dependencyName: {{ $n }}
    value: FactSet
  dest: attachments.0.content.body.1.type
{{- range $i, $f := $r.facts }}
- src:
    dependencyName: {{ $n }}
    value: {{ $f.title | quote }}
  dest: attachments.0.content.body.1.facts.{{ $i }}.title
- src:
    dependencyName: {{ $n }}
    dataTemplate: {{ $f.valueTemplate | quote }}
  dest: attachments.0.content.body.1.facts.{{ $i }}.value
{{- end }}
- src:
    dependencyName: {{ $n }}
    value: Action.OpenUrl
  dest: attachments.0.content.actions.0.type
- src:
    dependencyName: {{ $n }}
    value: {{ $r.buttonTitle | default "Open" | quote }}
  dest: attachments.0.content.actions.0.title
- src:
    dependencyName: {{ $n }}
    {{- if eq ($r.buttonLinkKind | default "template") "pipelineUrl" }}
    dataTemplate: {{ include "krci-events.tpl.pipelineUrl" (dict "fallback" $d.linkFallbackUrl) | quote }}
    {{- else }}
    dataTemplate: {{ $r.buttonLinkTemplate | default $d.linkFallbackUrl | quote }}
    {{- end }}
  dest: attachments.0.content.actions.0.url
{{- end }}
