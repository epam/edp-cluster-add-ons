{{/*
Labels every ServiceMonitor carries. `additionalLabels` must include the Prometheus release
label or the operator will not select the monitor.
*/}}
{{- define "tekton-monitoring.smLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- with .Values.serviceMonitor.additionalLabels }}
{{ toYaml . }}
{{- end }}
{{- end -}}
