# edp-cluster-add-ons

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

EDP Cluster Addons that extend the Kubernetes Cluster Functionality

**Homepage:** <https://epam.github.io/edp-install/>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| epmd-edp | <SupportEPMD-EDP@epam.com> | <https://solutionshub.epam.com/solution/epam-delivery-platform> |
| sergk |  | <https://github.com/SergK> |

## Source Code

* <https://github.com/epam/edp-cluster-add-ons>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| argocd | object | `{"createNamespace":false,"enable":false}` | ArgoCD Deployment |
| argocd.createNamespace | bool | `false` | whether to create the namespace or not |
| awsEfsCsiDriver | object | `{"enable":true}` | AWS EFS CSI Driver |
| certmanager | object | `{"createNamespace":true,"enable":true}` | Cert Manager |
| certmanager.createNamespace | bool | `true` | whether to create the namespace or not |
| defectdojo | object | `{"createNamespace":true,"enable":true}` | DefectDojo |
| defectdojo.createNamespace | bool | `true` | whether to create the namespace or not |
| dependencyTrack.createNamespace | bool | `true` |  |
| dependencyTrack.enable | bool | `true` |  |
| edp.createNamespace | bool | `true` |  |
| edp.enable | bool | `true` |  |
| extensionsOIDC.createNamespace | bool | `true` |  |
| extensionsOIDC.enable | bool | `true` |  |
| externalSecrets.createNamespace | bool | `true` |  |
| externalSecrets.enable | bool | `true` |  |
| fluentbit.createNamespace | bool | `false` |  |
| fluentbit.enable | bool | `false` |  |
| harbor.createNamespace | bool | `true` |  |
| harbor.enable | bool | `true` |  |
| harborHA.createNamespace | bool | `true` |  |
| harborHA.enable | bool | `true` |  |
| harborHAOKD.createNamespace | bool | `true` |  |
| harborHAOKD.enable | bool | `false` |  |
| ingressNginx.createNamespace | bool | `true` |  |
| ingressNginx.enable | bool | `true` |  |
| jaegerOperator.createNamespace | bool | `true` |  |
| jaegerOperator.enable | bool | `true` |  |
| keycloak.createNamespace | bool | `true` |  |
| keycloak.enable | bool | `true` |  |
| keycloakPostgresql.createNamespace | bool | `false` |  |
| keycloakPostgresql.enable | bool | `false` |  |
| minioOperator.createNamespace | bool | `true` |  |
| minioOperator.enable | bool | `true` |  |
| nexus.createNamespace | bool | `true` |  |
| nexus.enable | bool | `true` |  |
| opensearch.createNamespace | bool | `true` |  |
| opensearch.enable | bool | `true` |  |
| opentelemetryOperator.createNamespace | bool | `true` |  |
| opentelemetryOperator.enable | bool | `true` |  |
| postgresOperator.createNamespace | bool | `true` |  |
| postgresOperator.enable | bool | `true` |  |
| prometheusOperator.createNamespace | bool | `true` |  |
| prometheusOperator.enable | bool | `true` |  |
| redisOperator.createNamespace | bool | `true` |  |
| redisOperator.enable | bool | `true` |  |
| sonarqube.createNamespace | bool | `true` |  |
| sonarqube.enable | bool | `true` |  |
| storageClass.enable | bool | `true` |  |
| tekton.createNamespace | bool | `true` |  |
| tekton.enable | bool | `true` |  |
| vault.createNamespace | bool | `true` |  |
| vault.enable | bool | `true` |  |

