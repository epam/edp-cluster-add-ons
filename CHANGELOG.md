<a name="unreleased"></a>
## [Unreleased]

### Features
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
- Update nexus templates ([#27](https://github.com/epam/edp-cluster-add-ons/issues/27))
- Use Nexus Ingress object for the CI workload ([#28](https://github.com/epam/edp-cluster-add-ons/issues/28))
- Fix dependency-track resources configuration in values.yaml ([#20](https://github.com/epam/edp-cluster-add-ons/issues/20))
- Update conditional check for enabling extensions-oidc ([#11](https://github.com/epam/edp-cluster-add-ons/issues/11))
- Fix changelog generator ([#1](https://github.com/epam/edp-cluster-add-ons/issues/1))

### Routine
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
- Bump tekton version ([#59](https://github.com/epam/edp-cluster-add-ons/issues/59))
- Update README file with repository structure description ([#1](https://github.com/epam/edp-cluster-add-ons/issues/1))


<a name="v0.1.0"></a>
## v0.1.0 - 2023-06-29

[Unreleased]: https://github.com/epam/edp-cluster-add-ons/compare/v0.1.0...HEAD
