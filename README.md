# Cluster Add-ons Repository

<!-- TOC -->

- [Cluster Add-ons Repository](#cluster-add-ons-repository)
  - [Overview](#overview)
  - [Repository structure](#repository-structure)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Deploying and Configuring Argo CD](#deploying-and-configuring-argo-cd)
    - [Enabling and Deploying Add-ons](#enabling-and-deploying-add-ons)
  - [Working with the Repository](#working-with-the-repository)
    - [Adding New Add-ons](#adding-new-add-ons)
    - [Adding New Clusters](#adding-new-clusters)
    - [Chart Testing and CI/CD](#chart-testing-and-cicd)
  - [Available add-ons](#available-add-ons)

<!-- /TOC -->

## Overview

This repository contains a collection of pre-configured solutions (add-ons) for Kubernetes clusters. It follows the GitOps methodology and utilizes the Argo CD App of Apps pattern for streamlined configuration and deployment.

The repository offers a variety of Kubernetes add-ons that can be easily integrated into Kubernetes clusters, whether running on Openshift or any other Managed Kubernetes distribution. These add-ons enhance cluster capabilities and provide additional functionalities for the KubeRocketCI Platform.

Using Argo CD, one can leverage the repository to expedite the setup process of the KubeRocketCI Platform and cluster components. The repository provides ready-to-use configurations for add-ons, simplifying deployment and reducing complexity.

## Repository structure

The `edp-cluster-add-ons` repository is organized to facilitate easy management and deployment of add-ons across different clusters:

- `argo-cd/` - contains the Helm chart for main Argo CD with templates for AppProjects, OIDC integration, and external secrets
- `clusters/` - contains directories for different clusters (e.g., `core`, `prod`), each with its own set of add-ons and configurations
- `docs/` - comprehensive documentation for working with the repository

```bash
.
├── argo-cd               # Main Argo CD Helm chart
│   ├── Chart.yaml
│   ├── README.md
│   ├── templates
│   │   ├── appProjectCore.yaml
│   │   ├── appProjectKRCI.yaml
│   │   ├── external-secrets/
│   │   ├── oidc/
│   │   └── ...
└── clusters
    ├── core              # Core cluster directory
    │   ├── apps          # App of Apps Helm chart that references all add-ons
    │   │   ├── templates
    │   │   │   ├── argo-cd.yaml
    │   │   │   ├── atlantis.yaml
    │   │   │   └── ...
    │   │   ├── Chart.yaml
    │   │   ├── README.md
    │   │   └── values.yaml    # Values that store add-on specific configurations and cluster info
    │   ├── addons             # Directory containing individual add-on Helm charts
    │   │   ├── argo-cd
    │   │   ├── atlantis
    │   │   └── ...
    │   └── bootstrap-addons.yaml  # Initial Argo CD application
    └── prod                       # Production cluster directory
        └── ...
```

## Getting Started

### Prerequisites

Before using this repository, ensure you have:

- **Kubernetes Cluster**: Access to a Kubernetes cluster where you can deploy Argo CD and add-ons
- **Helm**: Helm command-line tool installed on your local machine
- **kubectl**: kubectl command-line tool installed and configured to interact with your Kubernetes cluster
- (OPTIONAL) **External Secrets Operator (ESO)**: Required if using External Secrets Operator for managing secrets
- (OPTIONAL) **keycloak-operator**: Required for Argo CD integration with Keycloak for SSO using OIDC

### Deploying and Configuring Argo CD

1. **Fork the Repository**:
   Fork this repository to your own GitHub account or organization to maintain your configurations.

2. **Configure Argo CD Helm Chart**:
   Update the `argo-cd/values.yaml` file to match your Kubernetes cluster requirements, including settings for ingress, domain, and other parameters.

3. **Configure AppProject Manifests**:
   Edit the `appProjectCore.yaml` and `appProjectKRCI.yaml` files in the `argo-cd/templates` directory to specify the correct repository URLs.

4. **Configure VCS Integration**:
   Create secrets for VCS integration using either kubectl or External Secrets Operator (ESO).

5. **Deploy Argo CD**:
   ```bash
   helm install argocd argo-cd/ -n argocd --create-namespace
   ```

For more detailed instructions, refer to the [Quick Start Guide](docs/quick-start-guide.md).

### Enabling and Deploying Add-ons

1. **Initialize Bootstrap Add-ons Application**:
   Update the repository URL in `clusters/core/apps/values.yaml` and `clusters/core/bootstrap-addons.yaml`, then apply:
   ```bash
   kubectl apply -f clusters/core/bootstrap-addons.yaml
   ```

2. **Enable Add-ons**:
   In the `clusters/core/apps/values.yaml` file, enable the desired add-ons by setting:
   ```yaml
   add-on-name:
     enable: true
     namespace: add-on-namespace
     createNamespace: true
   ```

3. **Configure Add-on Values**:
   Customize the add-on's configuration by editing its values.yaml file in `clusters/core/addons/add-on-name/`.

4. **Sync Applications**:
   In the Argo CD UI, sync the applications to deploy your add-ons.

## Working with the Repository

### Adding New Add-ons

To add a new add-on to the repository:

1. Create a new directory for your add-on in `clusters/<cluster-name>/addons/`
2. Add the necessary Helm chart files (Chart.yaml, values.yaml, templates/)
3. Create an Argo CD Application template in `clusters/<cluster-name>/apps/templates/`
4. Update the App of Apps values.yaml to include your add-on

For detailed instructions and best practices, see [Adding New Add-ons](docs/add-new-addon.md).

### Adding New Clusters

To add a new cluster to the repository:

1. Create a new directory for your cluster in `clusters/`
2. Create the initial bootstrap-addons.yaml file
3. Set up the addons directory and App of Apps Helm chart
4. Configure cluster-specific values

For step-by-step guidance, refer to [Adding New Clusters](docs/add-new-cluster.md).

### Chart Testing and CI/CD

This repository includes an automated CI pipeline that performs Helm chart validation and testing when pull requests are created:

1. **Chart Testing**: The CI workflow uses [chart-testing](https://github.com/helm/chart-testing) to lint and validate all Helm charts.
2. **Kind Cluster**: For chart installation testing, a Kubernetes in Docker (kind) cluster version 1.32 is automatically created.
3. **Installation Validation**: Each chart is installed in the test cluster to verify proper deployment.

You can also run chart tests locally using:

```bash
make test-charts-full
```

To update the add-ons table in this README:

```bash
make update-readme
```

For more information about chart testing, see [Chart Testing](docs/chart-testing.md).

## Available add-ons

The repository provides a wide range of pre-configured add-ons for Kubernetes clusters. The complete list of available add-ons, their versions, and default configurations is automatically generated below.

<!-- AUTOGENERATED CONTENT BELOW -->
| Component                    | version   | appVersion   | namespace              | createNamespace   | enable   |
|:-----------------------------|:----------|:-------------|:-----------------------|:------------------|:---------|
| argo-cd                      | 8.5.6     | v3.1.7       | krci                   | False             | False    |
| atlantis                     | 5.18.2    | v0.35.1      | atlantis               | False             | False    |
| aws-efs-csi-driver           | 3.2.2     | 2.1.11       | kube-system            | N/A               | False    |
| awx-operator                 | 2.19.1    | 2.19.1       | awx-operator           | False             | False    |
| capsule                      | 0.10.9    | 0.10.9       | capsule-system         | False             | False    |
| capsule-tenant               | N/A       | N/A          | capsule-system         | N/A               | False    |
| cert-manager                 | v1.18.2   | v1.18.2      | cert-manager           | False             | False    |
| defectdojo                   | 1.6.205   | 2.50.0       | defectdojo             | False             | False    |
| dependency-track             | 0.35.0    | v4.13.3      | dependency-track       | False             | False    |
| external-secrets             | 0.18.2    | 0.18.2       | external-secrets       | False             | False    |
| fluent-bit                   | 0.53.0    | 4.0.7        | logging                | False             | False    |
| gitfusion                    | 0.1.1     | 0.1.1        | krci                   | False             | False    |
| harbor                       | 0.1.0     | 1.17.2       | harbor                 | False             | False    |
| harbor-ha                    | 1.17.2    | 2.9.0        | harbor                 | False             | False    |
| harbor-ha-okd                | 1.13.0    | 2.9.0        | harbor                 | False             | False    |
| ingress-nginx                | 4.13.2    | 1.13.2       | ingress-nginx          | False             | False    |
| ingress-nginx-external       | 4.13.2    | 1.13.2       | ingress-nginx-external | False             | False    |
| jaeger-operator              | 2.57.0    | 1.61.0       | jaeger-operator        | False             | False    |
| karma-dashboard              | 2.11.0    | v0.121       | monitoring             | False             | False    |
| karpenter-np                 | 0.1.0     | 0.1.0        | karpenter              | False             | False    |
| karpenter                    | 1.6.1     | 1.6.1        | karpenter              | False             | False    |
| keda-tenants                 | 0.1.0     | 0.1.0        | keda                   | False             | False    |
| keda                         | 2.17.2    | 2.17.2       | keda                   | False             | False    |
| keycloak                     | 2.3.0     | 24.0.4       | security               | False             | False    |
| keycloak-postgresql          | 0.1.1     | 1.0          | security               | False             | False    |
| keycloak-operator            | 1.29.0    | 1.29.0       | keycloak-operator      | False             | False    |
| krakend                      | 0.1.36    | 2.7.2        | krci-krakend           | False             | False    |
| kuberocketci-pipelines       | N/A       | N/A          | krci                   | False             | False    |
| kuberocketci-rbac            | 0.1.0     | 0.1.0        | krci-security          | False             | False    |
| kuberocketci                 | 3.12.2    | 3.12.2       | krci                   | False             | False    |
| minio-operator               | 7.1.1     | v7.1.1       | minio-operator         | False             | False    |
| moon                         | 2.7.7     | 2.7.7        | moon                   | False             | False    |
| nexus-ce                     | 0.1.1     | 3.82.0       | nexus                  | False             | False    |
| nexus-operator               | 3.5.0     | 3.5.0        | nexus                  | False             | False    |
| nexus                        | 61.0.3    | 3.70.3       | nexus                  | False             | False    |
| oauth2-proxy                 | 8.2.0     | v7.12.0      | oauth2-proxy           | False             | False    |
| opensearch                   | 3.2.1     | 3.2.0        | logging                | False             | False    |
| opentelemetry-operator       | 0.95.1    | 0.134.0      | opentelemetry-operator | False             | False    |
| pgadmin                      | 1.49.0    | 9.7          | pgadmin                | False             | False    |
| postgres-operator            | 0.1.0     | 5.8.2        | postgres-operator      | False             | False    |
| prometheus-operator          | 77.6.0    | v0.85.0      | monitoring             | False             | False    |
| prometheus-blackbox-exporter | 11.3.1    | v0.27.0      | monitoring             | False             | False    |
| redis-operator               | 3.3.0     | 1.3.0        | redis-operator         | False             | False    |
| report-portal                | 25.8.29   | 25.1.8       | report-portal          | False             | False    |
| sonar                        | 2025.3.1  | 2025.3.1     | sonar                  | False             | False    |
| sonar-operator               | 3.3.0     | 3.3.0        | sonar                  | False             | False    |
| storage-class                | N/A       | N/A          | N/A                    | N/A               | False    |
| tekton-cache                 | 0.4.2     | 0.4.2        | tekton-cache           | False             | False    |
| tekton                       | N/A       | N/A          | tekton-pipelines       | False             | False    |
| tekton-custom-task           | 0.2.0     | 0.2.0        | krci                   | False             | False    |
| tekton-dashboard             | 0.52.0    | 0.52.0       | krci                   | False             | False    |
| vault-kms                    | 0.25.0    | 1.20.1       | vault                  | False             | False    |
| vault-okd                    | 0.25.0    | 1.20.1       | vault                  | False             | False    |
| vault                        | 0.30.0    | 1.20.1       | vault                  | False             | False    |
| vault-operator               | 1.23.0    | 1.23.0       | vault                  | False             | False    |
