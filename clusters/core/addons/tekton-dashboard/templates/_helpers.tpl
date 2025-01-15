{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "tekton-dashboard.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}


{{/*
Expand the name of the chart.
*/}}
{{- define "tekton-dashboard.name" -}}
{{- default .Chart.Name .Values.dashboard.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "tekton-dashboard.labels" -}}
helm.sh/chart: {{ include "tekton-dashboard.chart" . }}
{{ include "tekton-dashboard.selectorLabels" . }}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "tekton-dashboard.selectorLabels" -}}
app.kubernetes.io/name: {{ include "tekton-dashboard.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Define tekton-dashboard URL
*/}}
{{- define "tekton-dashboard.url" -}}
{{- printf "tekton-%s.%s" .Release.Namespace .Values.global.dnsWildCard  }}
{{- end }}
