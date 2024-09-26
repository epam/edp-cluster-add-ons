# keycloak-postgresql

![Version: 0.1.1](https://img.shields.io/badge/Version-0.1.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0](https://img.shields.io/badge/AppVersion-1.0-informational?style=flat-square)

A Helm chart for Keycloak Postgresql

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | postgresql | 12.5.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/edp/eks/addons/postgresql"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore-kk-postgress"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| postgresql.fullnameOverride | string | `"postgresql"` |  |
| postgresql.global.postgresql.auth.database | string | `"keycloak"` |  |
| postgresql.global.postgresql.auth.existingSecret | string | `"keycloak-postgresql"` |  |
| postgresql.global.postgresql.auth.username | string | `"admin"` |  |
| postgresql.image.tag | string | `"15.3.0-debian-11-r0"` |  |
| postgresql.nameOverride | string | `"postgresql"` |  |
| postgresql.primary.persistence.enabled | bool | `true` |  |
| postgresql.primary.persistence.size | string | `"3Gi"` |  |
| postgresql.primary.persistence.storageClass | string | `"ebs-sc"` |  |
| postgresql.readReplicas.replicaCount | int | `1` |  |

