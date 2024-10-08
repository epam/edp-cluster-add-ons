<a name="unreleased"></a>
## [Unreleased]

### Features
- Provision yum repositories in Nexus Repository Manager ([#125](https://github.com/epam/edp-cluster-add-ons/issues/125))
- Add support for AWX installation via AWX Operator ([#122](https://github.com/epam/edp-cluster-add-ons/issues/122))
- Implement SAML authentication for report-portal ([#120](https://github.com/epam/edp-cluster-add-ons/issues/120))
- Update OpenTelemetry Operator Helm Chart to Latest Version ([#97](https://github.com/epam/edp-cluster-add-ons/issues/97))
- Add to nexus-operator script for manage realms([#66](https://github.com/epam/edp-cluster-add-ons/issues/66))
- Add to nexus-operator script for manage tasks([#67](https://github.com/epam/edp-cluster-add-ons/issues/67))
- Add V2 add-ons approach with Argo CD ApplicationSet ([#56](https://github.com/epam/edp-cluster-add-ons/issues/56))
- Make possible deploy keycloak with pgo ([#46](https://github.com/epam/edp-cluster-add-ons/issues/46))
- Add branch plugin into sonar application ([#40](https://github.com/epam/edp-cluster-add-ons/issues/40))
- Install Argo CD ApplicationSet controller ([#37](https://github.com/epam/edp-cluster-add-ons/issues/37))
- Make it possible to deploy cache as shared component ([#74](https://github.com/epam/edp-cluster-add-ons/issues/74))
- Add Capsule templates to deploy EDP with Capsule isolation ([#31](https://github.com/epam/edp-cluster-add-ons/issues/31))
- Enable CORS for SonarQube Ingress ([#29](https://github.com/epam/edp-cluster-add-ons/issues/29))
- Add capsule ([#16](https://github.com/epam/edp-cluster-add-ons/issues/16))
- Install tekton supply chains as a part of tekton ecosystem ([#14](https://github.com/epam/edp-cluster-add-ons/issues/14))
- Add script for create projects and retention policy ([#9](https://github.com/epam/edp-cluster-add-ons/issues/9))
- Add sonar-operator to addons ([#3](https://github.com/epam/edp-cluster-add-ons/issues/3))
- Align values name from camel case to lower case ([#3](https://github.com/epam/edp-cluster-add-ons/issues/3))
- Add Vault template for openshift cluster ([#30](https://github.com/epam/edp-cluster-add-ons/issues/30))
- Add Vault with auto-unseal using AWS KMS ([#30](https://github.com/epam/edp-cluster-add-ons/issues/30))
- Add jaeger-operator, opentelementry-operator and aws-efs-csi-driver ([#1](https://github.com/epam/edp-cluster-add-ons/issues/1))

### Bug Fixes
- Fix ascii art diagram for fluentbit config for events ([#108](https://github.com/epam/edp-cluster-add-ons/issues/108))
- Align Report-portal psql secret name pattern ([#79](https://github.com/epam/edp-cluster-add-ons/issues/79))
- Enable uniq name for nexus eso objects ([#61](https://github.com/epam/edp-cluster-add-ons/issues/61))
- Align oidc settings into add-ons repo ([#65](https://github.com/epam/edp-cluster-add-ons/issues/65))
- Add Argo CD RBAC for applicationset ([#61](https://github.com/epam/edp-cluster-add-ons/issues/61))
- Align nexus ci secret name pattern ([#53](https://github.com/epam/edp-cluster-add-ons/issues/53))
- Set correct variable name in nexus Argo application ([#45](https://github.com/epam/edp-cluster-add-ons/issues/45))
- Add flag to disable oauth2-proxy in Chart.yaml ([#52](https://github.com/epam/edp-cluster-add-ons/issues/52))
- Align keycloak values to use PGO ([#50](https://github.com/epam/edp-cluster-add-ons/issues/50))
- Align keycloak cr resources ([#38](https://github.com/epam/edp-cluster-add-ons/issues/38))
- Align values file of the sonar-operator ([#43](https://github.com/epam/edp-cluster-add-ons/issues/43))
- Align sonar application with its chart dependency ([#42](https://github.com/epam/edp-cluster-add-ons/issues/42))
- Update nexus templates ([#27](https://github.com/epam/edp-cluster-add-ons/issues/27))
- Use Nexus Ingress object for the CI workload ([#28](https://github.com/epam/edp-cluster-add-ons/issues/28))
- Fix dependency-track resources configuration in values.yaml ([#20](https://github.com/epam/edp-cluster-add-ons/issues/20))
- Update conditional check for enabling extensions-oidc ([#11](https://github.com/epam/edp-cluster-add-ons/issues/11))
- Fix changelog generator ([#1](https://github.com/epam/edp-cluster-add-ons/issues/1))

### Code Refactoring
- Align file names of ESO components in Opensearch ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Kibana ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Extensions-oidc ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Keycloak ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Keycloak-postgresql ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Sonar-operator ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Argo CD ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Report-portal ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Nexus ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in DefectDojo ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Prometheus-operator ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Vault-kms and Vault-okd ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Harbor ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Harbor-ha-okd ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))
- Align file names of ESO components in Harbor-ha ([#155](https://github.com/epam/edp-cluster-add-ons/issues/155))

### Routine
- Remove deprecated keycloak groups ([#129](https://github.com/epam/edp-cluster-add-ons/issues/129))
- Add oauth2-proxy ([#131](https://github.com/epam/edp-cluster-add-ons/issues/131))
- Update extensions-oidc application ([#129](https://github.com/epam/edp-cluster-add-ons/issues/129))
- Move Role-ARN Annotation from Service Account to Values ([#136](https://github.com/epam/edp-cluster-add-ons/issues/136))
- Migrate from KeycloakRealmRoleBatch to KeycloakRealmRole ([#134](https://github.com/epam/edp-cluster-add-ons/issues/134))
- Add EKS OIDC configuration for Keycloak realm ([#129](https://github.com/epam/edp-cluster-add-ons/issues/129))
- Change deploy policy for all release nexus repos ([#125](https://github.com/epam/edp-cluster-add-ons/issues/125))
- Change deploy policy for edp-maven-releases nexus repo ([#125](https://github.com/epam/edp-cluster-add-ons/issues/125))
- Add external secret for AWX admin user ([#122](https://github.com/epam/edp-cluster-add-ons/issues/122))
- Implement cert-manager integration for capsule ([#118](https://github.com/epam/edp-cluster-add-ons/issues/118))
- Update kube-prometheus-stack chart ([#116](https://github.com/epam/edp-cluster-add-ons/issues/116))
- Ensure we can tollerate to opensearch issues ([#108](https://github.com/epam/edp-cluster-add-ons/issues/108))
- Update eks and grafana Helm charts ([#112](https://github.com/epam/edp-cluster-add-ons/issues/112))
- Update fluent-bit config for cloudevent ([#108](https://github.com/epam/edp-cluster-add-ons/issues/108))
- Update fluent-bit config ([#108](https://github.com/epam/edp-cluster-add-ons/issues/108))
- Allow run terminal in Argo UI ([#106](https://github.com/epam/edp-cluster-add-ons/issues/106))
- Update logging stack to the latest stable versions ([#104](https://github.com/epam/edp-cluster-add-ons/issues/104))
- Update prometheus-operator version ([#74](https://github.com/epam/edp-cluster-add-ons/issues/74))
- Align sonar QG by complies ([#101](https://github.com/epam/edp-cluster-add-ons/issues/101))
- Align operator versions and bump KubeRocketCI platform version to 3.9.0 ([#99](https://github.com/epam/edp-cluster-add-ons/issues/99))
- Disable api-server persistentVolume due to use of external database ([#86](https://github.com/epam/edp-cluster-add-ons/issues/86))
- Update Dependency-track chart version to 0.9.1 ([#86](https://github.com/epam/edp-cluster-add-ons/issues/86))
- Remove duplicate parser from fluent-bit ([#83](https://github.com/epam/edp-cluster-add-ons/issues/83))
- Update nexus image version to 3.69.0 ([#85](https://github.com/epam/edp-cluster-add-ons/issues/85))
- Update Opensearch chart version
- Update keycloak to the latest stable version ([#88](https://github.com/epam/edp-cluster-add-ons/issues/88))
- Add codeowners file to the repo ([#81](https://github.com/epam/edp-cluster-add-ons/issues/81))
- Remove unused parameter import realm ([#79](https://github.com/epam/edp-cluster-add-ons/issues/79))
- Update findbugs sonar plugin to 4.2.9 version ([#80](https://github.com/epam/edp-cluster-add-ons/issues/80))
- Update defectdojo to the appVersion 2.34.1 ([#78](https://github.com/epam/edp-cluster-add-ons/issues/78))
- Align opentelemetry components to the latest version ([#76](https://github.com/epam/edp-cluster-add-ons/issues/76))
- Move Keycloak CRs from sonar-operator to sonar ([#77](https://github.com/epam/edp-cluster-add-ons/issues/77))
- Update observability stack components ([#76](https://github.com/epam/edp-cluster-add-ons/issues/76))
- Update prometheus-operator version ([#74](https://github.com/epam/edp-cluster-add-ons/issues/74))
- Bump helm chart versions of opensearch addon ([#72](https://github.com/epam/edp-cluster-add-ons/issues/72))
- Bump cert-manager Helm chart version from 1.12.6 to 1.14.4 ([#71](https://github.com/epam/edp-cluster-add-ons/issues/71))
- Enable X-Frame flag for Grafana ([#69](https://github.com/epam/edp-cluster-add-ons/issues/69))
- Update Postgres clusters config ([#69](https://github.com/epam/edp-cluster-add-ons/issues/69))
- Update capsule app to ignore webhook caBundle diffs ([#44](https://github.com/epam/edp-cluster-add-ons/issues/44))
- Reduce logs volume from oauth2-proxy ([#65](https://github.com/epam/edp-cluster-add-ons/issues/65))
- Add description about init admin password ([#65](https://github.com/epam/edp-cluster-add-ons/issues/65))
- Align ci username pattern to EDP approach ([#65](https://github.com/epam/edp-cluster-add-ons/issues/65))
- Align pgo objects name pattern ([#57](https://github.com/epam/edp-cluster-add-ons/issues/57))
- Align argocd values ([#61](https://github.com/epam/edp-cluster-add-ons/issues/61))
- Bump Argo CD version to LTS ([#61](https://github.com/epam/edp-cluster-add-ons/issues/61))
- Bump ingress-nginx version to LTS ([#60](https://github.com/epam/edp-cluster-add-ons/issues/60))
- Align KubeRocketCI helm chart version ([#59](https://github.com/epam/edp-cluster-add-ons/issues/59))
- Configure ingresses for Keycloak user endpoints and admin console ([#58](https://github.com/epam/edp-cluster-add-ons/issues/58))
- Add external ingress-nginx controller ([#58](https://github.com/epam/edp-cluster-add-ons/issues/58))
- Remove EDPComponent CRD mentioned ([#52](https://github.com/epam/edp-cluster-add-ons/issues/52))
- Update Tekton Pipeline version ([#54](https://github.com/epam/edp-cluster-add-ons/issues/54))
- Align main values file ([#50](https://github.com/epam/edp-cluster-add-ons/issues/50))
- Disable subcharts deployment by default ([#50](https://github.com/epam/edp-cluster-add-ons/issues/50))
- Align values to new version nexus-operator([#48](https://github.com/epam/edp-cluster-add-ons/issues/48))
- Enable Docker support in Nexus ([#49](https://github.com/epam/edp-cluster-add-ons/issues/49))
- Use generic type instead of gcpsm to set provider configuration ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Align external-secret to name pattern ([#160](https://github.com/epam/edp-cluster-add-ons/issues/160))
- Allow the use of different ESO providers in Extensions-OIDC ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Keycloak ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Argo CD ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Keycloak-postgresql ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Opensearch ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in prometheus-operator ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Report-Portal ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in DefectDojo ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Sonar-operator ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Harbor-OKD ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Harbor-HA ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Harbor ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Vault ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Nexus ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Fluent-bit ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Grafana ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Allow the use of different ESO providers in Kibana ([#47](https://github.com/epam/edp-cluster-add-ons/issues/47))
- Bump keycloak version([#38](https://github.com/epam/edp-cluster-add-ons/issues/38))
- Bump keycloak-operator version([#38](https://github.com/epam/edp-cluster-add-ons/issues/38))
- Bump tekton-cache version to 0.3.2 ([#41](https://github.com/epam/edp-cluster-add-ons/issues/41))
- Align component versions ([#41](https://github.com/epam/edp-cluster-add-ons/issues/41))
- Bump edp-install version ([#39](https://github.com/epam/edp-cluster-add-ons/issues/39))
- Bump tekton-cache version ([#36](https://github.com/epam/edp-cluster-add-ons/issues/36))
- Align Argo CD diff in sonar-operator app ([#35](https://github.com/epam/edp-cluster-add-ons/issues/35))
- Align Argo CD diff in nexus app ([#35](https://github.com/epam/edp-cluster-add-ons/issues/35))
- Align Argo CD diff in opensearch app ([#35](https://github.com/epam/edp-cluster-add-ons/issues/35))
- Align Argo CD diff in argo app ([#35](https://github.com/epam/edp-cluster-add-ons/issues/35))
- Align Argo CD diff in harbors app ([#35](https://github.com/epam/edp-cluster-add-ons/issues/35))
- Align Argo CD diff keycloak configuration ([#35](https://github.com/epam/edp-cluster-add-ons/issues/35))
- Align Argo CD and cert-manager naming approach ([#25](https://github.com/epam/edp-cluster-add-ons/issues/25))
- Update Argo CD to version 2.9.3 ([#25](https://github.com/epam/edp-cluster-add-ons/issues/25))
- Update Tekton Triggers ([#34](https://github.com/epam/edp-cluster-add-ons/issues/34))
- Update Tekton Pipelines to version v0.53.3 ([#34](https://github.com/epam/edp-cluster-add-ons/issues/34))
- Update changelog ([#33](https://github.com/epam/edp-cluster-add-ons/issues/33))
- Add reportportal ([#33](https://github.com/epam/edp-cluster-add-ons/issues/33))
- Add-ons table now contains versions ([#32](https://github.com/epam/edp-cluster-add-ons/issues/32))
- Update README.md with addons ([#32](https://github.com/epam/edp-cluster-add-ons/issues/32))
- Update helm-docs ([#32](https://github.com/epam/edp-cluster-add-ons/issues/32))
- Update addons repo version ([#32](https://github.com/epam/edp-cluster-add-ons/issues/32))
- Update Harbor template ([#27](https://github.com/epam/edp-cluster-add-ons/issues/27))
- Bump edp version ([#27](https://github.com/epam/edp-cluster-add-ons/issues/27))
- Add sonar ci-user ES component ([#27](https://github.com/epam/edp-cluster-add-ons/issues/27))
- Align DefectDojo add-ons ([#27](https://github.com/epam/edp-cluster-add-ons/issues/27))
- Align Sonar add-ons ([#27](https://github.com/epam/edp-cluster-add-ons/issues/27))
- Align keycloak add-ons ([#27](https://github.com/epam/edp-cluster-add-ons/issues/27))
- Align oidc add-ons ([#27](https://github.com/epam/edp-cluster-add-ons/issues/27))
- Update capsule to the latest stable version ([#30](https://github.com/epam/edp-cluster-add-ons/issues/30))
- Update helm docs for sonarqube ([#29](https://github.com/epam/edp-cluster-add-ons/issues/29))
- Remove downloaded chart from repository ([#28](https://github.com/epam/edp-cluster-add-ons/issues/28))
- Update tekton stack ([#26](https://github.com/epam/edp-cluster-add-ons/issues/26))
- Update changelog ([#26](https://github.com/epam/edp-cluster-add-ons/issues/26))
- Update tekton-chains version ([#26](https://github.com/epam/edp-cluster-add-ons/issues/26))
- Update argo cd template to LTS ([#25](https://github.com/epam/edp-cluster-add-ons/issues/25))
- Upgrade pull request template ([#24](https://github.com/epam/edp-cluster-add-ons/issues/24))
- Bump nexus operator version ([#10](https://github.com/epam/edp-cluster-add-ons/issues/10))
- Align keycloak-operator usage ([#22](https://github.com/epam/edp-cluster-add-ons/issues/22))
- Add external secret templates for sonar-operator ([#21](https://github.com/epam/edp-cluster-add-ons/issues/21))
- Add templates for github issues ([#13](https://github.com/epam/edp-cluster-add-ons/issues/13))
- Set all values false by default in add-ons repository ([#18](https://github.com/epam/edp-cluster-add-ons/issues/18))
- Align add-ons repo to use LTS sonar-operator release and LTS sonar ([#12](https://github.com/epam/edp-cluster-add-ons/issues/12))
- Align keycloak-operator for latest stable version ([#17](https://github.com/epam/edp-cluster-add-ons/issues/17))
- Upgrade Harbor to the latest stable ([#68](https://github.com/epam/edp-cluster-add-ons/issues/68))
- Align add-ons repo to use LTS sonar-operator release and LTS sonar ([#12](https://github.com/epam/edp-cluster-add-ons/issues/12))
- Align add-ons repo to use LTS sonar-operator release and LTS sonar ([#12](https://github.com/epam/edp-cluster-add-ons/issues/12))
- Set in-toto format for the tekton taskrun ([#14](https://github.com/epam/edp-cluster-add-ons/issues/14))
- Bump nexus and edp-nexus-operator version ([#7](https://github.com/epam/edp-cluster-add-ons/issues/7))
- Bump sonar-operator from 2.14.0-RC.3 to 2.14.1 ([#6](https://github.com/epam/edp-cluster-add-ons/issues/6))
- Align values for Opensearch ([#4](https://github.com/epam/edp-cluster-add-ons/issues/4))
- Update Nexus to 3.58.1 version ([#5](https://github.com/epam/edp-cluster-add-ons/issues/5))
- Add DefectDojo KeycloakClient and update DefectDojo Helm Chart version ([#2](https://github.com/epam/edp-cluster-add-ons/issues/2))
- Remove unused tekton cache options ([#1](https://github.com/epam/edp-cluster-add-ons/issues/1))
- Define initial structure ([#1](https://github.com/epam/edp-cluster-add-ons/issues/1))

### Documentation
- Update README fluent-bit config for events ([#108](https://github.com/epam/edp-cluster-add-ons/issues/108))
- Give more details on how to work with Addons V2 ([#56](https://github.com/epam/edp-cluster-add-ons/issues/56))
- Update versions and changelog ([#55](https://github.com/epam/edp-cluster-add-ons/issues/55))
- Bump tekton version ([#59](https://github.com/epam/edp-cluster-add-ons/issues/59))
- Update README file with repository structure description ([#1](https://github.com/epam/edp-cluster-add-ons/issues/1))


<a name="v0.1.0"></a>
## v0.1.0 - 2023-06-29

[Unreleased]: https://github.com/epam/edp-cluster-add-ons/compare/v0.1.0...HEAD
