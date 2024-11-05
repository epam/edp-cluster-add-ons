{{- define "broker.name" -}}
{{- if .Values.broker.create -}}
{{- .Values.broker.name -}}
{{- else -}}
{{- .Values.existingBroker -}}
{{- end -}}
{{- end -}}
