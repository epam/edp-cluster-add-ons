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

Explore this repository to access a comprehensive collection of Kubernetes add-ons for your Kubernetes. Simplify deployment, enhance cluster capabilities, and stay up-to-date with the evolving landscape of Kubernetes.

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

## Available add-ons

Check out the list of available add-ons in the [chart](./clusters/core/apps/README.md) directory.

```bash
make update-readme
```

<!-- AUTOGENERATED CONTENT BELOW -->
| Component              | version   | appVersion   | createNamespace   | enable   |
|:-----------------------|:----------|:-------------|:------------------|:---------|
| argo-cd                | 7.7.11    | v2.13.2      | False             | False    |
| aws-efs-csi-driver     | 1.5.7     | 1.5.7        | N/A               | False    |
| awx-operator           | 2.19.1    | 2.19.1       | False             | False    |
| capsule                | 0.5.3     | 0.4.2        | False             | False    |
| capsule-tenant         | N/A       | N/A          | N/A               | False    |
| cert-manager           | 1.16.1    | v1.16.1      | False             | False    |
| defectdojo             | 1.6.127   | 2.34.1       | False             | False    |
| dependency-track       | 0.9.2     | v4.11.3      | False             | False    |
| kuberocketci           | 3.10.2    | 3.10.2       | False             | False    |
| kuberocketci-pipelines | N/A       | N/A          | False             | False    |
| kuberocketci-rbac      | 0.1.0     | 0.1.0        | False             | False    |
| external-secrets       | 0.10.5    | 1.0          | False             | False    |
| fluent-bit             | 0.46.11   | 3.0.7        | False             | False    |
| harbor                 | 0.1.0     | 1.12.2       | False             | False    |
| harbor-ha              | 1.13.0    | 2.9.0        | False             | False    |
| harbor-ha-okd          | 1.13.0    | 2.9.0        | False             | False    |
| ingress-nginx          | 4.11.3    | 1.11.3       | False             | False    |
| ingress-nginx-external | 4.11.3    | 1.11.3       | False             | False    |
| jaeger-operator        | 2.53.0    | 1.52.0       | False             | False    |
| keycloak               | 2.3.0     | 24.0.4       | False             | False    |
| keycloak-postgresql    | 0.1.1     | 1.0          | False             | False    |
| keycloak-operator      | 1.23.0    | 1.23.0       | False             | False    |
| krakend                | 0.1.36    | 2.7.2        | False             | False    |
| minio-operator         | 0.1.0     | 5.0.5        | False             | False    |
| nexus                  | 61.0.3    | 3.70.3       | False             | False    |
| nexus-operator         | 3.3.0     | 3.3.0        | False             | False    |
| oauth2-proxy           | 7.6.0     | v7.6.0       | False             | False    |
| opensearch             | 2.26.1    | 2.17.1       | False             | False    |
| opentelemetry-operator | 0.62.0    | 0.102.0      | False             | False    |
| postgres-operator      | 0.1.0     | 5.7.0        | False             | False    |
| report-portal          | 5.10.0    | 23.2         | False             | False    |
| prometheus-operator    | 65.5.1    | v0.77.2      | False             | False    |
| redis-operator         | 0.1.0     | 3.2.8        | False             | False    |
| sonar                  | 8.0.2     | 9.9.2        | False             | False    |
| sonar-operator         | 3.1.1     | 3.1.1        | False             | False    |
| storage-class          | N/A       | N/A          | N/A               | False    |
| tekton-cache           | 0.4.0     | 0.4.0        | False             | False    |
| tekton                 | N/A       | N/A          | False             | False    |
| tekton-custom-task     | 0.1.0     | 0.1.0        | False             | False    |
| vault                  | 0.24.1    | 1.13.1       | False             | False    |
| vault-kms              | 0.25.0    | 1.14.0       | False             | False    |
| vault-okd              | 0.25.0    | 1.14.0       | False             | False    |
| atlantis               | 5.8.0     | v0.30.0      | False             | False    |
