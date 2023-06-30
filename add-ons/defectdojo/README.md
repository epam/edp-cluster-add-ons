# defectdojo

![Version: 1.6.73](https://img.shields.io/badge/Version-1.6.73-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.23.3](https://img.shields.io/badge/AppVersion-2.23.3-informational?style=flat-square)

A Helm chart for DefectDojo Install

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://raw.githubusercontent.com/DefectDojo/django-DefectDojo/helm-charts | defectdojo | 1.6.73 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| defectdojo.alternativeHosts[0] | string | `"defectdojo-django.defectdojo"` |  |
| defectdojo.django.ingress.activateTLS | bool | `false` |  |
| defectdojo.django.ingress.enabled | bool | `true` |  |
| defectdojo.django.mediaPersistentVolume.persistentVolumeClaim.size | string | `"2Gi"` |  |
| defectdojo.django.mediaPersistentVolume.persistentVolumeClaim.storageClassName | string | `"ebs-sc"` |  |
| defectdojo.django.uwsgi.livenessProbe.initialDelaySeconds | int | `20` |  |
| defectdojo.fullnameOverride | string | `"defectdojo"` |  |
| defectdojo.host | string | `"defectdojo.example.com"` |  |
| defectdojo.initializer.run | bool | `true` |  |
| defectdojo.postgresql.primary.persistence.size | string | `"2Gi"` |  |
| defectdojo.postgresql.primary.persistence.storageClass | string | `"ebs-sc"` |  |
| defectdojo.rabbitmq.persistence.size | string | `"2Gi"` |  |
| defectdojo.rabbitmq.persistence.storageClass | string | `"ebs-sc"` |  |
| defectdojo.site_url | string | `"https://defectdojo.example.com"` |  |
| defectdojo.tag | string | `"2.17.0"` |  |

