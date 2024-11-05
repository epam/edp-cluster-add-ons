# krakend

![Version: 0.1.35](https://img.shields.io/badge/Version-0.1.35-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.7.2](https://img.shields.io/badge/AppVersion-2.7.2-informational?style=flat-square)

A Helm chart for deploying krakend.io in Kubernetes provided
and maintained by your friends at Equinix Metal

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://helm.equinixmetal.com | krakend | 0.1.35 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eso.enabled | bool | `true` | Install components of the ESO. |
| eso.generic.secretStore.providerConfig | object | `{}` | Defines SecretStore provider configuration. |
| eso.roleArn | string | `"arn:aws:iam::012345678910:role/AWSIRSA_Shared_ExternalSecretOperatorAccess"` | Role ARN for the ExternalSecretOperator to assume. |
| eso.secretName | string | `"/infra/core/addons/krakend"` | Value name in AWS ParameterStore, AWS SecretsManager or other Secret Store. |
| eso.secretStoreName | string | `"aws-parameterstore"` | Defines Secret Store name. |
| eso.type | string | `"aws"` | Defines provider type. One of `aws` or `generic`. |
| krakend.ingress.annotations."nginx.ingress.kubernetes.io/cors-allow-headers" | string | `"DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Authorization"` |  |
| krakend.ingress.annotations."nginx.ingress.kubernetes.io/cors-allow-methods" | string | `"OPTIONS, GET"` |  |
| krakend.ingress.annotations."nginx.ingress.kubernetes.io/cors-allow-origin" | string | `"*"` |  |
| krakend.ingress.annotations."nginx.ingress.kubernetes.io/enable-cors" | string | `"true"` |  |
| krakend.ingress.enabled | bool | `true` |  |
| krakend.ingress.hosts[0].host | string | `"api.example.com"` |  |
| krakend.ingress.hosts[0].paths[0].path | string | `"/"` |  |
| krakend.ingress.hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| krakend.krakend.config | string | `"{\n  \"$schema\": \"https://www.krakend.io/schema/krakend.json\",\n  \"version\": 3,\n  \"name\": \"KrakenD - API Gateway\",\n  \"timeout\": \"3000ms\",\n  \"cache_ttl\": \"300s\",\n  \"output_encoding\": \"json\",\n  \"extra_config\": {\n    \"router\": {\n      \"logger_skip_paths\": [\n        \"/__health\"\n      ]\n    },\n    \"auth/jwk-client\": {\n        \"@comment\": \"Enable a JWK shared cache amongst all endpoints of 60 minutes\",\n        \"shared_cache_duration\": 3600\n    }\n  },\n  \"endpoints\": [\n    {\n      \"endpoint\": \"/widgets/sonarqube/measures/component\",\n      \"method\": \"GET\",\n      \"output_encoding\": \"json\",\n      \"input_query_strings\": [\n        \"component\",\n        \"metricKeys\"\n      ],\n      \"extra_config\": {\n        \"auth/validator\": {\n          \"alg\": \"RS256\",\n          \"cache_duration\": 3600,\n          \"cache\": true,\n          \"disable_jwk_security\": false,\n          \"jwk_url\": \"{{ env \"JWK_URL\" }}\"\n        }\n      },\n      \"backend\": [\n        {\n          \"url_pattern\": \"/api/measures/component\",\n          \"encoding\": \"json\",\n          \"sd\": \"static\",\n          \"method\": \"GET\",\n          \"host\": [\n            \"{{ env \"SONARQUBE_URL\" }}\"\n          ],\n          \"extra_config\": {\n            \"qos/http-cache\": {},\n            \"modifier/martian\": {\n              \"header.Append\": {\n                \"scope\": [\n                  \"request\"\n                ],\n                \"name\": \"Authorization\",\n                \"value\": \"Basic {{ env \"SONARQUBE_TOKEN\" }}\"\n              }\n            }\n          }\n        }\n      ]\n    },\n    {\n      \"endpoint\": \"/widgets/deptrack/project\",\n      \"method\": \"GET\",\n      \"output_encoding\": \"json\",\n      \"input_query_strings\": [\n        \"name\"\n      ],\n      \"extra_config\": {\n        \"auth/validator\": {\n          \"alg\": \"RS256\",\n          \"cache_duration\": 3600,\n          \"cache\": true,\n          \"disable_jwk_security\": false,\n          \"jwk_url\": \"{{ env \"JWK_URL\" }}\"\n        }\n      },\n      \"backend\": [\n        {\n          \"url_pattern\": \"/api/v1/project\",\n          \"encoding\": \"json\",\n          \"sd\": \"static\",\n          \"method\": \"GET\",\n          \"host\": [\n            \"{{ env \"DEPTRACK_URL\" }}\"\n          ],\n          \"is_collection\": true,\n          \"extra_config\": {\n            \"qos/http-cache\": {},\n            \"modifier/martian\": {\n              \"header.Append\": {\n                \"scope\": [\n                  \"request\"\n                ],\n                \"name\": \"X-Api-Key\",\n                \"value\": \"{{ env \"DEPTRACK_TOKEN\" }}\"\n              }\n            }\n          }\n        }\n      ]\n    },\n    {\n      \"endpoint\": \"/widgets/deptrack/metrics/project/{uuid}/current\",\n      \"method\": \"GET\",\n      \"output_encoding\": \"json\",\n      \"input_query_strings\": [\n        \"name\"\n      ],\n      \"extra_config\": {\n        \"auth/validator\": {\n          \"alg\": \"RS256\",\n          \"cache_duration\": 3600,\n          \"cache\": true,\n          \"disable_jwk_security\": false,\n          \"jwk_url\": \"{{ env \"JWK_URL\" }}\"\n        }\n      },\n      \"backend\": [\n        {\n          \"url_pattern\": \"/api/v1/metrics/project/{uuid}/current\",\n          \"encoding\": \"json\",\n          \"sd\": \"static\",\n          \"method\": \"GET\",\n          \"host\": [\n            \"{{ env \"DEPTRACK_URL\" }}\"\n          ],\n          \"is_collection\": false,\n          \"extra_config\": {\n            \"qos/http-cache\": {},\n            \"modifier/martian\": {\n              \"header.Append\": {\n                \"scope\": [\n                  \"request\"\n                ],\n                \"name\": \"X-Api-Key\",\n                \"value\": \"{{ env \"DEPTRACK_TOKEN\" }}\"\n              }\n            }\n          }\n        }\n      ]\n    }\n  ]\n}\n"` |  |
| krakend.krakend.partials | string | `nil` |  |
| krakend.krakend.settings | string | `nil` |  |

