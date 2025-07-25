# Cluster Add-ons Repository

<!-- TOC -->

- [Cluster Add-ons Repository](#cluster-add-ons-repository)
  - [Overview](#overview)
  - [Repository structure](#repository-structure)
    - [How to enable an add-on](#how-to-enable-an-add-on)
  - [Available add-ons](#available-add-ons)

<!-- /TOC -->

## Overview

This repository contains a collection of pre-configured solutions (add-ons) for Kubernetes cluster. It follows the GitOps methodology and utilizes the ArgoCD App of Apps pattern for streamlined configuration and deployment.

The repository offers a variety of Kubernetes add-ons that can be easily integrated into Kubernetes cluster, whether running on Openshift or any other Managed Kubernetes distribution. These add-ons enhance cluster capabilities and provide additional functionalities for the KubeRocketCI Platform.

Using ArgoCD, one can leverage the repository to expedite the setup process of the KubeRocketCI Platform and cluster components. The repository provides ready-to-use configurations for add-ons, simplifying deployment and reducing complexity.

### Developer Tools Integration

This repository includes integration with developer tools to enhance the development experience:

- **Adding New Add-ons**: [See guide](docs/add-new-addon.md) for detailed instructions on adding new add-ons.

## Repository structure

- `argo-cd` - contains the Helm chart for main Argo CD
- `clusters` - contains the configuration files for the add-ons that are specific to the cluster

```bash
.
├── argo-cd
│   ├── Chart.yaml
│   ├── README.md
│   ├── templates
...
└── clusters
    ├── core
    │   ├── apps
    │   │   ├── templates
    │   │   |   ├── argo-cd.yaml
    │   │   |   ├── atlantis.yaml
    │   │   |   ├── ...
    │   │   ├── Chart.yaml
    │   │   ├── README.md
    │   │   ├── values.yaml
    │   ├── addons
    |   |   ├── argo-cd
    |   |   ├── atlantis
    |   |   ├── ...
    │   ├── bootstrap-addons.yaml
    ├── prod
```

### How to enable an add-on

1. Fork this repository.
2. To init add-ons onboarding process, deploy main Argo CD instance by running the following command:

```bash
helm install argocd argo-cd -n argocd --create-namespace
```

3. To get access to the Argo CD UI run port-forward command.
4. Configure integration with the forked repository by adding credential template to the Argo CD.
5. Apply the [`clusters/core/bootstrap-addons.yaml`](clusters/core/bootstrap-addons.yaml) application to the Argo CD.
6. Enable the add-on by setting the `enable` field to `true` in the [`clusters/core/apps/values.yaml`](clusters/core/apps/values.yaml) file.
7. To change the application namespace, update the namespace field in the [`clusters/core/apps/values.yaml`](clusters/core/apps/values.yaml) file.

## Available add-ons

Check out the list of available add-ons in the [chart](./clusters/core/apps/README.md) directory.

## Chart Testing and CI/CD

This repository includes an automated CI pipeline that performs Helm chart validation and testing when pull requests are created:

1. **Chart Testing**: The CI workflow uses [chart-testing](https://github.com/helm/chart-testing) to lint and validate all Helm charts.
2. **Kind Cluster**: For chart installation testing, a Kubernetes in Docker (kind) cluster version 1.32 is automatically created.
3. **Installation Validation**: Each chart is installed in the test cluster to verify proper deployment.

You can also run chart tests locally using:

```bash
make test-charts-full
```

```bash
make update-readme
```

<!-- AUTOGENERATED CONTENT BELOW -->
| Component                    | version   | appVersion   | namespace              | createNamespace   | enable   |
|:-----------------------------|:----------|:-------------|:-----------------------|:------------------|:---------|
| argo-cd                      | 7.7.11    | v2.13.2      | krci                   | False             | False    |
| atlantis                     | 5.17.2    | v0.34.0      | atlantis               | False             | False    |
| aws-efs-csi-driver           | 1.5.7     | 1.5.7        | kube-system            | N/A               | False    |
| awx-operator                 | 2.19.1    | 2.19.1       | awx-operator           | False             | False    |
| capsule                      | 0.5.3     | 0.4.2        | capsule-system         | False             | False    |
| capsule-tenant               | N/A       | N/A          | capsule-system         | N/A               | False    |
| cert-manager                 | 1.17.2    | 1.17.2       | cert-manager           | False             | False    |
| defectdojo                   | 1.6.188   | 2.46.3       | defectdojo             | False             | False    |
| dependency-track             | 0.33.0    | v4.13.2      | dependency-track       | False             | False    |
| external-secrets             | 0.14.2    | 0.14.2       | external-secrets       | False             | False    |
| fluent-bit                   | 0.49.0    | 4.0.1        | logging                | False             | False    |
| harbor                       | 0.1.0     | 1.12.2       | harbor                 | False             | False    |
| harbor-ha                    | 1.13.0    | 2.9.0        | harbor                 | False             | False    |
| harbor-ha-okd                | 1.13.0    | 2.9.0        | harbor                 | False             | False    |
| ingress-nginx                | 4.12.2    | 1.12.2       | ingress-nginx          | False             | False    |
| ingress-nginx-external       | 4.12.2    | 1.12.2       | ingress-nginx-external | False             | False    |
| jaeger-operator              | 2.57.0    | 1.61.0       | jaeger-operator        | False             | False    |
| karma-dashboard              | 2.9.6     | v0.121       | monitoring             | False             | False    |
| karpenter-np                 | 0.1.0     | 0.1.0        | karpenter              | False             | False    |
| karpenter                    | 1.3.3     | 1.3.3        | karpenter              | False             | False    |
| keda-tenants                 | 0.1.0     | 0.1.0        | keda                   | False             | False    |
| keda                         | 2.15.2    | 2.15.1       | keda                   | False             | False    |
| keycloak                     | 2.3.0     | 24.0.4       | security               | False             | False    |
| keycloak-postgresql          | 0.1.1     | 1.0          | security               | False             | False    |
| keycloak-operator            | 1.27.1    | 1.27.1       | keycloak-operator      | False             | False    |
| krakend                      | 0.1.36    | 2.7.2        | krci-krakend           | False             | False    |
| kuberocketci-pipelines       | N/A       | N/A          | krci                   | False             | False    |
| kuberocketci-rbac            | 0.1.0     | 0.1.0        | krci-security          | False             | False    |
| kuberocketci                 | 3.11.3    | 3.11.3       | krci                   | False             | False    |
| minio-operator               | 0.1.0     | 5.0.5        | minio-operator         | False             | False    |
| moon                         | 2.7.4     | 2.7.4        | moon                   | False             | False    |
| nexus-ce                     | 0.1.0     | 3.79.1       | nexus                  | False             | False    |
| nexus-operator               | 3.5.0     | 3.5.0        | nexus                  | False             | False    |
| nexus                        | 61.0.3    | 3.70.3       | nexus                  | False             | False    |
| oauth2-proxy                 | 7.6.0     | v7.6.0       | oauth2-proxy           | False             | False    |
| opensearch                   | 2.26.1    | 2.17.1       | logging                | False             | False    |
| opentelemetry-operator       | 0.62.0    | 0.102.0      | opentelemetry-operator | False             | False    |
| pgadmin                      | 1.45.1    | 9.3          | pgadmin                | False             | False    |
| postgres-operator            | 0.1.0     | 5.7.0        | postgres-operator      | False             | False    |
| prometheus-operator          | 72.3.0    | v0.82.0      | monitoring             | False             | False    |
| prometheus-blackbox-exporter | 9.7.0     | v0.26.0      | monitoring             | False             | False    |
| redis-operator               | 0.1.0     | 3.2.8        | redis-operator         | False             | False    |
| report-portal                | 5.10.0    | 23.2         | report-portal          | False             | False    |
| sonar                        | 8.0.2     | 9.9.2        | sonar                  | False             | False    |
| sonar-operator               | 3.3.0     | 3.3.0        | sonar                  | False             | False    |
| storage-class                | N/A       | N/A          | N/A                    | N/A               | False    |
| tekton-cache                 | 0.4.1     | 0.4.1        | tekton-cache           | False             | False    |
| tekton                       | N/A       | N/A          | tekton-pipelines       | False             | False    |
| tekton-custom-task           | 0.2.0     | 0.2.0        | krci                   | False             | False    |
| tekton-dashboard             | 0.52.0    | 0.52.0       | krci                   | False             | False    |
| vault-kms                    | 0.25.0    | 1.14.0       | vault                  | False             | False    |
| vault-okd                    | 0.25.0    | 1.14.0       | vault                  | False             | False    |
| vault                        | 0.30.0    | 1.19.0       | vault                  | False             | False    |
| vault-operator               | 1.22.5    | 1.22.5       | vault                  | False             | False    |
