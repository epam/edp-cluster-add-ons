{{- define "broker.name" -}}
{{- if .Values.extensionsOIDC.broker.create -}}
{{- .Values.extensionsOIDC.broker.name -}}
{{- else -}}
{{- .Values.extensionsOIDC.existingBroker -}}
{{- end -}}
{{- end -}}
