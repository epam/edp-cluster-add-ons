# EPAM Delivery Platform (EDP) Cluster Add-ons Repository

<!-- TOC -->

- [EPAM Delivery Platform EDP Cluster Add-ons Repository](#epam-delivery-platform-edp-cluster-add-ons-repository)
  - [Overview](#overview)
  - [Repository structure](#repository-structure)
  - [V2 Add-ons Approach with ArgoCD ApplicationSet](#v2-add-ons-approach-with-argocd-applicationset)
    - [How to enable an add-on](#how-to-enable-an-add-on)
  - [Available add-ons](#available-add-ons)

<!-- /TOC -->

## Overview

This repository contains a collection of pre-configured solutions (add-ons) for Kubernetes cluster. It follows the GitOps methodology and utilizes the ArgoCD App of Apps pattern for streamlined configuration and deployment.

The repository offers a variety of Kubernetes add-ons that can be easily integrated into Kubernetes cluster, whether running on Openshift or any other Managed Kubernetes distribution. These add-ons enhance cluster capabilities and provide additional functionalities for the EPAM Delivery Platform (EDP).

Using ArgoCD, one can leverage the repository to expedite the setup process of the EPAM Delivery Platform (EDP) and cluster components. The repository provides ready-to-use configurations for add-ons, simplifying deployment and reducing complexity.

Explore this repository to access a comprehensive collection of Kubernetes add-ons for your Kubernetes. Simplify deployment, enhance cluster capabilities, and stay up-to-date with the evolving landscape of Kubernetes.

## Repository structure

- `add-ons` - contains the source code of the Add Ons in the form of the Helm charts, used in both V1 and V2 approaches
- `bootstrap` - ([V2](#v2-add-ons-approach-with-argocd-applicationset) approach only) provision ApplicationSet
- `bootstrap.yaml` - ([V2](#v2-add-ons-approach-with-argocd-applicationset) approach only) contains the ArgoCD Application CRs, which deploys the ApplicationSet from the `bootstrap` directory
- `chart` - (V1 approach only) contains the Helm chart that uses Apps of Apps pattern and contains ArgoCD Application CRs
- `clusters` - ([V2](#v2-add-ons-approach-with-argocd-applicationset) approach only) contains the configuration files for the add-ons that are specific to the cluster

```bash
.
├── add-ons
│   ├── argocd
│   ├── aws-efs-csi-driver
│   ├── cert-manager
...
│   ├── tekton
│   └── vault
└── chart
    ├── Chart.yaml
    ├── README.md
    ├── templates
    │   ├── argocd.yaml
    │   ├── aws-efs-csi-driver.yaml
    │   ├── cert-manager.yaml
...
    │   ├── tekton.yaml
    │   └── vault.yaml
    └── values.yaml
    └── values.yaml
```

## V2 Add-ons Approach with ArgoCD ApplicationSet

In the V2 add-ons approach, we leverage the power of ArgoCD's ApplicationSet feature. The ApplicationSet is an API resource that represents a group of Argo CD Applications. It allows us to deploy multiple applications as a set, which can be useful when dealing with microservices, multi-tenant environments, or deploying applications at scale.

The ApplicationSet controller **automates** the process of generating Argo CD Applications based on a list of parameters. It can retrieve these parameters from different sources like Git files, JSON/YAML/TOML ConfigMaps, or even from cluster resources.

In the context of EDP add-ons, we define an ApplicationSet based on the addons and clusters.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: bootstrap-addons
spec:
  goTemplate: true
  goTemplateOptions: ["missingkey=error"]
  generators:
    - matrix:
        generators:
          - git:
              repoURL: https://github.com/epam/edp-cluster-add-ons
              revision: HEAD
              directories:
              - path: add-ons/*

          - clusters:
              selector:
                matchExpressions:
                # Check labels to see if addon is enabled.
                - key: enable_{{ .path.basename | snakecase }}
                  operator: In
                  values: ['true']
  template:
    metadata:
      # Application name is based on the cluster name and the addon name, e.g "in-cluster-argocd"
      name: '{{.name}}-{{.path.basename}}'
    spec:
      project: default
      source:
        helm:
          releaseName: '{{.path.basename}}'
          ignoreMissingValueFiles: true
          valueFiles:
          - '../../../clusters/{{.name}}/addons/{{.path.basename}}.yaml'
        repoURL: 'https://github.com/epam/edp-cluster-add-ons'
        path: '{{.path.path}}'
        targetRevision: HEAD
      destination:
        namespace: '{{.path.basename}}'
        # name of your cluster in Argo CD
        name: '{{.name}}'
      syncPolicy:
        automated: {}
        syncOptions:
          - CreateNamespace=true
          # We can have huge CRDs, so we need to use ServerSideApply
          - ServerSideApply=true
```

The ApplicationSet resource points to a Git directory that contains the definitions of all the applications that belong to the add-on. When the ApplicationSet is applied, the ApplicationSet controller generates an Argo CD Application for each enabled addon found in the Git directory.

### How to enable an add-on

To enable an add-on, follow the steps below:

1. Add a new directory with the name of the add-on in the `add-ons` directory.
2. Add a Helm chart for the add-on in the new directory.
3. Create a new `{{addon}}.yaml` file in the `clusters/{{cluster}}/addons` directory to enable the add-on for a specific cluster.
4. Enable the add-on by setting the `enable_{{addon}}: true` label on the Argo CD cluster (Secret) resource.

This approach provides several benefits:

- **Scalability**: We can manage a large number of applications efficiently.
- **Consistency**: All applications are managed in a uniform way.
- **Automation**: New applications can be automatically created by simply adding new definitions in the Git directory and enable flag on the Cluster resource.

This new approach simplifies the management of add-ons and enhances the scalability and flexibility of application deployment in the EDP platform.

## Available add-ons

Check out the list of available add-ons in the [chart](./chart/README.md) directory.

```bash
make update-readme
```

<!-- AUTOGENERATED CONTENT BELOW -->
| Component              | version   | appVersion   | createNamespace   | enable   |
|:-----------------------|:----------|:-------------|:------------------|:---------|
| argo-cd                | 6.7.2     | v2.10.3      | False             | False    |
| aws-efs-csi-driver     | 1.5.7     | 1.5.7        | N/A               | False    |
| capsule                | 0.5.3     | 0.4.2        | False             | False    |
| capsule-tenant         | N/A       | N/A          | N/A               | False    |
| cert-manager           | 1.14.4    | v1.14.4      | False             | False    |
| defectdojo             | 1.6.127   | 2.34.1       | False             | False    |
| dependency-track       | 0.9.1     | v4.11.3      | False             | False    |
| edp                    | 3.8.1     | 3.8.1        | False             | False    |
| extensions-oidc        | 1.20.0    | 1.20.0       | False             | False    |
| external-secrets       | 0.9.9     | 1.0          | False             | False    |
| fluent-bit             | 0.46.9    | 3.0.6        | False             | False    |
| harbor                 | 0.1.0     | 1.12.2       | False             | False    |
| harbor-ha              | 1.13.0    | 2.9.0        | False             | False    |
| harbor-ha-okd          | 1.13.0    | 2.9.0        | False             | False    |
| ingress-nginx          | 4.10.0    | 1.8.4        | False             | False    |
| ingress-nginx-external | 4.10.0    | 1.8.4        | False             | False    |
| jaeger-operator        | 2.53.0    | 1.52.0       | False             | False    |
| keycloak               | 2.3.0     | 24.0.4       | False             | False    |
| keycloak-postgresql    | 0.1.1     | 1.0          | False             | False    |
| minio-operator         | 0.1.0     | 5.0.5        | False             | False    |
| nexus                  | 61.0.3    | 3.69.0       | False             | False    |
| nexus-operator         | 3.2.0     | 3.2.0        | False             | False    |
| opensearch             | 2.19.1    | 2.13.1       | False             | False    |
| opentelemetry-operator | 0.56.0    | 0.98.0       | False             | False    |
| postgres-operator      | 0.1.0     | 5.4.3        | False             | False    |
| report-portal          | 5.10.0    | 23.2         | False             | False    |
| prometheus-operator    | 58.2.1    | v0.73.2      | False             | False    |
| redis-operator         | 0.1.0     | 3.2.8        | False             | False    |
| sonar                  | 8.0.2     | 9.9.2        | False             | False    |
| sonar-operator         | 3.1.0     | 3.1.0        | False             | False    |
| storage-class          | N/A       | N/A          | N/A               | False    |
| tekton-cache           | 0.3.2     | 0.3.2        | False             | False    |
| tekton                 | N/A       | N/A          | False             | False    |
| vault                  | 0.24.1    | 1.13.1       | False             | False    |
| vault-kms              | 0.25.0    | 1.14.0       | False             | False    |
| vault-okd              | 0.25.0    | 1.14.0       | False             | False    |
