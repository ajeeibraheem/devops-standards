{{- define "common-chart.name" -}}
{{ .Chart.Name }}
{{- end }}

{{- define "common-chart.fullname" -}}
{{ include "common-chart.name" . }}-{{ .Release.Name }}
{{- end }}

{{- define "common-chart.labels" -}}
app.kubernetes.io/name: {{ include "common-chart.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}
