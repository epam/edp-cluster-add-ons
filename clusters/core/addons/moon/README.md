# moon

![Version: 2.7.7](https://img.shields.io/badge/Version-2.7.7-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.7.7](https://img.shields.io/badge/AppVersion-2.7.7-informational?style=flat-square)

A Helm chart for Moon

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.aerokube.com | moon2 | 2.7.7 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| moon2.deployment.replicas | int | `1` |  |
| moon2.ingress.enabled | bool | `true` |  |
| moon2.ingress.host | string | `"moon.example.com"` |  |

